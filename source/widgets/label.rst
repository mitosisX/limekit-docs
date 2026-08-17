Label
###########

Displays text or an image. Labels are not interactive -- they are how your app
talks to the person using it.

.. code-block:: lua

  local ui = require("limekit.ui")

  local label = ui.Label("Total: 0")

.. note::

  ``setText`` accepts numbers as well as strings, so there is no need to call
  ``tostring()`` first:

  .. code-block:: lua

     label:setText(42)

Properties
***************

.. function:: setText(text) / getText()
  :no-index:

  The text shown.

.. function:: setTextAlignment(alignment)
  :no-index:

  Where the text sits within the label. One of ``left``, ``right``, ``center``,
  ``top``, ``bottom``, ``hcenter``, ``vcenter``, ``justify``, ``baseline``,
  ``leading`` or ``trailing``.

  .. code-block:: lua

     label:setTextAlignment("center")

.. function:: setWordWrap(wrap) / isWordWrap()
  :no-index:

  Whether long text wraps onto more lines instead of running off the edge.

.. function:: setImage(path)
  :no-index:

  Shows an image instead of text.

  .. code-block:: lua

     local res = require("limekit.res")
     label:setImage(res.Resources.images("logo.png"))

.. function:: getImagePath()
  :no-index:

  The path of the image currently shown.

.. function:: setCursor(cursor)
  :no-index:

  The mouse cursor shown over the label. One of ``arrow``, ``uparrow``,
  ``wait``, ``busy``, ``cross``, ``ibeam``, ``sizever``, ``sizehor``,
  ``sizeall``, ``blank``, ``splitv``, ``splith``, ``pointinghand``,
  ``forbidden``, ``whatsthis``, ``openhand``, ``closedhand``, ``dragcopy``,
  ``dragmove``, ``draglink``.

Styling
***************

Labels take stylesheets like any other widget, which is the usual way to change
their size and colour:

.. code-block:: lua

  local heading = ui.Label("Welcome")
  heading:setTextAlignment("center")
  heading:setStyleSheet("font-size: 28px; font-weight: bold; color: #333;")
