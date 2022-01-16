#!/usr/bin/env python
# coding: utf-8

# In[1]:



num = 6

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[3]:


# Program to check if a number is prime or not

num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")


# In[4]:


# function to check string is
# palindrome or not
def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")


# In[5]:


def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))


# In[6]:


string=input("Enter the string ")
freq=[None]*len(string)
for i in range(0,len(string)):
  freq[i]=1
  for j in range(i+1,len(string)):
    if(string[i]==string[j]):
        freq[i]=freq[i]+1
        string=string[:j]+'0'+string[j+1:];
print("Character and their frequency");
for i in range(0,len(freq)):
    if(string[i]!=' ' and string[i]!='0'):
        print(string[i]+"="+str(freq[i]))


# In[ ]:




