=================
Installation
=================

.. contents:: Content
    :depth: 1
    :local:
    :backlinks: top

What's Limekit?
=================

*Limekit* is a framework for building desktop applications in the
`lua <https://www.lua.org/>`_ language, without HTML and CSS. You keep one Lua
codebase, and your app works on ``Windows``, ``macOS`` and ``Linux``.

~ It is being developed by :mod:`Naveto Tech`, with :mod:`Omega Msiska` as the
lead developer on this project.

Key Features:

- **Modern UI**: craft good-looking interfaces, with dark and light modes.
- **Simplicity**: a working program in three lines of code.

    .. code-block:: lua
        :linenos:

        local ui = require("limekit.ui")
        local window = ui.Window { title = "Limekit app" }
        window:show()

    - That is all Limekit needs to run your program. Mind blowing, right? 😊

Guess what?
------------

- **Just Lua**: you don't need to know C, C++ or Python -- only Lua.
- **Cross-platform**: the same code runs on Windows, Linux and macOS.
- **Free**: the framework is free and open source.

Get Limer
===========

You make Limekit apps with **Limer**: it creates projects, runs them, lets
you design windows by dragging widgets, and builds your finished app into a
program you can give to anyone. Limer is **one download with everything
inside** -- there is nothing else to install.

Download the file for your computer from the
`latest release <https://github.com/mitosisX/Limer-Limekit/releases/latest>`_:

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Your computer
     - Download
     - Then
   * - Windows 10/11, 64-bit
     - ``Limer-<version>-windows.zip``
     - Unzip anywhere, run ``Limer.exe``
   * - Mac with Apple silicon (M1 and later)
     - ``Limer-<version>-macos.zip``
     - Unzip, move **Limer** to Applications, right-click it → **Open**
   * - Mac with an Intel chip
     - ``Limer-<version>-macos-intel.zip``
     - The same
   * - Linux, 64-bit
     - ``Limer-<version>-linux.tar.gz``
     - Unpack anywhere, run ``Limer/Limer``

Not sure which Mac you have? Apple menu → **About This Mac**: "Chip: Apple M…"
is Apple silicon; "Processor: Intel" is Intel.

The first time you open it
----------------------------

The downloads are not code-signed yet, so your system asks you to confirm
the first time:

- **Windows** may say *"Windows protected your PC"*: click **More info**, then
  **Run anyway**.
- **macOS** may say Limer *"cannot be opened because the developer cannot be
  verified"*: right-click **Limer** → **Open** → **Open**. On macOS 15 and
  later, if there is no Open button: **System Settings → Privacy & Security**,
  scroll down, **Open Anyway**.
- **Linux** needs Qt's usual system libraries, which most desktops already
  have. If Limer does not start, on Ubuntu or Debian::

      sudo apt install libxcb-cursor0 libxkbcommon-x11-0 libegl1

.. note::

   The macOS builds are checked automatically on Mac machines before every
   release, but have seen little use on real Macs yet. If something does not
   work, please `open an issue <https://github.com/mitosisX/Limer-Limekit/issues>`_.

When Limer opens you'll see its home page:

.. image:: images/limer/home.png
   :alt: Limer's home page

:doc:`Using Limer <limer>` walks through everything on it, with screenshots.

There are :mod:`plenty of examples` for your journey in Limekit: download
`limekit-demos <https://github.com/mitosisX/limekit-demos/>`_. The
``2.0-examples`` folder holds the ones written for this version.

Your first project
=====================

In Limer, click **New Project**, give it a name and click **Create Project**.
Limer makes the folder and opens it. A Limekit project is just a folder with
a particular shape:

.. code-block::

   my-app/
     app.json
     scripts/
       main.lua
     images/
     misc/

``app.json`` describes the app; the ``"api": "2.0"`` line marks it as a
Limekit 2.0 project:

.. code-block:: json

   {
     "api": "2.0",
     "project": {
       "name": "My app",
       "author": "You",
       "version": "1.0"
     }
   }

Open ``scripts/main.lua`` in your editor and put this in it:

.. code-block:: lua
   :linenos:

   local ui = require("limekit.ui")

   local window = ui.Window { title = "My app", size = { 400, 220 } }

   local label = ui.Label("Nothing clicked yet")
   label:setTextAlignment("center")

   local button = ui.Button("Click me")
   button:setOnClick(function()
       label:setText("You clicked the button")
   end)

   local layout = ui.VLayout()
   layout:setSpacing(10)
   layout:setMargins(20, 20, 20, 20)
   layout:addChild(label)
   layout:addChild(button)

   window:setLayout(layout)
   window:show()

Press **Run** in Limer (or **Ctrl+R**). Your window appears.

.. tip::

   **Using VS Code?** Install
   `Limekit for VS Code <https://marketplace.visualstudio.com/items?itemName=OmegaMsiska.limekit-vscode>`_
   (search "Limekit" in the Extensions panel). You get a ▶ Run button
   (Ctrl+F5), completion and docs for the whole API as you type, and errors
   you can click to jump to the line. It finds Limer on its own once you've
   opened the project in Limer.

You can now move on to :doc:`Core concepts <concepts>`, which covers the few
rules that apply to every widget in the framework.
