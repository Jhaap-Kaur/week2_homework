
# setting variable value
correct_pin = "1234"

# no. of attempts allowed
attempts = 3

for attempt in range (attempts):

    supplied_pin = input("Enter your PIN: ")

    if supplied_pin == correct_pin:
        print ("access granted", "number of attempts=",{attempt +1})
        break

    else:print ("access denied", "number of attempts remaining=",{attempts - attempt - 1})

