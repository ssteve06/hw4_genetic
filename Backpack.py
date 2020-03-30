""" 
this file contains the backpack class which
is the individuals that re mutated and hold different boxes
"""
from Box import Box


class Backpack():
    max_weight = 250
    curr_weight = 0
    importance = 0

    
    def __init__(self, boxes=[]):
        self.boxes = boxes
        if not boxes is []:
            self.curr_weight = sum([box.weight for box in boxes])
            self.importance = sum([box.importance for box in boxes])

    def reset_boxes(self):
        self.curr_weight = 0
        self.importance = 0
        self.boxes = []

    def add_box(self, box):
        if not self.check_box_bounds(box):
            return False
        self.boxes.append(box)
        self.curr_weight += box.weight
        self.importance += box.importance
        return True

    def check_box_bounds(self, box):
        return box.weight + self.curr_weight <= self.max_weight
    
    def __str__(self):
        string = ""
        for b in self.boxes:
            string += str(b) + " "
        string += " weight -> {}  importance -> {}".format(self.curr_weight, self.importance)
        return string