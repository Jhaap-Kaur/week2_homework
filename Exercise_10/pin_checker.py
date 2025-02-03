# import is a Python keyword used to bring in modules (pre-written code) into your script so you can use their functions and features.
# getpass is a Python module used for securely handling user input (especially passwords or PINs) without displaying them on the screen.
#import getpass
correct_pin = "1234"
print(correct_pin)
print(type(correct_pin))
attempts = 3
#for,if-else,in,break are statements ,for - used to create loops that iterates over sequence(list,range,string,etc)
for attempt in range(attempts): # attempt - is a loop variable(0,1,2) and in- is used to iterate over a range of attempts(3).
    supplied_pin = input("Enter your Pin: ")
    #supplied_pin = getpass.getpass("Enter your Pin: ")
    if supplied_pin == correct_pin:
        # f-string is a python string that allows embedding,add placeholders {},a placeholder can contain variables,operations,functions to format the value.
        print(f"Access granted. You succeeded in {attempt + 1} attempt.")
        break # loop control statement,Exit the loop immediately when the correct PIN is entered
    else:
        print(f"Failed : Access denied,try again with correct pin {attempts - attempt - 1} attempts left.")
        #This runs only if the loop finishes completely-all attempts used
else:
    print("Access denied!! You have used all attempts") # Only prints if the loop completes without `break`