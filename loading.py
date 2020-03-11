from time import sleep

try: from termcolor import cprint
except ModuleNotFoundError:
    print("You must install module 'colorama'\npip install termcolor")
    exit()
try: from colorama import Fore
except ModuleNotFoundError:
    print("You must install module 'colorama'\npip install colorama")
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
    
    
    for i in range(x):
        c = c+b
        if per == 1:
            cprint('['+symbol*i+' '*a+']' + str(round(c))+'% ', color, end='\r')
        elif per == 2:
            cprint('['+symbol*i+' '*a+']', color, end='\r')
        else:
            print(warn)
            exit()
        a-=1
        sleep(time)

loading(50, 'о', 1, .1, 'green')
#60 is count of characters
#w is the display character
#1 is when interest is shown, but 2 is notv
#.1 is the interval per seconds
#red is color of p-bar
