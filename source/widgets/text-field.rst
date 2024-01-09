TextField
===========

An input field where users can enter and edit a single line of text. It's commonly used for gathering textual information from users, such as usernames, passwords, search queries, or any other type of short text input. 

.. code-block:: lua

  local input = TextField(text: optional)

.. note::

  The next release will include a lot of text formating features

Properties
***************

.. function:: setOnTextChange(callback)

  The function executed text inside changes

  :params: ``self`` and ``text``

.. function:: setText(text)

  Sets text in the widget

.. function:: getText()

  Returns the text input

.. function:: setHint(text)

  Sets hint/placeholder text in the widget

.. function:: selectAll()

  Seleects all text

.. function:: setReadOnly(enable: bool)

  Sets widget to read-only or allow input

.. function:: redo()

  Redo text input

.. function:: undo()

  Undo text input

.. function:: setMaxLength()

  Sets the maximum input length in the widget
  
.. function:: appendText(text)

  Appends text to the widget