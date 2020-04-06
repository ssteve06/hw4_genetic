from Backpack import Backpack
from Box import Box
import random
 
pos_boxes = [Box(1, 20, 6), Box(2, 30, 5), Box(3, 60, 8), Box(4, 90, 7), Box(5, 50, 6), Box(6, 70, 9),
             Box(7, 30, 4), Box(8, 30, 5), Box(9, 70, 4), Box(10, 20, 9), Box(11, 20, 2), Box(12, 60, 1)]

class Population():
    generation = 0
    backpacks = []
    
    def __init__(self, pop_size=20, max_gen=20, percent_mutate=20):
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.mutate_chance = percent_mutate
        for _ in range(self.pop_size):
            self.backpacks.append(Backpack(self.gen_rand_box_combo(pos_boxes)))

    def gen_rand_box_combo(self, pos_boxes):
        used_boxes = []
        pos_indices = [i for i in range(len(pos_boxes))]
        random.shuffle(pos_indices)
        temp = Backpack()
        temp.reset_boxes()
        count = 0
        index = pos_indices[count]

        while temp.add_box(pos_boxes[index]):
            used_boxes.append(pos_boxes[index])
            while pos_boxes[index] in used_boxes:
                count += 1 
                if count >= len(pos_boxes):
                    return temp.boxes
                index = pos_indices[count]
                
                assert count < len(pos_indices)
            
        return temp.boxes


    def mutate_child(self, child):
        new_box = pos_boxes[random.randrange(len(pos_boxes))]
        remove_index = random.randrange(len(child.boxes))
        if not new_box in child.boxes and child.swap_box(remove_index, new_box):
            return child
        return self.mutate_child(child)

    def mate_packs(self, pack1, pack2):
        if len(pack1.boxes) == len(pack2.boxes):
            for box in pack1.boxes:
                if not box in pack2.boxes:
                    break
            else:
                return pack1

        return Backpack(self.gen_rand_box_combo(pack1.boxes + pack2.boxes))

    def create_new_backpacks(self):
        new_packs = []
        for _ in range(self.pop_size):
            child = self.mate_packs(self.backpacks[random.randrange(len(self.backpacks))],
                                    self.backpacks[random.randrange(len(self.backpacks))])
            if random.randint(0, 100) <= self.mutate_chance:
                child = self.mutate_child(child)
            new_packs.append(child)
        return new_packs

    def get_next_gen(self):
        self.backpacks.sort(key=lambda x: x.importance, reverse=True)
        self.backpacks = self.backpacks[:(int)(len(self.backpacks)/2)]
        next_gen = self.create_new_backpacks()
        next_gen.sort(key=lambda x: x.importance, reverse=True)
        self.backpacks = next_gen
        return self.backpacks[0]
        
    def genetic_alg(self):
        self.backpacks.sort(key=lambda x: x.importance, reverse=True)
        print("Fittest pack in original population had an importance of ", self.backpacks[0].importance)
        print(self.backpacks[0], end="\n\n")
        while self.generation < self.max_gen:
            self.get_next_gen()
            self.generation += 1
        print("Fittest pack in final population had an importance of ", self.backpacks[0].importance)
        print(self.backpacks[0])