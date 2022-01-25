def func(str_num):
    length = len(str_num)
    d = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    index = length - 1
    digit = 0
    value = 0
    for i in range(2,length):
        element = str_num[index]
        if element in d:
            value += d[element] *pow(16, digit)
        else:
            value += int(element) * pow(16, digit)
        index -= 1
        digit += 1
    return value
        
while True:
    try:
        s = input()
        result = func(s)
        print(result)
    except:
        break
        