#!/usr/bin/env python
# coding: utf-8

# # Basic Development Tools

# In this section we will install the basic tools needed to develop a serious *Python* application. For now, I will show how I install things on my *Macbook*. As the project progresses, I will add notes covering both Windows and Linix

# ## Mac Installation
# 
# All of the tools mentioned in this section are installed system-wide, meaning they are available for use on any project you start. *Python* applications may need additional tools on a per-project basis. These will be installed in a *Python Virtual Environment* we set up in the development section of these notes.

# ### XCode /Command Line Tools
# 
# Although it is not strictly needed for *Python* development work, there are many handy supporting tools available to *Mac* users by installing *XCode*.
# 
# *XCode* can be installed fro the *Mac Store*. Be warned that *XCode* is huge, so downloading it will take a while!
# 
# Once the installation is complete, open up the program (from the **Applications** directory) and check the version you have by navigating to **XCode->About XCode**.
# 
# Next, you will also need to install the command-line tools. This is done by opening up *XCode* and navigating to the **XCode->Open Developer Tool->More Developer Tools** and selecting the version of the **Command Line Tools** that matches your *XCode* version. 

# ### Homebrew
# 
# Many of the tools I use can be installed easily using a program known as *Homebrew*. You install this program on your system by running this comamnd:
# 
# ```{code}
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# ```
# 
# Once this command completes, check the program by running this command (leave off the leading exclamation point shown here. That is needed to get *Jupyter* to run system commands in this page):

# In[1]:


get_ipython().system('brew --version')


# ### Python
# 
# Obviously we need a recent version of *Python*. *Mac* systems have an older version of *Python* installed by default, but we will work with a newer version. At the time of this writing, Python version 3.11 has been released, but not all of the tools I use are ready for that version. For that reason, I will install *Python 3.10.8* for this project:
# 
# *Homebrew* will not install a program that is already in place on your system. The output from this command can be a bit verbose, so I will just show the command here:
# 
# ```{code}
# brew install python@3.10
# ```

# ### Git

# Git is simple to install using (Homebrew*:
# 
# ```{code}
# brew install git
# ```
# 
# Learning how to use both *Git* and *Github* is worth spending some of your time. Here is one of many tutorials to help you get started: [Git and Github for Beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)

# ### Programmer's Editor
# 
# Picking an editor for your work is a highly personal choice. Since I often work on the command-line on remote servers, I have used an editor called *Vim* for more years than I can count. THe version of this program for the *Mac* is installed on all of my *Mac* systems:
# 
# ```{code}
# brew install --cask macvim
# ```
# 
# This command actually installs both a command-line version of the program that you can launch using the program name **vim**, and a standard graphical version you launch like any normal application from the *Application* menu. The **--cask** option installs both versions.

# ## Windows 11 Installation
# 
# I have given up my older *Windows* versions, and have installed *Windows 11* on my development PC. Setting that system up is more complex than on the *Mac*. Instead of *Homebrew*, I use a similar tool called [Chocolatey](https://chocolatey.org). Unfortunately, installing this tool is a bit difficult since it needs *Microsoft's* super shell tool: *PowerShell*. It is possible to avoid this and just use the installation packages for *Windows* available from the project web sites, but I prefer to use a better management tool.

# ### Powershell
# 
# To install *PowerShell* on your PC, you need to download the program from the *Microsoft* website. *Windows 11* provides aprogram that makes this process easier:
# 
# ```{code}
# winget install --id Microsoft.Powershell --source winget
# ``` 
# 
# Once this command completes, you should find *PowerShell* in your list of installed applications. You can launch is like any other *Windows* programs.
# 
# To install *Chocolatey*, you need to run the *Administrative Shell* version of the program. 
# 
# With the *PowerShell* window open, enter this annoying command:

# ```{code}
# Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'### Python
# ```
# 
# Believe it or not, that command is all on one line. I highly recommend copy and paste to get it right! This will install the *Chocolatey* tool

# ### Python

# You can search for a package using this command:
# 
# ```{code}
# choco search python3
# ```
# 
# This should display a list of available versions of *Python*. We install it using this command:
# 
# ```{code}
# choco install python --version=3.10.8
# ```

# ### Git
# 
# *Git* can be install in a similar manner:
# 
# ```{code}
# choco install git
# ```
# 
# Here, we just get the latest available version.

# ### Programmer's Editor

# ## Linux Installation
# 
# There are many versions of *Linux* available  for PC hardware, and even for tiny machines like the *Raspberry Pi. I normally use the *Ubuntu* distribution, and my students have successfully run that operating system inside *Virtual Machines* on their *Windows* computers. The newer releases of *Windows* support something called *Windows Subsystem for LInux (WSL)* which lets you install *Ubuntu* or another Linux versions directly into your *Windows* environment. You open up a window that will run just like a normal *Linux* machine.
# 
# I will not show that setup here. Instead, I am assuming that you have a computer with the latest version of *Ubuntu* installed, and know how to get to a command-line. 

# In[ ]:




