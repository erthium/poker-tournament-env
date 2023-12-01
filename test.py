""" 
We need to create an environment where:
- Play the game poker
- Call other scripts written by other developers
- When it's their move, transfer the information in the game and get their action

There has to be one script precisely running the game, and other scripts (agents)
that are called by the game script to make their move.


The functions that needs to be written:

Main game that will get the agents from planned scripts and run the game

Game class that call the agents to make their move in order and cycle

In the end, the remaining hands will compared

------------------

Algo rules:
Cards are integers from 1 to 52
Diamonds: 1-13
Clubs: 14-26
Hearts: 27-39
Spades: 40-52

This way it's easier to find flushes
For straight and pairs, we can easily take the modulo and compare

After the game ends, hand points are calculated
Hand points are also integers
For the hand order, the player gets 20 * hand order points
plus 1 - 13 points for the highest card

Hand order from highest:
10 - Royal Flush
9 - Straight Flush
8 - Four of a Kind
7 - Full House
6 - Flush
5 - Straight
4 - Three of a Kind
3 - Two Pairs
2 - One pair
1 - High Card
"""


