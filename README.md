# Boggle
Solver for Boggle

Boggle is a game created by Parker Brothers (now Hasbro)
https://en.wikipedia.org/wiki/Boggle

Parameters:
A dictionary, as a text file containing the list of all valid words, one word per line.
A Boggle board, as a text file with number_of_rows, number_of_columns on the first line, followed by number_of_rows line, each containing number_of_columns characters separated by space(s).

Output:
The number of valid words found, the total score, and the list of longest words found.

Algorithm:
The dictionary is stored as an R-way TRIE, which allows for extremely efficient search. It takes a couple of seconds to crete the TRIE, but the solving of any 4x4 Boggle boards is instantaneous.

Example of board:
4 4
G N E S
S R I P
E T A L
T S E B
