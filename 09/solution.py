#!/usr/bin/python


def parse(inp):

  grid = dict()

  for i, row in enumerate(inp):
    for j, col in enumerate(row.strip()):
      grid[i,j] = int(col)

  return grid


def part_1(data):

  total = 0
  pts   = set(data)

  for i, j in data:
    neighbours = {(i+1,j), (i-1,j), (i,j+1), (i,j-1)} & pts

    if all(data[i,j] < data[x,y] for x, y in neighbours):
      total += data[i,j] + 1

  return total


def part_2(data):

  data   = data.copy()
  basins = []
  pts    = set(data)

  while set(data.values()) - {9}:
    start = next(pos for pos in data if data[pos] < 9)
    queue = [start]

    for i, j in queue:
      data.pop((i,j))
      neighbours = {(i+1,j), (i-1,j), (i,j+1), (i,j-1)} & pts

      for x, y in neighbours:
        if (x,y) not in queue and data[x,y] < 9:
          queue.append((x,y))

    basins.append(len(queue))

  *_, a, b, c = sorted(basins)

  return a * b * c


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

