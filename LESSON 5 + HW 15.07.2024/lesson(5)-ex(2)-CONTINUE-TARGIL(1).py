# lesson 5 ex 2 CONTINUE TARGIL 1

# TARGIL CONTINUE

# print all numbers between 1 - 100 , dont print numbers which are multiple of 7.
# sum all of the numbers (which are not multiple of 7)
# and print all

# START

total_sum = 0

for number in range(1, 101):
    if number % 7 == 0:
        continue
    print(number)
    total_sum += number

print("Total sum of numbers not multiple of 7:", total_sum);

# END

# 1
# 2
# 3
# 4
# 5
# 6
# 8
# 9
# 10
# 11
# 12
# 13
# 15
# 16
# 17
# 18
# 19
# 20
# 22
# 23
# 24
# 25
# 26
# 27
# 29
# 30
# 31
# 32
# 33
# 34
# 36
# 37
# 38
# 39
# 40
# 41
# 43
# 44
# 45
# 46
# 47
# 48
# 50
# 51
# 52
# 53
# 54
# 55
# 57
# 58
# 59
# 60
# 61
# 62
# 64
# 65
# 66
# 67
# 68
# 69
# 71
# 72
# 73
# 74
# 75
# 76
# 78
# 79
# 80
# 81
# 82
# 83
# 85
# 86
# 87
# 88
# 89
# 90
# 92
# 93
# 94
# 95
# 96
# 97
# 99
# Total sum of numbers not multiple of 7: 4215