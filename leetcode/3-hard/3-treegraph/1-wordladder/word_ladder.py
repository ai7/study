import sys
import itertools
from collections import deque, defaultdict


class Node(object):
    """Class that represents a node (vertex) in a graph"""

    def __init__(self, name=None):
        """
        Constructor

        @param name: id or name of vertex
        """
        self.name = name
        self.child = []  # children | adjacency list

        # attributes from CLR book for BFS/DFS
        self.color = 0  # 0: white [unvisited], 1: gray [found], 2: black [finished]
        self.distance = None  # BFS: distance from starting node
        self.parent = None  # parent node from BFS/DFS search
        self.time_discover = None  # DFS
        self.time_finish = None  # DFS

    def __repr__(self):
        return 'Node(%r)' % self.name

    def __str__(self):
        """id: neighbors [dist: x], ie: 3: [1, 2, 3] [dist: 5]"""
        child = [x[0].name for x in self.child]
        return '{}: {} [dist: {}]'.format(self.name, child, self.distance)

    def __len__(self):
        """Treat the degree of node as its length"""
        return len(self.child)

    def reset_attr(self):
        """Reset some attributes before DFS/BFS run"""
        self.color = 0
        self.distance = 1000000  # pseudo INFINITY for this assignment
        self.parent = None
        self.time_discover = None
        self.time_finish = None


class Graph(object):
    """Class that represents a Graph with vertices"""

    def __init__(self):
        """
        Constructor

        Use a dict for nodes so we can look it up via name.
        """
        self.nodes = defaultdict(Node)  # list of Nodes
        self.edge_count = 0  # number of edges

    def __getitem__(self, item):
        """
        Override Graph[key] to return node based on id, if no such node
        exists, one is created and returned.

        @param item: node id
        @rtype: Node
        """
        # if node already exist, return it
        return self.nodes[item]

    def __len__(self):
        """Size of graph is the number of vertices"""
        return len(self.nodes)

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
        """
        Add an edge from u -> v in graph

        @param u: name of starting node
        @type u: str
        @param v: name of ending node
        @type v: str
        """
        # If u and v are integers, cast to integer. This allows us to
        # support both number and string vertex names natively.
        if u.isdigit():
            u = int(u)
        if v.isdigit():
            v = int(v)

        # now fetch vertex u and v from graph
        node_u = self[u]  # will create if not exist
        if not node_u.name:
            node_u.name = u  # defaultdict create does not set name
        node_v = self[v]
        if not node_v.name:
            node_v.name = v

        node_u.child.append(node_v)  # add v to child list of u

        self.edge_count += 1

    def reset(self):
        """Reset all nodes attributes"""
        for k, v in self.nodes.items():
            v.reset_attr()


def breadth_first_search(g, s):
    """
    Breadth First Search.

    Based on CLR book. For each node, it calculates a distance (from
    starting vertex s), and the parent node.

    @param g: input graph, assume all unvisited
    @type g: Graph
    @param s: starting vertex name
    """
    # g.reset()

    node_s = g[s]  # get Node from name
    node_s.color = 1  # set to GRAY
    node_s.distance = 0
    node_s.parent = None

    queue = deque()  # create queue and add S to queue
    queue.append(node_s)

    while queue:

        node_v = queue.popleft()  # remove first element of queue

        for node_w in node_v.child:  # for each edge (v, w)

            if not node_w.color:  # if color is WHITE

                node_w.color = 1  # set color to GRAY
                node_w.distance = node_v.distance + 1
                node_w.parent = node_v
                queue.append(node_w)  # add to queue at the end

        node_v.color = 2  # BLACK, done with node V


def diff_by_one(word_a, word_b):
    """Return True if 2 words differ only by one char"""

    if not word_a or not word_b:  # neither should be empty
        return False

    size_a = len(word_a)  # length should be same
    size_b = len(word_b)
    if size_a != size_b:
        return False

    if word_a == word_b:  # can't be the same
        return False

    found_diff = False
    for i in range(size_a):
        if word_a[i] != word_b[i]:
            if found_diff:
                return False
            found_diff = True

    return True


class Solution:

    def ladderLength(self, beginWord, endWord, wordList):
        """
        @type beginWord: str
        @type endWord: str
        @type wordList: List[str]
        @rtype: int
        """
        if not beginWord or not endWord:
            return 0
        if beginWord == endWord:
            return 0

        # if beginWord in wordList:
        #    return 0
        if endWord not in wordList:
            return 0

        g = Graph()

        # add begin word to word list
        if beginWord not in wordList:
            wordList.append(beginWord)

        # build graph from wordList
        for u, v in itertools.combinations(wordList, 2):
            if diff_by_one(u, v):
                g.add_edge(u, v)
                g.add_edge(v, u)

        # now run bfs from beginWord to endWord
        x = g[beginWord]
        y = g[endWord]

        breadth_first_search(g, beginWord)

        if not y.distance:
            return 0
        else:
            return y.distance + 1


def main():
    sol = Solution()
    retval = sol.ladderLength('hit', 'cog',
                              ["hot", "dot", "dog", "lot", "log", "cog"])
    print(retval)


if __name__ == '__main__':
    sys.exit(main())
