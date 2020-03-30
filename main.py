from Backpack import Backpack
from Box import Box
import random
from time import sleep

pos_boxes = [Box(20, 6), Box(30, 5), Box(60, 8), Box(90, 7), Box(50, 6), Box(70, 9),
             Box(30, 4), Box(30, 5), Box(70, 4), Box(20, 9), Box(20, 2), Box(60, 1)]


# x = Backpack()
# x.check_box_bounds()

class Population():
    generation = 0
    backpacks = []
    
    def __init__(self, pop_size=50, max_gen=100):
        self.pop_size = pop_size
        self.max_gen = max_gen
        for x in range(self.pop_size):
            self.backpacks.append(Backpack(self.gen_rand_box_combo()))

    def gen_rand_box_combo(self):
        used_vals = []
        temp = Backpack()
        temp.reset_boxes()
        index = random.randrange(len(pos_boxes))

        while temp.add_box(pos_boxes[index]):
            used_vals.append(index)
            while index in used_vals:
               index = random.randrange(len(pos_boxes))
        return temp.boxes

    def get_parents_from_sorted(self):
        packs_next_gen = set()
        x = 0
        while len(packs_next_gen) < self.pop_size / 2:
            if (random.randrange((int)(self.pop_size / 2)) + x)**2 < (self.pop_size / 2)**2:
                packs_next_gen.add(self.backpacks[x])
            x = x + 1 if x < len(self.backpacks) - 1 else 0
        return packs_next_gen

    def prep_next_gen(self):
        packs_next_gen = []
        self.backpacks.sort(key=lambda x: x.importance, reverse=True)
        # print(self.backpacks[10])
        # print(self.backpacks[24])
        packs_next_gen = list(self.get_parents_from_sorted())
        packs_next_gen.sort(key=lambda x: x.importance, reverse=True)
        # print((packs_next_gen[10]))
        # print((packs_next_gen[24]))
        # print(self.backpacks[0].importance)
        
        
    


pop = Population()
pop.prep_next_gen()