Image
###########

Displays a picture, and can respond to being clicked.

.. code-block:: lua

  local ui  = require("limekit.ui")
  local res = require("limekit.res")

  local logo = ui.Image(res.Resources.images("logo.png"))

Properties
***************

.. function:: setImage(path)
  :no-index:

  The picture to show.

.. function:: getImagePath()
  :no-index:

  The path of the picture currently shown.

.. function:: setImageSize(width, height)
  :no-index:

  Scales the picture.

  .. important::

     Call ``setImage`` first. Resizing an Image that has no picture yet raises
     an error explaining exactly that -- in 1.x it produced a confusing crash.

  .. note::

     1.x also had a ``resizeImage`` method. It was an identical copy of
     ``setImageSize`` and has been removed.

.. function:: setImageAlignment(alignment)
  :no-index:

  Where the picture sits within the widget. Takes the same names as
  :doc:`Label </widgets/label>` -- ``center``, ``left``, ``top`` and so on.

.. function:: setOnClick(callback)
  :no-index:

  Runs when the picture is clicked, which turns an image into a button.

  .. code-block:: lua

     logo:setOnClick(function()
         openWebsite()
     end)
