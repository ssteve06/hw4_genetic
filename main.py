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
    
    def __init__(self, pop_size=10, max_gen=5):
        self.pop_size = pop_size
        self.max_gen = max_gen
        for x in range(self.pop_size):
            self.backpacks.append(Backpack(self.gen_rand_box_combo(pos_boxes)))

    def gen_rand_box_combo(self, pos_boxes):
        pos_indices = [i for i in range(len(pos_boxes))]
        random.shuffle(pos_indices)
        temp = Backpack()
        temp.reset_boxes()
        index = 0
        # index = random.randrange(len(pos_boxes))

        while temp.add_box(pos_boxes[pos_indices[index]]):
            index += 1
            while index < len(pos_indices) and pos_boxes[pos_indices[index]] in temp.boxes:
                index += 1 
            if index >= len(pos_indices):
                # print([str(box) for box in pos_boxes])
                return pos_boxes[(int)(-len(pos_boxes)/2):]
            # used_vals.append(index)
            # while index in used_vals or pos_boxes[index] in temp.boxes:
            #    index = random.randrange(len(pos_boxes))
        return temp.boxes

    # def get_parents_from_sorted(self):
    #     packs_next_gen = set()
    #     x = 0
    #     while len(packs_next_gen) < self.pop_size / 2:
    #         if (random.randrange((int)(self.pop_size / 2)) + x)**2 < (self.pop_size / 2)**2:
    #             packs_next_gen.add(self.backpacks[x])
    #         x = x + 1 if x < len(self.backpacks) - 1 else 0
    #     return packs_next_gen

    def mate_packs(self, pack1, pack2):
        return Backpack(self.gen_rand_box_combo(pack1.boxes + pack2.boxes))

    def create_new_backpacks(self):
        new_packs = []
        pair_list = [i for i in range(len(self.backpacks))]*4
        random.shuffle(pair_list)
        for x in range(0, len(pair_list), 2):
            new_packs.append(self.mate_packs(self.backpacks[pair_list[x]], self.backpacks[pair_list[x+1]]))
        return new_packs

    def get_next_gen(self):
        packs_next_gen = []
        self.backpacks.sort(key=lambda x: x.importance, reverse=True)
        del self.backpacks[(int)(-len(self.backpacks)/2):]
        next_gen = self.create_new_backpacks()
        next_gen.sort(key=lambda x: x.importance, reverse=True)
        self.backpacks = next_gen
        return self.backpacks[0]
        
    def genetic_alg(self):
        while self.generation < self.max_gen:
            print(self.get_next_gen())
            self.generation += 1


pop = Population()
# pop.get_next_gen()
pop.genetic_alg()