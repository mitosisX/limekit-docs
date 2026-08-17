==========
 FAQ
==========

.. contents:: Content
    :depth: 1
    :local:
    :backlinks: top

Getting started
=================

Do I need to know Python?
---------------------------

No. Limekit is written in Python, but you write Lua. You need Python
**installed** so the framework can run, and that is the whole of your
involvement with it.

Which Python version?
-----------------------

3.10 or newer. See :doc:`Installation <getting-started>`.

My widget doesn't show up
---------------------------

Almost always one of three things:

1. The widget was never added to a layout.
2. The layout was never given to the window with ``window:setLayout(layout)``.
3. ``window:show()`` was never called.

.. code-block:: lua

   local layout = ui.VLayout()
   layout:addChild(myWidget)      -- 1
   window:setLayout(layout)       -- 2
   window:show()                  -- 3

I get "attempt to index a nil value"
--------------------------------------

You are using a class without requiring its module first. In 2.0 nothing is
global:

.. code-block:: lua

   -- wrong
   local button = ui.Button("Save")

   -- right
   local ui = require("limekit.ui")
   local button = ui.Button("Save")

I get "module 'limekit.ui' not found"
---------------------------------------

Your project is being run by the 1.x engine, which has no module system. Add
``"api": "2.0"`` to the ``project`` block of your ``app.json`` -- see
:doc:`Core concepts <concepts>`.

Why does my method call say it takes no arguments?
----------------------------------------------------

You used a dot where a colon belongs. Widget methods need the colon, which
passes the widget itself:

.. code-block:: lua

   button.setText("Save")    -- wrong
   button:setText("Save")    -- right

Service classes are the exception -- their methods are static and take a dot:

.. code-block:: lua

   fs.FileSystem.readFile("notes.txt")

Working with widgets
======================

Why is my first row or column empty?
--------------------------------------

You are counting from 0. Everything in Limekit counts from **1** -- the first
row of a :doc:`Table </widgets/table>` is row 1, the first tab is tab 1.

Passing 0 raises an error saying so, so this shows up quickly.

How do I push a button to the right?
--------------------------------------

Add a stretch before it:

.. code-block:: lua

   local row = ui.HLayout()
   row:addStretch(1)
   row:addChild(ui.Button("Next"))

How do I change a widget's font or colour?
--------------------------------------------

With a stylesheet, which reads much like CSS:

.. code-block:: lua

   label:setStyleSheet("font-size: 20px; color: #2d7d46;")

For the whole app at once, use a theme instead -- see :doc:`Services <services>`.

How do I make one section of my interface show and hide?
----------------------------------------------------------

Put it in a :doc:`Container </widgets/container>` and hide the container. One
call hides everything inside it.

Errors and debugging
======================

My app printed an error but kept running
------------------------------------------

That is the error guard working as intended. Every callback you attach is
wrapped, so a mistake in one handler is reported rather than closing the app.

The report names the widget and the event, for example ``Button.onClick``, which
tells you where to look. Keep Limer's console visible while developing.

Why doesn't my app respond while it's working?
------------------------------------------------

Long work on the main thread freezes the interface. Move it to a
:doc:`Thread <batteries>` and use a :doc:`Signal <batteries>` to update your
widgets when it finishes.

.. important::

   Never touch a widget from inside a thread. That is what signals are for.

My progress bar doesn't move
------------------------------

Same cause as above -- the interface cannot repaint while your code is busy.

My database changes disappeared after restarting
--------------------------------------------------

You did not call ``save()``. Changes stay in memory until then.

.. code-block:: lua

   store:insert("notes", { title = "Hello" })
   store:save()

Setting a theme did nothing, or raised an error
-------------------------------------------------

The ``material``, ``darklight`` and ``darkstyle`` families come from optional
Python packages. If one is missing, Limekit now raises an error naming the
package to install. In 1.x the call silently did nothing, which is why this may
look like a new problem in an app that seemed fine before.

Migrating
===========

Do I have to migrate my 1.x app?
----------------------------------

No. Limekit ships both engines and picks one per project, so 1.x apps keep
running untouched. Migrate when you want the module system, the error guard and
consistent indexing.

What breaks when I migrate?
-----------------------------

Three things account for nearly all of it: globals becoming modules, the ``app``
table splitting into services, and indexes starting at 1. See
:doc:`Migrating from 1.x <migrating>` for the full list.

Building and shipping
=======================

How do I build an executable?
-------------------------------

Use Limer's Build option. It detects your project's API version the same way
Run does, so an app cannot be built against a different engine than the one you
tested against.

Does the person running my app need Python?
---------------------------------------------

Not for a built executable -- everything is bundled. Python is only needed while
you are developing.

Getting help
==============

- Ask in the `r/limekit <https://www.reddit.com/r/limekit>`_ community
- Email omegamsiskah@gmail.com

A good question includes what you expected, what happened instead, and the
smallest piece of Lua that shows the problem.
