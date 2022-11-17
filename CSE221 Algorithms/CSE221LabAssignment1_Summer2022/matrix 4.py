
a1 = '[[2, 8, 4],[4, 5, 6],[7, 1, 9]]'
b1 = '[[5, 9, 1],[6, 1, 3],[7, 8, 6]]'

dig ='0123456789'
s1=[]
A = []
for i in a1:
    if i in dig:
        s1 = s1+[int(i)]
    if ']' in i:
        A = A + [s1]
        s1=[]

s2=[]
B=[]
for i in b1:
    if i in dig:
        s2 = s2+[int(i)]
    if ']' in i:
        B = B + [s2]
        s2=[]

A.pop(-1)
B.pop(-1)

n=0
for i in A:
    n+=1


def Multiply_matrix(A,B): 

    C = [[0]*n for i in range(n)] #time Complexity will be O(n)

    for i in range(0,n): #time Complexity will be O(n)
        for j in range(0,n): #time Complexity will be O(n)
            for k in range(0,n): #time Complexity will be O(n)
                print(C[i][j])
                print(A[i][k])
                print(B[k][j])
                C[i][j] += A[i][k] * B[k][j]
    return C

#time Complexity: -
# n + n^3
# O(n^3)

s1 = Multiply_matrix(A,B)
val = str(s1)
# f.close()

# f = open('output04.txt', mode = 'w')
# f.write(val)
# f.close()


# # In[ ]:




