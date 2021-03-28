from app import app
from models.player import Player
import random


class Game:
    
    def __init__(self):
        self.choice = {
            'paper':'rock',
            'rock':'scissors',
            'scissors': 'paper'
        }
    
        
    