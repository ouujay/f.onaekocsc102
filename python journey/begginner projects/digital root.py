def digital_root(n):
    value = 0
    temp = n
    while temp>9:
            for i in str(temp):
                  value += int(i)
            temp = value
            value = 0
    return temp


digital_root(356)

   