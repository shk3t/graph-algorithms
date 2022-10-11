from utils import MAX_INT, to_found_path


def min_A(frm, destination, wgraph, h):
    pathes = {frm: None}
    mins = {point: MAX_INT for point in wgraph.keys()}  # without h(n)
    mins[frm] = 0

    while len(pathes) < len(wgraph):
        current, cur_val = min(mins.items(), key=(lambda el: el[1] + h[el[0]]))
        if current == destination:
            break
        del mins[current]

        neighbours = {
            (neigh, dist) for (neigh, dist) in wgraph[current] if neigh in mins
        }
        for neighbour, distance in neighbours:
            new_f = cur_val + distance + h[neighbour]
            prev_f = mins[neighbour] + (neighbour in pathes and h[pathes[neighbour]])
            if new_f < prev_f:
                mins[neighbour] = cur_val + distance
                pathes[neighbour] = current

    return {
        "Протяженность пути": mins.get(destination, "-"),
        "Найденный путь": to_found_path(destination, pathes),
    }
