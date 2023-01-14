#!/usr/bin/python


def parse(inp):

  return [line(ln) for ln in inp]


def line(coords):

  i, j = coords.split('->')

  a, c = map(int, i.split(','))
  b, d = map(int, j.split(','))

  x = tuple(range(a,b+1) if a < b else range(a,b-1,-1) if a > b else [a])
  y = tuple(range(c,d+1) if c < d else range(c,d-1,-1) if c > d else [c])

  if len(x) == 1: x = x * len(y)
  if len(y) == 1: y = y * len(x)

  return frozenset(map(complex, x, y))


def intersect(lines):

  intersections = set()

  for i, a in enumerate(lines):
    for b in lines[i+1:]:
      intersections |= a & b

  return len(intersections)


def part_1(data):

  nondiag = [frozenset(k)|{i,j} for i, j, *k in data
             if i.real == j.real or i.imag == j.imag]

  return intersect(nondiag)


def part_2(data):

  return intersect(data)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

