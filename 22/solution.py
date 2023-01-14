#!/usr/bin/python


def parse(inp):

  rects = []
  for ln in inp:
    state, ranges = ln.split()
    state  = state == 'on'
    ranges = [tuple(map(int,ax.strip('xyz=').split('..')))
              for ax in ranges.split(',')]
    rects.append(sum(ranges, (state,)))

  return rects


class Interval(set):

  def on(self, rng):

    x, y = rng
    for i, j in self.copy():
      if i <= x <= j+1 or x <= i <= y+1:
        x, y = min(i,x), max(j,y)
        self.remove((i,j))
    self.add((x,y))

  def off(self, rng):

    x, y = rng
    for i, j in self.copy():
      if x <= i <= j+1 <= y+1:
        self.remove((i,j))
      elif i <= x <= y+1 <= j+1:
        self.remove((i,j))
        self.add((i,x-1))
        self.add((y+1,j))
      elif i <= x <= j + 1:
        self.remove((i,j))
        self.add((i,x-1))
      elif i <= y <= j + 1:
        self.remove((i,j))
        self.add((y+1,j))

  def size(self):

    return sum(j - i + 1 for i, j in self)


def process1d(data):

  intervals = dict()

  for state, a, b, c, d, e, f in data:
    for x in range(c, d+1):
      for y in range(e, f+1):
        itv = intervals.get((x,y), Interval())
        if state: itv.on((a,b))
        else    : itv.off((a,b))
        intervals[(x,y)] = itv

  return sum(itv.size() for itv in intervals.values())


def part_1(data):

  data = [rect for rect in data if -50 <= min(rect) <= max(rect) <= 50]

  return process1d(data)


class Rect(set):

  def on(self, rect):

    rect = Rect({rect})

    for item in self:
      rect.off(item)

    self.update(sec_reduce(rect))

  def off(self, rect):

    g, h, i, j, k, l = rect

    for item in self.copy():
      u, v, w, x, y, z = item

      if not (h<u or g>v or j<w or i>x or l<y or k>z):

        a = ((u,min(v,g-1)),(max(u,g),min(v,h)),(max(u,h+1),v))
        b = ((w,min(x,i-1)),(max(w,i),min(x,j)),(max(w,j+1),x))
        c = ((y,min(z,k-1)),(max(y,k),min(z,l)),(max(y,l+1),z))
  
        sections = [p+q+r for p in a for q in b for r in c]
        sections.pop(13)
        sections = {s for s in sections
                    if s[0] <= s[1] and s[2] <= s[3] and s[4] <= s[5]}
  
        self.remove(item)
        self.update(sec_reduce(sections))

  def size(self):

    return sum((b-a+1) * (d-c+1) * (f-e+1) for a,b,c,d,e,f in self)


def sec_reduce(inp):

  inp = inp.copy()

  if len(inp) == 1:
    return inp

  while True:
    try:
      for first in inp:
        a,b,c,d,e,f = first
        for second in inp:
          g,h,i,j,k,l = second
          if (a,b,c,d) == (g,h,i,j) and f+1==k:
            inp.remove(first)
            inp.remove(second)
            inp.add((a,b,c,d,e,l))
          elif (c,d,e,f) == (i,j,k,l) and b+1==g:
            inp.remove(first)
            inp.remove(second)
            inp.add((a,h,c,d,e,f))
          elif (a,b,e,f) == (g,h,k,l) and d+1==i:
            inp.remove(first)
            inp.remove(second)
            inp.add((a,b,c,j,e,f))
      else:
        break

    except RuntimeError:
      pass

  return inp


def process3d(data):

  rect = Rect()

  for state, *new in data:
    new = tuple(new)
    if state: rect.on(new)
    else    : rect.off(new)

  return rect.size()


def part_2(data):

  return process3d(data)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

