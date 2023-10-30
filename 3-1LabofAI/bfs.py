from queue import Queue

visited = {}
parent = {}
level = {}
bfs_traversal_list = []
queue = Queue()


def bfs(adj_list, s):
    for n in adj_list.keys():
        visited[n] = False
        parent[n] = None
        level[n] = -1

    visited[s] = True
    level[s] = 0
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        bfs_traversal_list.append(u)
        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u] + 1
                queue.put(v)


in_adj_list = {}

while True:
    node = input("Enter your a node (or type 'done' to finish): ").strip()
    if node == 'done':
        break
    child = input(f"Enter your child node for {node} separate with space: ").strip().split()
    in_adj_list[node] = child

src = input("Enter the source node: ")
bfs(in_adj_list, src)
print(bfs_traversal_list)
