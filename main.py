# Main function

from mimetypes import guess_extension
from guessWord import *

if __name__ == "__main__":
    words = []
    # Open words file and eliminate new line characters
    with open('words.txt', 'r') as wordsFile:
        words = wordsFile.read().splitlines()
        solveInteractive(words)
    wordsFile.close()