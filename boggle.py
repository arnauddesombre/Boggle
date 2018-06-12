# radix (number of letters in the alphabet)
R = 26


class Node:
    def __init__(self):
        self.endWord = False
        self.children = [None] * R


class Trie:
    def __init__(self):
        self.root = Node()

    # Return the index of c in the alphabet
    def indexChar(self, c):
        return ord(c) - ord('A')
    
    # insert a word in the TRIE
    def insert(self, word):
        node = self.root
        for level in xrange(len(word)):
            index = self.indexChar(word[level])
            if node.children[index] == None:
                node.children[index] = Node()
            node = node.children[index]
        node.endWord = True

    # search for word in the TRIE. Return:
    # -1: word is not in the TRIE
    #  0: word is a prefix of a word in the TRIE (but not a full word)
    #  1: word is in the TRIE
    def search(self, word):
        node = self.root
        for level in xrange(len(word)):
            index = self.indexChar(word[level])
            if node.children[index] == None:
                return -1
            node = node.children[index]
        if node == None:
            return -1
        elif node.endWord:
            return 1
        else:
            return 0

    
class BoggleSolver:
    # Initializes the R-way TRIE using the given array of strings as the dictionary
    # Each word in the dictionary contains only the uppercase letters A through Z
    def __init__(self, dictionary):
        self.dictionary = Trie()
        with open(dictionary, 'r') as f:
            for word in f:
                self.dictionary.insert(word.strip())

    # Returns the set of all valid words in the given Boggle board
    def getAllValidWords(self, board):
        self.found = set()
        for r in xrange(board.rows()):
            for c in xrange(board.cols()):
                self.getAllValidWordsFromCell(board, r, c)
        return sorted(list(self.found))

    # Recursively find all valid words from cell (row, col)
    def getAllValidWordsFromCell(self, board, row, col, path=None, word=''):
        word += board.getLetter(row, col)
        valid = self.dictionary.search(word)
        if valid == -1:
            return
        elif valid == 1 and len(word) >= 3:
            self.found.add(word)
        if path == None:
            path = set([(row, col)])
        for drow in [-1, 0, 1]:
            for dcol in [-1, 0, 1]:
                if 0 <= row + drow < board.rows() and 0 <= col + dcol < board.cols():
                    if (row + drow, col + dcol) not in path:
                        path2 = set(path)
                        path2.add((row + drow, col + dcol))
                        self.getAllValidWordsFromCell(board, row + drow, col + dcol, path2, word)

    # Returns the score of the given word if it is in the dictionary, zero otherwise
    # The word contains only the uppercase letters A through Z
    def scoreOf(self, word):
        length = len(word)
        if length >= 8:
            return 11
        elif length == 7:
            return 5
        elif length == 6:
            return 3
        elif length == 5:
            return 2
        elif length >= 3:
            return 1
        return 0


class BoggleBoard:
    # Initializes an m-by-n Boggle board from the specified filename
    # Boggle board consists of two integers M and N, followed by the M x N
    # characters in the board, with the integers and characters separated by whitespace
    def __init__(self, filename):
        f = open(filename, 'r')
        self.m, self.n = map(int, f.readline().strip().split())
        self.board = [[[''] * self.n] for _ in xrange(self.m)]
        for i in xrange(self.m):
            self.board[i] = f.readline().strip().split()
        f.close()

    # Returns the number of rows
    def rows(self):
        return self.m

    # Returns the number of columns
    def cols(self):
        return self.n

    # Returns the letter in row i and column j
    def getLetter(self, i, j):
        return str.upper(self.board[i][j])

    # Returns a string representation of the board
    def __str__(self):
        string = ''
        for i in xrange(self.m):
            string += ' '.join(map(lambda x: (x + ' ')[:2], self.board[i])) + '\n'
        return string[:-1]


if __name__ == '__main__':
    
    dictionary = 'dictionary-yawl.txt'
    filename = 'boggle.txt'

    print 'initializing dictionary'
    solver = BoggleSolver(dictionary)

    print 'solving board'
    board = BoggleBoard(filename)
    solution = solver.getAllValidWords(board)

    print
    print board
    print
    print 'number of words =', len(solution)
    if len(solution) > 0:
        solution = sorted(solution, key=len)
        print 'longest words =', ', '.join([word for word in solution if len(word) == len(solution[-1])])
    print 'total score =', sum(map(solver.scoreOf, solution))
