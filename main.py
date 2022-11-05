import random

response = ["Yes",
            "No",
            "Ugh",
            "hohoho"]
print("Ben?")
while True:
    qusetion = input()
    print(random.choice(response))
