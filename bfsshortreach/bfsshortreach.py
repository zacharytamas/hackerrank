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
  >>> graph  # allocateEdges modifies in-place
  [[1, 2], [], [], []]
  """
  for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)


def generateNextFrontier(nodes, current_depth, visited):
  """
  >>> generateNextFrontier([0, 1], 1, [-1, -1])
  [(0, 2), (1, 2)]

  Now let's test that it will not add already visited nodes to the frontier.
  In this case, we have already visited the second node so it shouldn't be
  added to the frontier again.
  >>> generateNextFrontier([0, 1], 1, [-1, 6])
  [(0, 2)]
  """
  for i in nodes:
    if not visited.get(i):
      yield (i, current_depth + 1)
    else:
      print "_t_generateNextFrontier", "skipping", i


def markShortestDistance(distances, node_index, depth):
  """
  >>> distances = [-1, -1, -1]
  >>> node = 1
  >>> markShortestDistance(distances, node, 2)  # does in-place
  >>> distances
  [-1, 12, -1]

  Now let's try to mark a distance that is longer. It should ignore it.
  >>> markShortestDistance(distances, node, 3)
  >>> distances
  [-1, 12, -1]

  Now let's mark a shorter distance, which should replace the current shortest.
  >>> markShortestDistance(distances, node, 1)
  >>> distances
  [-1, 6, -1]
  """
  current = distances[node_index]
  distance = depth * WEIGHT

  if current == -1:  # If it's never been measured before, set it
    distances[node_index] = distance
  else:
    distances[node_index] = min(distances[node_index], distance)


def explore(graph, S):
  """Explores the graph, compiling a list of lengths to each node.
  >>> graph = [[1, 2], [], [], []]
  >>> S = 0
  >>> explore(graph, S)
  [0, 6, 6, -1]
  """

  # Initialize the distances array, all -1 at first, meaning no path.
  # We'll discover them soon.
  distances = initArray(len(graph), -1)
  distances[S] = 0  # The node has a distance of 0 from itself.
  visited = {}

  # Initialize the frontier with nodes that are reachable from
  # the beginning node S.
  frontier = list(generateNextFrontier(graph[S], 0, visited))

  print "_t_", frontier

  _t_frontier_count = 1

  while len(frontier):
    node, depth = frontier.pop(0)
    if visited.get(node):
      # print "_t_", "already visited", node, "skipping"
      continue
    visited[node] = True
    print node
    # if distances[node] != -1:
    #   continue
    markShortestDistance(distances, node, depth)
    frontier.extend(generateNextFrontier(graph[node], depth, visited))
    _t_frontier_count += 1

  return distances


def solve(N, edges, S):
  """
  >>> edges = [(0, 1), (0, 2)]
  >>> solve(4, edges, 0)
  [6, 6, -1]
  """

  graph = initArray(N)
  allocateEdges(graph, edges)
  result = explore(graph, S)

  # According to the output specs for this problem, we don't return the
  # distance from the starting element to itself, so let's remove it.
  del result[S]

  return result


def main():
  T = int(raw_input())

  for t in range(T):
    N, M = map(int, raw_input().split())
    edges = []
    for m in range(M):
      x, y = map(int, raw_input().split())
      edges.append((x - 1, y - 1))
    S = int(raw_input()) - 1
    result = solve(N, edges, S)
    for d in result:
      print d,
    print


if __name__ == '__main__':
  import doctest
  # doctest.testmod()
  main()
