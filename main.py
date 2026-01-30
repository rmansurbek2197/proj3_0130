# 1.11
fruits = ['apple', 'kiwi', 'banana', 'pear']
fruits.sort(key=len)
longest = max(fruits, key=len)
filtered = sorted([x for x in fruits if len(x) > 4])
print(longest)
print(filtered)

# 1.12
numbers = [-3, 5, -7, 2, -1, 8]
new_numbers = [x if x >= 0 else 0 for x in numbers]
new_numbers.sort()
print(sum(new_numbers) / len(new_numbers))
print(new_numbers)

# 1.13
scores = [2, 4, 6, 8]
new_scores = [x * 3 for x in scores]
new_scores.sort(reverse=True)
new_scores.append(9)
print(new_scores)

# 1.14
data = [1, 2, 2, 3, 1, 2, 4]
count_dict = {}
for x in data:
    count_dict[x] = count_dict.get(x, 0) + 1
max_item = max(count_dict, key=count_dict.get)
indices = [i for i, x in enumerate(data) if x == max_item]
unique = list(set(data))
print(count_dict)
print(max_item)
print(indices)
print(unique)

# 1.15
mylist = [10, 20, 30, 40, 50, 60, 70]
new_list = mylist[2:6]
print(sum(new_list))
print(new_list[::-1])
mylist.extend(new_list)
print(mylist)
