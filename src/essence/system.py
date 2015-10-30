class System(object):
    """Systems act on entities, examining (and possibly modifying) components
    to implement the game logic. Normally at each 'tick' of the game each system
    iterates over all the entities it is interested in to update them.
    """

    def update(world, *args, **kargs):
        pass


