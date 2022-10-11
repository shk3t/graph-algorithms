from data import FROM, TO, RELATIONS, FROM_RIGA_TO
from utils import to_graph, to_weighted_graph
from algo.bfs import bfs, bidir_bfs
from algo.dfs import dfs
from algo.greedy import greedy
from algo.min_a import min_A


if __name__ == "__main__":
    graph = to_graph(RELATIONS)
    wgraph = to_weighted_graph(RELATIONS)
    print("Поиск в ширину:", bfs(FROM, TO, graph), end="\n\n")
    print("Поиск в глубину:", dfs(FROM, TO, graph), end="\n\n")
    print("Поиск с ограничением глубины:", dfs(FROM, TO, graph, limit=5), end="\n\n")
    print(
        "Поиск в глубину с итеративным углублением:",
        dfs(FROM, TO, graph, deepening=True),
        end="\n\n",
    )
    print("Двунаправленный поиск:", bidir_bfs(FROM, TO, graph), end="\n\n")
    print("Жадный поиск:", greedy(FROM, TO, wgraph), end="\n\n")
    print(
        "Поиск методом минимизации суммарной оценки A*:",
        min_A(FROM, TO, wgraph, FROM_RIGA_TO),
        end="\n\n",
    )
