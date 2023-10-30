
visited = set()


def dfs(adj_list, root):
    if root not in visited:
        visited.add(root)
        for child in adj_list[root]:
            dfs(adj_list, child)


in_adj_list = {}
while True:
    node = input("Enter a node (or type 'done' to finish): ").strip()
    if node == 'done':
        break
    c = input(f"Enter the child node for {node} separate with space: ").strip().split()
    in_adj_list[node] = c

if in_adj_list:
    r = input("Enter your root node: ")
    dfs(in_adj_list, r)
    print(visited)
else:
    print("Yor graph is empty!")
