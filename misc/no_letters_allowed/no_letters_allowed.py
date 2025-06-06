banned='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()~`{}[]+-_=<>.,/?:;'

print("Input your wish!")
x=input('> ')

filtered=False
for i in range(0,len(banned),1):
    letter=banned[i]
    if letter in x:
        filtered=True
        break

if filtered==False:
    exec(eval(x))
else:
    print("No Hack~")