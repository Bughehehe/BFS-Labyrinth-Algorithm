
from PIL import Image, ImageDraw
import numpy as np
import numpy
import random
from numpy import asarray
ROWS = 30
COLUMNS = 50

def get_random_points(_a):
  start = [-1, -1]
  end = [-1, -1]
  condition_1 = 0
  condition_2 = 0
  while(condition_1 == 0):
    start_1 = random.randint(0, ROWS-1)
    start_2 = random.randint(0, COLUMNS-1)
    if _a[start_1][ start_2] == 0: 
       start = [start_1, start_2]
       condition_1 = 1

  while(condition_2 == 0):
    end_1 = random.randint(0, ROWS-1)
    end_2 = random.randint(0, COLUMNS-1)
    if _a[end_1][ end_2] == 0: 
       end = [end_1, end_2]
       condition_2 = 1
  return start, end


def get_more_walls(_a):
   for i in range(ROWS):
      for j in range(COLUMNS):
        if _a[i][j] == 0:
          if random.randint(0, 5) == 0: _a[i][j] = 1
          else: _a[i][j] = 1

img = Image.open('magazyn_mniejszy.png')
a = asarray(img)
shape = a.shape
a = a.tolist()
# print(a[0][0][3])
for i in range(ROWS):
    for j in range(COLUMNS):
        if a[i][j][0] == 255: a[i][j] = 1
        else: a[i][j] = 0
start, end = get_random_points(a)
print (start, end)