#!/usr/bin/python


def parse(inp):

  prep = [ln.split('|') for ln in inp.read().replace('|\n','|').splitlines()]
  data = {(tuple(a.split()),tuple(b.split())) for a, b in prep}

  return data


def decode(digits):

  digits  = sorted(digits, key=len)
  decoded = {1:digits[0], 7:digits[1], 4:digits[2], 8:digits[9]}

  for d in digits[6:9]:
    if len(set(d) & set(decoded[1])) == 1:
      decoded[6] = d
    elif len(set(d) & (set(decoded[1]) ^ set(decoded[4]))) == 2:
      decoded[9] = d
    else:
      decoded[0] = d
  for d in digits[3:6]:
    if len(set(d) & set(decoded[1])) == 2:
      decoded[3] = d
    elif len(set(d) & set(decoded[6])) == 5:
      decoded[5] = d
    else:
      decoded[2] = d

  return {frozenset(decoded[d]):d for d in decoded}


def part_1(data):

  return sum(len(val) in (2,3,4,7) for a, b in data for val in b)


def part_2(data):

  total = 0

  for key, digits in data:
    decoded = decode(key)
    values  = [decoded[frozenset(d)] for d in digits]
    total  += int(''.join(map(str,values)))

  return total


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

