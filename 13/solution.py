#!/usr/bin/python


def parse(inp):

  coords, folds = inp.read().split('\n\n')
  inf    = float('inf')
  coords = {tuple(map(int,c.split(','))) for c in coords.splitlines()}
  folds  = [(inf,int(ln[13:]))[::[-1,1][ln[11]=='y']]
            for ln in folds.splitlines()]

  return coords, folds


def do_fold(coords, folds):

  for i, j in folds:
    for old in coords.copy():
      x, y = old
      if i < x: x = 2 * i - x
      if j < y: y = 2 * j - y
      coords.remove(old)
      coords.add((x,y))

  return coords


def vis(coords):

  x, y   = zip(*coords)
  result = ''

  for j in range(min(y), max(y)+1):
    for i in range(min(x), max(x)+1):
      result += '.#'[(i,j) in coords]
    result += '\n'

  return result.strip()


def part_1(data):

  coords, folds = data

  return len(do_fold(coords, folds[:1]))


def part_2(data):

  coords, folds = data

  return vis(do_fold(coords, folds))


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

