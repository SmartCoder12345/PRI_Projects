"""
Author: #Smart_Coder
--> Tic-Tac-Toe
Version: 1.0
"""
import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.master.configure(bg="black")
        self.master.iconbitmap("asset/icon.ico")
        self.master.resizable(False, False)
        self.master.geometry("350x400")
        self.current_player = "X"
        self.board = [" "] * 9
        self.buttons = []
        self.second_player = ""

        self.label = tk.Label(master, text="Tic-Tac-Toe", font=("Arial", 30, "bold"), fg="white", bg="black")
        self.label.pack(pady=20)

        self.button_2player = tk.Button(master, text="Player vs Player", font=("Helvetica", 20), pady=10, padx=20,
                                        command=lambda: self.prepare_board(True))
        self.button_2player.pack(pady=20)

        self.button_1player = tk.Button(master, text="Player vs Computer", font=("Helvetica", 20), pady=10,
                                        command=lambda: self.prepare_board(False))
        self.button_1player.pack(pady=10)

    def prepare_board(self, is_2player: bool) -> None:
        self.label.destroy()
        self.button_1player.destroy()
        self.button_2player.destroy()

        if is_2player:
            self.second_player = "O"
        else:
            self.second_player = "Computer"

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text="", font=("Helvetica", 24), width=5, height=2, bg="grey",
                                   command=lambda row=i, col=j: self.play_move(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

        self.start_game()

    def start_game(self) -> None:
        self.status_label = tk.Label(self.master, text=f"{self.current_player}'s turn", font=("Helvetica", 20), fg="white", bg="black")
        self.status_label.grid(row=3, columnspan=3, pady=10)

    def computer_move(self) -> None:
        while True:
            row: int = random.randint(0, 2)
            col: int = random.randint(0, 2)
            if self.is_vacant(row * 3 + col):
                self.play_move(row, col)
                break

    def is_vacant(self, index: int) -> bool:
        if self.board[index] == " ":
            return True
        return False

    def play_move(self, row, col):
        index = row * 3 + col

        if self.is_vacant(index):
            if self.current_player == "Computer":
                self.board[index] = "O"  # Update the board state
                self.buttons[index].config(text="O")
            else:
                self.board[index] = self.current_player
                self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Winner", f"{self.current_player} wins!")
                self.reset_board()
            elif " " not in self.board:
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = self.second_player if self.current_player == "X" else "X"
                self.status_label.config(text=f"{self.current_player}'s turn")
                if self.current_player == "Computer":
                    self.computer_move()

    def check_winner(self):
        winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for pos in winning_positions:
            if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] != " ":
                self.buttons[pos[0]].config(bg="red")
                self.buttons[pos[1]].config(bg="red")
                self.buttons[pos[2]].config(bg="red")
                return True
        return False

    def reset_board(self):
        self.current_player = "X"
        self.board = [" "] * 9
        for button in self.buttons:
            button.config(text="", bg="grey")
        self.status_label.config(text=f"{self.current_player}'s turn")


def main():
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()


if __name__ == "__main__":
    main()
