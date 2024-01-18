print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

#.count
soma = name1 + name2
combinadinho = soma.lower()

t = combinadinho.count("t")
r = combinadinho.count("r")
u = combinadinho.count("u")
e = combinadinho.count("e")
soma_true = t + r + u + e

l = combinadinho.count("l")
o = combinadinho.count("o")
v = combinadinho.count("v")
e = combinadinho.count("e")
soma_love = l + o + v + e

#total = str(t + r + u + e) + str(l + o + v + e)

score = int(str(t + r + u + e) + str(l + o + v + e))

if score < 10 and score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

#print (combinadinho)