var = '13'

def ex6():
    var = 'foo'
    def inner():
        nonlocal var
        var = 'bar'
        print('inside inner, var is ', var)
    inner()
    print('inside outer function, var is ', var)

ex6()
print(var)
