Widgets
========

Widgets are the graphical elements that make up the user interface of an
application: buttons, text boxes, labels, windows, checkboxes, sliders and
more. They let people interact with your program by providing input, displaying
information, or triggering actions.

There are |widgets| widgets in the framework. Every one of them lives in
``limekit.ui``:

.. code-block:: lua

   local ui = require("limekit.ui")

.. important::

   Every app needs a Window. In your :mod:`main.lua`, create one like this:

   .. code-block:: lua
      :linenos:

      local ui = require("limekit.ui")

      local window = ui.Window { title = "Limekit", size = { 400, 300 } }
      window:show()

   This creates the window that holds your layouts and, through them, all of
   your widgets.

   See :doc:`Window </widgets/window>`.

.. important::

   Widgets are put on screen by adding them to a layout with ``addChild``, and
   the layout is then given to the window with ``setLayout``. A widget that is
   never added to a layout is never shown.

   See :doc:`Layout Managers </layouts>`.

.. admonition:: Hey, heads up!

   If you have not read :doc:`Core concepts <concepts>` yet, start there. It
   covers chaining, 1-based indexing, and the error guard -- all of which apply
   to every widget on the pages below.

Common to every widget
------------------------

These are available on all the widgets in this section, so the individual pages
do not repeat them.

.. function:: show() / hide()
  :no-index:

   Shows or hides the widget.

.. function:: close()
  :no-index:

   Closes the widget.

.. function:: setSize(width, height)
  :no-index:

   Resizes the widget.

.. function:: setFixedSize(width, height)
  :no-index:

   Sets a size the widget cannot grow or shrink from.

.. function:: setLocation(x, y)
  :no-index:

   Moves the widget to a position.

.. function:: setResizeRule(horizontal, vertical)
  :no-index:

   How the widget behaves when its container is resized. Each argument is one
   of ``fixed``, ``expanding``, ``minimum``, ``maximum``, ``preferred``,
   ``minimumexpanding`` or ``ignore``.

.. function:: setEnabled(enabled) / isEnabled()
  :no-index:

   Whether the widget responds to input. A disabled widget is greyed out.

.. function:: setVisible(visible) / isVisible()
  :no-index:

   Whether the widget is shown.

.. function:: setToolTip(text) / getToolTip()
  :no-index:

   The small label that appears when the pointer rests on the widget.

.. function:: setStyleSheet(css) / getStyleSheet()
  :no-index:

   Styles the widget with Qt stylesheet syntax, which reads much like CSS.

   .. code-block:: lua

      button:setStyleSheet("background-color: #2d7; color: white; padding: 8px;")

.. function:: setBackgroundColor(colour)
  :no-index:

   A shortcut for setting just the background. Accepts a colour name, a hex
   string, or an ``{r, g, b}`` table.

.. function:: setFocus()
  :no-index:

   Gives the widget keyboard focus.

The widgets
-------------

.. toctree::
   :maxdepth: 2
   :titlesonly:

   widgets/window
   widgets/label
   widgets/button
   widgets/command-button
   widgets/check-box
   widgets/radio-button
   widgets/button-group
   widgets/line-edit
   widgets/text-field
   widgets/combo-box
   widgets/font-combo-box
   widgets/list-box
   widgets/table
   widgets/tree-view
   widgets/spinner
   widgets/double-spinner
   widgets/slider
   widgets/advanced-slider
   widgets/knob
   widgets/progress-bar
   widgets/lcd-number
   widgets/calendar
   widgets/date-picker
   widgets/time-picker
   widgets/image
   widgets/gif-player
   widgets/container
   widgets/group-box
   widgets/tab
   widgets/accordion
   widgets/splitter
   widgets/scroller
   widgets/sliding-stacked-widget
   widgets/dock
   widgets/modal
   widgets/menu
   widgets/drop-menu
   widgets/menu-bar
   widgets/tool-bar
   widgets/status-bar
   widgets/separator
   widgets/hline
   widgets/vline
   widgets/spacer
