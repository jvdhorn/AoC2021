#!/usr/bin/python


def parse(inp):

  state, instr = inp.read().split('\n\n')

  instr = [ln.split(' -> ') for ln in instr.splitlines()]

  return state, instr


def simulate(state, instr, times):

  pairs = dict()

  for a, b in zip(state, state[1:]):
    pairs[a+b] = pairs.get(a+b, 0) + 1

  for _ in range(times):
    mutations = dict()
    for (x, y), z in instr:
      cnt = pairs.get(x+y, 0)
      mutations[x+y] = mutations.get(x+y, 0) - cnt
      mutations[x+z] = mutations.get(x+z, 0) + cnt
      mutations[z+y] = mutations.get(z+y, 0) + cnt
    for pair, mut in mutations.items():
      pairs[pair] = pairs.get(pair, 0) + mut

  chars = dict()
  for (a, b), cnt in pairs.items():
    chars[a] = chars.get(a, 0) + cnt
    chars[b] = chars.get(b, 0) + cnt

  chars = {char:(chars[char]+1)//2 for char in chars}

  return max(chars.values()) - min(chars.values())


def part_1(data):

  state, instr = data

  return simulate(state, instr, 10)


def part_2(data):

  state, instr = data

  return simulate(state, instr, 40)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

