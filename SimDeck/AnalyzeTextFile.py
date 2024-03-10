import datetime
import random
from collections import Counter
import subprocess
import time
import os

class AnalyzeTextFile:
    def __init__(self):
        self.recorded_hands = []

    def analyze_text_file(self, deck_name, parsed_deck):
        full_deck = []
        number_of_cards = 0
        for card_count, card_name in parsed_deck:
            full_deck.extend([card_name] * card_count)
            number_of_cards += card_count

        print("This function simulates drawing X cards from deck to hand, Y times.")
        print("Then it displays the most commonly drawn hands, and individual card data.")
        print("\nEnter hand [X] and sample [Y] size.")
        print("Type 'quit' to return to main.")

        while True:
            hand_size_input = input("Hand size [X]: ").strip().lower()
            if hand_size_input == 'quit':
                print("Returning to main.")
                return
            try:
                hand_size = int(hand_size_input)
                if hand_size <= 0:
                    raise ValueError("Hand size must be a positive whole number.")
                elif hand_size >= number_of_cards:
                    print("Hand size must be less than total number of cards.")
                    continue
                break
            except ValueError:
                print("Hand size must be a positive whole number.")

        while True:
            sample_size_input = input("Sample size [Y]: ").strip().lower()
            if sample_size_input == 'quit':
                print("Returning to main.")
                return
            try:
                sample_size = int(sample_size_input)
                if sample_size <= 0:
                    raise ValueError("Sample size must be a positive whole number.")
                elif sample_size > 10000:
                    print("Sample size must be less than 10,001.")
                    continue
                break
            except ValueError:
                print("Sample size must be a positive whole number.")

        print("\nANALYSIS")
        print(f"Deck name: {deck_name}")
        print(f"Number of cards: {number_of_cards}")
        print(f"Hand size: {hand_size}")
        print(f"Simulation sample size: {sample_size}")
        print(f"Analyzed: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

        for _ in range(sample_size):
            shuffled_deck = self.shuffle_deck(full_deck)
            hand = self.draw_hand(shuffled_deck, hand_size)
            self.recorded_hands.append(hand)

        most_common_hands = self.display_analysis()
        self.save_analysis(deck_name, parsed_deck, most_common_hands, sample_size, hand_size, number_of_cards)

    def shuffle_deck(self, full_deck):
        shuffled_deck = full_deck[:]
        random.shuffle(shuffled_deck)
        return shuffled_deck

    def draw_hand(self, deck, hand_size):
        hand = []
        for _ in range(hand_size):
            hand.append(deck.pop())
        hand.sort()
        return hand

    def display_analysis(self):
        hand_counts = Counter(tuple(hand) for hand in self.recorded_hands)
        sample_size = len(self.recorded_hands)
        hand_size = len(self.recorded_hands[0])
        most_common_hands = hand_counts.most_common(5)

        print("MOST COMMON HANDS\n")
        for hand, count in most_common_hands:
            percent = count / sample_size * 100  # Calculate the percentage
            print(hand, "\n  {:.1f}%".format(percent), "-", count, "times\n")

        print("INDIVIDUAL CARD RESULTS\n")
        card_occurrences = Counter(card for hand in self.recorded_hands for card in hand)
        sorted_cards = sorted(card_occurrences.items(), key=lambda x: (sum(1 for hand in self.recorded_hands if x[0] in hand) / sample_size), reverse=True)
        for card, occurrence in sorted_cards:
            hand_count = sum(1 for hand in self.recorded_hands if card in hand)
            card_percentage = (hand_count / sample_size) * 100
            total_draws = occurrence
            draw_percentage = (total_draws / (hand_size * sample_size)) * 100
            print(f"{card}\n  {card_percentage:.1f}% hands with at least 1 ({hand_count} times) - {draw_percentage:.1f}% of total cards drawn\n")

        return most_common_hands

    def get_analysis_folder_path(self):
        analysis_folder_path = os.path.join(os.getcwd(), "Analysis")
        if not os.path.exists(analysis_folder_path):
            os.makedirs(analysis_folder_path)
        return analysis_folder_path

    def save_analysis(self, deck_name, parsed_deck, most_common_hands, sample_size, hand_size, number_of_cards):
        analysis_folder_path = self.get_analysis_folder_path()
        current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f"{deck_name}_Analysis_{current_time}.txt"
        full_filepath = os.path.join(analysis_folder_path, filename)
        with open(full_filepath, 'w') as file:
            file.write(f"Deck analysis: {deck_name}\n")
            file.write(f"Number of cards: {number_of_cards}\n")
            file.write(f"Hand size: {hand_size}\n")
            file.write(f"Simulation sample size: {sample_size}\n")
            file.write(f"Analyzed: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            file.write("DECK CONTENTS (can copy for import)\n\n")
            for count, card in parsed_deck:
                file.write(f"{count} {card}\n")
            file.write("\nMOST COMMON HANDS\n\n")
            for hand, count in most_common_hands:
                percent = count / sample_size * 100
                file.write(f"{hand}\n  {percent:.1f}% - {count} times\n\n")
            file.write("INDIVIDUAL CARD RESULTS\n\n")
            card_occurrences = Counter(card for hand in self.recorded_hands for card in hand)
            sorted_cards = sorted(card_occurrences.items(), key=lambda x: (sum(1 for hand in self.recorded_hands if x[0] in hand) / sample_size), reverse=True)
            for card, occurrence in sorted_cards:
                hand_count = sum(1 for hand in self.recorded_hands if card in hand)
                card_percentage = (hand_count / sample_size) * 100
                total_draws = occurrence
                draw_percentage = (total_draws / (hand_size * sample_size)) * 100
                file.write(f"{card}\n  {card_percentage:.1f}% hands with at least 1 ({hand_count} times) - {draw_percentage:.1f}% of total cards drawn\n\n")
        print(f"Deck analysis file saved to: {full_filepath}")

if __name__ == "__main__":
    analyze_deck = AnalyzeTextFile()

    deck_name = "TestDeck"
    parsed_deck = [(4, "Card1"), (3, "Card2"), (2, "Card3")]
    analyze_deck.analyze_text_file(deck_name, parsed_deck)
