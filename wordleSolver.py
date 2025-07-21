# Author: Kaliuser876
# Created 7/21/2025
# Pulled the word list from a github repo

# A simple solution to make a wordle solver. It is not space effiecent, the best thing that it is doing
# is reading the dicitonary line by line so it wont get bloated. 
# Somthing I could implemenet is checking the contains letter inside of the first loop, however that would need another
# boolean value to check, while the curret implementation works. 

def main():
    containsLetter = False

    # Correct locations, correct letter
    correctLetters = input("Enter known letters in correct positions (use _ for unknowns): ").lower()

    # Correct letters, wrong location
    correctLettersWrongSpot = input("Enter known letters in wrong positions (a0,b3): ").lower()

    # Letters not in the word
    letterList = input("Enter letters not in the word (xzy): ").lower()

    # Parse the input to make it useable
    positionConstraints = {i: ch for i, ch in enumerate(correctLetters) if ch != '_'}
    wrongPositionConstraints = {}
    if correctLettersWrongSpot:
        for item in correctLettersWrongSpot.split(','):
            if len(item) >= 2 and item[1].isdigit():
                ch = item[0]
                pos = int(item[1])
                wrongPositionConstraints[pos] = ch
    letterList = set(letterList)
    containsLetters = set(ch for ch in correctLettersWrongSpot.replace(',', '') if ch.isalpha()) | set(positionConstraints.values())


    potentalAnswers = list() # Will be adding to the list of potentail answers. It will be very big
    # need to open the dictionary and be ready to compare all the words
    # iterating through the dictionary word by word
    with open("words_alpha.txt", 'r') as file:
        for line in file:
            word = line.strip()
            # Make sure the word is only 5 characters long
            if(len(word) != len("_____")):
                # Move on to the next word
                continue
            for character in letterList:
                # for every character in letterList, we check if the word contains the letter. If it does then we 
                # should remove it from our possible word list
                if character in word:
                    #Do not add this word, break out and move to the next word
                    containsLetter = True
                    continue
                # ELSE do nothing
                # Keep moving forward in the loop

            # Check if the word contained the letter
            # if it did then skip the word and move onto the next word
            if containsLetter:
                containsLetter = False
                continue
            # Otherwise add the word to potentail answers
            else:
                potentalAnswers.insert(0,word)
                continue

    # We now have a list of words that do not contain the letters. 
    # We have to check the letters we do know
    filteredAnswers = []

    for word in potentalAnswers:
        # Skip words with gray letters
        if any(ch in word for ch in letterList):
            continue

        # Ensure green letters are in correct positions
        if not all(word[i] == ch for i, ch in positionConstraints.items()):
            continue

        # Ensure yellow letters are in the word, but not at specified positions
        if not all(ch in word and word[i] != ch for i, ch in wrongPositionConstraints.items()):
            continue

        # Ensure all must-have letters are in the word
        if not all(ch in word for ch in containsLetters):
            continue

        filteredAnswers.append(word)

    potentalAnswers = filteredAnswers
    
    for word in potentalAnswers:
        print(word)

main()