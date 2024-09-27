from abc import ABC, abstractmethod

class Instrument(ABC):
    def __init__(self, name):
        self._name = name  

    @property
    def name(self):
        return self._name  

    @name.setter
    def name(self, value):
        self._name = value  

class StringInstrument(Instrument):
    def __init__(self, name, num_of_strings):
        super().__init__(name)
        self._num_of_strings = num_of_strings  

    @property
    def num_of_strings(self):
        return self._num_of_strings 

    @num_of_strings.setter
    def num_of_strings(self, value):
        self._num_of_strings = value 


violin = StringInstrument(name="Violin", num_of_strings=4)


print(f"Instrument: {violin.name}, Number of strings: {violin.num_of_strings}")
