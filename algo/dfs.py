from utils import to_found_path


def dfs(frm, destination, graph, limit=None, deepening=False):
    found = False
    search_order = []
    path = {frm: None}

    def dfs(current):
        search_order.append(current)

        if current == destination:
            nonlocal found
            found = True
            return

        if not limit or len(path) < limit:
            for neighbour in graph[current].difference(path):
                path[neighbour] = current
                dfs(neighbour)
                if found:
                    return
                del path[neighbour]

    if deepening:
        max_limit = limit if limit else 20
        limit = 2
        while limit <= max_limit:
            dfs(frm)
            if found:
                break
            limit += 1
    else:
        dfs(frm)

    return {
        "Найденный путь": to_found_path(destination, path) if found else [],
        "Этапы поиска": search_order,
    }
