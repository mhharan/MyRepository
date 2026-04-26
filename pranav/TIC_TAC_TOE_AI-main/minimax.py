from tic_tac_toe_logics import board_state
def score(board,player,depth):
    bs=board_state(board)
    if bs==-1:
        return 0
    if bs==player:
        return 1/depth
    else:
        return -1*depth


def MiniMax(board,isMaximizing,player,depth):
    if board_state(board)!=0:
        return score(board,player,depth)
    best_score=10 if isMaximizing else -2
    for row in range(3):
        for col in range(3):
            if board[row][col]==0:
                board[row][col]=player if not isMaximizing else ("O" if player=="X" else "X")
                sc=MiniMax(board,not isMaximizing,player,depth+1)
                board[row][col]=0
                best_score=min(sc,best_score) if isMaximizing else max(sc,best_score)
    return best_score


