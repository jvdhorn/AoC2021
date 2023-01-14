#!/usr/bin/python


def parse(inp):

  return list(map(int, inp.read().split(',')))


def part_1(data):

  return min(sum(abs(i-j) for j in data) for i in range(max(data)+1))


def part_2(data):

  return min(sum(abs(i-j)*(abs(i-j)+1)//2 for j in data)
             for i in range(max(data)+1))


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

