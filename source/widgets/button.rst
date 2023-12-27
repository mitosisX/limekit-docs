Button
###########

The button, one of the mostly used widget in any Graphical User Interface (GUI). Click on it and a computer will do some task for you.

.. code-block:: lua

  local button = Button(text)

This is done by calling a callback function after calling on a button. You can specify such a callback function with the ``setOnClick`` method

.. code-block:: lua
  :linenos:

  button:setOnClick(function(sender)
    -- some task here
  end)

Methods
***************

.. function:: setOnClick(callback)

  The function executed when the button is clicked

.. function:: setIcon(path)

  Sets an icon on the button
checkout * :doc:`Using resources </widgets/accordion>`

.. function:: setIconSize(width, height)
  
  Resizes the icon set in the button

.. function:: setText(text)
  
  Sets text on the button

.. function:: getText()

  Returns text on the button


.. function:: setFlat()

  Makes the button appear flat

.. function:: setCheckable(checkable: bool)

  Set whether or not the button can be checked/toggled

.. function:: isChecked()

  Return the check/toggle status of the button

.. function:: setMargins(left, top,right,bottom)

  Sets the margins of the button

