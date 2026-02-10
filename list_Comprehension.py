# 1.
numbers = [1, 2, 3, 4, 5]
result1 = [n * n for n in numbers]

#2
nums2 = [3, 10, 15, 20, 25, 30]
evens2 = [n for n in nums2 if n % 2 == 0]

#3
names3 = ["dan", "sara", "noa"]
upper_names3 = [name.upper() for name in names3] 

#4
nums4 = [20, 55, 70, 10, 90]
result4 = [n / 2 for n in nums4 if n > 50]

#5
words5 = ["hi", "python", "is", "awesome"]
lengths5 = [len(w) for w in words5 if len(w) > 2]

#6
squares6 = []
for x in range(10):
    squares6.append(x * x)

#7
evens7 = []
for x in range(50):
    if x % 2 == 0:
        evens7.append(x)

#8
names8 = ["Alice", "Bob", "Charlie"]
first_letters8 = []
for name in names8:
    first_letters8.append(name[0])

#9
nums9 = [120, 50, 200, 30]
small_nums9 = []
for n in nums9:
    if n < 100:
        small_nums9.append(n)

#10
nums10 = [5, 12, 8, 20]
modified10 = []
for n in nums10:
    if n > 10:
        modified10.append(n + 5)
    else:
        modified10.append(n)

#11
triple_nums = [n * 3 for n in range(1, 21)]

#12
divisible_by_5 = [n for n in triple_nums if n % 5 == 0]

#13
reversed_words = [word[::-1] for word in ["Alice", "Bob", "Charlie"]]

#14
special_squares = [n**2 for n in range(1, 31) if n % 3 == 0]

#15
is_even_list = [n % 2 == 0 for n in range(1, 16)]

#16
temps = [15, 25, 35, 10, 28]
temp_status = ["HOT" if t > 30 else "OK" if t >= 20 else "COLD" for t in temps]

#17
first_names = ["Dan", "Noa", "Yossi"]
last_names = ["Levi", "Cohen", "Mizrahi"]
full_names = [f"{first_names[i]} {last_names[i]}" for i in range(len(last_names))]
print(full_names)

#18
coords = [(x, y) for x in range(3) for y in range(3)]

#19
pairs_div_4 = [(x, y) for x in range(1, 11) for y in range(1, 11) if (x + y) % 4 == 0]

#20
users = [
    {"name": "Dan", "age": 17},
    {"name": "Noa", "age": 25},
    {"name": "Yossi", "age": 15},
    {"name": "Maya", "age": 31}
]
adult_names = [u["name"] for u in users if u["age"] >= 18]