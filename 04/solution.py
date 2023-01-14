#!/usr/bin/python


def parse(inp):

  seq, *boards = inp.read().split('\n\n')
  seq = list(map(int, seq.split(',')))
  boards = [[list(map(int,ln.split())) for ln in board.splitlines()]
            for board in boards]

  return seq, boards


def when(seq, board):

  called = [[seq.index(n) for n in ln] for ln in board]
  first  = min(map(max,called + list(zip(*called))))
  remain = sum(a for a, b in zip(sum(board,[]),sum(called,[])) if b > first)
  score  = remain * seq[first]

  return first, score


def part_1(data):

  seq, boards = data

  return min(when(seq, board) for board in boards)[1]


def part_2(data):

  seq, boards = data

  return max(when(seq, board) for board in boards)[1]


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

