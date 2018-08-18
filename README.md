# CS254-Project
Algorithm Project for CS 254
# Introduction
A Combinatorial game is a two player game that satisfies the following conditions:
1. The two players move alternatively.
2. The game is **deterministic**. There are no chance elements or randomization mechanisms.
3. The players have **perfect information**. Each player is aware of all the information about each state of the game and nothing is hidden.
4. The rules are such that the game must eventually end.

In this project, we shall be analysing and attempting to simulate and/or solve two such combinatorial games, namely:
1. Hackenbush
2. Chain Reaction

# Hackenbush
“Hackenbush is a two-player game invented by mathematician John Horton Conway.The game starts with the players drawing a "ground" line (conventionally, but not necessarily, a horizontal line at the bottom of the paper or other playing area) and several line segments such that each line segment is connected to the ground, either directly at an endpoint, or indirectly, via a chain of other segments connected by endpoints. Any number of segments may meet at a point and thus there may be multiple paths to ground.
On his turn, a player "cuts" (erases) any line segment of his choice. Every line segment no longer connected to the ground by any path "falls" (i.e., gets erased). According to the normal play convention of combinatorial game theory, the first player who is unable to move loses.” - *Wikipedia*  

This project will be analysing two variations of this game:-
* **Green Hackenbush** : In this variation of the game, all the line segments are colored green, and both the players can cut any line segment of their choice. Thus the game is impartial (each player has the same set of moves).
<img src="/document_related/ghb.png" width="500"> 

* **Blue-Red Hackenbush** : All the line segments are either colored blue or red, with the first player only allowed to cut blue segments, while the second player is allowed to cut only red segments.
<img src="/document_related/brhb.png" width="500">

# Chain Reaction
Chain reaction is a deterministic combinatorial game of perfect information for 2 - 8 players developed by Matt Buddy.
An example game in progress:   

<img src="/document_related/cr.png" height="300">
The rules of the two-player(Red and Green) game are:  

* The game takes place on a <a href="http://www.codecogs.com/eqnedit.php?latex=n&space;\times&space;m" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n&space;\times&space;m" title="n \times m" /></a>  board.   

* Each cell has a \textit{critical mass}. The critical mass of a cell is equal to the number of orthogonally adjacent cells.(4 for inner cells, 3 for edge cells and 2 for corner cells)
* All cells are initially empty. Each player can place *orbs* of their corresponding colours in an empty cell or a cell already contains one or more orbs of the same colour.
* When a cell reaches its critical mass, it immediately explodes and an orb is added to each of its orthogonally adjacent neighbours. This may result in neighbouring cells to reach their critical mass. The chain reaction of explosions continue untill every cell is stable.
* When a cell explodes near cell of different colour, those cells are converted to the exploding cell colour and normal explosion rules follow.
* The winner is the one who eliminates all orbs of the other colour. 

# Instructions
* Clone the respository into a local folder.
* Using **Jupyter Notebook** , open the files **chain-reaction.ipynb** , **green_hb.ipynb** and **redblue_hb.ipynb**.
The notebook files contain code,strategy and visualization of their respective topics.
