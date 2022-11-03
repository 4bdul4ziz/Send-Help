graph = {
    "a": ["b", "c", "d"],
    "b": ["e", "f"],
    "c": ["g", "h"],
    "d": ["i", "j"],
    "e": ["k", "l"],
    "f": ["m"],
    "m": [],
    "g": ["n"],
    "n": [],
    "h": ["o"],
    "o": [],
    "i": ["p", "q"],
    "q": [],
    "j": ["r"],
    "r": [],
    "k": ["s"],
    "s": [],
    "l": ["t"],
    "t": [],
    "p": ["u"],
    "u": [],
}
path = []


def dfs(graph, start_node, goal):
    if start_node not in path:
        path.append(start_node)
        if start_node == goal:
            print(path)
        else:
            for neighbour in graph[start_node]:
                dfs(graph, neighbour, goal)
        path.pop()


visited_traversal = set()


def dfs_traversal(visited_traversal, graph, start_node, goal):
    if goal not in visited_traversal:
        if start_node not in visited_traversal:
            print(start_node)
            visited_traversal.add(start_node)
            for neighbour_traversal in graph[start_node]:
                dfs_traversal(visited_traversal, graph, neighbour_traversal, goal)


dfs_traversal(visited_traversal, graph, "a", "n")
print("Depth-First Search path: ")
print("DFS traversal is : ")


k = dfs(graph, "a", "n")
l = dfs_traversal(visited_traversal, graph, "a", "n")

""" for i in range(len(k)):
 if i== (len(k)-1):
    print(k[i])
 else:
    print(k[i],end="-")
print("DFS cost: ",cost) """
