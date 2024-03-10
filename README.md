SIMDECK v1.0
Shawn Schaller, 2024-03-06
For Windows/Mac/Linux

QUICKSTART
Export a deck from MTG Arena, open this program, enter 1 to paste-from-clipboard, name the deck, and it will both import and save.
Enter 3 to analyze-deck, then the number of cards in a starting hand (e.g. 7) and the number of first-hand-draws to simulate (e.g. 10000).
Results will print to the screen and save in the Analysis folder of this program's directory.

OVERVIEW
SIMDECK is designed to simulate drawing a first-hand from a deck of cards a large number of times for analysis.
It is designed for MTG Arena desktop client (deck import/export), but works with any correctly formatted deck of cards.
SampleDeck.txt included in this directory is an example MTG Arena export pasted-and-saved.

The correct format via text file/clipboard is a single card name/type per line as follows:
(copies of card in deck, integer)(single space)(card name/type, string)
15 Slime Against Humanity

FUNCTIONS
The main screen displays the current deck to be analyzed, "None" by default until a deck is pasted (1) or imported (2).
Type a number 1-7 and hit enter to use the respective SIMDECK function.
Most prompts allow you to type "quit" to return to this main screen.

1 | Paste Deck from Clipboard/MTG Arena Export
Asks if you have deck data copied to your clipboard in the correct format (e.g. via MTG Arena deck export)
Asks you to name deck to save for reuse, WILL OVERWRITE EXISTING .TXT FILE OF SAME NAME IN DIRECTORY
Saves deck as (deck name).txt in directory, and re-copies deck to clipboard (e.g. for MTG Arena deck import)
Returns to main, recognizes this current deck (for analysis)

2 | Import Deck from Text File/Previous Deck
Displays decks (.txt files) in directory available for import (e.g. decks previously saved/pasted from clipboard [1])
Asks you to enter deck name (from the list) to import, WILL OVERWRITE EXISTING .TXT FILE OF SAME NAME IN DIRECTORY
Re-saves deck as (deck name).txt in directory, and copies deck to clipboard (e.g. for MTG Arena deck import)
Returns to main, recognizes this current deck (for analysis)

3 | *Analyze Current Deck [first paste (1)/import (2)]
Requires current deck to function, MUST PASTE (1) or IMPORT (2) DECK FIRST
Asks you to enter hand-size X (e.g. in MTG you start with 7 cards in your hand)
Asks you to enter number of first-hand-draws to simulate Y (e.g. the simulation sample-size)
Simulates shuffling deck, drawing X cards, recording results, and repeating process Y times
Shows most-commonly-drawn hands
Saves output as (deck name)_(date-and-time)_analysis.txt in "Analysis" folder in directory
Returns to main, retains current deck (for analysis)

4 | Edit Deck in Directory
Displays decks (.txt files) in directory available to open
Asks you to enter (case-sensitive) deck name (from the list) to open
Opens deck .txt file on screen
USER MUST EDIT .TXT FILE IN CORRECT FORMAT, THEN SAVE AND CLOSE
Suggests you save, close and import (2) deck when complete
Returns to main, DOES NOT retain as current deck (for analysis)

5 | Show Decks in Directory
Displays decks (.txt files) in directory available to open

6 | Help
Opens this README.txt file

7 | Exit
Exits the program

