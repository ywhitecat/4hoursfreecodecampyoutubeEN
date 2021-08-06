


secret_word = "giraffe"
guess = ""
out_of_guesses= False
guess_count=0
guess_limit=3

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit : #determines the conditions in other to execute next
        guess= input("Enter guess: ")
        guess_count +=1 #increment 1 everytime to variable guess_cout +=
    else:
        out_of_guesses=True

if out_of_guesses():
    print("You lose!!!")
else:
    print("You win! ")


