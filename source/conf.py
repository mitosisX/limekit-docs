# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "limekit docs"
copyright = "2023, Take bytes"
author = "Limekit"
release = "1.0"

version = "1.0"
author = "Omega Msiska"
contact = "omegamsiskah@gmail.com"

rst_epilog = """
.. |widgets| replace:: 35
"""

# pygment_style = "sphinx"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# numfig = False

# Disable numbered bullet points in HTML output
# html_use_numbered_lists = False
