from random import shuffle
example = [' ',' ','0']


def check_sufle(mylist):
    shuffle(mylist)
    return mylist

def take_input():
          guess = ' '
          while guess not in ['1','2','3']:
             guess = input('input should be 1 ,2 or 3')
              
          return int(guess)
def check_result(mylist,guess):
    if mylist[guess] == '0':
        print('you win')
    else:
        print('try again')


result = check_sufle(example)
print(result)
guess =take_input()
check_result(result,guess)
