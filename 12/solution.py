#!/usr/bin/python


def parse(inp):

  graph = dict()
  
  for ln in inp:
    a, b     = ln.strip().split('-')
    graph[a] = graph.get(a, frozenset()) | {b}
    graph[b] = graph.get(b, frozenset()) | {a}

  return graph


def search(graph, dup=False):

  graph = {key:val-{'start'} for key, val in graph.items()}
  queue = {('start',)}
  count = 0

  while queue:
    path = queue.pop()
    for dest in graph[path[-1]]:
      is_valid = dest.isupper() or dest not in path
      if dup:
        check    = sorted(filter(str.islower, path))
        is_valid = is_valid or sorted(set(check)) == check
      if dest == 'end': count += 1
      elif is_valid:
        queue.add(path+(dest,))

  return count


def part_1(data):

  return search(data)


def part_2(data):

  return search(data, dup=True)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

