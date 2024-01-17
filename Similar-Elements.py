n = int(input("No of Elements : "))
l = list(map(int,input("Elements : ").split()))[:n]

dic = {}
for i in range(n):
    if l[i] in dic:
        dic[l[i]].append(i+1)
    else:
        dic[l[i]] = [i+1]

for i,j in dic.items():
    if len(j) > 1:
        print('\nSimilar element : ',i)
        print('Positions : ',end="")
        for k in j:
            print(k,end=" ")
        print('\nOccurrence : ',len(j))

'''
Sample Output
-------------------------
No of Elements : 5

Elements : 15 15 23 15 23

Similar element :  15
Positions : 1 2 4 
Occurrence :  3

Similar element :  23
Positions : 3 5 
Occurrence :  2
-------------------------
Time Complexity  : O(n)
Space Complexity : O(n)
'''
