"Random Problem"
from random import randint


def MontyHall(x, change = True):
    counter_win = 0
    door_1 = 0
    door_2 = 0
    door_3 = 0
    for num in range(0, x):
        door = [1, 2, 3]
        winning_door = randint(1,3)
        initial_door = randint(1,3)
        door.pop(initial_door-1)
        if door[0] == winning_door:
            door.pop(1)
        else:
            door.pop(0)
        if (change):
            initial_door = door[0]
        if initial_door == winning_door:
            counter_win += 1
            if winning_door == 1:
                door_1 += 1
            elif winning_door == 2:
                door_2 += 1
            else:
                door_3 += 1
    print("You won",counter_win,"times out", x, "games when", 'switching your guess' if (change) else 'sticking to original guess')
    print("door 1 won",door_1,"times")
    print("door 2 won",door_2,"times")
    print("door 3 won",door_3,"times")
    return counter_win

sum_switch = 0
sum_keep = 0
for num in range(0, 10):
    sum_switch += MontyHall(100000, True)
    sum_keep += MontyHall(100000, False)
print("average for switching",sum_switch/10.0)
print("average for keeping",sum_keep/10.0)
