from tkinter import *
from tkinter import messagebox
from tic_tac_toe_logics import ai_move,start_game,board_state
root=Tk()
root.title("TIC-TAC-TOE")
def disable_all_buttons():
    for button in buttons:
        button.config(state=DISABLED)

def b_click(b):
    global game_board,buttons,ai,player
    row,col=b.grid_info()["row"],b.grid_info()["column"]
    if game_board[row][col]!=0:return
    game_board[row][col]=player
    b["text"]=player
    bs=board_state(game_board)
    if bs!=0:
        disable_all_buttons()
        if bs==-1:
            messagebox.showinfo("Game Over","Tied!")
            return
        if bs==player:
            messagebox.showinfo("Game Over", "You win!")
            return
        if bs==ai:
            messagebox.showinfo("Game Over", "Ai wins!")
            return
    game_board,move=ai_move(game_board,ai)

    for button in buttons:
        if move==(button.grid_info()["row"],button.grid_info()["column"]):
            button["text"]=ai
    bs = board_state(game_board)
    if bs!=0:
        disable_all_buttons()
        if bs==-1:
            messagebox.showinfo("Game Over","Tied!")

        if bs==player:
            messagebox.showinfo("Game Over", "You win!")

        if bs==ai:
            messagebox.showinfo("Game Over", "Ai wins!")


if __name__=="__main__":

    b1=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b1))
    b2=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b2))
    b3=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b3))

    b4=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b4))
    b5=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b5))
    b6=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b6))

    b7=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b7))
    b8=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b8))
    b9=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b9))
    buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

    game_board=start_game()
    yn=messagebox.askyesno("starting game...","Do you want to start first?")

    player,ai=("O","X") if yn else ("X","O")
    if not yn:
        game_board, move = ai_move(game_board, ai)
        for button in buttons:
            if move == (button.grid_info()["row"], button.grid_info()["column"]):
                button["text"] = ai
    root.mainloop()