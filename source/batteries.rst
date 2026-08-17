Batteries included
=====================

.. contents:: Content
    :depth: 2
    :local:
    :backlinks: top

Everything else the framework gives you: a database, background work, timers,
the system tray, notifications, and a few widget helpers.

Databases
-----------

``db.Sqlite3`` is a SQLite database. Point it at a file and it is created if it
does not exist; pass nothing and you get an in-memory database that disappears
when the app closes.

.. code-block:: lua

   local db = require("limekit.db")

   local store = db.Sqlite3("data/app.db")

   store:createTable("notes", {
       id    = "INTEGER PRIMARY KEY AUTOINCREMENT",
       title = "TEXT NOT NULL",
       body  = "TEXT",
   })

   store:insert("notes", { title = "First note", body = "Hello" })
   store:save()

   store:execute("SELECT title, body FROM notes;")
   for _, row in ipairs(store:fetchAll()) do
       print(row[1], row[2])
   end

   store:close()

.. important::

   Changes are not written to disk until you call ``save()``. Forgetting it is
   the most common reason a row "disappears" after a restart.

Connecting
~~~~~~~~~~~~

.. function:: db.Sqlite3(path)
  :no-index:

   Opens a database. ``path`` defaults to ``":memory:"``.

.. function:: close()
  :no-index:

   Closes the connection.

Tables
~~~~~~~~

.. function:: createTable(table_name, columns, if_not_exists)
  :no-index:

   Creates a table from a table of column names to SQL type definitions.
   ``if_not_exists`` defaults to ``true``.

.. function:: tableExists(table_name)
  :no-index:

   Whether the table exists.

.. function:: fetchTables()
  :no-index:

   A table of every table name in the database.

.. function:: getTableInfo(table_name)
  :no-index:

   The column definitions of a table.

Reading and writing
~~~~~~~~~~~~~~~~~~~~~

.. function:: execute(query, params)
  :no-index:

   Runs a single SQL statement. Pass ``params`` as a table rather than building
   the SQL by hand -- it is both safer and easier to read.

   .. code-block:: lua

      store:execute("SELECT * FROM notes WHERE title = ?;", { "First note" })

.. function:: executeMany(query, data)
  :no-index:

   Runs the same statement once per row in ``data``.

.. function:: insert(table_name, data, replace)
  :no-index:

   Inserts a row from a table of column names to values. Set ``replace`` to
   ``true`` to overwrite a conflicting row.

.. function:: fetchAll(as_dict)
  :no-index:

   Every remaining row from the last query. Rows come back as arrays; pass
   ``true`` to get them keyed by column name instead.

   .. code-block:: lua

      store:execute("SELECT title, body FROM notes;")
      for _, row in ipairs(store:fetchAll(true)) do
          print(row.title, row.body)
      end

.. function:: fetchOne(as_dict)
  :no-index:

   The next row only, or ``nil`` if there are none left. A single-column row
   comes back as a bare value rather than a one-item table.

Transactions and maintenance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: save()
  :no-index:

   Commits pending changes to disk.

.. function:: beginTransaction()
  :no-index:

   Starts a transaction.

.. function:: commit()
  :no-index:

   Commits the current transaction.

.. function:: rollback()
  :no-index:

   Abandons the current transaction.

.. function:: backup(target)
  :no-index:

   Copies the whole database to another file.

.. function:: vacuum()
  :no-index:

   Compacts the database file.

.. note::

   Any failure -- malformed SQL, a locked database, a path that cannot be
   written -- is reported as a Limekit error describing the problem. A locked
   database says so in as many words.

Threads
---------

Long work belongs off the interface thread. ``sys.Thread`` runs a function in
the background so your window stays responsive.

.. code-block:: lua

   local sys = require("limekit.sys")

   local worker = sys.Thread()
   worker:setOnThreadRun(function()
       -- slow work goes here
       sys.System.sleep(5)
   end)
   worker:start()

.. important::

   **Never touch a widget from inside a thread.** Interfaces may only be
   updated from the main thread. To tell your interface something has happened,
   use a :ref:`Signal <signals>` -- that is exactly what it is for.

.. function:: sys.Thread()
  :no-index:

   Creates a thread.

.. function:: setOnThreadRun(callback)
  :no-index:

   The function to run in the background. Like every Limekit callback, it is
   guarded -- an error in here is reported rather than crashing the app.

.. function:: start()
  :no-index:

   Begins running.

.. function:: stop()
  :no-index:

   Asks the thread to finish.

.. function:: wait(msecs)
  :no-index:

   Blocks until the thread finishes. With no argument, waits indefinitely.

.. function:: isRunning()
  :no-index:

   Whether the thread is currently running.

.. function:: sleep(seconds)
  :no-index:

   Pauses the thread for a number of seconds.

.. _signals:

Signals
---------

A ``sys.Signal`` is how a background thread asks the main thread to do
something. Call ``relay()`` from the thread; the handler runs safely on the
interface side.

.. code-block:: lua

   local sys = require("limekit.sys")
   local ui  = require("limekit.ui")

   local label  = ui.Label("Working...")
   local done   = sys.Signal()

   done:setOnSignal(function()
       label:setText("Finished!")     -- safe: runs on the main thread
   end)

   local worker = sys.Thread()
   worker:setOnThreadRun(function()
       sys.System.sleep(3)
       done:relay()                   -- safe to call from the thread
   end)
   worker:start()

.. function:: sys.Signal()
  :no-index:

   Creates a signal.

.. function:: setOnSignal(callback)
  :no-index:

   The function to run when the signal fires.

.. function:: relay()
  :no-index:

   Fires the signal. Safe to call from any thread.

Timers
--------

``sys.Timer`` runs a function repeatedly, or once after a delay.

.. code-block:: lua

   local sys = require("limekit.sys")

   local clock = sys.Timer()
   clock:setInterval(1000)            -- milliseconds
   clock:setOnTimeout(function()
       print("tick")
   end)
   clock:start()

.. important::

   Intervals are in **milliseconds**. ``1000`` is one second.

.. function:: sys.Timer()
  :no-index:

   Creates a timer.

.. function:: setInterval(msec) / getInterval()
  :no-index:

   How long between ticks, in milliseconds.

.. function:: setSingleShot(single) / isSingleShot()
  :no-index:

   When ``true``, the timer fires once and stops.

.. function:: setOnTimeout(callback)
  :no-index:

   The function to run on each tick.

.. function:: start(msec)
  :no-index:

   Starts the timer, optionally setting the interval at the same time.

.. function:: stop()
  :no-index:

   Stops the timer.

.. function:: isActive()
  :no-index:

   Whether the timer is currently running.

.. function:: sys.Timer.singleShot(msec, callback)
  :no-index:

   Runs a function once after a delay, without creating a timer to hold on to.

   .. code-block:: lua

      sys.Timer.singleShot(2000, function()
          print("two seconds later")
      end)

System tray
-------------

``ui.SysTray`` puts an icon in the operating system's notification area.

.. code-block:: lua

   local ui  = require("limekit.ui")
   local res = require("limekit.res")

   local menu = ui.Menu()
   local quit = ui.MenuItem("Quit")
   quit:setOnClick(function() sys.System.exit() end)
   menu:addMenuItem(quit)

   local tray = ui.SysTray(res.Resources.images("app.png"))
   tray:setToolTip("My app")
   tray:setMenu(menu)
   tray:show()

.. function:: ui.SysTray(icon)
  :no-index:

   Creates a tray icon.

.. function:: setIcon(path) / getIcon()
  :no-index:

   The icon shown in the tray.

.. function:: setToolTip(text) / getToolTip()
  :no-index:

   The tooltip shown on hover.

.. function:: setMenu(menu) / getMenu()
  :no-index:

   The menu shown when the icon is clicked.

.. function:: setOnActivated(callback)
  :no-index:

   Runs when the user interacts with the icon.

.. function:: show() / hide()
  :no-index:

   Shows or hides the icon.

.. note::

   Not every desktop has a system tray -- some Linux sessions run without one.
   Treat the tray as a convenience rather than the only way to reach your app.

Notifications
---------------

``ui.SysNotification`` shows a desktop notification.

.. code-block:: lua

   local note = ui.SysNotification(res.Resources.images("app.png"))
   note:showMessage("Download complete", "Your file is ready", "information", 5000)

.. function:: ui.SysNotification(icon)
  :no-index:

   Creates a notifier.

.. function:: showMessage(title, message, icon, duration)
  :no-index:

   Shows a notification. ``icon`` is one of ``none``, ``information``,
   ``warning`` or ``critical`` and defaults to ``information``. ``duration`` is
   in milliseconds and defaults to 3000.

.. function:: setIcon(path) / getIcon()
  :no-index:

   The icon shown alongside the message.

.. function:: setOnClick(callback)
  :no-index:

   Runs when the user clicks the notification.

Drop shadows
--------------

``ui.DropShadow`` adds a soft shadow behind any widget.

.. code-block:: lua

   local shadow = ui.DropShadow()
   shadow:setBlurRadius(20)
   shadow:setColor("#7090B0")
   shadow:setOffset(0, 4)
   shadow:applyTo(myCard)

.. function:: ui.DropShadow(widget)
  :no-index:

   Creates a shadow, optionally applying it immediately.

.. function:: setBlurRadius(radius) / getBlurRadius()
  :no-index:

   How soft the shadow is.

.. function:: setColor(colour) / getColor()
  :no-index:

   The shadow colour.

.. function:: setOffset(x, y)
  :no-index:

   How far the shadow is displaced.

.. function:: setOffsetX(x) / setOffsetY(y)
  :no-index:

   The horizontal and vertical displacement individually.

.. function:: applyTo(widget)
  :no-index:

   Attaches the shadow to a widget.

.. note::

   A shadow belongs to one widget at a time. Create one per widget you want to
   shade.

Autocomplete
--------------

``ui.AutoComplete`` adds a suggestion list to a
:doc:`LineEdit </widgets/line-edit>`.

.. code-block:: lua

   local completer = ui.AutoComplete({ "apple", "apricot", "avocado" })
   completer:setCaseSensitive(false)

   local search = ui.LineEdit()
   search:setAutoComplete(completer)

.. function:: ui.AutoComplete(items)
  :no-index:

   Creates a completer from a table of suggestions.

.. function:: setCaseSensitive(sensitive) / isCaseSensitive()
  :no-index:

   Whether matching respects capitalisation.

Keyboard shortcuts
--------------------

``ui.KeyboardShortcut`` binds a key combination to a function.

.. code-block:: lua

   local save = ui.KeyboardShortcut(window, "Ctrl+S")
   save:setOnPress(function()
       saveDocument()
   end)

.. function:: ui.KeyboardShortcut(parent, sequence)
  :no-index:

   Creates a shortcut on a widget. ``sequence`` is written the usual way:
   ``"Ctrl+S"``, ``"Ctrl+Shift+N"``, ``"F5"``.

.. function:: setSequence(sequence) / getSequence()
  :no-index:

   The key combination.

.. function:: setOnPress(callback)
  :no-index:

   Runs when the combination is pressed.

.. function:: setEnabled(enabled) / isEnabled()
  :no-index:

   Whether the shortcut is active.

.. function:: setAutoRepeat(repeat_) / isAutoRepeat()
  :no-index:

   Whether holding the keys fires repeatedly.
