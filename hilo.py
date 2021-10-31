import random

def suffle_new_game():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    shuffled_cards = []
    for card in cards:
        while True:
            rand_card = random.choice(cards)
            if rand_card not in shuffled_cards:
                shuffled_cards.append(rand_card)
                break
    print(shuffled_cards)
    return shuffled_cards

def play_game(cards):
    points = 300
    turn = 0
    while points > 0:
        one = cards[turn]
        print(f'your current points is {points}')
        print(f'your first card is {one}')
        guess = input('is the next card going to be higher or lower? hi/lo ')
        # assert guess == 'hi' or guess =='lo'
        turn += 1
        two = cards[turn]
        print(f'the next card is {two}')

        diffrence = one - two
        if diffrence >= 0 and guess == 'hi' or diffrence < 0 and guess == 'lo':
            points += 100
        elif diffrence >= 0 and guess == 'lo' or diffrence <0 and guess == 'hi':
            points -= 75

def main():
    print('welcome to hilo')
    cards = suffle_new_game()
    print(cards)
    high_score = 0
    run = input('would you like to play? y/n')
    # assert run == 'y' or run == 'n'
    if run == 'y':
        score = play_game(cards)
        if score > high_score:
            high_score = score
    
    print('Game Over')
    print(f'Score - {high_score}')

main()