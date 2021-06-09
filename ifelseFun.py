is_male = True
is_tall = False

if is_male or is_tall:
    print('Yip')
elif is_male and not(is_tall):
    print('hehe')
elif not(is_male) and is_tall:
    print('hehe')
else:
    print('Nope')