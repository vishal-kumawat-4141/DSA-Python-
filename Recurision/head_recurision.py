# head recurision :--> first we work own job then call function
# recurision:---->
# def Name():
#     print("vishal kumawat")
#     Name()

# this function calling is infinite times but python only 987 time run and give stack overflow error
# Name()

# head recurision
count = 0


def greet():
    global count
    if count == 4:
        return
    print("Good Morning!")
    count += 1
    greet()


greet()
