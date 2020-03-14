from time import sleep

try: from termcolor import cprint
except ModuleNotFoundError:
    print("You must install module 'termcolor'\npip install termcolor")
    exit()
try: from colorama import Fore
except ModuleNotFoundError:
    print("You must install module 'colorama'\npip install colorama")
    exit()
try: from colored import fg
except ModuleNotFoundError:
    print("You must install module 'colored'\npip install colored")
    exit()

def loading(x, symbol, per, time, color):
    '''
    Text colors:
grey
red
green
yellow
blue
magenta
cyan
white
rb(rainbow)
'''
    a = x-1
    b = 100/x
    c = 0
    warn = Fore.RED+"loading(int, char, 1 or 2, int or float, color(ex. 'red'))"

    #checking
    if type(x) != type(int()):
        print(warn)
        exit()

    if type(time) not in [type(float()), type(int())]:
        print(warn)
        exit()

    if len(symbol)>1:
        print(warn)
        exit()
    
    col = [45, 44, 43, 42, 41, 40, 106, 149, 142, 154, 11, 167, 202, 203, 204, 205, 206, 207, 13, 5, 127, 128, 129, 92, 93, 56, 57, 69, 39, 43, 44, 45]
    l=1
    for i in range(x):
        c = c+b
        if per == 2:
            if color == 'rb':
                
                if l == 32:l=1
                
                cprint(fg(col[l])+'['+symbol*i+' '*a+']', end='\r')
                l+=1
                
            else:cprint('['+symbol*i+' '*a+']', color, end='\r')
                
        elif per == 1:
            
            if color == 'rb':
                
                if l == 32:l=1
                
                cprint(fg(col[l])+'['+symbol*i+' '*a+']' + str(round(c))+'% ', end='\r')
                l+=1
                
            else:cprint('['+symbol*i+' '*a+']' + str(round(c))+'% ', color, end='\r')
                
        else:
            print(warn)
            exit()
        a-=1
        sleep(time)

loading(50, 'о', 2, .1, 'red')
#60 is count of characters
#w is the display character
#1 is when interest is shown, but 2 is not
#.1 is the interval per seconds
#red is color of p-bar
