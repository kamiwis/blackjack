import card_art
import random

def main():
    # Initialize list of card values
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Initialize hand of cards
    user_hand = []

    computer_hand = []

    restart = True
    while restart:
         # Greet user
        print(card_art.logo)

        # Deal 2 cards to user and print user score.
        for _ in range(2):
            user_hand.append(deal_card(cards))
        user_score = count_score(user_hand)
        print(f"Your cards: {user_hand}, current score: {user_score}")

        # Deal 2 card to computer.
        for _ in range(2):
            computer_hand.append(deal_card(cards))
        comp_score = count_score(computer_hand)

        # If computer has a blackjack and the user doesn't have a blackjack, computer wins.
        if check_blackjack(computer_hand):
            print(f"Computer's hand: {computer_hand}, computer score: {comp_score}")
            print("You lose.")

            # Prompt user to restart game
            restart = restart_game()
            if not restart:
                break
            else:
                continue

        # If the user has a blackjack and computer doesn't, the user wins.
        elif not check_blackjack(computer_hand) and check_blackjack(user_hand):
            print(f"Computer's hand: {computer_hand}, computer score: {comp_score}")
            print("You win!")

            # Prompt user to restart game
            restart = restart_game()
            if not restart:
                break
            else:
                continue

        # Reveal computer's first card to the user. 
        else:
            print(f"Computer's first card: {computer_hand[0]}")

        # Prompt user to hit or stand.
        user_choice = hit_or_stand()

        while user_choice:
            # If user chose hit, deal another card to user's hand and print new score. Prompt user until user wants to stand or score is over 21.
            user_hand.append(deal_card(cards))
            user_score = count_score(user_hand)
            print(f"Your cards: {user_hand}, current score: {user_score}")

            if user_score == 21:
                print("You win!")

            if user_score > 21:
                print("You lose.")
                # Prompt user to restart game
                restart = restart_game()
                if not restart:
                    break
                else:
                    continue
            else:
                user_choice = hit_or_stand()
        
        if not user_choice:
            computer_turn = True
            while computer_turn:
                computer_hand.append(deal_card(cards))
                comp_score = count_score(computer_hand)
                print(f"Computer's hand: {computer_hand}, computer score: {comp_score}")

                

            







        

    # If user chose hit, deal another card to user's hand and print new score. Prompt user until user wants to stand.
        # If user score is > 21, user loses
        # Else prompt user again

    # If user chose stand, deal another card to computer's hand.

    # Computer keeps drawing cards unless the computer's score goes over 16. 

    # Compare the scores and check if it's a win, tie, or loss.

    # Print players and computers final hands and scores.

    # Ask to play again.


def deal_card(cards):
    return random.choice(cards)

def check_blackjack(hand):
    if sum(hand) == 21:
        return True

def count_score(hand):
    count = sum(hand)
    if count > 21 and 11 in hand:
        count -= 10
    return count

def restart_game():
    new_game = input("Do you want to play another game of Blackjack? 'Y' or 'N': ")
    if new_game == 'Y':
        return True
    else:
        return False

def hit_or_stand():
    choice = input("Type 'Y' to hit, or 'N' to stand: ")
    if choice == "Y":
        return True
    else:
        return False




if __name__ == "__main__":
    main()
