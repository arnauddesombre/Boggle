# Boggle
Solver for Boggle.<br>
<i>boggle.py</i> finds all valid solutions of any Boggle board (classic 4x4, or any custom size)

Boggle is a game created by Parker Brothers (now Hasbro), see [wikipedia](https://en.wikipedia.org/wiki/Boggle) for more information.

Parameters:<br>
A dictionary, as a text file containing the list of all valid words, one word per line.<br>
A Boggle board, as a text file with <i>number_of_rows</i>, <i>number_of_columns</i> on the first line, followed by <i>number_of_rows</i> lines, each containing <i>number_of_columns</i> characters separated by space(s). See an example of board below.

Output:<br>
The number of valid words found, the total score, and the list of longest words found.

Algorithm:<br>
The dictionary is stored as an R-way TRIE, which allows for extremely efficient search. It takes a couple of seconds to crete the TRIE, but the solving of any 4x4 Boggle boards is instantaneous.

Example of board:<br>
4 4<br>
G N E S<br>
S R I P<br>
E T A L<br>
T S E B<br>
