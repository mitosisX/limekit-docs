GifPlayer
===========

A widget that allows you to view and play GIF (Graphics Interchange Format) files. It displays the animated or sequence of images contained within a GIF file, enabling you to watch the animation, which could be anything from a short loop to a longer sequence of frames. Typically, a GIF player provides controls to start, pause, stop, or navigate through the frames of the GIF, giving users control over the playback of the animation.

.. code-block:: lua

  local gif = GifPlayer(path)

*- GIF's play automatically.*

.. note::

  There's an issue with how GIFs are displayed in the Qt framework we're using. The output always ends up pixelated and in poor quality. Until the Qt developer addresses this problem, there's nothing we can do from our end.

Properties
***************

.. function:: start()

  Starts playing the GIF

.. function:: stop()
  
  Stops playing the GIF

.. function:: pause()
  
  Pause the GIF animation loop

.. function:: nextFrame()
  
  Jumps to the next frame
  
.. function:: getCurrentFrame()
  
  Gets the current frame

.. function:: justToFrame()
  
  Navigates to a specified frame

.. function:: getState()
  
  Get state of the animation: running, ``notrunning``, ``paused`` and ``running``