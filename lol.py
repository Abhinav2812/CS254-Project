from core import Board
from random import choice
def test():
    rows, cols = 9, 6
    no_of_games = 1
    no_of_players = 3
    no_of_moves_avg = 0
    board = Board(rows=rows, cols=cols, no_of_players=no_of_players)
    pltarray = []
    cnt = 0
    while not board.game_complete():
        for i in range(no_of_players):
            pos = choice(board.valid_moves())
            board.play(pos, mid_states=False)
            #print("Move:" + str(pos))
            figname = "pics/fig" + str(cnt)
            board.drawGraphical(figname)
            cnt += 1
            print("Here")
            if board.game_complete():
                break
    assert(board.verify_game_over())
test()
