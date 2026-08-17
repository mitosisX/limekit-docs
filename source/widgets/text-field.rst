TextField
###########

A multi-line text box, for notes, descriptions, logs and anything else too long
for a :doc:`LineEdit </widgets/line-edit>`.

.. code-block:: lua

  local ui = require("limekit.ui")

  local notes = ui.TextField()
  notes:setHint("Write something...")

Text
***************

.. function:: setText(text) / getText()
  :no-index:

  The contents of the field.

.. function:: setPlainText(text) / getPlainText()
  :no-index:

  The contents as plain text, with any formatting stripped.

  .. note::

     ``setText`` inspects what you give it and may interpret HTML-looking
     content as formatting. ``setPlainText`` never does -- reach for it when the
     text comes from a file or from the user and should be shown exactly as-is.

.. function:: setHtml(html) / getHtml()
  :no-index:

  The contents as HTML, for when you want bold, colours or links.

.. function:: setHint(text) / getHint()
  :no-index:

  Greyed-out text shown while the field is empty.

.. function:: setReadOnly(readonly) / isReadOnly()
  :no-index:

  Lets the user read and select but not edit.

.. function:: appendText(text)
  :no-index:

  Adds text to the end without disturbing what is already there. This is what
  you want for a log or console view.

.. function:: clear()
  :no-index:

  Empties the field.

.. function:: getLineCount()
  :no-index:

  How many lines the field currently holds.

.. function:: scrollToEnd()
  :no-index:

  Scrolls to the bottom -- pair it with ``appendText`` to follow a growing log.

  .. code-block:: lua

     local function log(message)
         notes:appendText(message .. "\n")
         notes:scrollToEnd()
     end

Appearance
***************

.. function:: setTextAlignment(alignment)
  :no-index:

  Where text sits in the field. Takes the same names as
  :doc:`Label </widgets/label>`.

.. function:: setTextColor(colour)
  :no-index:

  The text colour. Accepts a name, a hex string, or an ``{r, g, b}`` table.

.. function:: setTextSize(size)
  :no-index:

  The font size in points.

.. function:: setWrapMode(mode)
  :no-index:

  How long lines wrap.

Events
***************

.. function:: setOnTextChange(callback)
  :no-index:

  Runs whenever the text changes.

.. function:: setOnCursorMove(callback)
  :no-index:

  Runs when the cursor moves to a different position.
