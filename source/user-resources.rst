Accessing Resources
====================

There are three folders for app resources: :mod:`images`, :mod:`script`, and :mod:`misc`. To access resources from each folder, functions with names matching the folders are used.

.. note::

  The :mod:`misc` folder contains miscellaneous content, from lua modules, to audio, to csv files.

  It is automatically added to :mod:`package.path`

.. important::

  Put your own ``scripts`` and ``images`` in the :mod:`scripts` and :mod:`images` folders, respectively, and store third-party lua modules in the :mod:`misc` folder and not in the :mod:`scripts` folder.

Use the function ``image(path)`` to access images. Apply this same concept to access resources in the other folders.

.. code-block:: lua

  local button = Button('Next')
  button:setIcon(images('next_icon.png')) -- this points to the icon inside the images folder

  -- accessing subfolders

  local button = Button('Play')
  button:setIcon(images('folder1/folder2/folder3/play.png'))

.. note::

  Do not use use ``../`` or ``./`` to access folders.


