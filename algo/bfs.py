from queue import Queue
from utils import to_found_path


def bfs(frm, destination, graph):
    search_order = []
    pathes = {frm: None}
    queue = Queue()
    queue.put(frm)

    while len(pathes) < len(graph):
        current = queue.get()
        search_order.append(current)

        if current == destination:
            break

        for neighbour in graph[current].difference(pathes.keys()):
            pathes[neighbour] = current
            queue.put(neighbour)

    return {
        "Найденный путь": to_found_path(destination, pathes),
        "Этапы поиска": search_order,
    }


def bidir_bfs(frm, destination, graph):
    bridge = None
    search_order = []
    pathes1 = {frm: None}
    pathes2 = {destination: None}
    queue1 = Queue()
    queue2 = Queue()
    queue1.put(frm)
    queue2.put(destination)

    while len(pathes1) + len(pathes2) < len(graph):
        current1 = queue1.get()
        current2 = queue2.get()
        search_order.append(current1)
        search_order.append(current2)

        if current1 in pathes2.keys():
            bridge = current1
            break

        for neighbour in graph[current1].difference(pathes1.keys()):
            pathes1[neighbour] = current1
            queue1.put(neighbour)

        if current2 in pathes1.keys():
            bridge = current2
            break

        for neighbour in graph[current2].difference(pathes2.keys()):
            pathes2[neighbour] = current2
            queue2.put(neighbour)

    return {
        "Найденный путь": to_found_path(bridge, pathes1)
        + to_found_path(bridge, pathes2)[1::-1],
        "Этапы поиска": search_order,
    }
