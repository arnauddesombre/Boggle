# Boggle
Solver for Boggle.<br>
<i>boggle.py</i> finds all valid solutions of any Boggle board (classic 4x4, or any custom size).

Boggle is a game created by Parker Brothers (now Hasbro), see [wikipedia](https://en.wikipedia.org/wiki/Boggle) for more information.

Parameters:<br>
A dictionary, as a text file containing the list of all valid words, one word per line.<br>
A Boggle board, as a text file with <i>number_of_rows</i>, <i>number_of_columns</i> on the first line (two numbers, separated by one or more spaces), followed by <i>number_of_rows</i> lines, each containing <i>number_of_columns</i> characters separated by one or more spaces. See an example of board below.

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

Note that letter <b>Q</b> as a special treatment in the English Boggle.<br>
In he English language, the letter Q is almost always followed by the letter U. Consequently, the side of one die is printed with the two-letter sequence Qu instead of Q (and this two-letter sequence must be used together when forming words). When scoring, Qu counts as two letters; for example, the word QuEUE scores as a 5-letter word even though it is formed by following a sequence of only 4 dice. 
