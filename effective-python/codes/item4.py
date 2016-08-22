# coding: utf-8
from urlparse import parse_qs

def rgb_parse(qs):
    '''
    输入样本： red=5&blue=7&green=
    '''
    my_values = parse_qs(qs, keep_blank_values=True)
    print 'Red', my_values.get('red')
    print 'Green', my_values.get('green')
    print 'Opacity', my_values.get('opacity')


def rgb_parse_one(qs):

    my_values = parse_qs(qs, keep_blank_values=True)

    red = my_values.get('red', [''])[0] or 0
    green = my_values.get('green', [''])[0] or 0
    opacity = my_values.get('opacity', [''])[0] or 0

    print 'Red: %r' % red
    print 'Green: %r' % green
    print 'Opacity: %r' % opacity


def rgb_parse_two(qs):

    my_values = parse_qs(qs, keep_blank_values=True)

    # 严重牺牲可读性
    red = int(my_values.get('red', [''])[0] or 0)
    green = int(my_values.get('green', [''])[0] or 0)
    opacity = int(my_values.get('opacity', [''])[0] or 0)

    print 'Red: %r' % red
    print 'Green: %r' % green
    print 'Opacity: %r' % opacity


def rgb_parse_three(qs):

    my_values = parse_qs(qs, keep_blank_values=True)

    # 使用单行if else易读性增强
    red = my_values.get('red', [''])
    red = int(red[0]) if red[0] else 0
    green = my_values.get('green', [''])
    green = int(green[0]) if green[0] else 0
    opacity = my_values.get('opacity', [''])
    opacity = int(opacity[0]) if opacity[0] else 0

    print 'Red: %r' % red
    print 'Green: %r' % green
    print 'Opacity: %r' % opacity


def rgb_parse_four(qs):

    my_values = parse_qs(qs, keep_blank_values=True)

    # 使用单行if else易读性增强
    red = my_values.get('red', [''])
    if red[0]:
        red = int(red[0])
    else:
        red = 0

    green = my_values.get('green', [''])
    if green[0]:
        green = int(green[0])
    else:
        green = 0

    opacity = my_values.get('opacity', [''])
    if opacity[0]:
        opacity = int(opacity[0])
    else:
        opacity = 0

    print 'Red: %r' % red
    print 'Green: %r' % green
    print 'Opacity: %r' % opacity


def get_first_int(values, key, default=0):

    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


def rgb_parse_five(qs):

    my_values = parse_qs(qs, keep_blank_values=True)
    red = get_first_int(my_values, 'red')
    green = get_first_int(my_values, 'green')
    opacity = get_first_int(my_values, 'opacity')

    print 'Red: %r' % red
    print 'Green: %r' % green
    print 'Opacity: %r' % opacity

if __name__ == '__main__':
    rgb_parse_two('red=5&blue=7&green=')
