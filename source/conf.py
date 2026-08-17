# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "limekit docs"
copyright = "2026, Take bytes"
author = "Omega Msiska"
release = "2.0"

version = "2.0"
contact = "omegamsiskah@gmail.com"

# Counts used across the docs. Keep these in step with the registry -- run
# `python -m limekit` against any project and the module tables it installs
# are the source of truth.
rst_epilog = """
.. |widgets| replace:: 49
.. |classes| replace:: 80
"""

# pygment_style = "sphinx"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = []

# Lua is not one of Sphinx's default highlight languages for `::` blocks, so
# set it explicitly -- nearly every code block in these docs is Lua.
highlight_language = "lua"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Widens the content column past the theme's 800px default, plus some
# readability tweaks. See _static/custom.css.
html_css_files = ["custom.css"]

html_theme_options = {
    # NOTE: sphinx_rtd_theme 3.x removed "display_version"; the version is
    # rendered from `release` by the theme itself. Do not re-add it -- it is
    # rejected as an unsupported option and fails the -W build.
    "navigation_depth": 3,
    "collapse_navigation": False,
    "sticky_navigation": True,
}

# numfig = False

# Disable numbered bullet points in HTML output
# html_use_numbered_lists = False
