
def f(n):
    s = []
    def func(n, s):
        i = 0
        while i < n:
            if i == 0:
                s.append(1)
            elif i == 1:
                s.append(1)
            else:
                s.append(s[i-2]+s[i-1])
            i += 1

    func(n,s)
    print(s)

#f(1)
    f(-10)