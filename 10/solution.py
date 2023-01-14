#!/usr/bin/python


def parse(inp):

  return inp.read().splitlines()


def dechunk(ln):

  cp = ''
  while cp != ln:
    cp = ln
    ln = ln.replace('()','').replace('[]','').replace('{}','').replace('<>','')

  return ln


def part_1(data):

  total   = 0
  scores  = {'':0, ')':3, ']':57, '}':1197, '>':25137}
  translt = dict.fromkeys((40,60,91,123))

  for line in data:
    reduced = dechunk(line).translate(translt)[:1]
    total  += scores[reduced]

  return total


def part_2(data):

  scores = '_([{<'
  total  = []

  for line in data:
    reduced = dechunk(line)
    valid   = not set(reduced) & set(')]}>')
    if valid:
      running = 0
      for c in reduced[::-1]: running = running * 5 + scores.index(c)
      total.append(running)

  return sorted(total)[len(total)//2]


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

