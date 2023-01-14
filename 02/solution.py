#!/usr/bin/python


def parse(inp):

  instr = []

  for ln in inp:
    d, m = ln.split()
    if   d == 'forward': instr.append(complex(0, int(m)))
    elif d == 'down'   : instr.append(int(m))
    elif d == 'up'     : instr.append(-int(m))

  return instr


def part_1(data):

  result = sum(data)

  return int(result.real * result.imag)


def part_2(data):

  hor = ver = aim = 0

  for ins in data:
    hor += ins.imag
    ver += ins.imag * aim
    aim += ins.real
  
  return int(hor * ver)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

