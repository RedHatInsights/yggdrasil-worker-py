import re
import typing
from os import path


class Worker:
    def __init__(self, directive: str, rx: typing.Callable[[str, str, dict, bytes]]) -> None:
        '''
        '''
        if re.match("-", directive) is not None:
            raise Exception("invalid directive '" + directive + "'")

        self.directive = directive
        self.rx = rx
        self.object_path = path.join(
            "/com/redhat/yggdrasil/Worker1", directive)
        self.bus_name = "com.redhat.yggdrasil.Worker1." + directive

    def connect(self) -> None:
        '''
            Connects to the configured bus and exports the worker.
        '''
        pass
