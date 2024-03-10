#In Analyze function, get it to actually open the analysis file.

from PasteFromClipboard import PasteFromClipboard
from ImportFromTextFile import ImportFromTextFile
from AnalyzeTextFile import AnalyzeTextFile

def main():
    print("QUICK START\nExport MTG Arena deck.\nEnter 1 to paste, and follow prompts.\nEnter 3 to analyze, and follow prompts.")
    deck_name = None
    parsed_deck = None
    while True:
        # Prompt the user for input
        print(f"\nCURRENT DECK: {deck_name}")
        print("Type a number (1-7) and Enter to manage a deck.\n")
        print("1 | Paste Deck from Clipboard/MTG Arena Export [replaces CURRENT DECK]")
        print("2 | Import Deck from Text File/Previous Deck [replaces CURRENT DECK]")
        print("3 | *Analyze Current Deck [requires valid CURRENT DECK]") 
        print("4 | Edit Deck in Directory")
        print("5 | Show Decks in Directory")
        print("6 | Help")
        print("7 | Exit")
        user_input = input("\nEnter a number (1-7): ")
        print()

        # Convert the input to an integer
        try:
            choice = int(user_input)
        except ValueError:
            print("Invalid input. Enter a number (1-7) to select an action.")
            continue

        # Check if the input is within the valid range
        if choice < 1 or choice > 7:
            print("Invalid input. Enter a number (1-7) to select an action.\n")
            continue

        if choice == 5:
            display_decks = ImportFromTextFile()  # Instantiate the ImportFromTextFile class
            display_decks.display_text_files_in_directory()  # Call the view_text_files_in_directory method

        elif choice == 1:
            paste_from_clipboard = PasteFromClipboard()
            deck_name = paste_from_clipboard.process_deck()
            if deck_name:
                parsed_deck = paste_from_clipboard.get_parsed_deck()

        elif choice == 2:
            import_from_text_file = ImportFromTextFile()  # Instantiate the ImportFromTextFile class
            deck_name = import_from_text_file.process_deck()
            if deck_name:
                parsed_deck = import_from_text_file.get_parsed_deck()

        elif choice == 4:
            edit_deck = ImportFromTextFile()  # Instantiate the ImportFromTextFile class
            edit_deck.open_text_file()  # Call the view_text_files_in_directory method

        elif choice == 6:
            help_file = ImportFromTextFile()  # Instantiate the ImportFromTextFile class
            help_file.open_help_file()  # Call the view_text_files_in_directory method
        
        elif choice == 3:
            # Check if parsed_deck and deck_name are present
            if parsed_deck is None or deck_name is None:
                print("No current deck. Paste (1) or import (2) a deck to analyze.")
                continue
            else:
                analyze_deck = AnalyzeTextFile()
                analyze_deck.analyze_text_file(deck_name, parsed_deck)
            
        elif choice == 7:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
