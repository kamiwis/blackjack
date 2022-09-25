import card_art
import random
import os
from time import sleep

def deal_card(cards):
    return random.choice(cards)

def count_score(hand):
    count = sum(hand)
    if count == 21 and len(hand) == 2:
        return 0
    if count > 21 and 11 in hand:
        count -= 10
    return count

def compare(user, comp):
    if user > 21 and comp > 21:
        return "You went over. You lose"
    if user == comp:
        return "Draw "
    elif comp == 0:
        return "Lose, opponent has Blackjack"
    elif user == 0:
        return "Win with a Blackjack"
    elif user > 21:
        return "You went over. You lose"
    elif comp > 21:
        return "Opponent went over. You win"
    elif user > comp:
        return "You win"
    else:
        return "You lose"

def clear():
    sleep(1)
    os.system("clear")

def play_game():
    print(card_art.logo)
    # Initialize list of card values
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Initialize hand of cards
    user_hand = []
    computer_hand = []
    game_over = False

    for _ in range(2):
        user_hand.append(deal_card(cards))
        computer_hand.append(deal_card(cards))

    while not game_over:
        # Deal 2 cards to user and print user score.
        user_score = count_score(user_hand)
        comp_score = count_score(computer_hand)
        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        # If computer has a blackjack and the user doesn't have a blackjack, computer wins.
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_turn = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_turn == "y":
                user_hand.append(deal_card(cards))
            else:
                game_over = True
        
    while comp_score != 0 and comp_score < 17:
        computer_hand.append(deal_card(cards))
        comp_score = count_score(computer_hand)
    
    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {comp_score}")
    print(compare(user_score, comp_score))
        
            
    
                
while input("Do you want to play a game of Blackjack? 'Y' or 'N': ") == "Y":
    clear()
    play_game()
