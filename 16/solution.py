#!/usr/bin/python


def parse(inp):

  binary = ''.join('{:04b}'.format(int(c, 16)) for c in inp.read().strip())
  stack  = [[]]

  while '1' in binary:
    ver    = int(binary[0:3], 2)
    typ    = int(binary[3:6], 2)
    binary = binary[6:]

    if typ == 4:
      rep = ''
      go  = True

      while go:
        go     = binary[0] == '1'
        rep   += binary[1:5]
        binary = binary[5:]

      stack[-1].append([ver, typ, int(rep, 2)])

    else:
      ind = binary[0]

      if ind == '0':
        val    = len(binary) - int(binary[1:16], 2) - 16
        binary = binary[16:]

      else:
        val    = int(binary[1:12], 2)
        binary = binary[12:]

      stack[-1].append([ver, typ, ind, val])
      stack.append([])

    while len(stack) > 1:
      (*_, prev), curr = stack[-2:]

      if ((prev[2] == '0' and prev[3] == len(binary))
       or (prev[2] == '1' and prev[3] == len(curr))):
        prev[2:] = stack.pop()

      else:
        break

  return stack[0][0]


def part_1(data):

  ver, typ, *args = data

  return ver if typ == 4 else ver + sum(map(part_1, args))


def prod(inp):

  product, *remaining = inp

  while remaining:
    product *= remaining.pop()

  return product


ops = [
  sum,
  prod,
  min,
  max,
  None,
  lambda x: int.__gt__(*x),
  lambda x: int.__lt__(*x),
  lambda x: int.__eq__(*x),
]


def part_2(data):

  ver, typ, *args = data

  return args[0] if typ == 4 else ops[typ](map(part_2, args))


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

