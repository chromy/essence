from sortedcontainers import SortedSet

from .entity import Entity

MISSING = object()

class World(object):
    """World coordinates the entities, components and systems."""

    def __init__(self):
        self._highest_id_seen = 0
        self._database = {}
        self._entities = []
        self._entities_by_component = {}
        self.systems = []

    def _get_relation(self, component_type):
        try:
            return self._database[component_type]
        except KeyError:
            self._database[component_type] = {}
            return self._database[component_type]

    def _entities_with(self, component_type):
        try:
            return self._entities_by_component[component_type]
        except KeyError:
            self._entities_by_component[component_type] = SortedSet()
            return self._entities_by_component[component_type]

    def create_entity(self):
        """Create a new entity.

        The entity will have a higher UID than any previously associated
        with this world.

        :return: the new entity
        :rtype: :class:`essence.Entity`"""
        self._highest_id_seen += 1
        entity = Entity(self._highest_id_seen, self)
        self._entities.append(entity)
        return entity

    def destroy_entitiy(self, entity):
        """Remove the entity and all connected components from the world.

        Long-hand for :func:`essence.Entity.destroy`.
        """
        for relation in self._database.values():
            relation.pop(entity, None)
        for l in self._entities_by_component.values():
            l.discard(entity)
        self._entities.remove(entity)

    def add_component(self, entity, component):
        """Add component to entity.

        Long-hand for :func:`essence.Entity.add`.

        :param entity: entity to associate
        :type entity: :class:`essence.Entity`
        :param component: component to add to the entity
        :type component: :class:`essence.Component`"""
        component_type = type(component)
        relation = self._get_relation(component_type)
        if entity in relation:
            # PYTHON2.6: Numbers required in format string.
            msg = "Component {0} can't be added to entity {1} since it already has a component of type {2}.".format(component, entity, component_type)
            raise DuplicateComponentError(msg)
        relation[entity] = component
        self._entities_with(component_type).add(entity)

    def get_component(self, entity, component_type, missing=MISSING):
        """Get the component of type component_type associated with entity.

        Long-hand for :func:`essence.Entity.get`.

        :param entity: entity to query
        :type entity: :class:`essence.Entity`
        :param component_type: component to add to the entity
        :type component_type: The :class:`type` of a :class:`Component` subclass
        :param missing: value to return if
        :type missing: :class:`essence.Component`
        :raises:"""
        relation = self._get_relation(component_type)
        if entity not in relation:
            if missing is MISSING:
                raise NoSuchComponentError()
            else:
                return missing
        return relation[entity]

    def remove_component(self, entity, component_type):
        """Remove the component of component_type from entity.

        Long-hand for :func:`essence.Entity.remove`.

        :param entity: entity to associate
        :type entity: :class:`essence.Entity`
        :param component_type: Type of component
        :type component_type: The :class:`type` of a :class:`Component` subclass"""
        relation = self._get_relation(component_type)
        del relation[entity]
        self._entities_with(component_type).remove(entity)

    def has_component(self, entity, component_type):
        """Returns True iff entity has a component of component_type.

        Long-hand for :func:`essence.Entity.has`.

        :param entity: entity
        :type entity: :class:`essence.Entity`
        :param component_type: Type of component
        :type component_type: The :class:`type` of a :class:`Component` subclass
        :return: Result
        :rtype: :class:`bool`"""
        return self.get_component(entity, component_type, None) is not None

    @property
    def entities(self):
        """An iterator over all existing entities associated with this world.

        :return: Iterable of all created entities
        :rtype: :class:`Iterator`"""
        return iter(self._entities)

    def entities_with(self, component_type):
        """Returns an iterator over all existing entities associated with this world
        which have a component of component_type.

        :return: Iterable of all created entities with component_type components
        :rtype: :class:`Iterator`"""
        return iter(self._entities_with(component_type))


    def update(self, *args, **kwargs):
        """Calls update on each of the systems self.systems."""
        for system in self.systems:
            system.update(self, *args, **kwargs)

class DuplicateComponentError(Exception):
    pass

class NoSuchComponentError(KeyError):
    pass


