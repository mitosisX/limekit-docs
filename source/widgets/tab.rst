Tab
###########

A set of pages with a row of tabs along one edge. Each page is a widget --
usually a :doc:`TabItem </widget-items/tab-item>` or a
:doc:`Container </widgets/container>` holding a layout.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local tabs = ui.Tab()

  local general = ui.TabItem()
  local generalLayout = ui.VLayout()
  generalLayout:addChild(ui.Label("General settings"))
  general:setLayout(generalLayout)

  tabs:addTab(general, "General")

.. important::

  **Tab positions start at 1.** The first tab is ``1``, not ``0``.

Pages
***************

.. function:: addTab(child, title, icon)
  :no-index:

  Adds a page. ``icon`` is optional.

  .. code-block:: lua

     local res = require("limekit.res")
     tabs:addTab(general, "General", res.Resources.images("gear.png"))

.. function:: removeTab(index)
  :no-index:

  Removes the page at a position.

.. function:: getChildAt(index)
  :no-index:

  The widget on the page at a position.

.. function:: getIndexOf(child)
  :no-index:

  Which position a given widget is on.

.. function:: getCount()
  :no-index:

  How many pages there are.

Selection
***************

.. function:: setCurrentIndex(index) / getCurrentIndex()
  :no-index:

  The page currently shown.

.. function:: setCurrentChild(child)
  :no-index:

  Shows the page holding a particular widget.

Appearance
***************

.. function:: setTabText(index, text) / getTabText(index)
  :no-index:

  The label on a tab.

.. function:: setTabIcon(index, icon)
  :no-index:

  The icon on a tab.

.. function:: setTabToolTip(index, tip)
  :no-index:

  The tooltip for a tab.

.. function:: setTabEnabled(index, enabled)
  :no-index:

  Whether a tab can be selected.

.. function:: setTabVisible(index, visible)
  :no-index:

  Whether a tab is shown at all.

.. function:: setMovable(movable) / isMovable()
  :no-index:

  Lets the user drag tabs into a different order.

.. function:: setTabsClosable(closable) / isTabsClosable()
  :no-index:

  Puts a close button on each tab. Pair it with ``setOnTabClose``.

.. function:: setTabPosition(position) / getTabPosition()
  :no-index:

  Which edge the tabs sit on.

.. function:: setCornerChild(child)
  :no-index:

  Puts a widget in the corner beside the tabs -- often a small "add" button.

Events
***************

.. function:: setOnTabChange(callback)
  :no-index:

  Runs when a different page is selected.

.. function:: setOnTabClose(callback)
  :no-index:

  Runs when a tab's close button is clicked.

  .. code-block:: lua

     tabs:setTabsClosable(true)
     tabs:setOnTabClose(function(sender, index)
         sender:removeTab(index)
     end)

  .. note::

     Clicking the close button does not remove the page by itself -- that is up
     to your handler, so you can ask the user to save first.
