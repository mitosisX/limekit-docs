CommandButton
===============

A button that combines a label and a command. It's designed to present descriptive text alongside an actionable command or link. This type of button is useful for displaying informative text or explanations along with a clickable action, providing more context to users about the function the button performs.

.. code-block:: lua

  local date = CommandButton(text)

Properties
***************

.. function:: setOnClick(callback)
  :noindex:

  The function executed when the button is clicked

.. function:: setText(text)
  
  Sets text on the button

.. function:: getText()

  Returns text on the button

.. function:: setDescription()

  Sets the a description. This appears as text beneath the primary text

.. function:: getDescription()

  Returns the provided description