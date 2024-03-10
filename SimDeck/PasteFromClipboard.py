import pyperclip
import datetime
import re

class BreakOutOfFunction(Exception):
    pass

class PasteFromClipboard:
    def __init__(self):
        """commenting out the initial self.parsed_deck = []"""
        self.deck_name = ""  # Initialize deck_name attribute

    def paste_from_clipboard(self):
        while True:
            response = input("Is your deck copied to your clipboard (e.g. MTG Arena export)?\nType 'quit' to return to main.\n[Y/N]: ").strip().lower()
            if response == 'quit':
                raise BreakOutOfFunction("Returning to main.")
            elif response not in ['y', 'ye', 'yes']:
                print("\nTry again to copy your deck contents to your clipboard.")
                continue

            try:
                clipboard_contents = pyperclip.paste().strip().split('\n')
            except pyperclip.PyperclipException as e:
                print("Error accessing clipboard: ", e)
                print("Try again to copy your deck contents to your clipboard.")
                continue

            self.parsed_deck = []  # Reset parsed deck for each attempt
            total_cards = 0  # Variable to store the total number of cards

            for line in clipboard_contents:
                parts = line.strip().split(' ', 1)  # Split the line into two parts at the first space
                if len(parts) != 2 or not parts[0].isdigit():  # Check if the line has the correct format
                    continue  # Skip to the next line if the format is invalid

                card_count = int(parts[0])
                card_name = parts[1]
                self.parsed_deck.append((card_count, card_name))
                total_cards += card_count  # Increment the total cards count

            if total_cards < 1:
                print("\nError accessing clipboard: No valid data found.")
                continue

            return True  # Return True if parsing was successful

    def get_deck_name(self):
        while True:
            deck_name = input("\nName this deck (alphanumeric).\nType 'quit' to return to main.\nWill overwrite existing deck file of same name.\n\nDeck name: ").strip()

            if deck_name.lower() == 'quit':
                raise BreakOutOfFunction("Returning to main.")

            if not deck_name:
                print("Deck name cannot be blank.")
                continue

            if not re.match("^[a-zA-Z0-9_]*$", deck_name):
                print("Invalid deck name. Use alphanumeric characters only.")
                continue

            return deck_name

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

    def process_deck(self):
        try:
            if self.paste_from_clipboard():
                total_cards = sum(card_count for card_count, _ in self.parsed_deck)
                deck_name = self.get_deck_name()
                if deck_name:  # Check if a valid deck name was obtained
                    self.save_deck_to_file(deck_name, total_cards)
                    self.copy_to_clipboard()
                    self.print_parsed_deck()
                    print("Success!")
                    return deck_name
                else:
                    print("Something went wrong. Returning to main.")
        except BreakOutOfFunction as e:
            print(e)

# Testing code
if __name__ == "__main__":
    # Instantiate the PasteFromClipboard class
    paste_from_clipboard = PasteFromClipboard()

    # Call the process_deck method to test your functionality
    paste_from_clipboard.process_deck()
