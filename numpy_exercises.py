#!/usr/bin/env python
# coding: utf-8

# # Numpy Exercises
# <hr style="border:2px solid green"> </hr>
# 

# In[137]:


import numpy as np


# In[139]:


#Use the following code for the questions below:
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# ### 1. How many negative numbers are there?

# In[8]:


len(a[a<0])


# ### 2. How many positive numbers are there?

# In[9]:


len(a[a>0])


# ### 3. How many even positive numbers are there?

# In[13]:


len(a[(a%2==0) & (a > 0)])


# ### 4. If you were to add 3 to each data point, how many positive numbers would there be?

# In[15]:


b = a+3
len(b[b>0])


# ### 5. If you squared each number, what would the new mean and standard deviation be?

# In[19]:


c = a**2
print("Mean:", np.mean(c) )
print("Standard Deviation:", np.std(c) )


# ### 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

# In[20]:


d= c-74
np.mean(d)


# ### 7. Calculate the z-score for each data point. 

# In[23]:


z= ( c - np.mean(c) ) / np.std(c)
z


# ### 8. Copy the setup and exercise directions from `More Numpy Practice` into your `numpy_exercises.py` and add your solutions.
# 
# 

# # More Numpy Practice

# In[24]:


## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ### Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

# In[25]:


sum_of_a = np.sum(a)
sum_of_a


# ### Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# In[26]:


min_of_a = np.min(a)
min_of_a


# ### Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
# 

# In[27]:


max_of_a = np.max(a)
max_of_a 


# ### Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
# 

# In[28]:


mean_of_a = np.mean(a)
mean_of_a


# ### Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
# 

# In[29]:


product_of_a= np.product(a)
product_of_a


# ### Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
# 

# In[31]:


squares_of_a = np.square(a)
squares_of_a


# ### Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
# 

# In[38]:


a= np.array(a) #A was a list! Not an array! now the code should work! 
odds_in_a = a[a%2 !=0]
odds_in_a


# ### Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
# 

# In[39]:


evens_in_a = a[a%2 == 0]
evens_in_a


# ### What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
# #### Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
# 

# In[40]:


b = [
    [3, 4, 5],
    [6, 7, 8]
]


# ### Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# 

# In[42]:


b= np.array(b)

#python
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b


# In[50]:


#numpy
np.sum(b)


# ### Exercise 2 - refactor the following to use numpy. 
# 

# In[43]:


#python
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
min_of_b


# In[51]:


#numpy
np.min(b)


# ### Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# 

# In[44]:


#python
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b


# In[52]:


#numpy
np.max(b)


# ### Exercise 4 - refactor the following using numpy to find the mean of b
# 

# In[45]:


#python
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b


# In[53]:


#numpy
np.mean(b)


# ### Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# 

# In[46]:


#python
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_of_b


# In[54]:


#numpy
np.product(b)


# ### Exercise 6 - refactor the following to use numpy to find the list of squares 
# 

# In[47]:


#python
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b


# In[55]:


#numpy
np.square(b)


# ### Exercise 7 - refactor using numpy to determine the odds_in_b
# 

# In[48]:


#python
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
odds_in_b


# In[57]:


#numpy
b[b%2!=0]


# ### Exercise 8 - refactor the following to use numpy to filter only the even numbers

# In[49]:


#python
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
evens_in_b


# In[58]:


#numpy
b[b%2==0]


# ### Exercise 9 - print out the shape of the array b.

# In[59]:


np.shape(b)


# ### Exercise 10 - transpose the array b.
# 

# In[60]:


np.transpose(b)


# ### Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
# 

# In[65]:


np.reshape(b,1*6)


# ### Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
# 

# In[74]:


np.reshape(b,6*1) #why did this not work?


# In[75]:


b.reshape(6,1)


# ### Setup 3
# #### HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.

# In[77]:


c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array(c)


# ### Exercise 1 - Find the min, max, sum, and product of c.

# In[79]:


c.min()


# In[80]:


c.max()


# In[81]:


c.sum()


# In[82]:


c.product()


# In[83]:


np.product(c)


# ### Exercise 2 - Determine the standard deviation of c.

# In[84]:


c.std()


# ### Exercise 3 - Determine the variance of c.

# In[95]:


#The variance is the average of the squared differences from the mean. To figure out the variance, first calculate the difference between each point and the mean; then, square and average the results.
variance_of_c = np.sum( (c - c.mean() ) **2 ) /np.size(c)
variance_of_c


# ### Exercise 4 - Print out the shape of the array c

# In[97]:


np.shape(c)


# ### Exercise 5 - Transpose c and print out transposed result.
# 

# In[98]:


print(np.transpose(c))


# ### Exercise 6 - Get the dot product of the array c with c. 
# 

# In[101]:


np.dot(c,c)


# ### Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
# 

# In[120]:


np.sum( c * np.transpose(c) )


# ### Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
# 

# In[121]:


np.product( c * np.transpose(c) )


# ### Setup 4

# In[123]:


d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d= np.array(d)


# ### Exercise 1 - Find the sine of all the numbers in d
# 

# In[125]:


np.sin(d)


# ### Exercise 2 - Find the cosine of all the numbers in d
# 

# In[126]:


np.cos(d)


# ### Exercise 3 - Find the tangent of all the numbers in d
# 

# In[127]:


np.tan(d)


# ### Exercise 4 - Find all the negative numbers in d
# 

# In[128]:


d[d<0]


# ### Exercise 5 - Find all the positive numbers in d
# 

# In[129]:


d[d>0]


# ### Exercise 6 - Return an array of only the unique numbers in d.
# 

# In[131]:


np.unique(d)


# ### Exercise 7 - Determine how many unique numbers there are in d.

# In[132]:


np.size( np.unique(d) )


# ### Exercise 8 - Print out the shape of d.
# 

# In[133]:


np.shape(d)


# ### Exercise 9 - Transpose and then print out the shape of d.
# 

# In[134]:


np.shape( np.transpose(d) )


# ### Exercise 10 - Reshape d into an array of 9 x 2

# In[136]:


d.reshape(9,2)

