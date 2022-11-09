#!/usr/bin/env python
# coding: utf-8

# In[68]:


import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[52]:


#    1. How many negative numbers are there?

print(np.count_nonzero(a < 0))
#print(f"{}")


# In[105]:


#    2. How many positive numbers are there?

print(np.sum(a >0))


# In[112]:


#    3. How many even positive numbers are there?

print(np.sum((a > 0) & (a%2 == 0)))


# In[75]:


#    4. If you were to add 3 to each data point, 
#       how many positive numbers would there be?

b=a+3

print(np.sum(b<0))


# In[83]:


#    5. If you squared each number, what would 
#       the new mean and standard deviation be?
squared=a**2

print(f"Original List: \t {a}")
print(f"Each squared: \t {squared}")


# In[99]:


#    6. A common statistical operation on a dataset is centering.
#       This means to adjust the data such that the mean of the
#       data is 0. This is done by subtracting the mean from each
#       data point. Center the data set. See this link for more on
#       centering.

import statistics as st

list_average = st.mean(a)

centered = a-list_average

print(f"Centered: \t {centered}")

#a.mean()
#create function to center data
#center_function = lambda x: x - x.mean()
#apply function to original NumPy array
#data_centered = center_function(a)
#view updated Array
#data_centered
#data_centered.mean()


# In[104]:


#    7. Calculate the z-score for each data point. Recall that the
#       z-score is given by:

#       z = (x-avg)/std

z_scores = a-(st.mean(a))/st.stdev(a)
print(f"Z-Scores: \t {z_scores}")


# In[ ]:


#    BONUS. Awesome Bonus For much more practice with numpy, Go to https://github.com/rougier/numpy-100 
#           and clone the repo down to your laptop. To clone a repository: - Copy the SSH address of
#           the repository - cd ~/codeup-data-science - Then type git clone git@github.com:rougier/numpy-100.git - 
#           Now do cd numpy-100 on your terminal. - Type git remote remove origin, so you won't accidentally 
#           try to push your work to Rougier's repo.

#           Congratulations! You have cloned Rougier's 100 numpy exercises to your computer. Now you need to 
#           make a new, blank, repository on GitHub.

#           Go to https://github.com/new to make a new repo. Name it numpy-100.
       
#           DO NOT check any check boxes. We need a blank, empty repo.
      
#           Finally, follow the directions to "push an existing repository from 
#           the command line" so that you can push up your changes to your own account.
#           Now do work, add it, commit it, and push it!

