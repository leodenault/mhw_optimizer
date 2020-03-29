from abc import ABCMeta, abstractmethod


class HeaderHandler:
    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_output(self, combination):
        pass

    @abstractmethod
    def name(self):
        pass
