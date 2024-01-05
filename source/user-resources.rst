Accessing Resources
====================

There are three folders for app resources: :mod:`images`, :mod:`script`, and :mod:`misc`. To access resources from each folder, functions with names matching the folders are used.

.. note::

  The :mod:`misc` folder contains miscellaneous content, from lua modules, to audio, to csv files.

.. important::

  Put your own ``scripts`` and ``images`` in the :mod:`scripts` and :mod:`images` folders, respectively, and store third-party lua modules in the :mod:`misc` folder and not in the :mod:`scripts` folder.

Use the function ``image(path)`` to access images. Apply this same concept to access resources in the other folders.

.. code-block:: lua

  local button = Button('Next')
  button:setIcon(images('next_icon.png'))

  -- accessing subfolders

  local button = Button('Next')
  button:setIcon(images('folder1/folder2/folder3/next_icon.png'))

.. note::

  Do not use use ``../`` or ``./`` to access folders, type in the full path.


