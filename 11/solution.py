#!/usr/bin/python


def parse(inp):

  grid = dict()

  for i, row in enumerate(inp):
    for j, col in enumerate(row.strip()):
      grid[i,j] = int(col)

  return grid


def simulate(grid, lim=float('inf')):

  grid  = grid.copy()
  count = steps = 0

  while steps < lim:
    steps += 1
    flash  = []

    for octopus in grid:
      grid[octopus] += 1
      if grid[octopus] == 10: flash.append(octopus)

    for i, j in flash:
      for octopus in {(i+x,j+y) for x in (-1,0,1) for y in (-1,0,1)} & set(grid):
        grid[octopus] += 1
        if grid[octopus] == 10: flash.append(octopus)

    grid.update(dict.fromkeys(flash, 0))
    count += len(flash)

    if len(set(grid.values())) == 1:
      break

  return count, steps


def part_1(data):

  count, steps = simulate(data, 100)

  return count


def part_2(data):

  count, steps = simulate(data)

  return steps


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

