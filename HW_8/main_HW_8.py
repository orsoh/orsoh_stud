from random import choice
from flib_HW_8 import get_user_choice
from flib_HW_8 import get_computer_choice
from flib_HW_8 import get_winner
from flib_HW_8 import make_message
from flib_HW_8 import start_game
from flib_HW_8 import stop_choice
import flib_HW_8

WIN_RULES = {
     'камень': ('ящерица', 'ножницы'),
     'ножницы': ('бумага', 'ящерица'),
     'бумага': ('камень', 'спок'),
     'ящерица': ('спок', 'бумага'),
     'спок': ('ножницы', 'камень')
}

counter_user_wins = 0
counter_computer_wins = 0




start_game()