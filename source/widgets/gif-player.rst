GifPlayer
############

Plays an animated GIF. Useful for loading indicators and small animations.

.. code-block:: lua

  local ui  = require("limekit.ui")
  local res = require("limekit.res")

  local spinner = ui.GifPlayer(res.Resources.images("loading.gif"))
  spinner:start()

Playback
***************

.. function:: ui.GifPlayer(filename)
  :no-index:

  Creates a player for a GIF file.

.. function:: start()
  :no-index:

  Begins playing.

.. function:: stop()
  :no-index:

  Stops playing and returns to the first frame.

.. function:: pause()
  :no-index:

  Freezes on the current frame.

.. function:: nextFrame()
  :no-index:

  Steps forward one frame.

.. function:: jumpToFrame(frame)
  :no-index:

  Jumps to a particular frame.

.. function:: setSpeed(speed) / getSpeed()
  :no-index:

  Playback speed as a percentage. ``100`` is normal, ``200`` is twice as fast.

Information
***************

.. function:: getCurrentFrame()
  :no-index:

  Which frame is showing.

.. function:: getFramesCount()
  :no-index:

  How many frames the animation has.

.. function:: getState()
  :no-index:

  Whether the animation is running, paused or stopped.
