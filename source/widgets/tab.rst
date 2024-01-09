Tab
===========

A container widget that organizes multiple pages or panels of content into separate tabs, allowing users to switch between different sections within a single window.

.. code-block:: lua

  local tab = Tab()

.. admonition:: Hey!

  Check out :doc:`TabItem </widget-items/tab-item>` for more

Properties
***************

.. function:: setOnTabClose(callback)

  Executed when the tab is being closed

.. function:: addTab(tabitem, title, icon: optional):

  Adds a :mod:`TabItem` to the widget

.. function:: setTabsCloseable(closeable: bool)

  Sets whether tabs can be closed

.. function:: setTabsPosition(position)

  Sets the side where the tabs appear: ``left``, ``top``, ``right``, ``bottom``

.. function:: setToolTip(index, text)

  Sets tooltip text to a particular tab index

.. function:: getCurrentIndex()

  Returns the current tab index

.. function:: removeTab(index)

  Removes a tab on a specified index

