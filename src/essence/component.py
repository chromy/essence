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


