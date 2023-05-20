
from PIL import Image, ImageDraw
import numpy as np
import numpy
import random
from PIL import Image
from numpy import asarray
ROWS = 30
COLUMNS = 50
START = [ROWS-28, COLUMNS-28]
END = [ROWS-28,COLUMNS-48]
# end = [rows-1,columns-1]
START = [2, 2]
END = [28,48]

def get_less_walls(_a):
   for i in range(rows):
      for j in range(columns):
        if _a[i][j] == 1:
          if random.randint(0, 1) == 0: _a[i][j] = 0
          else: _a[i][j] = 1

def get_more_walls(_a):
   for i in range(rows):
      for j in range(columns):
        if _a[i][j] == 0:
          if random.randint(0, 10) == 0: _a[i][j] = 1
          else: _a[i][j] = 0

def get_random_points(_a):
  start = [-1, -1]
  end = [-1, -1]
  condition_1 = 0
  condition_2 = 0
  while(condition_1 == 0):
    start_1 = random.randint(0, rows-1)
    start_2 = random.randint(0, columns-1)
    if _a[start_1][ start_2] == 0: 
       start = [start_1, start_2]
       condition_1 = 1

  while(condition_2 == 0):
    end_1 = random.randint(0, rows-1)
    end_2 = random.randint(0, columns-1)
    if _a[end_1][ end_2] == 0: 
       end = [end_1, end_2]
       condition_2 = 1
  return start, end


def make_step(k):
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == k:
        if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:
          m[i-1][j] = k + 1
        if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:
          m[i][j-1] = k + 1
        if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:
          m[i+1][j] = k + 1
        if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:
           m[i][j+1] = k + 1

def print_m(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print( str(m[i][j]).ljust(2),end=' ')
        print()

def draw_matrix(a,m, the_path = []):
    im = Image.new('RGB', (zoom * len(a[0]), zoom * len(a)), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i in range(len(a)):
        for j in range(len(a[i])):
            color = (255, 255, 255)
            r = 0
            if a[i][j] == 1:
                color = (0, 0, 0)
            if i == start[0] and j == start[1]:
                color = (0, 255, 0)
                r = borders
            if i == end[0] and j == end[1]:
                color = (0, 255, 0)
                r = borders
            draw.rectangle((j*zoom+r, i*zoom+r, j*zoom+zoom-r-1, i*zoom+zoom-r-1), fill=color)
            if m[i][j] > 0:
                r = borders
                draw.ellipse((j * zoom + r, i * zoom + r, j * zoom + zoom - r - 1, i * zoom + zoom - r - 1),
                               fill=(255,0,0))
    for u in range(len(the_path)-1):
        y = the_path[u][0]*zoom + int(zoom/2)
        x = the_path[u][1]*zoom + int(zoom/2)
        y1 = the_path[u+1][0]*zoom + int(zoom/2)
        x1 = the_path[u+1][1]*zoom + int(zoom/2)
        draw.line((x,y,x1,y1), fill=(255, 0,0), width=5)
    draw.rectangle((0, 0, zoom * len(a[0]), zoom * len(a)), outline=(0,255,0), width=2)
    images.append(im)

images = []

# a = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0 ,0, 0, 0, 1, 0, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1 ,1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0 ,0, 0, 0, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]

## RANDOM
# a = numpy.random.random_integers(0, 1, (rows, columns))
# a = a.tolist()
# get_less_walls(a)
# a[start[0]][start[1]] = 0
# a[end[0]][end[1]] = 0


img = Image.open('magazyn_mniejszy.png')
a = asarray(img)
shape = a.shape
rows = shape[0]
columns = shape[1]
a = a.tolist()

for i in range(rows):
    for j in range(columns):
        if a[i][j][0] == 255: a[i][j] = 0
        else: a[i][j] = 1
get_more_walls(a)
start, end = get_random_points(a)
zoom = 20
borders = 6
m = []

for i in range(len(a)):
    m.append([])
    for j in range(len(a[i])):
        m[-1].append(0)
i,j = start
m[i][j] = 1
k = 0
while m[end[0]][end[1]] == 0:
    if (k <= rows*columns):
      k += 1
      make_step(k)
      draw_matrix(a, m)
    else: break


i, j = end
k = m[i][j]
the_path = [(i,j)]
while k > 1:
  if i > 0 and m[i - 1][j] == k-1:
    i, j = i-1, j
    the_path.append((i, j))
    k-=1
  elif j > 0 and m[i][j - 1] == k-1:
    i, j = i, j-1
    the_path.append((i, j))
    k-=1
  elif i < len(m) - 1 and m[i + 1][j] == k-1:
    i, j = i+1, j
    the_path.append((i, j))
    k-=1
  elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
    i, j = i, j+1
    the_path.append((i, j))
    k -= 1
  draw_matrix(a, m, the_path)

if k == 0: print("/////////// Nie znaleziono rozwiązań ////////////")


for i in range(rows*columns):
    if i % 2 == 0:
        draw_matrix(a, m, the_path)
    else:
        draw_matrix(a, m)

# print_m(m)
# print(the_path)


images[0].save('opis.gif',
               save_all=True, append_images=images[1:],
               optimize=False, duration=1, loop=0)

print("GIF IS READY")