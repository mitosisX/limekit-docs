Services
==========

.. contents:: Content
    :depth: 2
    :local:
    :backlinks: top

Services are the parts of Limekit that are not widgets: your project's own
files, the filesystem, the machine you are running on, dialogs, and themes.

In 1.x these were all bundled into a single global ``app`` table. In 2.0 they
are grouped by what they do, and every one of their methods is **static** --
you call it on the class itself with a dot, and you never construct anything:

.. code-block:: lua

   local fs = require("limekit.fs")

   local text = fs.FileSystem.readFile("notes.txt")   -- dot, not colon

Project resources
-------------------

``res.Resources`` resolves paths inside your own project. There are three
folders -- ``images``, ``scripts`` and ``misc`` -- and one function per folder.

.. code-block:: lua

   local res = require("limekit.res")
   local ui  = require("limekit.ui")

   local button = ui.Button("Next")
   button:setIcon(res.Resources.images("next_icon.png"))

   -- subfolders work the same way
   button:setIcon(res.Resources.images("icons/arrows/next.png"))

.. note::

   The :mod:`misc` folder is for everything that is not an image or one of your
   own scripts: audio, CSV files, third-party lua modules. Both ``scripts`` and
   ``misc`` are added to ``package.path`` automatically, so anything in them is
   requirable.

.. important::

   Do not use ``../`` or ``./`` in a resource name. These functions resolve
   against your project folder, which is what makes them work identically in
   development and inside a built executable.

.. function:: res.Resources.images(name)
  :no-index:

   The full path to a file in your project's ``images`` folder.

.. function:: res.Resources.scripts(name)
  :no-index:

   The full path to a file in your project's ``scripts`` folder.

.. function:: res.Resources.misc(name)
  :no-index:

   The full path to a file in your project's ``misc`` folder.

.. function:: res.Resources.route(key)
  :no-index:

   Resolves a named route declared in ``app.json``, so a path used in many
   places is written down once.

   .. code-block:: json

      {
        "project": {
          "routes": {
            "single": {
              "logo": "images::brand/logo.png"
            },
            "group": {
              "icons": {
                "group_label": "images",
                "save": "icons/save.png",
                "open": "icons/open.png"
              }
            }
          }
        }
      }

   .. code-block:: lua

      res.Resources.route("logo")          -- a single route
      res.Resources.route("icons::save")   -- an item inside a group

   A ``single`` route's value carries its own ``marker::resource`` prefix. In a
   group, declaring ``group_label`` once lets every item in that group drop the
   prefix.

The filesystem
----------------

``fs.FileSystem`` reads and writes files, folders and JSON. Every failure --
a missing file, a permissions problem, malformed JSON -- is reported as a
Limekit error naming what went wrong, rather than a raw Python traceback.

.. code-block:: lua

   local fs = require("limekit.fs")

   if fs.FileSystem.exists("settings.json") then
       local settings = fs.FileSystem.readJSON("settings.json")
       print(settings.theme)
   end

Files
~~~~~~

.. function:: fs.FileSystem.readFile(path, encoding)
  :no-index:

   Returns the whole file as a string. ``encoding`` defaults to ``utf-8``.

.. function:: fs.FileSystem.readFileLines(path, encoding)
  :no-index:

   Returns a table of lines.

.. function:: fs.FileSystem.writeFile(path, content, encoding)
  :no-index:

   Writes ``content``, replacing whatever was there.

.. function:: fs.FileSystem.appendFile(path, content, encoding)
  :no-index:

   Adds ``content`` to the end of the file.

.. function:: fs.FileSystem.createFile(path)
  :no-index:

   Creates an empty file.

.. function:: fs.FileSystem.deleteFile(path)
  :no-index:

   Deletes a file.

.. function:: fs.FileSystem.copyFile(source, destination)
  :no-index:

   Copies a file.

.. function:: fs.FileSystem.renameFile(path, new_path)
  :no-index:

   Renames or moves a file.

.. function:: fs.FileSystem.getFileSize(path)
  :no-index:

   Size in bytes. Pair it with ``sys.System.bytesToReadableSize``.

.. function:: fs.FileSystem.isFileEmpty(path)
  :no-index:

   Whether the file has no content.

JSON
~~~~~

.. function:: fs.FileSystem.readJSON(path)
  :no-index:

   Reads a JSON file and returns it as a lua table.

.. function:: fs.FileSystem.writeJSON(path, data, indent)
  :no-index:

   Writes a lua table as JSON. ``indent`` defaults to 4.

.. function:: fs.FileSystem.formatJSON(text, indent)
  :no-index:

   Pretty-prints a JSON string without touching a file.

Folders and paths
~~~~~~~~~~~~~~~~~~~

.. function:: fs.FileSystem.exists(path)
  :no-index:

   Whether a file or folder exists.

.. function:: fs.FileSystem.isFolder(path)
  :no-index:

   Whether the path is a folder.

.. function:: fs.FileSystem.createFolder(path)
  :no-index:

   Creates a folder, including any missing parents.

.. function:: fs.FileSystem.listFolder(path)
  :no-index:

   A table of the names directly inside a folder.

.. function:: fs.FileSystem.walkDir(path, show_hidden)
  :no-index:

   One level of a folder, folders first. Each entry is a table with ``name``,
   ``path`` and ``is_dir`` -- which is what a file tree needs to draw a row and
   decide whether it can be expanded. ``show_hidden`` defaults to ``false``.

   Despite the name it does not recurse; call it again on any entry whose
   ``is_dir`` is true.

   .. code-block:: lua

      for _, entry in ipairs(fs.FileSystem.walkDir(folder)) do
          print(entry.name, entry.is_dir and "folder" or "file")
      end

.. function:: fs.FileSystem.joinPaths(...)
  :no-index:

   Joins path segments using the right separator for the platform.

.. function:: fs.FileSystem.normalPath(path)
  :no-index:

   Normalises a path.

.. function:: fs.FileSystem.getFileName(path)
  :no-index:

   The filename portion of a path.

.. function:: fs.FileSystem.getFileExt(path)
  :no-index:

   The file extension.

.. function:: fs.FileSystem.getDirName(path)
  :no-index:

   The folder containing the path.

The system
------------

``sys.System`` describes and interacts with the machine your app is running on.

.. code-block:: lua

   local sys = require("limekit.sys")

   print(sys.System.getOSName())
   print(sys.System.getProcessorName())
   print(sys.System.getCPUCount())

Machine information
~~~~~~~~~~~~~~~~~~~~~

.. function:: sys.System.getOSName()
  :no-index:

   The operating system name.

.. function:: sys.System.getOSVersion()
  :no-index:

   The operating system version.

.. function:: sys.System.getPlatformName()
  :no-index:

   The platform identifier.

.. function:: sys.System.getProcessorName()
  :no-index:

   The CPU model name.

.. function:: sys.System.getCPUCount()
  :no-index:

   How many CPU cores are available.

.. function:: sys.System.getStandardPath(name)
  :no-index:

   A well-known folder on the user's machine. Accepts names like ``desktop``,
   ``documents``, ``downloads``, ``music``, ``pictures``, ``movies``, ``home``,
   ``temp``, ``fonts``, ``applications``, ``cache``, ``appdata``, ``config``.

   .. code-block:: lua

      local desktop = sys.System.getStandardPath("desktop")

Clipboard
~~~~~~~~~~

.. function:: sys.System.getClipboardText()
  :no-index:

   The text currently on the clipboard.

.. function:: sys.System.setClipboardText(text)
  :no-index:

   Puts text on the clipboard.

Text and encoding
~~~~~~~~~~~~~~~~~~~

.. function:: sys.System.splitString(text, sep)
  :no-index:

   Splits a string into a table. ``sep`` defaults to a space.

.. function:: sys.System.randomChoice(items)
  :no-index:

   Picks one item from a table at random.

.. function:: sys.System.bytesToReadableSize(size)
  :no-index:

   Turns a byte count into something like ``"1.4 MB"``.

.. function:: sys.System.makeHash(kind, text)
  :no-index:

   Hashes a string. ``kind`` is one of ``md5``, ``sha1``, ``sha224``,
   ``sha256``, ``sha384``, ``sha512``.

.. function:: sys.System.toBase64(text)
  :no-index:

   Encodes a string as base64.

.. function:: sys.System.fromBase64(text)
  :no-index:

   Decodes a base64 string.

.. function:: sys.System.emoji(name)
  :no-index:

   Looks up an emoji by name, e.g. ``sys.System.emoji("thumbs_up")``.

Process control
~~~~~~~~~~~~~~~~~

.. function:: sys.System.sleep(seconds)
  :no-index:

   Pauses for a number of seconds.

   .. important::

      This blocks the interface. For anything longer than an instant, use a
      :doc:`Thread or Timer <batteries>` instead.

.. function:: sys.System.execute(cmd)
  :no-index:

   Runs an external command and returns its output.

   .. note::

      Commands are given 30 seconds to finish. Past that, Limekit raises an
      error rather than leaving your app frozen forever.

.. function:: sys.System.exit(code)
  :no-index:

   Quits the application. ``code`` defaults to 0.

Arithmetic
~~~~~~~~~~~~

.. function:: sys.Expr.evalExpression(expression)
  :no-index:

   Evaluates an arithmetic expression given as a string. Useful for calculators
   and anywhere the user types a sum.

   .. code-block:: lua

      sys.Expr.evalExpression("2 + 3 * 4")   -- 14

   Numbers and the operators ``+ - * / // % **`` only. Anything else -- a
   function call, a variable, a string -- is rejected. It cannot reach Python,
   and it refuses calculations large enough to hang your app.

Dialogs
---------

``ui.Dialogs`` covers the standard message, input and file dialogs. Every one
takes the parent window as its first argument, and every one returns ``nil``
when the user cancels.

.. code-block:: lua

   local ui = require("limekit.ui")

   local name = ui.Dialogs.textInput(window, "Welcome", "What's your name?")
   if name then
       ui.Dialogs.info(window, "Hello", "Nice to meet you, " .. name)
   end

Messages
~~~~~~~~~

.. function:: ui.Dialogs.info(parent, title, message)
  :no-index:

   An information message.

.. function:: ui.Dialogs.warning(parent, title, message)
  :no-index:

   A warning message.

.. function:: ui.Dialogs.critical(parent, title, message)
  :no-index:

   An error message.

.. function:: ui.Dialogs.alert(parent, title, message)
  :no-index:

   A plain message with no icon.

.. function:: ui.Dialogs.question(parent, title, message)
  :no-index:

   Asks a yes/no question and returns a boolean.

   .. code-block:: lua

      if ui.Dialogs.question(window, "Quit", "Save before closing?") then
          saveEverything()
      end

Input
~~~~~~

.. function:: ui.Dialogs.textInput(parent, title, label, text)
  :no-index:

   Asks for a single line of text.

.. function:: ui.Dialogs.multilineInput(parent, title, label, text)
  :no-index:

   Asks for several lines of text.

.. function:: ui.Dialogs.integerInput(parent, title, label, value, min_value, max_value, step)
  :no-index:

   Asks for a whole number.

.. function:: ui.Dialogs.doubleInput(parent, title, label, value, min_value, max_value, decimals)
  :no-index:

   Asks for a decimal number.

.. function:: ui.Dialogs.comboBoxInput(parent, title, label, items, index)
  :no-index:

   Asks the user to pick from a list. ``index`` is the 1-based item selected
   when the dialog opens.

Files, colours and fonts
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: ui.Dialogs.openFile(parent, title, directory, filters)
  :no-index:

   Asks the user to choose a file to open, and returns its path.

   ``filters`` is a table mapping a description to its extensions:

   .. code-block:: lua

      local path = ui.Dialogs.openFile(window, "Open image", "", {
          Images = { "png", "jpg", "jpeg" },
          ["All files"] = { "*" },
      })

.. function:: ui.Dialogs.saveFile(parent, title, directory, filters)
  :no-index:

   Asks where to save a file, and returns the chosen path.

.. function:: ui.Dialogs.pickFolder(parent, title, directory)
  :no-index:

   Asks the user to choose a folder.

.. function:: ui.Dialogs.pickColour(parent, initial)
  :no-index:

   Opens the colour picker.

.. function:: ui.Dialogs.pickFont(parent)
  :no-index:

   Opens the font picker.

Themes and styles
-------------------

``ui.Theme`` restyles the whole application in one call. Themes are grouped
into five families.

.. code-block:: lua

   local ui = require("limekit.ui")

   ui.Theme.setTheme("material", "dark_teal")

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Family
     - What it is
   * - ``material``
     - Google Material Design themes
   * - ``misc``
     - The stylesheet themes bundled with Limekit
   * - ``darklight``
     - Simple dark and light modes
   * - ``darkstyle``
     - The QDarkStyle theme
   * - ``qtthemes``
     - Bundled colour palettes

.. function:: ui.Theme.setTheme(family, name)
  :no-index:

   Applies a theme. Both arguments are case-insensitive.

.. function:: ui.Theme.getThemes(family)
  :no-index:

   A table of every theme name available in that family -- use it to build a
   theme picker.

   .. code-block:: lua

      for _, name in ipairs(ui.Theme.getThemes("material")) do
          print(name)
      end

.. function:: ui.Theme.setStyle(name)
  :no-index:

   Applies a platform widget style rather than a theme.

.. function:: ui.Theme.getStyles()
  :no-index:

   A table of the styles this platform offers.

.. important::

   The ``material``, ``darklight`` and ``darkstyle`` families come from optional
   Python packages. If one is not installed, Limekit raises an error naming the
   package you need. In 1.x the call quietly did nothing at all.
