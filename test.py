import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.Font('arial.ttf', 25)


# font = pygame.font.SysFont('arial', 25)

class Direction(Enum): # hướng di chuyển
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
direction = Direction.RIGHT
clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]  # --> v <-- ^
idx = clock_wise.index(direction)
idx
a= -1 / 4
print(float(a))
a = (5,6,7,8)
mini_sample = random.sample(a, 100)
print(mini_sample)