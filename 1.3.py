graph = {
  '1' : ['2','3'],
  '2' : ['1', '6'],
  '3' : ['1','4', '5'],
  '4' : ['3'],
  '5' : ['3','8','7'],
  '6' : ['2'],
  '7' : ['5'],
  '8' : ['5']
}

visited =[]
queue = []

def bfs(visited, graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end = ' ')
        for v in graph[m]:
            if v not in visited:
                visited.append(v)
                queue.append(v)

bfs(visited,graph,'2')