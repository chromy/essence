MISSING = object()

class World(object):
    """World coordinates the entities, components and systems."""

    def __init__(self):
        self._highest_id_seen = 0
        self._database = {}
        self._entities = []
        self._systems = []

    def _get_relation(self, component_type):
        try:
            return self._database[component_type]
        except KeyError:
            self._database[component_type] = {}
            return self._database[component_type]

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

    def update(self):
        for system in self.systems:
            system.update()

class Component(object):
    """Components are normally raw data, what might be called a struct or
    a POD-type in other languages. Any state an entity might need
    in your game or system should be recorded on a Component. Examples of
    common components include Position, Sprite (or Model), Health, etc.

    In :mod:`essence` an implementation of a Position component might look
    like this::

        class Position(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

    Note that the Position component does not inherit from :class:`Component`;
    in general there is no requirement to have your components inherit from
    this class (or any class) but you may find it useful for organising your
    code.
    """
    pass

class System(object):
    """Systems act on entities, examining (and possibly modifying) components
    to implement the game logic. Normally at each 'tick' of the game each system
    iterates over all the entities it is interested in to update them.
    """

    def update(world, *args, **kargs):
        pass

class Entity(object):
    """Entities are unique ids which tie together groups of components.

    This class provides a convenient handle for adding, removing and accessing
    components (although in practice the components are actually stored on the
    world instance to allow for efficient iteration over groups of components).

    You should not normally need to create an Entity by hand, instead you should
    use :func:`essence.World.create_entity`. This ensures the entity gets a
    unique id and is added to the world.

    Entity objects compare equal only if they are bound to the same world and
    have the same uid.
    """

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

    def destroy(self, *args, **kargs):
        """Remove this entity and all connected components from the world.

        Short-hand for :func:`essence.World.destroy_entity`.
        """
        return self.world.destroy_entitiy(self, *args, **kargs)


    def __eq__(self, other):
        return self.world is other.world and self.uid == other.uid

    def __hash__(self):
        return hash((self.world, self.uid))

    def __repr__(self):
        return '<Entity({self.world}, {self.uid}>'.format(self=self)

class DuplicateComponentError(Exception):
    pass

class NoSuchComponentError(KeyError):
    pass


