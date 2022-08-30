# Main function

from mimetypes import guess_extension
from guessWord import *

if __name__ == "__main__":
    # Interactive mode will allow you to play the daily game, pressing no is to run on all the answer set
    interactive = input("Would you like to use interactive mode? (Y/N): \n")
    words = []
    # Open words file and eliminate new line characters
    with open('words.txt', 'r') as wordsFile:
        words = wordsFile.read().splitlines()


        if(interactive == "Y"):
            solveInteractive(words)

        elif(interactive == "N"):
            guessesPerSolve = 0
            guessesPerSolveAvg = 0
            with open('answers.txt', 'r') as answersFile:
                answers = answersFile.read().splitlines()
                for answer in answers:
                    guessesPerSolve = guessesPerSolve + solve(answer, words)
                guessesPerSolveAvg = guessesPerSolve / len(answers)
                print(guessesPerSolveAvg)
            answersFile.close()

    wordsFile.close()