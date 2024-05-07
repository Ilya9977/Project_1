def f(x, y):
    if x > y and y > x:
        print('I')
    elif x > 0 and y < 0:
        print('II')
    elif x < 0 and y > 0:
        print('III')
    else:
        print('IV')