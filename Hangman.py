def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This Function checks if the input is valid
    :param letter_guessed: the letter that was guessed
    :param old_letters_guessed: the letters wich were previously guessed
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: True or False
    :rtype: bool
    """

    if(!letter_guessed.isalpha) or (len(letter_guessed) > 1) or (old_letters_guessed.count(letter_guessed.lower()) > 0):#if the input is invalid then return False
        return False
    else:
        return True
def choose_word(file_path, index):
    """
    This Function chooses a word for the game by the index the user picks
    :param file_path: the path to the file containing the words
    :param index: the number of the word in the file
    :type file_path: string
    :type index: int
    :return: Tuple containing the word and the number of words
    :rtype: Tuple
    """
    words_file = open(file_path,"r")
    words = words_file.read()
    words_list=words.split(" ")
    Non_duplicate_words_list=[]
    for word in words_list:
        if word not in Non_duplicate_words_list:#checks if there are any duplicate words, and if so they are not added into the new list
            Non_duplicate_words_list.append(word)
    Non_duplicate_words_list_length = len(Non_duplicate_words_list) 
    secret_word = Non_duplicate_words_list[(index%Non_duplicate_words_list_length)-1]
    word_tuple = (Non_duplicate_words_list_length,secret_word)#creates a tuple containing the word and the amount of words in the list and the secret word
    words_file.close()
    return word_tuple
def show_hidden_word(secret_word, old_letters_guessed):
    """
    This Function show the hidden word and the progress you made guessing letters
    :param secret_word: the secret word
    :param old_letter_guessed: the letters wich were previously guessed
    :type secret_word: string
    :type old_letter_guessed: list
    :return: The secret word
    :rtype: string
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            secret_word=secret_word.replace(letter, " _")#if the letter of the secret word is'nt in the old_letters_guessed then it's replaced with a _
    return secret_word
def check_win(secret_word, old_letters_guessed):
    """
    This Function checks if you won the game
    :param secret_word: the word the user needs to guess
    :param old_letter_guessed: the letters witch were previously guessed
    :type secret_word: string
    :type old_letter_guessed: list
    :return: True or False
    :rtype: bool
    """
    for letter in secret_word:
        if letter in old_letters_guessed:
           secret_word = secret_word.replace(letter,'')#replacing the letters in the old_letters_guessed list in a blank spot
    if len(secret_word) == 0:#if all the letters in the secret word got replaced then all the letters were guessed and then the user won
        return True
    else:
        return False
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    This Function updates the old_letter_guessed list
    :param letter_guessed: the letter that was guessed
    :param old_letter_guessed: the letters witch were previously guessed
    :type letter_guessed: string
    :type old_letter_guessed: list
    :return: True or False
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        return True
    else:
        print("X")
        old_list = str(old_letters_guessed)
        old_list = old_list.replace(',',' -> ')
        old_list = old_list.replace('[','')
        old_list = old_list.replace(']','')
        old_list = old_list.replace("'",'')
        print(old_list)
        return False
def check_lose(num_of_tries,word,old_letters_guessed):
    """this function checks if the user lost the game. And if so he prints: You Lost
    :param num_of_tries: the amount of failed tries
    :param word: the word the user needs to guess
    :param old_letters_guessed: a list of all the old letters that were guessed
    :type num_of_tries: int
    :type word: string
    :type old_letters_guessed: list
    :return: None"""
    if num_of_tries == 6:
            print_hangman(6)
            print("You lost")
            print(show_hidden_word(word,old_letters_guessed))
def print_hangman(num_of_tries):
    """
    This Function prints the state of the hangman
    :param num_of_tries: the number of fails the user have
    :type letter_guessed: int
    :return: Hangman state
    :rtype: string
    """
    HANGMAN_PHOTOS = {0: 
    """x-------x""", 1: 
    """
x-------x
|
|
|
|
|""",2: """
x-------x
|       |
|       0
|
|
| """,3: """
x-------x
|       |
|       0
|       |
|
|""",4: """
x-------x
|       |
|       0
|      /|\\
|
|""",5: """
x-------x
|       |
|       0
|      /|\\
|      /
|""",6: """
x-------x
|       |
|       0
|      /|\\
|      / \\
|"""}   

    print(HANGMAN_PHOTOS[num_of_tries])
def print_logo():
    """This function prints to welcome screen for the game
    :return:None"""
    HANGMAN_LOGO = """ 
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
""" 
    MAX_TRIES = 6
    print(HANGMAN_LOGO,MAX_TRIES)
def main():
    """
    This Function is the main function who runs the game
    """
    old_letters_guessed = []
    num_of_tries = 0
    print_logo()#call a function to print the logo of the game
    file_to_use = input("Enter file path: ")
    num_of_word = int(input("Enter Index: "))
    word_and_length = choose_word(file_to_use,num_of_word)#creating a tuple containing the secret word and the number of the word in the file
    print_hangman(num_of_tries)#calls a function to show the hangman's state
    while num_of_tries < 6:#runs a loop until the user fails
        print(show_hidden_word(word_and_length[1],old_letters_guessed))
        guess=input("Please enter a guess: ")
        if try_update_letter_guessed(guess, old_letters_guessed) == True:#if the guess is valid than add the guess into the old_letters_guessed list
            old_letters_guessed.append(guess.lower())
            if guess.lower() not in word_and_length[1]:#checks if the valid guess is correct
                print(":(")
                num_of_tries=num_of_tries+1
                print_hangman(num_of_tries)
        else:
            continue#if the guess is not valid then the while loop will skip to the next run
        check_lose(num_of_tries,word_and_length[1],old_letters_guessed)#calls a function to check if the user lost 
        if check_win(word_and_length[1], old_letters_guessed) == True:#checks if the user won
            print(show_hidden_word(word_and_length[1],old_letters_guessed))
            print("You won !!!")
            break
        
if __name__ == "__main__":
    main()   
