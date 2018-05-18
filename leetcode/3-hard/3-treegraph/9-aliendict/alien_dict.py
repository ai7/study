#  Given an alphabetized list of words of an alien language, find the
#  alphabetized order of characters in that language.

#  * Simple Example:
#     * Input: rad, dar, ard
#     * Output: r, d, a

# input: cat, dog, elephant
# output: error, not enough information

# cat cbx

import sys
from collections import defaultdict


class Node(object):

    def __init__(self, name=None):
        self.name = name
        self.child = []  # children/neighbors
        self.visited = False

    def __repr__(self):
        return 'Node(%r)' % self.name

    def __str__(self):
        """id: neighbors, ie: 3: [1, 2, 3]"""
        child = [x.name for x in self.child]
        return '{}: {}'.format(self.name, child)

    def __len__(self):
        return len(self.child)


class Graph(object):

    def __init__(self):
        self.nodes = defaultdict(Node)  # list of Nodes
        self.edge_count = 0  # number of edges

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, item):
        return self.nodes[item]  # will create if not exist

    def __str__(self):
        return 'Graph: {:d} nodes, {:d} edges'.format(len(self), self.edge_count)

    def __repr__(self):
        s1 = str(self)
        s2 = '\n'.join([repr(v) for i, v in self.nodes.items()])
        return '{}\n{}'.format(s1, s2)

    def print_graph(self):
        """Print graph as ADJ list format"""
        for k, v in self.nodes.items():
            print(v)

    def add_edge(self, u, v):
        # create node a, b
        # add to graph with edge a -> b
        node_u = self[u]
        if not node_u.name:
            node_u.name = u
        node_v = self[v]
        if not node_v.name:
            node_v.name = v
        node_u.child.append(node_v)
        self.edge_count += 1

    def find_min(self):
        # find the node with no child
        # TODO: improve this
        for x in self.nodes:
            if not x._child:
                return x

    def pop_end(self):
        # remove node with no childs
        # should only have one
        node_x = self.find_min()
        if not node_x:
            return
        for m in self.nodes:
            # remove references to m in neighbor list
            new_child = []
            for c in m._child:
                if c != node_x.id:
                    new_child.append(c)
            m._child = new_child


def dfs(g, v):
    v.visited = True
    for u in v.child:
        if not u.visited:
            dfs(g, u)
    print(v.name)


def dfs_loop(g):
    for k, v in g.nodes.items():
        if not v.visited:
            dfs(g, v)


def process_pair(g, chars, word_a, word_b):

    if not word_a or not word_b:
        return

    # add chars to alphabet list
    chars.update(set(word_a))
    chars.update(set(word_b))

    for (a, b) in zip(word_a, word_b):
        if a != b:
            # add edge A[i] -> B[i] to graph
            # G.add_edge(word_a[x], word_b[x])
            g.add_edge(b, a)
            break


def create_order(word_list):
    if not word_list:
        return

    g = Graph()
    alphabet = set()

    # process words in pair, create graph
    n = len(word_list)
    for i in range(n-1):
        process_pair(g, alphabet, word_list[i], word_list[i+1])

    g.print_graph()

    # check if all alphabet is in graph
    if len(g) != len(alphabet):
        print("not enough information")
        return

    dfs_loop(g)


def main():
    create_order(['rad', 'dar', 'ard'])


if __name__ == '__main__':
    sys.exit(main())
