# Tail recurision :---> first we call function then do own job ...
count = 0


def greet():
    global count
    if count == 4:
        return
    count += 1
    greet()
    print("Good Morning!")


greet()
