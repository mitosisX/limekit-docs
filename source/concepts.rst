Core concepts
================

.. contents:: Content
    :depth: 2
    :local:
    :backlinks: top

There are only a handful of rules in Limekit, and they hold everywhere. Read
this page once and the |classes| classes in the reference section will all
behave the way you expect.

Modules
---------

Limekit 2.0 puts nothing in the global namespace. You ask for what you need:

.. code-block:: lua

   local ui = require("limekit.ui")

There are six modules:

.. list-table::
   :header-rows: 1
   :widths: 22 18 60

   * - Module
     - Classes
     - What's in it
   * - ``limekit.ui``
     - 49 widgets
     - Windows, buttons, layouts, menus, dialogs, themes -- everything you can see or click
   * - ``limekit.sys``
     - 5
     - The machine, threads, signals, timers, and safe arithmetic
   * - ``limekit.fs``
     - 1
     - Reading and writing files, folders and JSON
   * - ``limekit.res``
     - 1
     - Your project's own images, scripts and misc files
   * - ``limekit.db``
     - 1
     - SQLite databases
   * - ``limekit.chart``
     - 9
     - Line, bar and area charts

Require only what a file actually uses. It is normal for a small app to need
just one line:

.. code-block:: lua

   local ui = require("limekit.ui")

and for a larger one to need a few:

.. code-block:: lua

   local ui  = require("limekit.ui")
   local fs  = require("limekit.fs")
   local res = require("limekit.res")

.. note::

   ``require`` works from any file in your project, not just ``main.lua``.
   Your ``scripts`` and ``misc`` folders are both added to ``package.path``
   automatically, including every subfolder, so your own modules require the
   same way: ``require("helpers.formatting")``.

Autocomplete in your editor
-----------------------------

Because every class is registered in one place, Limekit ships type stubs for
the `Lua Language Server <https://luals.github.io/>`_. Point your editor's
``Lua.workspace.library`` setting at the framework's ``runtime/lua/stubs``
folder and you get completion and signatures for every widget as you type.

Creating widgets
------------------

Most widgets take their most obvious value as the single constructor argument:

.. code-block:: lua

   local button = ui.Button("Save")
   local label  = ui.Label("Total:")
   local list   = ui.ListBox({ "one", "two", "three" })

:doc:`Window </widgets/window>`, :doc:`Modal </widgets/modal>` and
:doc:`Chart </charts>` also accept a table of options, which reads better when
you are setting several things at once:

.. code-block:: lua

   local window = ui.Window {
       title    = "My app",
       size     = { 800, 600 },
       location = { 100, 100 },
       icon     = res.Resources.images("app.png"),
   }

Every key is optional. A bare ``ui.Window()`` gives you a 400x400 window
titled "Limekit".

Setters chain
---------------

Every setter returns the widget it was called on, so you can run them together:

.. code-block:: lua

   local title = ui.Label("Welcome")
       :setTextAlignment("center")
       :setWordWrap(true)
       :setStyleSheet("font-size: 24px;")

This is a convenience, not a requirement -- separate lines work identically and
are often clearer.

Getters, setters and ``is``
-----------------------------

Properties follow one naming rule. A property called ``text`` gives you
``getText()`` and ``setText(value)``. Boolean properties additionally get an
``is`` form, because it reads better:

.. code-block:: lua

   checkbox:setChecked(true)

   if checkbox:isChecked() then      -- same as checkbox:getChecked()
       print("on")
   end

.. important::

   Always call widget methods with a colon (``widget:setText("hi")``), never a
   dot. The colon passes the widget itself as the first argument, which is what
   every method expects.

Counting starts at 1
----------------------

Rows, columns, tabs, list items, and every other index in Limekit start at
**1**, the same as Lua's own tables.

.. code-block:: lua

   local table_ = ui.Table(3, 2)
   table_:setCellText(1, 1, "top left")     -- first row, first column
   table_:setCellText(3, 2, "bottom right") -- third row, second column

Passing ``0`` is an error, and the message says so rather than quietly
selecting the wrong cell.

.. note::

   This was not true in 1.x -- some widgets counted from 0 and others from 1.
   If you are porting an app, this is the change most likely to need attention.
   See :doc:`Migrating from 1.x <migrating>`.

Strings instead of constants
------------------------------

Anywhere the framework needs one of a fixed set of values, it takes a plain,
case-insensitive string:

.. code-block:: lua

   slider:setOrientation("vertical")
   label:setTextAlignment("center")
   theme:setTheme("material", "dark_teal")

Get one wrong and Limekit raises an error listing the accepted values, so a
typo shows up immediately instead of being silently ignored.

Errors do not kill your app
-----------------------------

Every callback you attach through a ``setOn...`` method crosses a guard. If
your code raises, Limekit catches it, reports it with the widget and event
name attached, and the application keeps running:

.. code-block:: lua

   local button = ui.Button("Break on purpose")
   button:setOnClick(function()
       error("something went wrong")
   end)

Clicking that button prints a report naming ``Button.onClick`` and leaves the
window perfectly usable. In 1.x an error in most handlers escaped into Qt and
took the whole app down with it.

.. important::

   The guard reports errors -- it does not hide them. Keep an eye on Limer's
   console while you develop.

Project layout
----------------

A Limekit project is a folder:

.. code-block::

   my-app/
     app.json          -- project metadata
     scripts/
       main.lua        -- the entry point, always
     images/           -- your icons and pictures
     misc/             -- everything else: audio, csv, third-party lua modules

``scripts/main.lua`` is what Limekit runs. ``scripts`` and ``misc`` are both on
``package.path``, so your own Lua modules are requirable from anywhere.

Marking a project as 2.0
--------------------------

Limekit ships both the 1.x and 2.0 engines and picks the right one per project.
It works out which you want in two ways:

1. **You tell it.** Add an ``api`` key to ``app.json``. This always wins:

   .. code-block:: json

      {
        "project": {
          "name": "My app",
          "version": "1.0",
          "api": "2.0"
        }
      }

2. **It looks at your code.** If ``scripts/main.lua`` contains a
   ``require("limekit.…")`` call, the project is treated as 2.0.

Anything else runs on the 1.x engine, which is why every existing project keeps
working without being touched. Declaring ``api`` explicitly is the more
predictable of the two, and is recommended for new projects.

.. note::

   Run and Build use the same detection, so an app cannot build against a
   different engine than the one you tested it on.

Running your app
------------------

Press Run in :mod:`Limer`, or from a terminal:

.. code-block:: console

    $ python -m limekit path/to/my-app
