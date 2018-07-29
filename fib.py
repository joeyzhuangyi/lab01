'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

def produceFibsList(n):
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''
    # TODO = fill in the code here, and return the correct result using the return keyword
    number = []
    if n == 1:
        number.append(1)
    elif n == 2:
        number.append(1)
        number.append(1)
    elif ( n>2):

        number.append(1)
        number.append(1)
        pre1=1
        pre2=1
        for i in range(2,n):
            a = pre2
            pre2 = pre2+pre1
            pre1 = a
            number.append(pre2)
        
    print(number)
              
            
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
