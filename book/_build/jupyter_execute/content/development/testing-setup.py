#!/usr/bin/env python
# coding: utf-8

# # Testing Setup
All code you right should be tested to make sure it works as you expect. Long ago, testing was ignored and sometimes left for the users to do and give feedback to the developers. Thankfully, those days are over. Now developers are expected to fully test the programs *before* the user gets their hands on it!

## Test Driven Development

The modern development scheme is called *Test Driven Development*. To beginners, this may look strange. 

We begin by thinking up a small piece of code we can add to the project. We then think about how we will know that new piece of code actually works. Once we know that, we write a test that will exercise our new code and prove that it works. Tests should produce no output if things work, and print some kind of error message if they fail. 

Once th etest is in place, we run it and prove our vode does not work. It shouldn't because we have not written it yet! Once the test is in place, we write the code and make sure the test passes. 

We are not quite done at that point. Instead, we study the new code and see if there is a way ot clean it up. We do not wanto to change how it works, jus make is work "beter". This is called *refactoring*. Once you are happy with the new code, you repeat the process over and over until you are done.

As you write new tests, you run all the old tests again to make sure you have not broken something that worked earlier. If you break something, your code is *regressing* and this type of testing is called *regression testing*.


### Managing Tests

Rather than do all of this work manually, we will use a powerful testing tool called *PyTest*. We install this program by adding a **pytest** line ot our **requirements.in** file, then running **make reqs**.

*PyTest* manages all test code in a single **tests** directory in the project **root** directory. All test files need to have a name that begins with **test_** folowd by some test name. Let's write a test that checks the version number:

tests/test_version.py
```{code}
from mmqprop import version

def test_version_string():
    assert version() == '0.1.0'
```

Obviously, if we change the version number, we will need to change this test. We will get to that later.

If *PyTest* is installed, we can run this test as follows:
# In[1]:


get_ipython().system('cd ../../.. && python -m pytest tests')


# Now we know our testing structure is in place and works. If that test had failed, we would have seen an error message.

# In[ ]:




