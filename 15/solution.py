#!/usr/bin/python


def parse(inp):

  grid = dict()

  for i, row in enumerate(inp):
    for j, col in enumerate(row.strip()):
      grid[(i,j)] = int(col)

  return grid


def search(grid):

  start = min(grid)
  end   = max(grid)

  queue = {(0, start)}
  visit = {start}

  while queue:
    nxt          = min(queue)
    score, (x,y) = nxt
    queue.remove(nxt)

    for d in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
      if d == end:
        return score+grid[d]
      elif d not in visit and d in grid:
        queue.add((score+grid[d], d))
        visit.add(d)


def part_1(data):

  return search(data)


def part_2(data):

  h, w = max(data)
  h   += 1
  w   += 1

  for x, y in data.copy():
    for i in range(5):
      for j in range(5):
        pos       = (x + i * h, y + j * w)
        val       = (data[(x,y)] + i + j - 1) % 9 + 1
        data[pos] = val

  return search(data)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

