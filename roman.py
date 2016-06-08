def main():
    roman = str(input("Enter the Roman number : "))
    arr = []
    ans = int_convert(roman_eq(roman,arr))
    print("The Integer value Of %s is %d"%(roman,ans))

def roman_eq(x,a):
    length = len(x)
    for i in range(length):
        if(x[i] == 'I'):
            a.append(1)
        elif(x[i] =='V'):
            a.append(5)
        elif(x[i] == 'X'):
            a.append(10)
        elif(x[i] == 'L'):
            a.append(50)
        elif(x[i] == 'C'):
            a.append(100)
        elif(x[i] == 'D'):
            a.append(500)
        elif(x[i] == 'M'):
            a.append(1000)
        else:
            print("Enter valid character !")
            a.append(0)
    return a

def int_convert(a):
    i = len(a) - 1
    k = a[i]
    while(i>0):
        if(a[i]>a[i-1]):
            k -= a[i-1]
        elif(a[i] == a[i-1] or a[i]<a[i-1]):
            k += a[i-1]
        else:
            pass
        i -= 1
    return k

if __name__ == '__main__':
    main()
