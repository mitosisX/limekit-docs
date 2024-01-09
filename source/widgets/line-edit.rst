LineEdit
===========

An input field where users can enter and edit a single line of text. It's commonly used for gathering textual information from users, such as usernames, passwords, search queries, or any other type of short text input. 

.. code-block:: lua

  local input = LineEdit(text: optional)

Properties
***************

.. function:: setOnTextChange(callback)
  :noindex:

  The function executed text inside changes

.. function:: setOnReturnPress(callback)

  The function executed when ``Enter`` key has been pressed

.. function:: setOnTextSelection(callback)

  The function executed when text inside the widget get's selected

  :params: ``self`` and ``text``

.. function:: setInputMode(callback)

  Sets how text input is handled. Available options ``normal``, ``hideinput``, ``passwordonedit`` and ``password``

.. function:: setText(text)

  Sets text in the widget

.. function:: getText()

  Returns the text input

.. function:: setHint(text)

  Sets hint/placeholder text in the widget

.. function:: getSelectedText()

  Returns selected text

.. function:: checkTextSelected()

  Returns if widget has any text selected

.. function:: setReadOnly(enable: bool)

  Sets widget to read-only or allow input

.. function:: redo()

  Redo text input

.. function:: undo()

  Undo text input

.. function:: setMaxLength()

  Sets the maximum input length in the widget
  
.. function:: selectAll()

  Selects all text
  
.. function:: getStartSelection()

  Returns the start cursor position for selected text

.. function:: getEndSelection()

  Returns the end cursor position for selected text

.. function:: getSelectionLength()

  Returns count for text selected