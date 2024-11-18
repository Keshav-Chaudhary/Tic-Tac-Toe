from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

class TicTacToe:
    def __init__(self):
        self.board = ["", "", "", "", "", "", "", "", ""]
        self.current_player = "X"

    def chk_wins(self):
        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] != "":
                return self.board[combo[0]]
        if "" not in self.board:
            return "Draw"
        return None

    def make_move(self, position):
        if self.board[position] == "" and self.chk_wins() is None:
            self.board[position] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        self.board = ["", "", "", "", "", "", "", "", ""]
        self.current_player = "X"


game = TicTacToe()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "reset" in request.form:
            game.reset_game()
        return redirect(url_for("index"))
    
    winner = game.chk_wins() 
    return render_template("index.html", board=game.board, current_player=game.current_player, winner=winner)

@app.route("/move/<int:position>", methods=["POST"])
def move(position):
    game.make_move(position)
    return redirect(url_for("index"))

@app.route('/reset', methods=['POST'])
def reset():
    game.reset_game()
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')


