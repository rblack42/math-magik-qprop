#!/usr/bin/env python
# coding: utf-8

# # Project Setup

# We begin all *Python* applications by coming up with a program name. This name becomes the name of a single directory somewhere on your development system. Under that directory we will keep everything needed to recreate this program on another machine.
# 
# We will manage that directory using a very popular *Source Code Control System* called *Git*. This tool tracks all changes to your project and lets you "back up" if you manage to break the project. No self-respecting developer works without using a tool like *Git* today!
# 
# We will host a copy of the project directory on a public server: *Github*. This site is home to literally millions of open-source* projects as well as some private projects not visible except to registered users. *Github* is free, and all you need to do to use it is to navigate to their [Github website](https://github.com) and register. You will be asked to pick a user name which will become part of the URL you use to reach your projecta. My *Github* user name is **rblack42**. At the present time I have over 100 projects hosted there, as well as a huge number of student projects from my teaching days! (I do pay a subscription fee to let me keep student work private.)

# ## Verify Development Tools are in place

# Let's start off by verifying that we have the basic tools we will need, ready to go. Details on installing these tools is included in the [appendix](../appendix/installing-basic-tools.ipynb). I will show how I check this on the *Macbook* laptop I use for development work:

# ### Python
# 
# *Python* is a very popular programming language for beginners. I taught this to beginning college students for many years. You can see an example of my course notes at [COSC1336 Lecture notes](http://www.co-pylit.org/courses/cosc1336). (No, you cannot get credit for taking this course, I am retired10

# In[1]:


get_ipython().system('python --version')


# ### Git
# 
# I use *Git* to track changes to all of my software development projects. When combined with an account on *Github* you have a reliable way to protect your code and make it available to collaborators who might want to join you in your development work.

# In[2]:


get_ipython().system('git --version')


# ### Programmer's Editor
# 
# My favorite editor for all text writing, but especially for writing software code is *Vim*. It has been around longer that the personal computer. It was originally developed back when computers only had command line interfaces. No mice anywhere! Feel free to install any editor you like. Just make sure it produces simple text output. Do **NOT** not use something fancy like a word processor.

# In[3]:


get_ipython().system('vim --version')


# That is a lot of output. This program has many features for serious development work, and it can even be extended using *Python* to teach it new tricks.

# In[ ]:




