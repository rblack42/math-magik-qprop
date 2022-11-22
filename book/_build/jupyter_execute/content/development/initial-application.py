#!/usr/bin/env python
# coding: utf-8

# # Initial Application

# To get started with our development, we will build the smallest chunk of code we can, to just run the program.
# 
# First, create a home for the code inside of the project directory. This new directory should have the same name as the project. Run this command while working in the top-level project directory:
#     
# ```{code}
# mkdir mmqprop
# ```
# 
# Now, edit a new file inside of this new directory:
# 
# 
# 
# ```{code}
# vim mmqprop/__init__.py
# ```
# 
# This file will turn the directory into a *Python* package. Here is the code you need:
# 
# mmqprop/__init.py:
# ```{code}
# __version__ = '0.1.0'
# 
# def version():
#     return __version__
# 
# ```
# 
# This snippet establishes the version number for the project and sets up a way to fetch that number. We will set things up to update this number as the project development proceeds.
# 

# Next, we set up another piece of code that will help us run the program. This file also lives in the **mmqprop** package directory:
#     
# mmqprop/__min__.py:
# ```{code}
# from . import version
# 
# print("mmqprop version:", version())
# ```
# 
# In order to demonstrate running this code in this *Jupyter* page, we need to convince the (Jupyter application to move to the right directory and then run the command. 
# 
# From the top level project directory, we should just use this command:
#     
# ```{code}
# python -m mmqprop
# ```

# First, let's see where *Juputer* thinks we are working with *Python* code on this page:

# In[1]:


get_ipython().system('pwd')


# We actually need to be three levels up to get to the project root directory. We can make *Jupyter* move there, then run the command as follows:

# In[2]:


get_ipython().system('cd ../../.. && python -m mmqprop')


# That is what we should see at this point. 

# The first part of that line changes the working directory to the top level of the project, three levels up. The **&&** combines commands, one after the other. The last part of the line is the actual command that runs the program. After this entire line completes, *Jupyter* will return to the original working directory, which is where this document page lives.
#                 

# In[3]:


get_ipython().system('pwd')


# At this point we have a basic, very primitive, *Python* application running. Next, we will set up testing.
