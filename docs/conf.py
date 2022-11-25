# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Project information -- #

project = 'helloWorld'
copyright = '2020, None'
author = 'None'

# The short X.Y version
version = '<number>'
# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration -- #

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output -- #

# Output file base name for HTML help builder.
htmlhelp_basename = 'helloWorlddoc'

# -- Extension configuration -------------------------------------------------

# add sourcecode to path
import sys, os
sys.path.insert(0, os.path.abspath('../src'))
 
#-- SETUP THE RTD LOWER-LEFT --#
try:
   html_context
except NameError:
   html_context = dict()
html_context['display_lower_left'] = True

if 'REPO_NAME' in os.environ:
	REPO_NAME = os.environ['REPO_NAME']
else:
	REPO_NAME = ''
 
# SET CURRENT_VERSION
from git import Repo
repo = Repo( search_parent_directories=True )
 
if 'current_version' in os.environ:
   # get the current_version env var set by buildDocs.sh
   current_version = os.environ['current_version']
else:
   # the user is probably doing `make html`
   # set this build's current version by looking at the branch
   current_version = repo.active_branch.name
 
# tell the theme which version we're currently on ('current_version' affects
# the lower-left rtd menu and 'version' affects the logo-area version)
html_context['current_version'] = current_version
html_context['version'] = current_version
 
# POPULATE LINKS TO OTHER VERSIONS
html_context['versions'] = list()
 
versions = repo.tags
for version in versions:
   html_context['versions'].append( (str(version), '/' +REPO_NAME+ '/' + str(version)+ '/') )
   
##########################
# "EDIT ON GITHUB" LINKS #
##########################
 
html_context['display_github'] = True
html_context['github_user'] = 'maltfield'
html_context['github_repo'] = 'rtd-github-pages'
html_context['github_version'] = 'master/docs/'
 
