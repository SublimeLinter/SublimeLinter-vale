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

    syntax = (
        'plain text',
        'markdown'
    )
    cmd = 'vale --no-wrap'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.5.0'
    regex = (
        r'(?P<line>\d+):(?P<col>\d+)\s{2,}'
        r'((?P<error>error)|(?P<warning>warning))\s{2,}'
        r'(?P<message>.+?)(?=\s{2,})'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
