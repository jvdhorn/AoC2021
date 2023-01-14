#!/usr/bin/python


def parse(inp):

  algo, imag = inp.read().split('\n\n')
  algo = [c=='#' for c in ''.join(algo.split())]
  grid = set()

  for i, row in enumerate(imag.split()):
    for j, c in enumerate(row):
      if c == '#': grid.add(complex(i,j))

  return algo, grid


def simulate(data, steps):

  order = ((256, -1-1j), (128, -1), (64, -1+1j), (32, -1j),
           (16, 0), (8, 1j), (4, 1-1j), (2, 1), (1, 1+1j))

  algo, grid = data

  flip = algo[0] and not algo[-1]

  for n in range(steps):
    new_grid = set()
    reals    = [int(item.real) for item in grid]
    imags    = [int(item.imag) for item in grid]

    for i in range(min(reals)-1, max(reals)+2):
      for j in range(min(imags)-1, max(imags)+2):
        x   = complex(i,j)
        ind = sum(p for p, ent in order if x + ent in grid)

        if ((not flip and algo[ind])
             or (flip and algo[ind^511 if n%2 else ind] == n%2)):
          new_grid.add(x)

    grid = new_grid

  return grid


def part_1(data):

  return len(simulate(data, 2))


def part_2(data):

  return len(simulate(data, 50))


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

