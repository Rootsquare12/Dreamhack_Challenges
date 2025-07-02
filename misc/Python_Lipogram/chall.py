import unicodedata

def checker(user_input):
    banned_alphabet="aefghmprvwxyAEFGHMPRVWXY"
    banned_character="'\"\\`:;/<>~!@#$%^&*|"
    test = unicodedata.normalize('NFKC', user_input)
    if user_input!=test: # Please, No Hack!!!
        print("Sorry, I can't read your handwriting.")
        return False
    for i in range(0,len(banned_alphabet),1):
        x=banned_alphabet[i]
        if x in test:
            return False
    for i in range(0,len(banned_character),1):
        x=banned_character[i]
        if x in test:
            return False
    return True
        
print("Welcome to Python Lipogram challenge!")
print("Show me your lipogram!")
x=input('> ')

result=checker(x)

if result==True:
    print("What a masterpiece! I gave you flag.",flush=True)
    flag = 'DH{**flag**}' # I gave! Take this.
    try:
        exec(x)
    except:
        pass
else:
    print("Not a valid lipogram!")