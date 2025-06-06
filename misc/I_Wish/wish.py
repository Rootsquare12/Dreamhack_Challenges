banned='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()~`{}[]+-_=<>.,/?:;|'

print("Input your wish!")
x=input('> ')

filtered=False
for i in range(0,len(banned),1):
    letter=banned[i]
    if letter in x:
        filtered=True
        break

if filtered==False:
    print("Wish granted!")
    exec(eval(x))
else:
    print("Sorry, I didn't understand your wish.")