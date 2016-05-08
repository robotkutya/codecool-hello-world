import sys

#This function gets the name from the command line arguments
def get_name():
    l = len(sys.argv)
    n = ''
    if l <= 1:
        return(n)
        #Alternatively, we could return 'World'
    else:
        for i in range(1, l):
            n = n + sys.argv[i] + ' '
        #n ends with a <space>, we want to get rid of that
        n = n[:-1]
        return(n)

def say_hello(n):
    if n == '':
        print('Hello World!')
    else:
        print('Hello ' + n +'!')

#now the actual program
name = get_name()
say_hello(name)
