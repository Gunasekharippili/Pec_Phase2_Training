import random as r

number = r.randint(1, 50)
chance = 5
while chance != 0:
    k = int(input("Guess Number "))
    if number < k:
        print(k, "is larger than Actually Number")
    elif number > k:
        print(k, "is smaller than Actually Number")
    else:
        print("Yeah, you guessed right")
        break
    chance -= 1
else:
    print("Yup, Actually Number is : ", number)
