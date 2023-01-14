#!/usr/bin/python


def parse(inp):

  return inp.read().splitlines()


def part_1(data):

  T       = list(zip(*data))
  gamma   = int(''.join(str(int(col.count('1')>len(col)//2)) for col in T), 2)
  epsilon = gamma ^ 2**len(T)-1

  return gamma * epsilon


def get_rating(data, func):

  T     = list(zip(*data))
  lines = set(range(len(data)))

  for col in T:
    sel   = [col[l] for l in lines]
    keep  = str(int(func(sel.count('1'), sel.count('0'))))
    lines = {l for l in lines if col[l] == keep}

    if len(lines) == 1:
      return int(data[lines.pop()], 2)


def part_2(data):

  oxygen = get_rating(data, int.__ge__)
  cotwo  = get_rating(data, int.__lt__)

  return oxygen * cotwo


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

