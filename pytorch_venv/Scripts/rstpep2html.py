#!C:\Users\kewjs\Documents\02-Self_Learning\01-Data_Science\14-Pytorch_Tutorial\Pytorch_Tutorial-main\pytorch_venv\Scripts\python.exe

# $Id: rstpep2html.py 8927 2022-01-03 23:50:05Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing HTML from PEP
(Python Enhancement Proposal) documents.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates (X)HTML from reStructuredText-format PEP files.  '
               + default_description)

publish_cmdline(reader_name='pep', writer_name='pep_html',
                description=description)
