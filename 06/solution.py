#!/usr/bin/python


def parse(inp):

  return list(map(int, inp.read().split(',')))


def simulate(fish, days):

  state = [fish.count(t) for t in range(9)]

  for _ in range(days):
    state     = state[1:] + state[:1]
    state[6] += state[-1]

  return sum(state)


def part_1(data):

  return simulate(data, 80)


def part_2(data):

  return simulate(data, 256)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

