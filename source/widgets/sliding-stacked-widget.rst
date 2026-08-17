SlidingStackedWidget
#######################

A stack of pages that slide from one to the next instead of simply appearing.
Good for onboarding flows, wizards, and image carousels.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local slides = ui.SlidingStackedWidget()
  slides:addChild(welcomePanel)
  slides:addChild(detailsPanel)
  slides:addChild(finishPanel)

  slides:setAnimation("OutCubic")
  slides:setSpeed(400)

  nextButton:setOnClick(function()
      slides:slideNext()
  end)

Pages
***************

.. function:: addChild(child)
  :no-index:

  Adds a widget as a page.

.. function:: addLayout(layout)
  :no-index:

  Adds a whole layout as a page.

.. function:: getCount()
  :no-index:

  How many pages there are.

.. function:: setCurrentIndex(index) / getCurrentIndex()
  :no-index:

  The page shown. **Positions start at 1.**

.. function:: setCurrentWidget(widget)
  :no-index:

  Shows a particular page.

Moving between pages
***********************

.. function:: slideNext()
  :no-index:

  Slides to the next page.

.. function:: slidePrev()
  :no-index:

  Slides to the previous page.

.. function:: slideInIdx(index, direction)
  :no-index:

  Slides to a page by position.

.. function:: slideInWgt(widget, direction)
  :no-index:

  Slides to a particular page.

Animation
***************

.. function:: setAnimation(animation)
  :no-index:

  The easing curve used, such as ``OutCubic``, ``InOutQuad`` or ``Linear``.

  .. note::

     An unrecognised name now raises an error listing what is valid. In 1.x a
     typo here silently did nothing.

.. function:: getAnimations()
  :no-index:

  A table of every animation name you can use.

.. function:: setSpeed(speed)
  :no-index:

  How long the slide takes, in milliseconds. Defaults to 500.

.. function:: setEasing(easing)
  :no-index:

  Sets the easing curve directly.

.. function:: setOrientation(orientation)
  :no-index:

  Whether pages slide ``horizontal`` or ``vertical``.

Automatic playback
*********************

.. function:: autoStart(msec)
  :no-index:

  Advances through the pages on its own, waiting ``msec`` between each.
  Defaults to 3000. This is how you build a carousel.

.. function:: autoStop()
  :no-index:

  Stops automatic playback.
