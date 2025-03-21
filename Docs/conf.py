# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'EnergyScope_documentation'
copyright = '2021, G. Limpens'
author = 'G. Limpens'

# The full version, including alpha/beta/rc tags
release = '2.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinxcontrib.bibtex',
               'nbsphinx',
               'sphinx_design'
]
# Bibliography:
bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrt'
bibtex_reference_style = 'super'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'default' #There is a mistake with sphinx_rtd_theme, cannot be installed even by adding it in requirements and extensions = []
numfig = True # Add figure numbering
numtab = True # Add table numbering

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []


# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'images/estd_graphical_abstract.png'

# To add interactive maps:
nbsphinx_custom_formats = {
    ".md": ["jupytext.reads", {"fmt": "mystnb"}],
}