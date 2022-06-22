def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


starting =0
while starting < 100:
    if is_even(starting):
        print(f"{starting} is Even")
    else:
        print(f"{starting} is odd")
        

    starting = starting + 1
print("finished")




