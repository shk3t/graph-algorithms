MAX_INT = 10**9


def to_graph(relations):
    graph = {}
    for relation in relations:
        graph[relation[0]] = set()
        graph[relation[1]] = set()
    for relation in relations:
        graph[relation[0]].add(relation[1])
        graph[relation[1]].add(relation[0])
    return graph


def to_weighted_graph(relations):
    graph = {}
    for relation in relations:
        graph[relation[0]] = set()
        graph[relation[1]] = set()
    for relation in relations:
        graph[relation[0]].add((relation[1], relation[2]))
        graph[relation[1]].add((relation[0], relation[2]))
    return graph


def to_found_path(destination, history):
    path = []
    node = destination
    while node:
        path.append(node)
        node = history[node]
    return path[::-1]
