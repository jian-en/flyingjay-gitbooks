def log(message, *values, **kwargs):
    print(type(values))
    print(values)
    print kwargs
    values_str = ','.join(str(x) for x in values)
    print('%s:%s' % (message, values_str))

log('My numbers are', *[1, 2])
log('Hi there')
