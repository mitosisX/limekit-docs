Image
=========

This widget allows developers to load and display images from files or resources, enabling users to view visual content as part of the application's design or functionality.

.. code-block:: lua

  local image = Image(path)

Properties
***************

.. function:: setOnClick(callback)

  Executed when the image is clicked.
  
.. function:: setImage(path)

  Sets the current image

.. function:: setImageAlign(align)

  Set how the image is aligned. Available options include ``left``, ``right``, ``bottom``, ``top``, ``center``, ``hcenter`` and ``vcenter``

.. function:: resizeImage(width, height)

  Resizes the images to the specified dimensions