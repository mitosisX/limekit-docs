App object
==============

Is a collection of different functions (tools) that your program can use for various task. These tasks include reading files, gathering info about the computer's CPU, checking how much memory is available, choosing files and many more.

.. code-block:: lua

   -- an example of how to access various functions from the app object
   local processor = app.getProcessorName()

.. function:: isIDE()

   Returns whether the app is being run in :mod:`Limekit Runner` or as executable

.. function:: joinPaths(...)

   Joins multiple paths into one

.. function:: randomChoice(table)

   Randomly selects a string from a table

.. function:: getStandardPath(location)

   A set of standard locations on a user's system where different types of files or resources are commonly stored. These locations are predefined and provide a consistent way to access specific directories such as user's documents, desktop, applications, and more across different platform. Available arguments for :mod:`location` parameter include: ``desktop``, ``documents``, ``fonts``, ``applications``, ``music``, ``movies``, ``pictures``, ``temp``, ``home``, ``applocaldata``, ``cache``, ``genericdata``, ``runtime``, ``config``, ``download``, ``genericcache``, ``genericconfig``, ``appdata``, ``appconfig``, ``publicshare``, ``templates``

   .. code-block:: lua

      -- how to get the location for desktop
      local desktop = app.getStandardPath('desktop')

.. For some reason, I did not cover the sort Table or Array, quicksort, 
   
.. function:: splitString(string, delimeter)

   Split the string by the delimite

.. function:: intRange(from, to)

   Returns a table with a ranger of integers

.. function:: sleep(seconds)

   Sleep for some time. Use ``1, 2, 3, ...`` and not ``1000, 2000`` to represent time

.. function:: weightedGraph(data, startNode, endNode)

   Perfoms a weighted graph algorithm on data.

   .. code-block:: lua

      -- Based on the provided data, calculates shortest path from point a to point c
      local graph = app.weightedGraph({{'point a', 'point b', 20}, {'point a', 'point c', 10}, {'point b', 'point c', 50}}, 'point a', 'point c')

.. function:: getStyles()

   Returns platform-dependent UI styles that can be applies to the whole application.

.. function:: setStyle(style)

   Set the style to the whole application. Obtained from the above function

.. function:: makeHash(hashType, string)

   Generate a hash from the :mod:`string` based on the hash-type provided: Available hash types: ``md5``, ``sha1``, ``sha224``, ``sha256``, ``sha384``, ``sha512``, ``sha3_224``, ``sha3_256``, ``sha3_384``, ``sha3_512``

.. function:: hexToRGB(hex)

   Converts a hex to RGB values

.. function:: readFileLines(file)

   Reads the file lines for a particular file

.. function:: bytesToReadableSize(bytes)

   Converts bytes to readable size, ie, :mod:`2 kb, 10 GB`

.. function:: toBase64(string)

   Converts string to base64 encoding

.. function:: fromBase64(b64)

   Converts base64 string to readable string

.. function:: setFont(file, textSize)

   Sets the font and text size for the whole application

.. function:: extractZip(zip, destination)

   Extracts the content of a zip file to some destination

.. function:: checkIfFolder(path)

   Chcks if given path is a folder or not

.. function:: exists(path)

   Checks if given path is empty or not

.. function:: checkFolderEmpty()

   Checks if a given path is an exmpty dir or not

.. function:: getFileSize(file)

   Returns file size

.. function:: getFileExt(file)

   Returns only the file extension for a file path

.. function:: copyFile(source, destination)

   Copies a file from source to destination

.. function:: readFile(file)

   Reads a file and returns its content

.. function:: writeFile(file, content)

   Write content to a file

.. function:: appendFile(file, content)

   Does not overwrite, only appeands content to the file

.. function:: quite()

   Quits the application

.. function:: getCheck()
.. function:: getCheck()
.. function:: getCheck()
.. function:: getCheck()
.. function:: getCheck()
.. function:: getCheck()
.. function:: getCheck()
.. function:: getCheck()
.. function:: getCheck()
.. function:: getCheck()
