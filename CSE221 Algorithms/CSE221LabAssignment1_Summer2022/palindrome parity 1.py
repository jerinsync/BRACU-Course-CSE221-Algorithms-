
f = open('input.txt', mode = 'r')
mainlist = []
numlist = []
lines = ['1 madam \n', '2 apple \n', '3.6 racecar']
even = 0
odd = 0
np = 0
p = 0
pal = 0
npal = 0
element = 0

for i in lines:
    element+=1
    a = i.strip().split()
    noparity = 0
    parity = 0
    number = a[0]
    palflag = 0
    notpalflag = 0
    for i in number:
        if '.' in number:
            noparity += 1
        else:
            num = int(number)
            parity += 1
        
    string = a[1]
    n = len(string) // 2
    if len(string) == 0:
        notpalflag += 1
    if len(string) >= 1:
        for j in range(n):
            if string[j] != string[len(string)-1-j]:
                notpalflag += 1
                break

        if notpalflag==0:
            palflag += 1
        
    
    if noparity > 0 and notpalflag > 0:
        list1 = f'{a[0]} cannot have parity and {a[1]} is not a palindrome\n'
        npal += 1
        np+=1

    elif noparity > 0 and palflag > 0:
        list1 = f'{a[0]} cannot have parity and {a[1]} is a pailndrome\n'
        pal += 1
        np+=1

    elif parity > 0 and palflag > 0:
        p += 1
        pal += 1
        if num%2 == 0:
            list1 = f'{a[0]} has even parity and {a[1]} is a pailndrome\n'
            even += 1
        else: 
            list1 = f'{a[0]} has odd parity and {a[1]} is a pailndrome\n'
            odd += 1

    elif parity > 0 and notpalflag > 0:
        p += 1
        npal += 1
        if num%2==0:
            list1 = f'{a[0]} has even parity and {a[1]} is not a pailndrome\n'
            even += 1
        else:
            list1 = f'{a[0]} has odd parity and {a[1]} is not a pailndrome\n'
            odd += 1
    
    mainlist.append(list1)
    numlist.append(a[0])

s1 = []
s1.append(f'Percentage of odd parity: {int((odd/element)*100)}%\n')
s1.append(f'Percentage of even parity: {int((even/element)*100)}%\n')
s1.append(f'Percentage of no parity: {int((np/element)*100)}%\n')
s1.append(f'Percentage of palindrome: {int((pal/element)*100)}%\n')
s1.append(f'Percentage of non-palindrome: {int((npal/element)*100)}%\n')
f.close()

f = open('output.txt', mode = 'w')
f.writelines(mainlist)
f.close()

f = open('record.txt', mode = 'w')
f.writelines(s1)
f.close()


# # In[ ]:




