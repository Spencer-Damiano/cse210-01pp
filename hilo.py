import random

def suffle_new_game():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    shuffled_cards = []
    for _ in cards:
        while True:
            rand_card = random.choice(cards)
            if rand_card not in shuffled_cards:
                shuffled_cards.append(rand_card)
                break
    return shuffled_cards

def play_game(cards):
    points = 300
    turn = 0
    while points > 0:
        one = cards[turn]

        if one == cards[12]:
            play_again(points)
            break

        print()
        print(f'your current score is {points}')
        print(f'your card is {one}')
        turn += 1
        guess = input('is the next card going to be higher or lower? hi/lo ')
        print('-' * 15)
        # assert guess == 'hi' or guess =='lo'
        
        two = cards[turn]

        diffrence = one - two
        if diffrence <= 0 and guess == 'hi' or diffrence > 0 and guess == 'lo':
            points += 100
        elif diffrence >= 0 and guess == 'hi' or diffrence < 0 and guess == 'lo':
            points -= 75
        
        if points == 0:
            play_again(points)

def play_again(points):
    print(f'your score was {points}')
    again = input('would you like to play again? ')
    if again == 'y':
        play_game(suffle_new_game())
    elif again == 'n':
        game_over(points)


def game_over(points):
    print('game over')
    print(f'score - {points}')

def main():
    print('welcome to hilo')
    cards = suffle_new_game()
    high_score = 0
    run = input('would you like to play? y/n ')
    # assert run == 'y' or run == 'n'
    if run == 'y':
        score = play_game(cards)

main()