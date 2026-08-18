Migrating from 1.x
=====================

.. contents:: Content
    :depth: 2
    :local:
    :backlinks: top

Nothing forces you to migrate. Limekit ships both engines and picks one per
project, so a 1.x app keeps running exactly as it did. This page is for when
you decide to move an app across.

Start here
------------

Add ``"api": "2.0"`` to your ``app.json`` and add the ``require`` line to the
top of every Lua file that touches the framework. Then work through the tables
below. Most apps need changes in three places: the ``app`` object, indexes, and
event handler attachment.

.. code-block:: json

   {
     "project": {
       "name": "My app",
       "api": "2.0"
     }
   }

Globals became modules
------------------------

In 1.x every class was a global. In 2.0 nothing is, so each file starts by
requiring what it uses.

.. code-block:: lua

   -- 1.x
   local button = Button("Save")
   local window = Window { title = "App" }

   -- 2.0
   local ui = require("limekit.ui")
   local button = ui.Button("Save")
   local window = ui.Window { title = "App" }

Widgets, layouts, menus, dialogs and themes all live in ``limekit.ui``. See
:doc:`Core concepts <concepts>` for the full list of modules.

The app object was split up
-----------------------------

The single ``app`` table is gone. Its contents moved to classes grouped by what
they actually do.

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - 1.x
     - 2.0
   * - ``app.readFile(path)``
     - ``fs.FileSystem.readFile(path)``
   * - ``app.writeFile(path, text)``
     - ``fs.FileSystem.writeFile(path, text)``
   * - ``app.joinPaths(...)``
     - ``fs.FileSystem.joinPaths(...)``
   * - ``images("app.png")``
     - ``res.Resources.images("app.png")``
   * - ``scripts("helper.lua")``
     - ``res.Resources.scripts("helper.lua")``
   * - ``misc("song.mp3")``
     - ``res.Resources.misc("song.mp3")``
   * - ``app.getProcessorName()``
     - ``sys.System.getProcessorName()``
   * - ``app.getStandardPath(name)``
     - ``sys.System.getStandardPath(name)``
   * - ``app.splitString(text, sep)``
     - ``sys.System.splitString(text, sep)``
   * - ``app.randomChoice(items)``
     - ``sys.System.randomChoice(items)``
   * - ``app.sleep(seconds)``
     - ``sys.System.sleep(seconds)``
   * - ``app.setStyle(name)``
     - ``ui.Theme.setStyle(name)``
   * - ``app.getStyles()``
     - ``ui.Theme.getStyles()``
   * - file and message dialogs
     - ``ui.Dialogs`` -- see :doc:`Services <services>`

These are all static, so you call them on the class with a dot and pass no
receiver:

.. code-block:: lua

   local fs = require("limekit.fs")
   local text = fs.FileSystem.readFile("notes.txt")

Two removals worth knowing about:

* ``app.evalExpression`` is now ``sys.Expr.evalExpression``. It evaluates
  arithmetic only. The 1.x version could reach Python's ``eval``; this one
  cannot, by construction.
* ``app.weightedGraph`` has no 2.0 equivalent. It was a graph algorithm living
  in a GUI framework -- write it in Lua, or keep that part of the app on 1.x.

Indexes all start at 1
------------------------

This is the change most likely to break an app quietly, because the old code
still runs -- it just touches the wrong cell.

.. code-block:: lua

   -- 1.x: Table used 0-based rows and columns
   table_:setCellText(0, 0, "first cell")

   -- 2.0: everything is 1-based
   table_:setCellText(1, 1, "first cell")

Affects :doc:`Table </widgets/table>`, :doc:`Tab </widgets/tab>`,
:doc:`ListBox </widgets/list-box>`, :doc:`TreeView </widgets/tree-view>`,
:doc:`ComboBox </widgets/combo-box>` and the layouts. Passing ``0`` now raises
an error naming the problem, so the ones you miss announce themselves.

Renamed classes
-----------------

The old names still work -- they are registered as aliases pointing at the same
class -- but the new names are what the documentation uses.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - 1.x
     - 2.0
     - Notes
   * - ``Dockable``
     - ``ui.Dock``
     - Always was the same class under two names
   * - ``TreeWidget``
     - ``ui.TreeView``
     - 1.x shipped two incompatible tree widgets; the working one survived
   * - ``ChartCanvas``
     - ``chart.ChartView``
     - Same wrapper, clearer name

Methods that changed
----------------------

Most of these were broken in 1.x. Where a method could not possibly have worked,
it was replaced rather than reproduced.

.. list-table::
   :header-rows: 1
   :widths: 22 34 44

   * - Widget
     - Change
     - Why
   * - :doc:`Modal </widgets/modal>`
     - Constructor is ``Modal(title, parent)``, not ``Modal(parent, title)``
     - Title first matches every other constructor -- ``Button("Save")``,
       ``Label("Total:")``. Passing them the old way round raises rather than
       misbehaving, but the error names QDialog, not the swap
   * - :doc:`Modal </widgets/modal>`
     - ``show()`` no longer blocks; use ``open()`` for that
     - 1.x's ``show()`` called Qt's blocking modal loop, so it meant something completely different from every other widget's ``show()``
   * - :doc:`Image </widgets/image>`
     - ``resizeImage`` removed; use ``setImageSize``
     - They were byte-for-byte identical methods
   * - :doc:`FormLayout </layouts/form-layout>`
     - ``getAt`` replaced by ``getRowAt``
     - The old one *removed* the row it claimed to read
   * - :doc:`Dock </widgets/dock>`
     - ``setMagneticAreas`` replaced by ``setAllowedAreas``
     - The old one silently ignored area names it did not recognise
   * - :doc:`LCDNumber </widgets/lcd-number>`
     - ``setValuee`` replaced by ``setValue``
     - Misspelled, and its body could only ever raise
   * - :doc:`TimePicker </widgets/time-picker>`
     - ``setDate(y, m, d)`` replaced by ``setTime(hour, minute, second)``
     - A time picker holds a time; the old method fed a date into it and never worked
   * - :doc:`DatePicker </widgets/date-picker>`
     - ``setDate(year, month, day)`` -- the old ``hour``/``minutes`` arguments are gone
     - They were never displayed, and the old call signature raised on every use
   * - :doc:`SlidingStackedWidget </widgets/sliding-stacked-widget>`
     - ``setAnimation`` raises on an unknown name; ``setCurrentWidget`` off-by-one fixed
     - A misspelled animation used to do nothing at all, silently
   * - :doc:`Menu </widgets/menu>`
     - ``buildFromTemplate`` and ``fromTemplate`` removed
     - Three inconsistent versions existed; use ``addMenuItem`` and ``addMenu``
   * - :doc:`ToolbarButton </widget-items/toolbar-item>`
     - ``isChecked()`` now returns a boolean
     - The old one called its own result and always raised
   * - :doc:`SysNotification <batteries>`
     - ``setMessage`` replaced by ``showMessage``
     - The old one silently dropped every notification on machines without a system tray
   * - :doc:`Thread <batteries>`
     - ``sleep(seconds)`` now sleeps
     - The old one called itself with no base case
   * - :doc:`LineChart </charts>`
     - ``setData`` now plots the points
     - The old one printed them to the console instead
   * - :doc:`AreaChart </charts>`
     - Constructor takes the upper and lower series
     - The old signature did not exist on the underlying Qt class
   * - :doc:`Sqlite3 <batteries>`
     - No ``with``-statement support
     - Lua has no ``with``; it was unreachable code

Things that now raise instead of failing quietly
--------------------------------------------------

1.x tended to print a warning, or nothing at all, and carry on. 2.0 raises a
proper error that names the problem. If your app relied on one of these
silently doing nothing, you will hear about it the first time you run:

* Setting a theme whose optional package is not installed.
* Passing an unrecognised enum string -- an orientation, alignment, cursor,
  animation, or dock area.
* Reading a file that does not exist, or running a database query that fails.
  These surface as a Limekit error rather than a raw Python traceback.
* Calling ``setImageSize`` on an :doc:`Image </widgets/image>` before
  ``setImage``.

Errors in your handlers
-------------------------

You no longer need defensive ``pcall`` wrappers around callbacks. Every handler
attached through a ``setOn...`` method is guarded: if it raises, Limekit reports
it with the widget and event name and the app keeps running.

.. code-block:: lua

   -- 1.x: an error here could take the whole app down
   button:setOnClick(function()
       riskyThing()
   end)

   -- 2.0: reported, app survives
   button:setOnClick(function()
       riskyThing()
   end)

Same code, different outcome.

What did not change
---------------------

* **Timer intervals are still milliseconds.** ``timer:setInterval(1000)`` is
  still one second.
* **Colours** still accept the same strings and ``{r, g, b}`` tables.
* **Your project layout** is unchanged: ``app.json``, ``scripts/main.lua``,
  ``images/``, ``misc/``.
* **Stylesheets** are unchanged.
