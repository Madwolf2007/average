def average(lists):
    count = 0
    plus = 0
    for i in lists:
        count = count + 1
        plus = plus + i
    ave = plus / count
    print(ave)
