import os

def filter(user_input):
    banned_word = ['cat','head','tail','less','more','grep','pr','nl','fmt','curl','dump','readelf','strings','file','nm','locate','awk','cut','dd','tr','sh','bash','s','h','ls','echo','python','eval','printf','cd','pwd','xargs','basename','dirname','root','bin','sys','dev','etc','su','u','sudo']
    banned_character = "$#<>!@%^&*():;'\"\\|?,_~`"
    for x in banned_word:
        if x in user_input:
            return False
    for i in range(0,len(banned_character),1):
        letter=banned_character[i]
        if letter in user_input:
            return False
    return True

def main():
    while True:
        command = input("$ ")
        check = filter(command)
        if check == True:
            if command=='exit':
                print('bye')
                break
            else:
                os.system(command)
        else:
            print("No Hack~ ^_^")

if __name__ == "__main__":
    main()