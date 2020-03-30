"""
This file contains the box class which represents the boxes that the 
backpacks can hold
"""

class Box():
    def __init__(self, weight, importance):
        self.weight = weight
        self.importance = importance
    def __str__(self):
        return "({}, {})".format(self.weight, self.importance)

    def __eq__(self, other_box):
        return self.weight == other_box.weight and self.importance == other_box.importance