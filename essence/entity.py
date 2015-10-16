try:
    from functools import total_ordering
except ImportError:
    from total_ordering import total_ordering

@total_ordering
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

    def __lt__(self, other):
        return self.uid < other.uid


