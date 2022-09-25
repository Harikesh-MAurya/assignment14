# 1. Write a Python script to create a list of first N natural numbers.
# 2. Write a Python script to create a list of first N odd natural numbers.
# 3. Write a Python script to create a list of first N even natural numbers.
# 4. Write a Python script to find the greatest number in a given list of numbers.
# 5. Write a Python script to find the smallest number in a given list of 10 numbers.
# 6. Write a Python script to calculate the sum of elements in a given list of numbers.
# 7. Write a Python script to remove all non int values from a list.
# 8. Write a Python script to print distinct elements along with their frequencies of
# occurrence in the list.
# 9. Write a Python script to print indices of all occurrences of a given element in a given
# list.
# 10. Write a python script to sort a list.

# 1) .........................................................
# n=int(input("Enter n : "))
# b=[]
# for i in range(1,n+1):
#     b.append(i)
# print(b,end=" ")
    
    
# 2) .........................................................
# n=int(input("Enter n : "))
# b=[]
# for i in range(1,n+1,2):
#     b.append(i)
# print(b,end=" ")
    
    
# 3)........................................................
# n=int(input("Enter n : "))
# b=[]
# for i in range(2,n+1,2):
#     b.append(i)
# print(b,end=" ")
    
    
# 4) .......................................................
# l1=[1,2,3,4,5,6,7,8,9,10]
# # print(max(l1))
# for i in range(0,len(l1)-1):
#     for j in range(1,len(l1)):
#         if l1[i]<l1[j]:
#             l1[i]=l1[j]
# print(l1[i])


# 5)......................................................
# l1=[1,2,3,4,5,6,7,8,9,10]
# # # print(max(l1))
# for i in range(1,len(l1)):
#     for j in range(0,len(l1)-1):
#         if l1[i]>l1[j]:
#             l1[i]=l1[j]
# print(l1[i])


# 6).......................................................
# l1=[1,2,3,4,5,6,7,8,9,10]
# s=0
# for i in range(0,len(l1)):
#     s+=l1[i]
# print(s)


# 7)..........................................................
# l1=[1,2,'java',3,73.3,4,5,'pythone',6,7,28.3,8,9,'C',10,True]
# for i in l1:
#     if (type(i)==int):
#         l1.remove(i)
#     print(l1)
        

# 8).................................................
l2=[1,2,3,6,2,5,2,8,9,1,3,7,8,4,1,6,8,7,4,2]
freq={}
for i in l2:
    for j in str(i):
        if (j in freq):
            freq[j]+=1
        else:
            freq[j]=1
for key,value in freq.i():
    print("%d : %d"%(int(key),int(value)))