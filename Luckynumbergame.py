Number= int(input("Guess your Luck, Enter a number from 1 to 50:"))
match Number:
    case 14:
        print("Ohh that's my Birthdate, Congrats you won 5$")
    case 1:
        print("Kudos 🤑, You did it ! you Won 50$")
    case 50:
        print("Congrats, You won 1$")
    case _:
        print("Better luck Next Time. Thank you 🙏")