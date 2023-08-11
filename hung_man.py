from random import choice

words_list = ['python', 'java', 'html', 'css', 'js']
chosen_word = choice(words_list)

chosen_word_list = list(chosen_word)
filling_list = ['_' for i in range(0, len(chosen_word))]

counter = 4
win = False
print('-' * 25, f'\nTry To Guess The Word:\nYou Have {counter} Tries\n', '-' * 25)

while counter > 0:
    for letter in filling_list: print(letter, end="")
    print('\n')
    if filling_list == chosen_word_list:
        win = True
        break

    print(f"Round {counter}{'.This is your last round!' if counter == 0 else ''}:")
    user_letter = input("Enter: ").strip().lower()

    if len(user_letter) > 1:
        print("\nEnter Just One Letter, Please. \n")
        continue
    if not user_letter.isalpha():
        print("\nJust letters are availabe. \n")
        continue

    if user_letter in chosen_word_list:
        print("True!")
        for i in range(0, len(chosen_word_list)):

            if chosen_word_list[i] == user_letter:
                
                filling_list[i] = user_letter.upper()
                chosen_word_list[i] = chosen_word_list[i].upper()
    else:
        print("False!!")
        counter -= 1

if win:
    print(f"\nCongratulations ^^\nYou Guessed Rightly, The Word Is {chosen_word}\n")
else:
    print("Good Luck\n")
     