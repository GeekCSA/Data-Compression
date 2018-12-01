import heapq as hq
import Data_Compression as dc


def bulidHuffman(S, P):
    h = []
    for node in [Node(p, s) for p, s in sorted(zip(P, S))]:
        hq.heappush(h, node)

    for i in range(len(S) - 1):

        left_node = hq.heappop(h)
        right_node = hq.heappop(h)

        new_node = Node(left_node.probability + right_node.probability, None, left_node, right_node)

        hq.heappush(h, new_node)

    return hq.heappop(h)

def extractCodeFromTree(root_of_tree, code_words, word):

    if root_of_tree.left == None and root_of_tree.right == None:
        code_words.append([word, root_of_tree.probability])
        return
    if root_of_tree.left != None:
        word += "0"
        extractCodeFromTree(root_of_tree.left, code_words, word)
    word = word[0:len(word) - 1]
    if root_of_tree.right != None:
        word += "1"
        extractCodeFromTree(root_of_tree.right, code_words, word)
    word = word[0:len(word) - 1]

class Huffman(dc.CodeWords):
    def __init__(self, S, P):

        root_of_tree = bulidHuffman(S, P)
        word = ""
        code_words = []
        extractCodeFromTree(root_of_tree, code_words, word)

        code_words = sorted(code_words, key=lambda x: x[1]) # Sort the code word by probabilities

        P = [cw[1] for cw in code_words]
        C = [cw[0] for cw in code_words]

        super().__init__(C, P)

class Node:

    def __init__(self, probability, data = None, left = None, right = None):

        self.left = left
        self.right = right
        self.data = data
        self.probability = probability

    def getData(self):
        return self.data

    def __lt__(self, other):
        return self.probability < other.probability