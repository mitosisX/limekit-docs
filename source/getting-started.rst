=================
Installation
=================

.. highlight:: console

.. contents:: Content
    :depth: 1
    :local:
    :backlinks: top

What's Limekit
==============

*Limekit* is framework for building desktop applications using the `lua <https://www.lua.org/>`_ language without the need for HTML and CSS. On the other hand allowing developers to maintain one lua codebase and create cross-platform apps that work on Windows, macOS, and Linux.

Key Features:

- **Modern UI**: Limekit allows developers to craft beautiful UI's with dark and light modes available.
- **Simplicity**: One of the notable features of Limekit is it's ability to create a working program in under 2 lines of code as shown below.

    .. code-block:: lua
        :linenos:

        local window = Window{title='Limekit app', icon=images('app.png')}
        window:show()

    - This is basically enough for Limekit to run your program 😊
    
- **No C, C++ or python knowledge**: You don't need to know any python, C or C++ to develop programs in Limekit, just lua
- **Cross-platform**: Run the same code base in Windows, Linux and macOS
- **C Function Conversion**: Converts some Python functions to C functions and compiles them into machine instructions using high optimization options for irreversible obfuscation.
- **Free**: The framework is free to use

Installing Python
======================

The Limekit framework is built in Python 3.10, so you'll need to have Python 3.10 installed to run your code with it. Follow the tutorial to get Python 3.10 installed on your OS.

.. note::
    This guide is for those who haven't delved into Python before and are installing it for the very first time.

Windows
----------

- Installing python on Windows is pretty straight forward. Simply visit `python's website <https://python.org/>`_ to download for your system

Once the installation is complete, open your terminal (Comamnd Prompt or PowerShell) and type the following command::

    $ python

If you get a python console in form of ``>>>``, you are good to go! 😊

After installation, type :command:`pyarmor --version` on the command prompt. If everything worked fine, you will see the version number for the Pyarmor_ package you just installed.

Not all the platforms are supported, more information check :doc:`../reference/environments`