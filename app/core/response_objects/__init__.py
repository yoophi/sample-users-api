class ResponseSuccess(object):
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return True


class ResponseFailure(object):
    SYSTEM_ERROR = "SystemError"

    def __init__(self, type_, message):
        self.type = type_
        self.message = self._format_message(message)

    def __bool__(self):
        return False

    @classmethod
    def build_system_error(cls, message=None):
        return cls(cls.SYSTEM_ERROR, message)

    @property
    def value(self):
        return {
            'type': self.type,
            'message': self.message,
        }

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return "{}: {}".format(msg.__class__.__name__, "{}".format(msg))

        return msg
