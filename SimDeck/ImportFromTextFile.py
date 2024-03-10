import datetime
import os
import pyperclip
import subprocess

class BreakOutOfFunction(Exception):
    pass

class ImportFromTextFile:
    def __init__(self):
        """commenting-out first self.parsed_deck = []""" 
        self.deck_name = None  # Initialize deck_name attribute as None

    def import_from_text_file(self):
        while True:
            file_name = input("\nSelect deck to import.\nType 'quit' to return to main.\nWill edit/overwrite existing deck file.\nDeck name: ").strip()

            if file_name.lower() == 'quit':
                raise BreakOutOfFunction("Returning to main.")

            file_name += ".txt"  # Append '.txt' to the file name

            try:
                with open(file_name, 'r') as file:
                    file_contents = file.readlines()
            except FileNotFoundError:
                print(f"Deck '{file_name[:-4]}' not found. Enter valid deck name.")
                continue

            self.parsed_deck = []  # Reset parsed deck for each attempt
            total_cards = 0  # Variable to store the total number of cards

            for line in file_contents:
                parts = line.strip().split(' ', 1)  # Split the line into two parts at the first space
                if len(parts) != 2 or not parts[0].isdigit():  # Check if the line has the correct format
                    continue  # Skip to the next line if the format is invalid

                card_count = int(parts[0])
                card_name = parts[1]
                self.parsed_deck.append((card_count, card_name))
                total_cards += card_count  # Increment the total cards count

            if total_cards < 1:
                print("\nError accessing deck: No valid data found.")
                continue

            # Set the deck name
            self.deck_name = file_name[:-4]  # Remove the '.txt' extension
            break  # Exit the loop after successfully importing the file

        return True  # Return True if parsing was successful

    def get_deck_name(self):
        # Return the deck name obtained during import
        return self.deck_name

    def save_deck_to_file(self, deck_name, total_cards):
        file_name = deck_name + ".txt"
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(file_name, "w") as file:
            file.write(f"Deck name: {deck_name}\n")
            file.write(f"Modified: {current_time}\n")
            file.write(f"Number of cards: {total_cards}\n\n")
            file.write("File (MTG Arena Deck Import/Export) format:\nDeck (header on its own line)\n(card count) (space) (card name)\n\n")
            file.write("Deck\n")
            for card_count, card_name in self.parsed_deck:
                file.write(f"{card_count} {card_name}\n")

        print(f"Deck saved as '{file_name}'.")

    def print_parsed_deck(self):
        total_cards = sum(card_count for card_count, _ in self.parsed_deck)
        print(f"Number of cards: {total_cards}")
        print("# Name")
        for card_count, card_name in self.parsed_deck:
            print(f"{card_count} {card_name}")

    def copy_to_clipboard(self):
        # Prepare deck contents to be copied to clipboard
        deck_contents = "Deck\n\n"
        for card_count, card_name in self.parsed_deck:
            deck_contents += f"{card_count} {card_name}\n"

        # Copy deck contents to clipboard
        try:
            pyperclip.copy(deck_contents)
            print("Deck copied to clipboard for MTG Arena import.")
        except pyperclip.PyperclipException as e:
            print("Error copying deck contents to clipboard: ", e)
            print()

    def get_parsed_deck(self):
        return self.parsed_deck

    def display_text_files_in_directory(self):
        text_files = [f for f in os.listdir() if f.endswith('.txt') and f != 'README.txt']
        if text_files:
            print("Decks in directory:")
            for file_name in text_files:
                print(file_name[:-4])  # Print file names without the '.txt' extension
            return True
        else:
            print("No decks found in directory.")
            return False

    def open_help_file(self):
        try:
            subprocess.Popen(['README.txt'], shell=True)
            print(f"Help file README.txt opened.")
        except Exception as e:
            print(f"Error opening help file README.txt: {e}")

    def open_text_file(self):
        while True:
            # Get the list of text files in the current directory excluding README.txt
            text_files = [f for f in os.listdir() if f.endswith('.txt') and f != 'README.txt']

            if not text_files:
                print("No decks in directory.")
                return

            # Display available deck files for the user to select
            print("Decks in directory:")
            for file_name in text_files:
                print(file_name[:-4])  # Print file names without the '.txt' extension

            deck_name = input("\nSelect deck to edit (case-sensitive).\nType 'quit' to return to main.\nDeck name: ")

            if deck_name.lower() == 'quit':
                print("Returning to main.")
                return

            file_name = deck_name + '.txt'

            # Check if the selected file exists in the directory
            if file_name not in text_files:
                print(f"'{deck_name}' not found.\n")
                continue

            try:
                subprocess.Popen([file_name], shell=True)
                print(f"'{deck_name}' opened.")
                print("\nSave/close deck file when finished, then import (2).")
                break
            except Exception as e:
                print(f"Error opening '{deck_name}': {e}")

    def process_deck(self):
        try:
            if self.display_text_files_in_directory():
                if self.import_from_text_file():
                    total_cards = sum(card_count for card_count, _ in self.parsed_deck)
                    deck_name = self.get_deck_name()
                    if deck_name:  # Check if a valid deck name was obtained
                        self.save_deck_to_file(deck_name, total_cards)
                        self.copy_to_clipboard()
                        self.print_parsed_deck()
                        print("Success!")
                        return deck_name
                    else:
                        print("Returning to main.")
        except BreakOutOfFunction as e:
            print(e)

# Testing code
if __name__ == "__main__":
    # Instantiate the ImportFromTextFile class
    import_from_text_file = ImportFromTextFile()

    # Call the process_deck method to test your functionality
    import_from_text_file.process_deck()
