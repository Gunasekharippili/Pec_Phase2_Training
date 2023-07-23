# queries 4
# a->b
# b->c
# c->d
# c->e
# input = a->d
# output path found or not

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
    print(visited, end="->")


graph = {
    "a" : "b",
    "b" : "c",
    "c" : ["d", "e"]
}
print(BFS(graph, "a"))