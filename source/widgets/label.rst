Label
=========

A widget primarily used for showing text in a user interface. These widgets are often used to provide descriptions, titles, or informative messages within an application. They help in presenting static content that users can read or refer to as part of the interface design.

.. code-block:: lua

  local label = Label(text)

Properties
***************

.. function:: setOnClick(callback)

  Executed when the widget is clicked.

.. function:: setText(text)
  :noindex:

  Sets text on the label

.. function:: getText()
  :noindex:

  Returns the text displayed on the widget
  
.. function:: setTextAlign(align)

  Set how the text is aligned. Available options include ``left``, ``right``, ``bottom``, ``top``, ``center``, ``hcenter`` and ``vcenter``

.. function:: setWordWrap(enable: bool)

  Enable or disable word wrap

.. function:: setBold(enable: bool)

  Enable or disable bold text

.. function:: setTextSize(size)

  Sets text size

.. function:: setCompanion(widget)

  When the user hits the specific shortcut key shown on the label, the keyboard focus moves to the widget linked with that label.

  The companion system works exclusively for ``Labels`` that have text where a single character has an ``'&'`` symbol before it. This '&' character is assigned as the shortcut key.

