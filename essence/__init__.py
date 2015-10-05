MISSING = object()

class World(object):
    """World coordinates the entities, components and systems."""

    def __init__(self):
        self._highest_id_seen = 0
        self._database = {}

    def _get_relation(self, component_type):
        try:
            return self._database[component_type]
        except KeyError:
            self._database[component_type] = {}
            return self._database[component_type]

    def new_entity(self):
        """Create a new entity.

        The entity will have a higher UID than any previously associated
        with this world.

        :return: the new entity
        :rtype: :class:`essence.Entity`"""
        self._highest_id_seen += 1
        return Entity(self._highest_id_seen, self)

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
            msg = "Component {} can't be added to entity {} since it already has a component of type {}.".format(component, entity, component_type)
            raise DuplicateComponentError(msg)
        relation[entity] = component

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

    def has_component(self, entity, component_type):
        """Returns True iff entity has a component of component_type.

        Long-hand for :func:`essence.Entity.has`.

        :param entity: entity
        :type entity: :class:`essence.Entity`
        :param component_type: Type of component
        :type component_type: The :class:`type` of a :class:`Component` subclass"""
        return self.get_component(entity, component_type, None) is not None

class Component(object):
    pass

class System(object):
    pass

class Entity(object):
    def __init__(self, uid, world):
        self.world = world
        self.uid = uid

    def add(self, *args, **kargs):
        """Add a component to this entity

        Short-hand for :func:`essence.World.add_component`.
        
        :param component: Component to add
        :type component: :class:`Component`"""
        self.world.add_component(self, *args, **kargs)

    def get(self, *args, **kargs):
        """

        Short-hand for :func:`essence.World.get_component`.
        
        :param component_type: Type of component
        :type component_type: The :class:`type` of a :class:`Component` subclass"""
        return self.world.get_component(self, *args, **kargs)

    def remove(self, *args, **kargs):
        """

        Short-hand for :func:`essence.World.remove_component`.
        
        :param component_type: Type of component
        :type component_type: The :class:`type` of a :class:`Component` subclass"""
        self.world.remove_component(self, *args, **kargs)

    def has(self, *args, **kargs):
        """

        Short-hand for :func:`essence.World.has_component`.
        
        :param component_type: Type of component
        :type component_type: The :class:`type` of a :class:`Component` subclass"""
        return self.world.has_component(self, *args, **kargs)


class DuplicateComponentError(Exception):
    pass

class NoSuchComponentError(KeyError):
    pass


