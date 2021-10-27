
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends2 = friends.copy()
friends.extend(lucky_numbers)
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.pop()
friends.append("Jim")
lucky_numbers.reverse()
friends.sort()
print(friends.count("Jim"))

