# With each word that can be a possible guess there are a finite number of possible outcomes you could get from guessing that word.
# For example you could guess the word correct on your first try or you could get none of the letters right, and every other possiblity
# in between. Each of these results will narrow the subsequent selection pool in different ways, some results leaving more possible words left than others.

# There are 3^5 possibilities of outcomes given there are 3 options (Green, Yellow, Grey) for each square and 5 total squares. And each of these outcomes has a
# specific probability of occuring based on how many other words match that pattern. So to judge a word we will use the expected reduction in words we will get
# for any guess.


# Iteration 1
# For iteration 1 we will simply get an expected value of words remaining after a guess by multiplying each probability by the number of words remaining.
# E[x] = Sum( prob(config) * number_of_words_left )
# We want to minimize the number of matches possible so there are less words to guess from.


from __future__ import division

def solveInteractive(words):
    # Initial guess - I ran this once and got the word raise. No need to run every time
    # init_guess = guess(words)
    guess = "raise"
    # Number of guesses thus far
    guessNum = 1
    # Coloring pattern
    config = []
    # Number of words left after guess
    wordsLeft = 0
    # Make copy of words list so we can remove words
    reducedSet = list(words)
    # response array from filter function [0] is array and [1] is words left
    resArr = []
    # Loop until guess is correct
    print("\n\nWordle Bot guess #1: raise\n")
    correct = input("Did I get it right?\n")
    while guessNum < 6 and correct == "no":
        # Receive information from guess
        response = input("Enter the colors that appeared: \n")
        config = response.split(" ")

        resArr = filterWordList(config, guess, reducedSet)
        numWordsLeft = resArr[1]
        reducedSet = resArr[0]

        print("\nThere are now only {} words left\n\n".format(numWordsLeft))

        # Adjust words list based on information received from guess
        # Calculate best word for guess next
        guess = guessWord(reducedSet)
        guessNum += 1

        print("Wordle Bot guess #{}: {}\n".format(guessNum, guess))

        correct = input("Did I get it right?\n")
        
        
    if correct == "yes":
        print("Yes! The bot took {} guesses".format(guessNum))
    else:
        print("Oh no :( I ran out of tries...")

def solve(answer, words):
    # Initial guess - I ran this once and got the word raise. No need to run every time
    # init_guess = guess(words)
    guess = "raise"
    # Number of guesses thus far
    guessNum = 1
    # Coloring pattern
    if guess == answer:
        correct = 1
    else:
        correct = 0
        # Receive information from guess
        config = colorize(answer, guess)
    # Make copy of words list so we can remove words
    reducedSet = list(words)
    # response array from filter function [0] is array and [1] is words left
    resArr = []
    while correct == 0:
        resArr = filterWordList(config, guess, reducedSet)
        reducedSet = resArr[0]

        # Adjust words list based on information received from guess
        # Calculate best word for guess next
        guess = guessWord(reducedSet)
        guessNum += 1
        if guess == answer:
            correct = 1
        else:
            correct = 0
            # Receive information from guess
            config = colorize(answer, guess)
    return guessNum

def colorize(answer, guess):
    config = []
    for letter in range(5):
        # Green color
        if guess[letter] == answer[letter]:
            config[letter] = "green"
        # Grey color
        elif (not answer.contains(guess[letter])):
            config[letter] = "grey"
        # First lets checks for duplicates - Yellow with duplicates we need to be careful
        elif guess.count(guess[letter]) > 1:
            # List of indices with duplicate letters
            dups = []
            for ind in range(5):
                # Capture the indices of the duplicate letters that aren't index
                if guess[ind] == guess[letter] and ind != letter:
                    dups.append(ind)

            # Need to figure out this logic

            # If duplicate is after current letter
                # Check color of duplicate
                    # If green then check if answer has duplicate
                        # If no then color grey
                        # If yes color yellow
                    # If grey then 
                # Check if answer has duplicate
                    # If no - color grey
                    # if yes - color yellow
            # If duplicate is before current letter
                # Check coloring of duplicate letter
                    # Grey case is already handled and wont reach here
                    # If yellow 

            if ():
                print(0)
        # Yellow color no duplicates
        elif (guess[letter] != answer[letter] and answer.contains(guess[letter])):
            config[letter] = "yellow"
    return config

def guessWord(words):
    # Possible color configurations {this was generated and added}
    configs = ["green","green","green","green","green"],["green","green","green","green","grey"],["green","green","green","yellow","yellow"],["green","green","green","yellow","grey"],["green","green","green","grey","green"],["green","green","green","grey","yellow"],["green","green","green","grey","grey"],["green","green","yellow","green","yellow"],["green","green","yellow","green","grey"],["green","green","yellow","yellow","green"],["green","green","yellow","yellow","yellow"],["green","green","yellow","yellow","grey"],["green","green","yellow","grey","green"],["green","green","yellow","grey","yellow"],["green","green","yellow","grey","grey"],["green","green","grey","green","green"],["green","green","grey","green","yellow"],["green","green","grey","green","grey"],["green","green","grey","yellow","green"],["green","green","grey","yellow","yellow"],["green","green","grey","yellow","grey"],["green","green","grey","grey","green"],["green","green","grey","grey","yellow"],["green","green","grey","grey","grey"],["green","yellow","green","green","yellow"],["green","yellow","green","green","grey"],["green","yellow","green","yellow","green"],["green","yellow","green","yellow","yellow"],["green","yellow","green","yellow","grey"],["green","yellow","green","grey","green"],["green","yellow","green","grey","yellow"],["green","yellow","green","grey","grey"],["green","yellow","yellow","green","green"],["green","yellow","yellow","green","yellow"],["green","yellow","yellow","green","grey"],["green","yellow","yellow","yellow","green"],["green","yellow","yellow","yellow","yellow"],["green","yellow","yellow","yellow","grey"],["green","yellow","yellow","grey","green"],["green","yellow","yellow","grey","yellow"],["green","yellow","yellow","grey","grey"],["green","yellow","grey","green","green"],["green","yellow","grey","green","yellow"],["green","yellow","grey","green","grey"],["green","yellow","grey","yellow","green"],["green","yellow","grey","yellow","yellow"],["green","yellow","grey","yellow","grey"],["green","yellow","grey","grey","green"],["green","yellow","grey","grey","yellow"],["green","yellow","grey","grey","grey"],["green","grey","green","green","green"],["green","grey","green","green","yellow"],["green","grey","green","green","grey"],["green","grey","green","yellow","green"],["green","grey","green","yellow","yellow"],["green","grey","green","yellow","grey"],["green","grey","green","grey","green"],["green","grey","green","grey","yellow"],["green","grey","green","grey","grey"],["green","grey","yellow","green","green"],["green","grey","yellow","green","yellow"],["green","grey","yellow","green","grey"],["green","grey","yellow","yellow","green"],["green","grey","yellow","yellow","yellow"],["green","grey","yellow","yellow","grey"],["green","grey","yellow","grey","green"],["green","grey","yellow","grey","yellow"],["green","grey","yellow","grey","grey"],["green","grey","grey","green","green"],["green","grey","grey","green","yellow"],["green","grey","grey","green","grey"],["green","grey","grey","yellow","green"],["green","grey","grey","yellow","yellow"],["green","grey","grey","yellow","grey"],["green","grey","grey","grey","green"],["green","grey","grey","grey","yellow"],["green","grey","grey","grey","grey"],["yellow","green","green","green","yellow"],["yellow","green","green","green","grey"],["yellow","green","green","yellow","green"],["yellow","green","green","yellow","yellow"],["yellow","green","green","yellow","grey"],["yellow","green","green","grey","green"],["yellow","green","green","grey","yellow"],["yellow","green","green","grey","grey"],["yellow","green","yellow","green","green"],["yellow","green","yellow","green","yellow"],["yellow","green","yellow","green","grey"],["yellow","green","yellow","yellow","green"],["yellow","green","yellow","yellow","yellow"],["yellow","green","yellow","yellow","grey"],["yellow","green","yellow","grey","green"],["yellow","green","yellow","grey","yellow"],["yellow","green","yellow","grey","grey"],["yellow","green","grey","green","green"],["yellow","green","grey","green","yellow"],["yellow","green","grey","green","grey"],["yellow","green","grey","yellow","green"],["yellow","green","grey","yellow","yellow"],["yellow","green","grey","yellow","grey"],["yellow","green","grey","grey","green"],["yellow","green","grey","grey","yellow"],["yellow","green","grey","grey","grey"],["yellow","yellow","green","green","green"],["yellow","yellow","green","green","yellow"],["yellow","yellow","green","green","grey"],["yellow","yellow","green","yellow","green"],["yellow","yellow","green","yellow","yellow"],["yellow","yellow","green","yellow","grey"],["yellow","yellow","green","grey","green"],["yellow","yellow","green","grey","yellow"],["yellow","yellow","green","grey","grey"],["yellow","yellow","yellow","green","green"],["yellow","yellow","yellow","green","yellow"],["yellow","yellow","yellow","green","grey"],["yellow","yellow","yellow","yellow","green"],["yellow","yellow","yellow","yellow","yellow"],["yellow","yellow","yellow","yellow","grey"],["yellow","yellow","yellow","grey","green"],["yellow","yellow","yellow","grey","yellow"],["yellow","yellow","yellow","grey","grey"],["yellow","yellow","grey","green","green"],["yellow","yellow","grey","green","yellow"],["yellow","yellow","grey","green","grey"],["yellow","yellow","grey","yellow","green"],["yellow","yellow","grey","yellow","yellow"],["yellow","yellow","grey","yellow","grey"],["yellow","yellow","grey","grey","green"],["yellow","yellow","grey","grey","yellow"],["yellow","yellow","grey","grey","grey"],["yellow","grey","green","green","green"],["yellow","grey","green","green","yellow"],["yellow","grey","green","green","grey"],["yellow","grey","green","yellow","green"],["yellow","grey","green","yellow","yellow"],["yellow","grey","green","yellow","grey"],["yellow","grey","green","grey","green"],["yellow","grey","green","grey","yellow"],["yellow","grey","green","grey","grey"],["yellow","grey","yellow","green","green"],["yellow","grey","yellow","green","yellow"],["yellow","grey","yellow","green","grey"],["yellow","grey","yellow","yellow","green"],["yellow","grey","yellow","yellow","yellow"],["yellow","grey","yellow","yellow","grey"],["yellow","grey","yellow","grey","green"],["yellow","grey","yellow","grey","yellow"],["yellow","grey","yellow","grey","grey"],["yellow","grey","grey","green","green"],["yellow","grey","grey","green","yellow"],["yellow","grey","grey","green","grey"],["yellow","grey","grey","yellow","green"],["yellow","grey","grey","yellow","yellow"],["yellow","grey","grey","yellow","grey"],["yellow","grey","grey","grey","green"],["yellow","grey","grey","grey","yellow"],["yellow","grey","grey","grey","grey"],["grey","green","green","green","green"],["grey","green","green","green","yellow"],["grey","green","green","green","grey"],["grey","green","green","yellow","green"],["grey","green","green","yellow","yellow"],["grey","green","green","yellow","grey"],["grey","green","green","grey","green"],["grey","green","green","grey","yellow"],["grey","green","green","grey","grey"],["grey","green","yellow","green","green"],["grey","green","yellow","green","yellow"],["grey","green","yellow","green","grey"],["grey","green","yellow","yellow","green"],["grey","green","yellow","yellow","yellow"],["grey","green","yellow","yellow","grey"],["grey","green","yellow","grey","green"],["grey","green","yellow","grey","yellow"],["grey","green","yellow","grey","grey"],["grey","green","grey","green","green"],["grey","green","grey","green","yellow"],["grey","green","grey","green","grey"],["grey","green","grey","yellow","green"],["grey","green","grey","yellow","yellow"],["grey","green","grey","yellow","grey"],["grey","green","grey","grey","green"],["grey","green","grey","grey","yellow"],["grey","green","grey","grey","grey"],["grey","yellow","green","green","green"],["grey","yellow","green","green","yellow"],["grey","yellow","green","green","grey"],["grey","yellow","green","yellow","green"],["grey","yellow","green","yellow","yellow"],["grey","yellow","green","yellow","grey"],["grey","yellow","green","grey","green"],["grey","yellow","green","grey","yellow"],["grey","yellow","green","grey","grey"],["grey","yellow","yellow","green","green"],["grey","yellow","yellow","green","yellow"],["grey","yellow","yellow","green","grey"],["grey","yellow","yellow","yellow","green"],["grey","yellow","yellow","yellow","yellow"],["grey","yellow","yellow","yellow","grey"],["grey","yellow","yellow","grey","green"],["grey","yellow","yellow","grey","yellow"],["grey","yellow","yellow","grey","grey"],["grey","yellow","grey","green","green"],["grey","yellow","grey","green","yellow"],["grey","yellow","grey","green","grey"],["grey","yellow","grey","yellow","green"],["grey","yellow","grey","yellow","yellow"],["grey","yellow","grey","yellow","grey"],["grey","yellow","grey","grey","green"],["grey","yellow","grey","grey","yellow"],["grey","yellow","grey","grey","grey"],["grey","grey","green","green","green"],["grey","grey","green","green","yellow"],["grey","grey","green","green","grey"],["grey","grey","green","yellow","green"],["grey","grey","green","yellow","yellow"],["grey","grey","green","yellow","grey"],["grey","grey","green","grey","green"],["grey","grey","green","grey","yellow"],["grey","grey","green","grey","grey"],["grey","grey","yellow","green","green"],["grey","grey","yellow","green","yellow"],["grey","grey","yellow","green","grey"],["grey","grey","yellow","yellow","green"],["grey","grey","yellow","yellow","yellow"],["grey","grey","yellow","yellow","grey"],["grey","grey","yellow","grey","green"],["grey","grey","yellow","grey","yellow"],["grey","grey","yellow","grey","grey"],["grey","grey","grey","green","green"],["grey","grey","grey","green","yellow"],["grey","grey","grey","green","grey"],["grey","grey","grey","yellow","green"],["grey","grey","grey","yellow","yellow"],["grey","grey","grey","yellow","grey"],["grey","grey","grey","grey","green"],["grey","grey","grey","grey","yellow"],["grey","grey","grey","grey","grey"]

    # This will be the words remaining for a specific configuration for a specific word
    wordsRem = 0
    # Used to calculate probability of this configuration appearing, used in Ex calculation
    prob = 0.0
    totalWords = len(words)
    minEx = 100000
    minIndex = 0
    for word in words:
        # This will be used to track the sum in the Ex calculation
        eXwords = 0.0
        confIndex = 0
        while eXwords < minEx and confIndex < 238:
            wordsRem = filterWordList(configs[confIndex], word, words)[1]
            prob = wordsRem / totalWords
            eXwords += wordsRem * prob
            confIndex += 1
        # If it made it through every 
        if confIndex == 238:
            minEx = eXwords
            minIndex = words.index(word)
    return words[minIndex]


# This function will calculate the number of words remaining for a specific word if config showed up as a result
def filterWordList(config, word, checkWordSet):
    # reducedSet will serve as the set of words we narrow down as we go through the config
    reducedSet = list(checkWordSet)
    for index in range(5):
        if config[index] == "green":
            # For each word, if it does not contain the specific letter at the specific spot then remove it
            for checkWord in checkWordSet:
                if (checkWord[index] != word[index]) and checkWord in reducedSet:
                    reducedSet.remove(checkWord)

        if config[index] == "yellow":
            # Check if current letter is a double letter
            if word.count(word[index]) > 1:
                # List of indices with duplicate letters
                dups = []
                for ind in range(5):
                    # Capture the indices of the duplicate letters that aren't index
                    if word[ind] == word[index] and ind != index:
                        dups.append(ind)
                    # Check number of duplicate letters
                if len(dups) ==  1:
                    # If the other duplicate letter is under green or yellow then we should only include words with duplicate letters
                    if config[dups[0]] == "green" or config[dups[0]] == "yellow":
                        for checkWord in checkWordSet:
                            if (not checkWord.count(word[index]) > 1 or word[index] == checkWord[index]) and checkWord in reducedSet:
                                reducedSet.remove(checkWord)
                    # If other occurance of duplicate letter in guess is grey
                    else:
                        # Per Wordle convention, if the other letter is grey it must be after the one in index, otherwise it is an impossible config
                        if not dups[0] < index:
                            # If the other one is grey then we shouldn't have any words with duplicate guesses in the answers
                            for checkWord in checkWordSet:
                                if (checkWord.count(word[index]) != 1 or word[index] == checkWord[index]) and checkWord in reducedSet:
                                    reducedSet.remove(checkWord)
                # If not one then has to be 2 since no word has 3 of the same
                else:
                    # Word must have 3 of the same letter
                    if (config[dups[0]] == "green" or config[dups[0]] == "yellow") and (config[dups[1]] == "green" or config[dups[1]] == "yellow"):
                        for checkWord in checkWordSet:
                            if (not checkWord.count(word[index]) > 2 or word[index] == checkWord[index]) and checkWord in reducedSet:
                                reducedSet.remove(checkWord)
                    elif (config[dups[0]] == "green" or config[dups[0]] == "yellow") and (config[dups[1]] == "grey"):
                        # Per Wordle convention, if the other letter is grey it must be after the one in index, otherwise it is an impossible config
                        if not dups[1] < index:
                            for checkWord in checkWordSet:
                                if (not checkWord.count(word[index]) > 1 or word[index] == checkWord[index]) and checkWord in reducedSet:
                                    reducedSet.remove(checkWord)
                    else:
                        # Per Wordle convention, if the other letter is grey it must be after the one in index, otherwise it is an impossible config
                        if not dups[0] < index:
                            # If the other one is grey then we shouldn't have any words with duplicate guesses in the answers
                            for checkWord in checkWordSet:
                                if (checkWord.count(word[index]) != 1 or word[index] == checkWord[index]) and checkWord in reducedSet:
                                    reducedSet.remove(checkWord)
            else:
                # For each word, if it doesn't contain the letter or if it is in the same spot (would be green) then remove
                for checkWord in checkWordSet:
                    if ((not word[index] in checkWord) or word[index] == checkWord[index]) and checkWord in reducedSet:
                        reducedSet.remove(checkWord)
                        

        if config[index] == "grey":
            # Need to check for double letter because we can't remove a word just because there is a grey for a letter, the guess could have two of the same
            # Check if current letter is a double letter
            if word.count(word[index]) > 1:
                # List of indices with duplicate letters
                dups = []
                for ind in range(5):
                    # Capture the indices of the duplicate letters that aren't index
                    if word[ind] == word[index] and ind != index:
                        dups.append(ind)
                # Check number of duplicate letters
                if len(dups) ==  1:
                    # If the other duplicate letter is green or yellow then we should only include words with duplicate letters
                    if config[dups[0]] == "green" or config[dups[0]] == "yellow":
                        # Per Wordle convention, if the other letter is grey it must be after the one in index, otherwise it is an impossible config
                        if dups[0] < index:
                            for checkWord in checkWordSet:
                                if (checkWord.count(word[index]) != 1 or checkWord[index] == word[index]) and checkWord in reducedSet:
                                    reducedSet.remove(checkWord)

                    # If other occurance of duplicate letter in guess is grey
                    else:
                        for checkWord in checkWordSet:
                            if word[index] in checkWord and checkWord in reducedSet:
                                reducedSet.remove(checkWord)
                else:
                    # Word must have 2 of the same letter
                    if (config[dups[0]] == "green" or config[dups[0]] == "yellow") and (config[dups[1]] == "green" or config[dups[1]] == "yellow"):
                        if dups[0] < index and dups[1] < index:
                            for checkWord in checkWordSet:
                                if (checkWord.count(word[index]) != 2 or checkWord[index] == word[index]) and checkWord in reducedSet:
                                    reducedSet.remove(checkWord)
                    elif (config[dups[0]] == "green" or config[dups[0]] == "yellow") and (config[dups[1]] == "grey"):
                        if dups[0] < index:
                            for checkWord in checkWordSet:
                                if (checkWord.count(word[index]) != 1 or checkWord[index] == word[index]) and checkWord in reducedSet:
                                    reducedSet.remove(checkWord)
                    else:
                        # For each word, if it contains the letter then remove it from the list
                        for checkWord in checkWordSet:
                            if word[index] in checkWord and checkWord in reducedSet:
                                reducedSet.remove(checkWord)
            else:
                # For each word, if it contains the letter then remove it from the list
                for checkWord in checkWordSet:
                    if word[index] in checkWord and checkWord in reducedSet:
                        reducedSet.remove(checkWord)
    return [reducedSet, len(reducedSet)]