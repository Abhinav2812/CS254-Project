from core import Board
from random import choice
import matplotlib.animation as animation
import matplotlib.pyplot as plt
def test():
    fig = plt.figure()
    rows, cols = 9, 6
    no_of_games = 1
    no_of_players = 3
    no_of_moves_avg = 0
    board = Board(rows=rows, cols=cols, no_of_players=no_of_players)
    pltarray = []
    while not board.game_complete():
        for i in range(no_of_players):
            pos = choice(board.valid_moves())
            board.play(pos, mid_states=False)
            print("Move:" + str(pos))
            x = board.drawGraphical()
            pltarray.append(x)
            if board.game_complete():
                break
    assert(board.verify_game_over())
    ani = animation.ArtistAnimation(fig, pltarray, interval=50, blit=True,
                                repeat_delay=1000)
    plt.draw()
    plt.show()
test()
