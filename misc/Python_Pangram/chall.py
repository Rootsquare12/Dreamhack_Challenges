import unicodedata

def checker(user_input):
    test = unicodedata.normalize('NFKC', user_input)
    cnt = [0]*26
    allowed_characters="()[]:., "
    if user_input!=test:
        print("Sorry, I can't read your handwriting.")
        return False
    if len(test)>100:
        print("Sorry, Pangrams are valuable when they are short.")
        return False
    for i in range(0,len(test),1):
        x=test[i]
        code=ord(x)
        if (code<32 or code>126):
            return False
        elif code>=97 and code<=122:
            cnt[code-97]+=1
        else:
            if x not in allowed_characters:
                return False
    for i in range(0,26,1):
        if cnt[i]==0:
            return False
    return True
        
print("Welcome to Python Pangram challenge!")
print("Show me your pangram!")
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
    print("Not a valid pangram!")