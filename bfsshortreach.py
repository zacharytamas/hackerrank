# 2015-10-28

# Variables
# T = Number of test cases
# N = Number of nodes in graph
# M = Number of edges in graph
# S = Starting node (index)

# The weight of each edge is a constant value
WEIGHT = 6


def initArray(size, child=None):
  """
  >>> initArray(5)
  [[], [], [], [], []]
  >>> initArray(2, -1)
  [-1, -1]
  """
  if child is None:
    child = []
  return [child for i in range(size)]


def allocateEdges(graph, edges):
  """
  >>> graph = [[], [], [], []]
  >>> edges = [(0, 1), (0, 2)]
  >>> allocateEdges(graph, edges)
  [[1, 2], [], [], []]
  """
  for a, b in edges:
    graph[a].append(b)
  return graph


def explore(graph, S):
  """Explores the graph, compiling a list of lengths to each node.
  >>> graph = [[1, 2], [], [], []]
  >>> S = 0
  >>> r = explore(graph, S)

  The length of the array returned should be one less than
  the number of nodes in the graph.
  >>> len(r) == (len(graph) - 1)
  True

  And the result should be this.
  >>> r == [6, 6, -1]
  True
  """
  return []


def solve(N, edges, S):
  """
  >>> edges = [(0, 1), (0, 2)]
  >>> solve(4, edges, 0)
  6 6 -1
  """

  graph = initArray(N)
  allocateEdges(graph, edges)


def main():
  pass


if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
