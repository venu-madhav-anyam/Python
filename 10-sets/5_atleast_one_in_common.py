my_favs = ["Tom", "Jerry", "Ben 10"]
friend_favs = ["Powerpuff", "Jerry", "Scooby"]

res = any(x in friend_favs for x in my_favs)
print(res)
