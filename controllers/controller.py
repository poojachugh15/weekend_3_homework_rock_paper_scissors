
from app import app
from flask import render_template, redirect, request
# from models.game import Game
# from models.player import Player
from models.get_winner import winner

@app.route('/')
def index():
    return render_template('index.html', title="Home", message="Welcome to play the game")

@app.route('/<choice1>/<choice2>')
def player_1_choice(choice1, choice2):
    whowins = winner(choice1, choice2)
    return render_template('show_winner.html', title="Game Winner", player1_choice=choice1, player2_choice=choice2, show_winner=whowins)
    
    # # show the user profile for that user
    # player1 = 'Player 1 %s' % choice1
    # player2 =  'Player 2 %s' % choice2
    # print (player1 + player2)   
    # whowins = winner(choice1, choice2)    
    # return whowins

    