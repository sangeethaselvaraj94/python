import sys
from time import sleep

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.HEADER + 'Welcome to FLAMES - Fun Compatibility\n' + bcolors.ENDC)
print(bcolors.OKBLUE + '*'*62 + bcolors.ENDC)
print(bcolors.BOLD + 'Friends | Lover | Affectionate | Marriage | Enemies | Siblings' + bcolors.ENDC)
print(bcolors.OKBLUE + '*'*62 + bcolors.ENDC)
print('\n')

FLAMES =['FRIENDS','LOVER','AFFECTIONATE','MARRIAGE','ENEMIES','SIBLINGS']

def split(word): 
    return list(word) 

def removeNthElement(n,flameslist): 
    # list starts with 0 index
    # pos will retain the nth element to be popped
    pos = n - 1
    index = 0
    len_list = (len(flameslist)) 
      
    # breaks out once the list becomes empty 
    while len_list > 0:  

        index = (pos + index) % len_list 
          
        # removes the required element and decrement the length
        flameslist.pop(index)
        len_list -= 1

        # Return the final element available in list
        if len_list == 1:
            return flameslist[0]
  
try:
    n1 = str(input('Enter Person1 Name : ')).strip()
    n1 = n1.replace(' ','').lower()
    if n1.isalpha() and len(n1)>0:
        n2 = str(input('Enter Person2 Name : ')).strip()
        n2 = n2.replace(' ','').lower()
        if n2.isalpha() and len(n2)>0:
            name1 = split(n1)
            name2 = split(n2)

            t1 = split(n1) 
            t2 = split(n2)
        else:
            raise ValueError("\nOOPS!! Not a valid Name...\n") 
    else:
        raise ValueError("\nOOPS!! Not a valid Name...\n") 

except ValueError as e:
    print(bcolors.FAIL)
    print(e) 
    print(bcolors.ENDC)
    sys.exit()

for i,el in enumerate(name1):
    for j,elm in enumerate(name2):
        if el==elm:
            t1.remove(el)
            t2.remove(elm)
            break
    name2 = t2

count = len(t1+t2)

# Driver code 
result = removeNthElement(count,FLAMES)
print('')
for x in '------Analysing Compatibility------':
    print(f'{bcolors.WARNING}{x}{bcolors.ENDC}', end='', flush=True)
    sleep(0.1)
print('')

if result:
    print(f'\n{bcolors.OKGREEN}Hurray!! FLAMES compatibility between {n1} and {n2} is **{result}**\n {bcolors.ENDC}')
else:
    print(bcolors.FAIL + 'OOPS!! Unable to find Compatibility' +bcolors.ENDC)