from abc import ABC, abstractmethod

class RFIDReader(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def request(self, req_id):
        pass

    @abstractmethod
    def SelectTagSN(self):
        pass

    @abstractmethod
    def tohexstring(self, uid):
        pass
