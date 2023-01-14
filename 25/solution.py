#!/usr/bin/python


def parse(inp):

  south = set()
  east  = set()

  for i, row in enumerate(inp):
    for j, col in enumerate(row):
      if   col == 'v': south.add((i,j))
      elif col == '>': east.add((i,j))
  
  return (i+1,j), south, east


def vis(size, south, east):

  for x in range(size[0]):
    line = ['v' if (x,y) in south
       else '>' if (x,y) in east 
       else '.' for y in range(size[1])]
    print(''.join(line))


def part_1(data):

  (x, y), south, east = data

  count = 0
  go    = True

  while go:
    count += 1
    go     = False

    new_east  = set()
    union     = south | east
    for i, j in east:
      new = i, (j+1)%y
      if new in union:
        new_east.add((i, j))
      else:
        new_east.add(new)
        go = True
    east = new_east

    new_south = set()
    union     = south | east
    for i, j in south:
      new = (i+1)%x, j
      if new in union:
        new_south.add((i, j))
      else:
        new_south.add(new)
        go = True
    south = new_south

  return count


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

