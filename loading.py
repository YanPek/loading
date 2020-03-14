from time import sleep

try: from termcolor import cprint
except ModuleNotFoundError:
    print('You must install module "colorama"\npip install termcolor')
    exit()
try: from colorama import Fore
except ModuleNotFoundError:
    print('You must install module "colorama"\npip install colorama')
    exit()

def warn():
    print(Fore.RED + "loading(int, char, 1 or 2, int or float, color(ex. 'red'))")
    exit()

def loading(x, symbol, per, time, color):
    '''
    Text colors: grey, red, green, yellow, blue, magenta, cyan, white.
    '''
    a = x - 1
    b = 100 / x
    c = 0

    #checking
    if type(x) is not int:
        warn()

    if type(time) not in [float, int]:
        warn()

    if len(symbol) > 1:
        warn()
    
    
    for i in range(x):
        c = c + b
        if per == 1:
            cprint('[' + symbol * i + ' ' * a + ']' + str(round(c)) + '% ', color, end='\r')
        elif per == 2:
            cprint('[' + symbol * i + ' ' * a + ']', color, end='\r')
        else:
            warn()
        a -= 1
        sleep(time)

# 60  is count of characters
# w   is the display character
# 1   is when interest is shown, but 2 is notv
# .1  is the interval per seconds
# red is color of p-bar
loading(60, 'w', 1, .1, 'red')
