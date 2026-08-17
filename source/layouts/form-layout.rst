FormLayout
#############

Rows of labelled fields, with the labels lined up down one side and the inputs
down the other. It is the quickest way to build a settings or details form
without doing the alignment yourself.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local form = ui.FormLayout()
  form:addChild("Name", ui.LineEdit())
  form:addChild("Email", ui.LineEdit())
  form:addChild("Age", ui.Spinner())

Properties
***************

.. function:: addChild(title, child)
  :no-index:

  Adds a labelled row.

  Called with only one argument, it adds a widget spanning the full width with
  no label -- useful for a submit button or a note at the end of the form:

  .. code-block:: lua

     form:addChild("Password", ui.LineEdit())
     form:addChild(ui.Button("Sign in"))     -- spans both columns

.. function:: addLayout(title, layout)
  :no-index:

  Adds a labelled row whose value side is a whole layout, for when one field
  needs several widgets.

  .. code-block:: lua

     local nameRow = ui.HLayout()
     nameRow:addChild(ui.LineEdit())
     nameRow:addChild(ui.LineEdit())

     form:addLayout("Full name", nameRow)

.. function:: getRowAt(index)
  :no-index:

  The row at a position. **Rows start at 1.**

  .. note::

     1.x had a ``getAt`` method here that *removed* the row it claimed to be
     reading. ``getRowAt`` reads without changing anything.

.. seealso::

  :doc:`Layout Managers </layouts>` for the methods every layout shares.
