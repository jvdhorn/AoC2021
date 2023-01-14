#!/usr/bin/python


class MONAD(object):

  ops = {
    'add': int.__add__,
    'mul': int.__mul__,
    'div': lambda a,b: a//b if a>0<b or a<0>b else -(-a//b),
    'mod': int.__mod__,
    'eql': int.__eq__,
  }

  def __init__(self, instr):

    self.instr = instr

  def __call__(self, number, z=None):

    number = iter(number)
    var    = dict.fromkeys('wxyz', 0)
    if z is not None: var.update(z=z)

    for op, *inp in self.instr:
      if op == 'inp':
        try:
          var[inp[0]] = int(next(number))
        except StopIteration:
          return var
      else:
        a, b = inp
        A = var[a]
        B = var[b] if b in var else int(b)
        if not (op == 'div' and B == 0) and not (op == 'mod' and (A<0 or B<=0)):
          var[a] = int(self.ops[op](A,B))

    return var


def parse(inp):

  programs = []
  for ln in inp:
    if ln.startswith('inp'): programs.append([])
    programs[-1].append(ln.split())

  return programs


def part_1(data):

  func = MONAD(sum(data,[]))

  curr = (9,) * 14
  best = func(curr)['z']

  q = [(best, curr)]

  while q:
    best, curr = q.pop()

    for i in range(13,-1,-1):
      for j in range(9,0,-1):
        inp = curr[:i]+(j,)+curr[i+1:]
        res = func(inp)['z']

        if res < best * 2:
          best = res
          q.append((res,inp))

          if res == 0:
            return ''.join(map(str,inp))


def part_2(data):

  func = MONAD(sum(data,[]))

  curr = (1,) * 14
  best = func(curr)['z']

  q = [(best, curr)]

  while q:
    best, curr = q.pop()

    for i in range(13,-1,-1):
      for j in range(1,10):
        inp = curr[:i]+(j,)+curr[i+1:]
        res = func(inp)['z']

        if res < best:
          q.append((res,inp))

          if res == 0:
            return ''.join(map(str,inp))


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

