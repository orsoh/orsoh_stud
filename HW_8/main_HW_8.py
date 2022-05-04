from random import choice
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