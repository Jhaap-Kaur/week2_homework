# setting variable value
import getpass
# to use this getpass module - need to open terminal and copy path into terminal and enter pin through the terminal
correct_pin = "1234"

# no. of attempts allowed
attempts = 3

# for loop with no of attempts included so programme knows when to stop
for attempt in range (attempts):

    supplied_pin = getpass.getpass('Enter your PIN: ')

    if supplied_pin == correct_pin:
        print(f"access granted. You succeeded in {attempt + 1} attempt")
        # to format values in an f string, add placeholders {}, a placeholder can contain variables and operations
        # functions and modifiers to format the value
        # break statement used here to stop the loop if condition is true
        break
    # else statement if pin is incorrect print access denied and include no of attempts remaining
    # programme ends
    else:
        print (f"access denied. You failed access denied:{attempts -attempt -1} attempts left")

# below statement will only print's if the loop completes without break (when pin is type incorrectly x3)
else:
    print("Access denied!! You have used all attempts")
