import random
word_bank = ['kiwi' , 'grape' , 'strawberry' , 'watermelon' , 'blueberry' , 'mango' , 'pineapple' , 'peach' , 'pear']

play_again = True
while play_again:
    word = random.choice(word_bank)
    attempts = 7
    guessed = False
    
    print('\n--- New Game Started ---')
    print('Current word: ' + '_ ' * len(word))
    
    while attempts > 0 and not guessed:
        print('\nAttempts left: ' + str(attempts))
        guess = input('Guess the word: ').lower().strip()
        
        if guess == word:
            print('\nCongratulations!! You guessed correctly! The word was: ' + word)
            guessed = True
        else:
            attempts -= 1
            print('Wrong guess!')
            if attempts > 0:
                print('Attempts left: ' + str(attempts))
            else:
                print('Game Over! No attempts left.')
    
    if attempts == 0 and not guessed:
        print('\nYou have run out of attempts! The word was: ' + word)
    
    response = input('\nDo you want to play again? (yes/no): ').lower()
    play_again = response == 'yes'

print('Thanks for playing!')
