import sgtk

HookClass = sgtk.get_hook_baseclass()


class DoSomething(HookClass):
    """
    A basic hook that will do something

    :ivar bool fail: If the hook should fail or not
    """

    def execute(self, fail, **kwargs):
        if fail:
            self.logger.info('I going to Raise an Error')
            raise sgtk.TankError("This is the Error")

        self.logger.info('I AM DOING SOMETHING !!!!')
        return True
