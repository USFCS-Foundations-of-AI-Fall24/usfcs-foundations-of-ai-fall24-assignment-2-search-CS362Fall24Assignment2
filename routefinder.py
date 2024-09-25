from queue import PriorityQueue

from docx import Document
import math

from Graph import Graph, Node, Edge


class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = set()
    start_state.h = heuristic_fn(start_state)
    start_state.f = start_state.g + start_state.h
    search_queue.put((start_state.f, start_state))
    ## you do the rest.
    cost_so_far = {}
    cost_so_far[start_state.location] = 0

    while not search_queue.empty():
        current_priority, current_state = search_queue.get()

        if goal_test(current_state):
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = current_state.prev_state
            return path[::-1]

        if use_closed_list:
            closed_list.add(current_state)

        for neighbor, cost in current_state.mars_graph.get_neighbors(current_state):
            new_cost = cost_so_far[current_state.location] + cost

            if neighbor.location not in cost_so_far or new_cost < cost_so_far[neighbor.location]:
                cost_so_far[neighbor.location] = new_cost
                # priority = new_cost + heuristic_fn(neighbor)
                neighbor.g = new_cost
                neighbor.h = heuristic_fn(neighbor)
                neighbor.f = neighbor.g + neighbor.h

                neighbor.prev_state = current_state
                search_queue.put((neighbor.f, neighbor))

                if use_closed_list and neighbor not in closed_list:
                    closed_list.add(current_state)

    return None

## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :

    if state.location:
        try:
            x1, y1 = map(int, state.location.split(","))
            x2, y2 = 1, 1
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2)**0.5

        except (ValueError, TypeError):
            print(f"Debug - Invalid location format: {state.location}")
            return 0
    else:
        print(f"Debug - Invalid location format: {state.location}")
        return 0




## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    graph = Graph()

    doc = Document(filename)
    read_data = []

    obstacles = set()

    for para in doc.paragraphs:
        read_data.append(para.text)

    for line in read_data:
        line = line.strip()

        if ":" in line:
            src, neighbors = line.split(":")
            src = src.strip()
            graph.add_node(Node(src))

            for neighbor in neighbors.split():
                neighbor = neighbor.strip()
                edge = Edge(src=src, dest=neighbor)
                graph.add_edge(edge)

    return graph


