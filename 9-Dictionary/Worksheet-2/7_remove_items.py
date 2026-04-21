spells = {'fireball': 5, 'healing': 10, 'curse': 2}
banned = ['curse', 'fireball']

del spells[banned[0]]
del spells[banned[1]]

print(spells)