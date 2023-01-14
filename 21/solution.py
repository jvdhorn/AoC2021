#!/usr/bin/python


def parse(inp):

  return [int(ln.split()[-1]) for ln in inp]


def repeats(players, mod, rng, split):

  rep    = list(range(1, rng+1)) * len(players) * split
  chunks = list(map(sum, zip(*[iter(rep)] * split)))
  scores = []

  for n, p in enumerate(players):
    rolls = chunks[n::len(players)]
    score = [(sum(rolls[:i+1]) + p - 1) % mod + 1 for i in range(len(rolls))]
    scores.append(score)

  return scores


def simulate(reps, trgt):

  need = []

  for rep in reps:
    repsum   = sum(rep)
    div, mod = divmod(trgt, repsum)
    add      = next(n for n in range(len(rep)) if sum(rep[:n]) >= mod)
    need.append(div * len(rep) + add)

  low    = min(need)
  win    = need.index(low)
  rolls  = [low] * (win + 1) + [low - 1] * (len(need) - win - 1)
  scores = []

  for rep, roll in zip(reps, rolls):
    div, mod = divmod(roll, len(rep))
    score    = div * sum(rep) + sum(rep[:mod])
    scores.append(score)

  return rolls, scores


def part_1(data):

  reps          = repeats(data, 10, 100, 3)
  rolls, scores = simulate(reps, 1000)
  result        = sum(rolls) * 3 * min(scores)

  return result


def sim_dirac(start, scores, score_lim=float('inf'), steps_lim=float('inf')):

  queue       = [(start, 0, 0, 1)]
  count_score = dict()
  count_steps = dict()

  while queue:
    pos, score, steps, N = queue.pop()

    if steps < steps_lim and score < score_lim:
      for nxt, n in scores[pos]:
        queue.append((nxt, score+nxt, steps+1, N * n))

    elif steps < steps_lim:
      count_score[steps] = count_score.get(steps, 0) + N

    elif score < score_lim:
      count_steps[score] = count_steps.get(score, 0) + N

  return count_score, count_steps


def part_2(data):

  throws = [0]
  for _ in range(3):
    throws = [i+j for i in throws for j in range(1,4)]
  throws = [(n, throws.count(n)) for n in sorted(set(throws))]

  scores = dict()
  for n in range(10):
    opts = [((n + throw) % 10 + 1, count) for throw, count in throws]
    scores[n+1] = opts

  a_steps, _ = sim_dirac(data[0], scores, 21)
  a_wins     = 0
  for i, x in a_steps.items():
    _, b_score = sim_dirac(data[1], scores, 21, i-1)
    a_wins    += x * sum(b_score.values())
  
  b_steps, _ = sim_dirac(data[1], scores, 21)
  b_wins     = 0
  for j, y in b_steps.items():
    _, a_score = sim_dirac(data[0], scores, 21, j)
    b_wins    += y * sum(a_score.values())
  
  return max(a_wins, b_wins)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

