homies = ['2pac', 'biggie', 'dre', 'snoop dogg', 'Waren G', 'Ice Cube']
lucky_number = [6, 30, 17, 8, 24, 19, 12, 26]

homies.append(lucky_number)
homies.extend(lucky_number)

homies.insert(1, 'DMX')
homies.remove('Waren G')


homies.pop()
# homies.clear()
print(homies.count('dre'))


lucky_number.sort()
lucky_number.reverse()

print(lucky_number)

homies2 = homies.copy()
print(homies2)