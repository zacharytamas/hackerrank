
def formula(A, B):
  """Returns the next term in the series given two previous values.
  >>> formula(0, 1)
  1
  >>> formula(1, 1)
  2
  >>> formula(1, 2)
  5"""
  return B ** 2 + A


def nth_term(A, B, N):
  """
  >>> nth_term(0, 1, 5)
  5
  """
  result = None
  for i in range(N - 2):
    result = formula(A, B)
    A = B
    B = result
  return result


def main():
  args = map(lambda s: int(s), raw_input().split())
  print nth_term(*args)

if __name__ == '__main__':
  import doctest
  doctest.testmod()
