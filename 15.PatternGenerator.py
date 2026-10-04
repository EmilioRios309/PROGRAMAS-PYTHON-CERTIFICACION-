def numeber_pattern(n):
    if not isinstance(n,int):
        print('Argument must be an integer value.')

    if n < 1:
        print('Argument must be an integer greater than 0.')

    string = ''
    for x in range(1,n+1):
        string += str(x) + ' '

    return string.strip( )

print(numeber_pattern(4))