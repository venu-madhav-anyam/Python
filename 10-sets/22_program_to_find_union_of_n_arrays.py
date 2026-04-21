friends_colors = [["red", "blue"],["green", "red"],["yellow", "blue"]]
res = list(set().union(*friends_colors))
print(res)