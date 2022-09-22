import card_art
import random

def main():
    # Initialize list of card values
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Greet user
    print(card_art.logo)

    # Initialize hand of cards
    user_hand = []

    computer_hand = []

    # Deal 2 cards to user and print user score.

    # Deal 2 card to computer.

    # If computer has a blackjack and the user doesn't have a blackjack, computer wins.

    # If the user has a blackjack and computer doesn't, the user wins.

    # Reveal computer's first card to the user. 

    # Prompt user to hit or stand.

    # If user chose hit, deal another card to user's hand and print new score.
        # If user score is > 21, user loses

    # If user chose stand, only deal another card to the computer's hand

def check_blackjack(hand):
    if sum(hand) == 21:
        return True

def count_score(hand):
    count = sum(hand)
    if count > 21 and 11 in hand:
        count -= 10
    return count




if __name__ == "__main__":
    main()
