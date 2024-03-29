#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Adam Hollett
# Copyright (c) 2017 Adam Hollett
#
# License: MIT
#

"""This module exports the Vale plugin class."""

from SublimeLinter.lint import Linter, util


class Vale(Linter):
    """Provides an interface to vale."""

    defaults = {
        'selector': 'text.plain, text.html.markdown',
    }
    cmd = ('vale', '--no-wrap', '${args}', '${temp_file}')
    regex = (
        r'(?P<line>\d+):(?P<col>\d+)\s{2,}'
        r'(?P<error_type>\S+)\s{2,}'
        r'(?P<message>.+?)(?=$)'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = 'md'
    error_stream = util.STREAM_BOTH
    word_re = None
