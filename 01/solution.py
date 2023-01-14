#!/usr/bin/python


def parse(inp):

  return list(map(int, inp.read().splitlines()))


def slide(data, window):

  merged = list(map(sum, zip(*[data[n:] for n in range(window)])))

  return sum(i < j for i, j in zip(merged, merged[1:]))


def part_1(data):

  return slide(data, 1)


def part_2(data):

  return slide(data, 3)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

