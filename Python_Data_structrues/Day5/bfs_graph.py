def BFS(graph, start):
    q = [start]
    visited = [start]

    while len(q) != 0:
        ele = q.pop(0)
        print(ele)
        for i in graph[ele]:
            if i not in visited:
                q.append(i)
                visited.append(i)
    print(visited)


graph = {
    "a" : ["b", "c"],
    "b" : ["a", "d"],
    "c" : ["a", "d"],
    "d" : ["b","c","e"],
    "e" : ["d"]
}
print(BFS(graph, "a"))