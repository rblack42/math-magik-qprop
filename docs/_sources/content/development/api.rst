API
###

This section details the components of the **mmqprop** application. The
information generated here is extracted automatically from the application
code.

Primary mmqprop class
---------------------

..  automodule:: mmqprop
    :members: 

Command Line Event Loop
-----------------------

This class is responsible for loading all installed command plugins, creating
the application context for this run and starting the user command loop. A
simple **>** prompt is provided as a prompt. The **app_debug** flag can be set
in the code to debug the application during development.

..  automodule:: mmqprop.EventLoop
    :members:

Application Context
-------------------

The **Context** class constructs a data store passed to all commands.

..  automodule:: mmqprop.Context
    :members:

Application Command Plugins
---------------------------

Each application command is implemented in a separate file with a name starting
with **cmd_**. New commands can be added by simple writing a new file and
placing it in the **commands** directory.

..  automodule:: mmqprop.commands.cmd_versions
    :members:

..  automodule::   mmqprop.commands.cmd_debug
    :members:

Load Standard QPROP Data Files
------------------------------

These files support loading example data files found in the **QPROP** Fortran
source files. 

Basic File Input
................

The input files have a *Fortram* flavor, using the **!** character to start an
end-of-line comment. Thif file provides code that loads a neded file, deletes
all comments, and returns a simple list of data chinks from the file.

..  automodule::    mmqprop.file_io
    :members:

The next file processes a propeller data file.

..  automodule::    mmqprop.Propeller
    :members:

Next, we process a motor data file

..  automodule::    mmqprop.Motor
    :members:
    
Circulation
...........

..  automodule:::  mmqprop.Circulation
    :members:
    
Standard Atmosphere Model
-------------------------

..  automodule:: mmqprop.StdAtm
    :members:
