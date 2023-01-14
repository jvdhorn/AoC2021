#!/usr/bin/python


def parse(inp):

  return list(map(SFN, inp))


class SFN(list):

  def __init__(self, line=''):

    depth = 0

    for c in line:
      depth += c == '['
      depth -= c == ']'

      if c.isnumeric():
        self.append([depth, int(c)])

  def explode(self):

    for i, ((da, na), (db, nb)) in enumerate(zip(self, self[1:])):
      if da == db > 4:
        if i > 0:
          self[i-1][1] += na
        if i + 2 < len(self):
          self[i+2][1] += nb
        self[i:i+2] = [[da-1, 0]]

        return True

  def split(self):

    for i, (d, n) in enumerate(self):
      if n > 9:
        self[i:i+1] = [[d+1, n//2], [d+1, (n+1)//2]]

        return True

  def reduce(self):

    while True:
      if self.explode(): continue
      if not self.split(): break

  def __add__(self, other):

    new    = SFN()
    new[:] = [item[:] for item in self[:] + other[:]]
    if self and other:
      for item in new:
        item[0] += 1
    new.reduce()

    return new

  def magnitude(self):

    copy = [item[:] for item in self]

    while len(copy) > 1:
      for i, ((da, na), (db, nb)) in enumerate(zip(copy, copy[1:])):
        if da == db:
          copy[i:i+2] = [[da-1, 3*na + 2*nb]]
          break

    return copy[0][1]


def part_1(data):

  return sum(data, SFN()).magnitude()


def part_2(data):

  return max((a+b).magnitude() for a in data for b in data if a != b)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

