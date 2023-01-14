#!/usr/bin/python


rmats = (
 (( 1, 0, 0), ( 0, 1, 0), ( 0, 0, 1)),
 (( 1, 0, 0), ( 0,-1, 0), ( 0, 0,-1)),
 (( 1, 0, 0), ( 0, 0,-1), ( 0, 1, 0)),
 (( 1, 0, 0), ( 0, 0, 1), ( 0,-1, 0)),

 ((-1, 0, 0), ( 0,-1, 0), ( 0, 0, 1)),
 ((-1, 0, 0), ( 0, 1, 0), ( 0, 0,-1)),
 ((-1, 0, 0), ( 0, 0,-1), ( 0,-1, 0)),
 ((-1, 0, 0), ( 0, 0, 1), ( 0, 1, 0)),

 (( 0, 0, 1), ( 1, 0, 0), ( 0, 1, 0)),
 (( 0, 0,-1), ( 1, 0, 0), ( 0,-1, 0)),
 (( 0, 1, 0), ( 1, 0, 0), ( 0, 0,-1)),
 (( 0,-1, 0), ( 1, 0, 0), ( 0, 0, 1)),

 (( 0, 0, 1), (-1, 0, 0), ( 0,-1, 0)),
 (( 0, 0,-1), (-1, 0, 0), ( 0, 1, 0)),
 (( 0,-1, 0), (-1, 0, 0), ( 0, 0,-1)),
 (( 0, 1, 0), (-1, 0, 0), ( 0, 0, 1)),

 (( 0, 1, 0), ( 0, 0, 1), ( 1, 0, 0)),
 (( 0,-1, 0), ( 0, 0,-1), ( 1, 0, 0)),
 (( 0, 0,-1), ( 0, 1, 0), ( 1, 0, 0)),
 (( 0, 0, 1), ( 0,-1, 0), ( 1, 0, 0)),

 (( 0,-1, 0), ( 0, 0, 1), (-1, 0, 0)),
 (( 0, 1, 0), ( 0, 0,-1), (-1, 0, 0)),
 (( 0, 0,-1), ( 0,-1, 0), (-1, 0, 0)),
 (( 0, 0, 1), ( 0, 1, 0), (-1, 0, 0)),
)


def parse(inp):

  observations = [[tuple(map(int, ln.split(','))) for ln in s.split('\n')[1:]]
                  for s in inp.read().strip().split('\n\n')]

  return Analyser(observations)


def matmul(mat, vec):

  return tuple(sum(map(int.__mul__, row, vec)) for row in mat)


def crossdiff(first, second):

  return ((a-i, b-j, c-k) for a, b, c in first for i, j, k in second)


def manhattan(data):

  dist = []

  for a, b, c in data:
    for i, j, k in data:
      dist.append(abs(a-i) + abs(b-j) + abs(c-k))

  return dist


class Analyser(object):

  _beacons  = None
  _scanners = None


  def __init__(self, data):

    self.data = data


  def build(self):

    data = self.data[:]
    done = [0]
    perm = [[[matmul(mat, vec) for vec in ent]
             for mat in rmats] for ent in data]
    scan = {(0,0,0)}

    for first in done:
      todo = [n for n in range(len(data)) if n not in done]
      for second in todo:
        for new in perm[second]:
          if second in done: break
          diff   = crossdiff(data[first], new)
          counts = dict()

          for offset in diff:
            cnt = counts[offset] = counts.get(offset, 0) + 1
            if cnt == 12:
              a, b, c = offset
              data[second] = list(crossdiff(new, [(-a, -b, -c)]))
              scan.add(offset)
              done.append(second)
              break

    self._beacons  = set(sum(data, []))
    self._scanners = scan


  def beacons(self):

    if self._beacons is None:
      self.build()

    return self._beacons


  def scanners(self):

    if self._scanners is None:
      self.build()

    return self._scanners


def part_1(data):

  return len(data.beacons())


def part_2(data):

  return max(manhattan(data.scanners()))
 

if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

