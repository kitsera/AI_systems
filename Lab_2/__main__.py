import queue
import time

class Position:
    def __init__(self, position):
        self.position = position
        self.childs = []
        self.parent = None
        self.depth = 0

    def __str__(self):
        return str(self.position[0:3]) + '\n' + str(self.position[3:6]) + '\n' + str(self.position[6:9])

    def get_position(self):
        return self.position

    def append_child(self, child):
        self.childs.append(child)
        child.set_parent(self.position)
        child.set_depth(self.depth+1)

    def get_childs(self):
        return self.childs

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def set_depth(self, depth):
        self.depth = depth

    def get_depth(self):
        return self.depth



class BFS:
    def __init__(self, startPos, goalPos):
        self.goalPos = goalPos
        self.startPos = startPos
        self.queue = queue.Queue()
        self.queue.put(startPos)
        self.states = {}

    def algo_iter(self):
        queue_i = queue.Queue()
        queue_i.put(Position(self.startPos))
        states = []
        while not queue_i.empty():
            self.position = queue_i.get()
            states.append(self.position.get_position())

            if self.position.get_position() == self.goalPos:
                print(self.position)
                print("Глибина, на якій знайдено рішення: " + str(self.position.get_depth()))
                print("Кількість станів в базі: " + str(len(states)))
                global time_init
                print("Час для знаходження: " + str(time.time()-time_init))
                return True

            self.zero = self.find_zero()
            if self.move_left() != 0 and self.move_left():
                left_child = Position(self.move_left())
                self.position.append_child(left_child)

            if self.move_down() != 0 and self.move_down():
                down_child = Position(self.move_down())
                self.position.append_child(down_child)

            if self.move_right() != 0 and self.move_right():
                right_child = Position(self.move_right())
                self.position.append_child(right_child)

            if self.move_up() != 0 and self.move_up():
                up_child = Position(self.move_up())
                self.position.append_child(up_child)
            for child in self.position.get_childs():
                if child.get_position() not in states:
                    queue_i.put(child)
                    states.append(child.get_position())


    def move_up(self):
        if self.zero > 2:
            new_pos = list(self.position.get_position())
            new_pos[self.zero] = self.position.get_position()[self.zero - 3]
            new_pos[self.zero - 3] = 0
            return new_pos
        else:
            return 0

    def move_right(self):
        if self.zero % 3 != 2:
            new_pos = list(self.position.get_position())
            new_pos[self.zero] = self.position.get_position()[self.zero + 1]
            new_pos[self.zero + 1] = 0
            return new_pos
        else:
            return 0

    def move_down(self):
        if self.zero < 6:
            new_pos = list(self.position.get_position())
            new_pos[self.zero] = self.position.get_position()[self.zero + 3]
            new_pos[self.zero + 3] = 0
            return new_pos
        else:
            return 0

    def move_left(self):
        if self.zero % 3 != 0:
            new_pos = list(self.position.get_position())
            new_pos[self.zero] = self.position.get_position()[self.zero - 1]
            new_pos[self.zero - 1] = 0
            return new_pos
        else:
            return 0

    def find_zero(self):
        return self.position.get_position().index(0)


init_pos = [4, 1, 8, 6, 0, 5, 7, 3, 2]
mp = [1, 2, 3, 0, 4, 5, 6, 7, 8]
goal_pos = [0, 1, 2, 3, 4, 5, 6, 7, 8]

bfs = BFS(init_pos, goal_pos)
time_init = time.time()
bfs.algo_iter()