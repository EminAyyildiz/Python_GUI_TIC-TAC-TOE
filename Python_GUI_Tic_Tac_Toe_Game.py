import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("### Tic Tac Toe Game ### Designed by Emin Ayyıldız")

        self.buttons = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, width=10, height=5, font=('times new roman', 30, 'bold'), command=lambda row=i, col=j: self.button_clicked(row, col))
                self.buttons[i][j].grid(row=i, column=j)
                self.buttons[i][j].config(bg="red")

        self.player = 1
        self.winner = None

        reset_button = tk.Button(self.root, text="RESET", font=('times new roman', 25, 'bold'), command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3)
        self.reset_button = reset_button

        self.root.configure(bg='yellow')
        self.root.mainloop()

    def button_clicked(self, row, col):
        if self.buttons[row][col]["text"] == "":
            if self.player == 1:
                self.buttons[row][col]["text"] = "X"
                self.buttons[row][col].config(fg="red")
                self.player = 2
            elif self.player == 2:
                self.buttons[row][col]["text"] = "O"
                self.buttons[row][col].config(fg="blue")
                self.player = 1
            self.check_for_winner()

    def check_for_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                self.winner = self.buttons[i][0]["text"]
            elif self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                self.winner = self.buttons[0][i]["text"]
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            self.winner = self.buttons[0][0]["text"]
        elif self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            self.winner = self.buttons[0][2]["text"]

        if self.winner:
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(state="disabled")
            messagebox.showinfo("Info", f"Winner: {self.winner}!", icon='info')
            self.reset_button.config(state="normal")
            if messagebox.askyesno("New Game", "Do you want to start a new game?"):
                self.new_game()

    def new_game(self):
        self.player = 1
        self.winner = None
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")

    def reset_game(self):
        self.player = 1
        self.winner = None
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")

game = TicTacToe()
