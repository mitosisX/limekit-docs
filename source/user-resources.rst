Accessing Resources
====================

There are three folders for app resources: :mod:`images`, :mod:`script`, and :mod:`misc`. To access resources from each folder, functions with names matching the folders are used.

Use the function ``image(path)`` to access images. Apply this same concept to access resources in the other folders.

.. code-block:: lua

  local button = Button('Next')
  button:setIcon(images('next_icon.png'))

  -- accessing a subfolder

  local button = Button('Next')
  button:setIcon(images('folder1/folder2/folder3/next_icon.png'))