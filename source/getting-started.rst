=================
Installation
=================

.. highlight:: console

.. contents:: Content
    :depth: 1
    :local:
    :backlinks: top

What's Limekit?
=================

*Limekit* is framework for building desktop applications using the `lua <https://www.lua.org/>`_ language without the need for HTML and CSS. On the other hand allowing developers to maintain one lua codebase and create cross-platform apps that work on ``Windows``, ``macOS``, and ``Linux``.

~ It is being developed by company called :mod:`Take bytes`, with :mod:`Omega Msiska` as the lead developer on this project.

Key Features:

- **Modern UI**: Limekit allows developers to craft beautiful UI's with dark and light modes available.
- **Simplicity**: One of the notable features of Limekit is it's ability to create a working program in under 2 lines of code as shown below.

    .. code-block:: lua
        :linenos:

        local window = Window{title='Limekit app', icon=images('app.png')}
        window:show()

    - This is basically enough for Limekit to run your program. Mind blowing right? 😊

Guess what?
------------
    
- **No C, C++ or python knowledge**: You don't need to know any python, C or C++ to develop programs in :mod:`Limekit`, just lua
- **Cross-platform**: Run the same code base in Windows, Linux and macOS
- **Free**: The framework is free to use

Installing Python
======================

The Limekit framework is built in Python 3.10, so :command:`you'll need to have Python 3.10 installed` to use the framework. Follow the tutorial to get Python 3.10 installed on your OS.

.. note::
    This guide is for those who haven't delved into Python before and are installing it for the very first time.

Windows
----------

- Installing python on Windows is pretty straight forward. Simply visit `python's website <https://www.python.org/downloads/release/python-31011/>`_ to download for your system

Once the installation is complete, open your terminal (Comamnd Prompt or PowerShell) and type the following command::

    $ python

If you get a similar output as the one below, you are good to go! 😊

.. code-block::
    
    Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Navigate to the bottom of the page to follow through the final stages

Linux
----------

.. note::

    The framework has only been tested on Ubuntu, but it's expected to function on other Linux distros as well.

.. important::
    
    Before trying to install python3.10, try executing ``python3.10`` or ``python3 --version`` in the terminal to see if python is already installed, as most Linux distributions come with python installed

Head over to `this website <https://www.linuxcapable.com/how-to-install-python-3-10-on-ubuntu-linux/>`_ to learn how to install python3.10 on your Linux

Done installing. What's next?
===============================

.. important::

    Read the below instructions before downlaoding anything

    All required files should be downloaded from the :mod:`Releases` page (right hand side) in the github links provided

    :mod:`Installation requires an active internet connection`

Head over to `our github repo <https://github.com/mitosisX/Limer-Limekit/>`_ to download :mod:`Limer`.

There are :mod:`over 30 examples` prepared for your journey in Limekit, just click `here <https://github.com/mitosisX/limekit-ui-examples/>`_ to downlaod them

.. note::

    :mod:`Limer` is the program that ``only`` runs your apps. It's not an IDE or an editor.

Download all the zip files from the :mod:`Releases` section and extract them. Inside the windows-only.zip or linuxmac-only.zip there should be a ``READ ME.txt`` file that explains everything.

If everything goes as planned, you'll be greeted by a screen similar to the one shown below.

.. image:: images/limekit.png

You can now start learning how to use widgets.