import sys
import copy

class Node:
    def __init__(self, other_nodes, value):
        self.other_nodes = other_nodes
        self.value = value

    def __str__(self):
        return "Value: {}\nOther Nodes: {}".format(self.value, [self.other_nodes])

node_1 = Node([], 1)
node_2 = Node([], 2)
node_3 = Node([], 3)
node_4 = Node([], 4)
node_5 = Node([], 5)
node_6 = Node([], 6)
node_7 = Node([], 7)

node_1.other_nodes = [node_2, node_3]
node_2.other_nodes = [node_1, node_3, node_4]
node_3.other_nodes = [node_4, node_5, node_6]
node_4.other_nodes = [node_4]
node_5.other_nodes = [node_7, node_1]
node_6.other_nodes = [node_7]
node_7.other_nodes = [node_6, node_5]

graph_1 = node_1


node_1_0 = Node([], 0)
node_1_1 = Node([], 1)
node_1_2 = Node([], 2)
node_1_3 = Node([], 3)

node_1_0.other_nodes = [node_1_2, node_1_1]
node_1_1.other_nodes = [node_1_2]
node_1_2.other_nodes = [node_1_3, node_1_0]
node_1_3.other_nodes = [node_1_3]

graph_2 = node_1_2


def graph_bfs(graph):
    nodes = [graph]
    seen_nodes = {}
    output = []

    while len(nodes) > 0:
        node = nodes.pop(0)


        if node.value not in seen_nodes:
            seen_nodes[node.value] = True
            output.append(node.value)

            for sub_node in node.other_nodes:
                nodes.append(sub_node)

    return output

print graph_bfs(graph_2)
print graph_bfs(graph_1)

def graph_dfs(graph):
    nodes = [graph]
    seen_nodes = {}
    output = []

    while len(nodes) > 0:
        node = nodes.pop()

        if node.value not in seen_nodes:
            seen_nodes[node.value] = True
            output.append(node.value)

            for sub_node in node.other_nodes:
                nodes.append(sub_node)

    return output

print graph_dfs(graph_2)
print graph_dfs(graph_1)

class WeightGraph:
    def __init__(self, edges):
        self.edges = edges
        self.vertices = len(self.edges)

w_graph_1 = WeightGraph(
[
   [0, 4, 0, 0, 0, 0, 0, 8, 0],
   [4, 0, 8, 0, 0, 0, 0, 11, 0],
   [0, 8, 0, 7, 0, 4, 0, 0, 2],
   [0, 0, 7, 0, 9, 14, 0, 0, 0],
   [0, 0, 0, 9, 0, 10, 0, 0, 0],
   [0, 0, 4, 14, 10, 0, 2, 0, 0],
   [0, 0, 0, 0, 0, 2, 0, 1, 6],
   [8, 11, 0, 0, 0, 0, 1, 0, 7],
   [0, 0, 2, 0, 0, 0, 6, 7, 0]
]
)

w = sys.maxint
w_graph_2 = WeightGraph(
[
   [0, 4, w, w, w, w, w, 8, w],
   [4, 0, 8, w, w, w, w, 11, w],
   [w, 8, 0, 7, w, 4, w, w, 2],
   [w, w, 7, 0, 9, 14, w, w, w],
   [w, w, w, 9, 0, 10, w, w, w],
   [w, w, 4, 14, 10, 0, 2, w, w],
   [w, w, w, w, w, 2, 0, 1, 6],
   [8, 11, w, w, w, w, 1, 0, 7],
   [w, w, 2, w, w, w, 6, 7, 0]
]
)


def min_distances_index(vertices_pairs_and_cost, vertices_reached):
    min_value = [(), sys.maxint]
    min_index = -1
    for index in range(len(vertices_pairs_and_cost)):
        value = vertices_pairs_and_cost[index]
        if value[1] < min_value[1] and value[0][1] not in vertices_reached:
            min_value = value
            min_index = index

    return min_index

def djikstra_min_distance(graph, start):
    distances = [sys.maxint] * graph.vertices

    vertices_reached =  {}
    edges = [[(0,0), 0]]

    while len(vertices_reached) < graph.vertices:
        index = min_distances_index(edges, vertices_reached)
        min_edge = edges.pop(index)

        new_vertice = min_edge[0][1]
        vertices_reached[new_vertice] = True
        distances[new_vertice] = min_edge[1]

        for i in range(len(graph.edges[new_vertice])):
            if graph.edges[new_vertice][i] != 0 and i not in vertices_reached:
                edges.append([(start, i), graph.edges[new_vertice][i] + distances[new_vertice]])
    return distances

print
print 'distances'
print djikstra_min_distance(w_graph_1, 0)


w_graph_3 = WeightGraph(
    [
    [0,   5,  w, 10],
    [w,  0,  3,  w],
    [w, w, 0,   1],
    [w, w, w, 0]
    ])

def floyd_worshall_algorithm(graph):
    distances = copy.deepcopy(graph.edges)

    for vertex_index in range(graph.vertices):
        for connecting_vertex_index in range(len(graph.edges)):
            first_level_weight = distances[vertex_index][connecting_vertex_index]
            if ( first_level_weight != w):
                for third_level_connecting_index in range(len(distances[connecting_vertex_index])):
                    second_level_weight = distances[connecting_vertex_index][third_level_connecting_index]
                    if (second_level_weight != w) and (first_level_weight + second_level_weight) < distances[vertex_index][third_level_connecting_index]:
                        distances[vertex_index][third_level_connecting_index] = first_level_weight + second_level_weight
    return distances

print floyd_worshall_algorithm(w_graph_3)


w_graph_4 = WeightGraph(
    [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
    ])

# 0 -> 1, 0 -> 3
# 1 -> 2
# 2 -> 3
# 3 -> None
# set([pointed at]) -< all nodes not included yet
# remove from the set when a node is pointed at
# if not pointed at then add to the list
def dag_topological_sorting_me(graph):
    dag_ordering = []
    while(len(dag_ordering) < graph.vertices):
        not_yet_ordered = set(range(graph.vertices)) - set(dag_ordering)

        for i in range(graph.vertices):
            for j in list(not_yet_ordered):
                if (i not in dag_ordering) and graph.edges[i][j] != 0:
                    not_yet_ordered -= set([j])
        dag_ordering += list(not_yet_ordered)
    return dag_ordering


print dag_topological_sorting_me(w_graph_4)

def dag_recursive_visit(graph, i, visited, sorted_list):
    visited[i] = True

    for j in range(graph.vertices):
        if (graph.edges[i][j] > 0)  and not visited[j]:
            dag_recursive_visit(graph, j, visited, sorted_list)

    sorted_list.append(i)

def dag_sort_recursive(graph):
    visited = [False] * graph.vertices
    sorted_list = []

    for i in range(graph.vertices):
        if not visited[i]:
            dag_recursive_visit(graph, i, visited, sorted_list)

    sorted_list.reverse()
    return sorted_list

print dag_sort_recursive(w_graph_4)


def all_words_of_size_n(boggle_board, current_coord, n):
    if n == 0:
        return []

    if n == 1:
        return [boggle_board[current_coord[0]][current_coord[1]]]

    output_words = []
    x_coord = current_coord[0]
    y_coord = current_coord[1]

    for x_mod in [-1, 0, 1]:
        for y_mod in [-1, 0, 1]:
            if not (x_mod == 0 and y_mod == 0):
                new_x = x_coord + x_mod
                new_y = y_coord + y_mod
                if (new_x < 0 or new_x >= len(boggle_board) or new_y < 0 or new_y >= len(boggle_board[x_coord])):
                    continue
                subwords = all_words_of_size_n(boggle_board, (new_x, new_y), n-1)
                for word in subwords:
                    output_words.append(boggle_board[x_coord][y_coord] + word)
    return output_words

def boggle_solve_shitty_but_works(boggle_board, dictionary):
    max_word_size = max([len(key) for key in dictionary.keys()])

    all_possible_words= []
    for word_size in range(1, max_word_size + 1):
        for i in range(len(boggle_board)):
            for j in range(len(boggle_board[i])):
                all_possible_words += all_words_of_size_n(boggle_board, [i,j], word_size)

    count = 0
    found_words = {}
    for word in all_possible_words:
        if word in dictionary and word not in found_words:
            found_words[word] = True
    return found_words.keys()


def words_from_depth_first_search(boggle_board, current_coord, current_word, visited, dictionary, solutions):
    if current_word in dictionary and current_word not in solutions:
        solutions[current_word] = True

    for x_mod in [-1, 0, 1]:
        for y_mod in [-1, 0, 1]:
            new_x = current_coord[0] + x_mod
            new_y = current_coord[1] + y_mod
            if (new_x < 0 or new_x >= len(boggle_board) or new_y < 0 or new_y >= len(boggle_board[current_coord[0]])):
                    continue
            if not (x_mod == 0 and y_mod == 0) and (new_x, new_y) not in visited:
                visited = visited.union(set([(new_x, new_y)]))
                words_from_depth_first_search(boggle_board, (new_x, new_y), current_word + boggle_board[new_x][new_y], visited, dictionary, solutions)
                visited -= set([(new_x, new_y)])


def better_boggle_depth_first_traversal(boggle_board, dictionary):
    words = {}
    for i in range(len(boggle_board)):
        for j in range(len(boggle_board[i])):
            visited = set([])
            words_from_depth_first_search(boggle_board, (i,j), '', visited, dictionary, words)
    return words.keys()





dictionary = {'geeks': True, 'for': True, 'quiz': True, 'go': True, 'quke': True}
boggle_board = [
    ['g', 'i', 'z'],
    ['u', 'e', 'k'],
    ['q', 's', 'e'],
]

print all_words_of_size_n(boggle_board, [1, 1], 2)
print boggle_solve_shitty_but_works(boggle_board, dictionary)
print better_boggle_depth_first_traversal(boggle_board, dictionary)


