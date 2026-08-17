Scroller
###########

Wraps content that is too big for the space available and adds scroll bars.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local longList = ui.VLayout()
  for i = 1, 100 do
      longList:addChild(ui.Label("Item " .. i))
  end

  local scroller = ui.Scroller()
  scroller:setResizable(true)
  scroller:setLayout(longList)

.. important::

  Set ``setResizable(true)`` in almost every case. Without it the content keeps
  its original size instead of fitting the width of the scroller, and you get a
  horizontal scroll bar you did not want.

Contents
***************

.. function:: setLayout(layout) / getLayout()
  :no-index:

  The layout to scroll.

.. function:: setChild(child) / getChild()
  :no-index:

  A single widget to scroll, instead of a layout.

.. function:: setResizable(resizable) / isResizable()
  :no-index:

  Whether the content resizes to fit the scroller's width.

Scroll bars
***************

.. function:: setVerticalScrollBarBehavior(behavior)
  :no-index:

  When the vertical bar appears.

.. function:: setHorizontalScrollBarBehavior(behavior)
  :no-index:

  When the horizontal bar appears.

.. function:: maxVerticalScroll() / minVerticalScroll()
  :no-index:

  The ends of the vertical scroll range.

.. function:: maxHorizontalScroll() / minHorizontalScroll()
  :no-index:

  The ends of the horizontal scroll range.

Events
***************

.. function:: setOnScroll(callback)
  :no-index:

  Runs as the user scrolls.

  .. code-block:: lua

     scroller:setOnScroll(function(sender, value)
         if value == sender:maxVerticalScroll() then
             loadMoreItems()
         end
     end)
