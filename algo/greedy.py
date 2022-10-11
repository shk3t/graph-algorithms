from utils import to_found_path


def greedy(frm, destination, wgraph):
    search_order = []
    path = {frm: None}
    total_distance = 0

    def grab(current):
        nonlocal total_distance
        search_order.append(current)

        if current == destination:
            return True

        neighbours = sorted(
            [(neigh, dist) for (neigh, dist) in wgraph[current] if neigh not in path],
            key=(lambda el: el[1]),
        )
        for neighbour, distance in neighbours:
            path[neighbour] = current
            total_distance += distance
            found = grab(neighbour)
            if found:
                return True
            del path[neighbour]
            total_distance -= distance

    grab(frm)
    return {
        "Протяженность пути": total_distance,
        "Найденный путь": to_found_path(destination, path),
        "Этапы поиска": search_order,
    }
