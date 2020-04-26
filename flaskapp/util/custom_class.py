import numpy as np

class CustomClass():
    def __init__(self):
        self.some_string = "here is some string"
        self.counter = 1
        self.np_array = np.zeros((50,50))

    def get_attributes(self):
        self.counter += 1
        return self.some_string, self.counter, self.np_array

class_instance = CustomClass()