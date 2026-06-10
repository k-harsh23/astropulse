from abc import ABC, abstractmethod


class BaseProducer(ABC):

    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def save(self):
        pass