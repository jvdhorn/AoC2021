#!/usr/bin/python

def counter():

  n = 0
  while True:
    yield n
    n += 1


def get_paths(maze):

  conn = dict()

  for i, row in enumerate(maze):
    for j, col in enumerate(row):
      if isinstance(col, int):
        neighbours = [maze[i-1][j], row[j-1], row[j+1], maze[i+1][j]]
        conn[col]  = [n for n in neighbours if n is not None]

  paths = dict()

  for x in conn:
    queue   = [(x,frozenset())]
    visited = dict()

    while queue:
      nxt, path = queue.pop(0)
      visited.update({nxt:path})

      for y in conn[nxt]:
        if y not in visited:
          queue.append((y, path|{y}))

    paths[x] = visited

  return paths


def parse(inp):

  return inp.read().splitlines()


def initialize(inp):

  count = counter()
  maze  = [[next(count) if c>='.' else None for c in row] for row in inp]
  state = tuple(x for c, x in sorted(zip(''.join(inp),sum(maze,[]))) if c>'.')
  paths = get_paths(maze)

  return state, paths


def simulate(state, paths):

  skip    = {p for p in paths if list(map(len,paths[p].values())).count(1)==3}
  rooms   = tuple(zip(*list(zip(*[iter(sorted(state))]*len(skip)))[::-1]))
  target  = tuple(map(frozenset, rooms))
  hallway = tuple(set(range(min(sum(rooms,())))) - skip)
  state   = tuple(map(frozenset,zip(*[iter(state)]*(len(state)//len(skip)))))

  queue   = {state}
  visited = {state:0}
  inf     = float('inf')

  while queue:
    state = queue.pop()

    for kind, positions in enumerate(state):
      todo = set(positions)

      for goal in rooms[kind]:
        if goal in todo: todo.remove(goal)
        else           : break

      for pos in todo:
        options = (rooms[kind][-len(todo)],)
        if pos not in hallway: options = options + hallway

        for dest in options:
          path  = paths[pos][dest]
          avail = not path & frozenset.union(*state)

          if avail:
            new_pos    = (positions - {pos} | {dest},)
            new_state  = state[:kind] + new_pos + state[kind+1:]
            new_energy = visited.get(state, 0) + len(path) * 10 ** kind

            if visited.get(new_state, inf) > new_energy:
              queue.add(new_state)
              visited.update({new_state:new_energy})

            if dest in target[kind]: break

  return visited.get(target)


def part_1(data):

  state, paths = initialize(data)

  return simulate(state, paths)


def part_2(data):

  data         = data[:3] + ['  #D#C#B#A#','  #D#B#A#C#'] + data[3:]
  state, paths = initialize(data)

  return simulate(state, paths)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

