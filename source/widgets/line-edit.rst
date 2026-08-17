LineEdit
###########

A single-line text box. Use it for names, search terms, passwords -- anything
that fits on one line. For longer text use a :doc:`TextField </widgets/text-field>`.

.. code-block:: lua

  local ui = require("limekit.ui")

  local name = ui.LineEdit()
  name:setHint("Your name")

Text
***************

.. function:: setText(text) / getText()
  :no-index:

  The contents of the box.

.. function:: setHint(text) / getHint()
  :no-index:

  Greyed-out text shown while the box is empty, describing what to type.

.. function:: setMaxLength(length) / getMaxLength()
  :no-index:

  The most characters the user may type.

.. function:: setReadOnly(readonly) / isReadOnly()
  :no-index:

  Lets the user read and select the text but not change it.

.. function:: clear()
  :no-index:

  Empties the box.

.. function:: undo() / redo()
  :no-index:

  Steps back and forward through the user's edits.

Input mode
***************

.. function:: setInputMode(mode) / getInputMode()
  :no-index:

  How the typed text is displayed. One of:

  .. list-table::
     :header-rows: 1
     :widths: 28 72

     * - Mode
       - Behaviour
     * - ``normal``
       - Shows the text as typed
     * - ``password``
       - Shows dots instead of characters
     * - ``passwordonedit``
       - Shows each character briefly, then hides it
     * - ``hideinput``
       - Shows nothing at all

  .. code-block:: lua

     local password = ui.LineEdit()
     password:setInputMode("password")

Selection
***************

.. function:: selectAll()
  :no-index:

  Selects everything in the box.

.. function:: getSelectedText()
  :no-index:

  The currently selected text.

.. function:: checkTextSelected()
  :no-index:

  Whether anything is selected.

.. function:: getStartSelection() / getEndSelection()
  :no-index:

  Where the selection begins and ends.

.. function:: getSelectionLength()
  :no-index:

  How many characters are selected.

Events
***************

.. function:: setOnTextChange(callback)
  :no-index:

  Runs on every keystroke.

  .. code-block:: lua

     local search = ui.LineEdit()
     search:setOnTextChange(function(sender)
         filterResults(sender:getText())
     end)

.. function:: setOnReturnPress(callback)
  :no-index:

  Runs when the user presses Enter -- the usual way to submit a single field.

.. function:: setOnTextSelection(callback)
  :no-index:

  Runs when the selection changes.

Autocomplete
***************

.. function:: setAutoComplete(completer)
  :no-index:

  Attaches an :doc:`AutoComplete </batteries>` suggestion list.

  .. code-block:: lua

     local completer = ui.AutoComplete({ "apple", "apricot", "avocado" })

     local fruit = ui.LineEdit()
     fruit:setAutoComplete(completer)

Appearance
***************

.. function:: setCursor(cursor)
  :no-index:

  The mouse cursor shown over the box. See :doc:`Label </widgets/label>` for the
  list of names.
