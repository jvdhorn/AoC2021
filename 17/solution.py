#!/usr/bin/python


def parse(inp):

  coords = inp.read().split()[-2:]

  return [list(map(int,ln.strip('xy=,').split('..'))) for ln in coords]


def part_1(data):

  (a,b), (c,d) = data

  return ~c * -c // 2


def get_xy(i, j, n):

  x = n * (2 * i + 1 - n) // 2 if n < i else i * (i + 1) // 2
  y = n * (2 * j + 1 - n) // 2

  return x, y


def part_2(data):

  (a,b), (c,d) = data
  collection   = set()

  for i in range(int((2*a)**.5), b+1):
    for j in range(c, -c):
      x = y = n = 0
      while x < b and y > c:
        x, y = get_xy(i, j, n)
        if a <= x <= b and c <= y <= d:
          collection.add((i,j))
          break
        n += 1

  return len(collection)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)
