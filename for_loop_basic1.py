# 1 Basic
for i in range(0, 500):
    print(i)

#2 MUltiples of 5
for i in range(5 , 1001, 5):
    print(i)

# 3 Counting
for i in range(1 , 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# 4 Whoa
odd_sum=0
for i in range(0, 500000):
    if i % 2 != 0:
        odd_sum += i
print(odd_sum)

# 5 Countdown
for i in range(2018, 0 , -4):
    print(i)

# 6 Flexible
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)
