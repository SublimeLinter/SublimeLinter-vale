

# SublimeLinter-contrib-vale

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [Vale](https://valelint.github.io/docs). It will be used with files that have the `Plain text` or `Markdown` syntaxes.

This version is updated to work with the later versions of SublimeLinter. It may disappear in the infrequent event that [the original package](https://packagecontrol.io/packages/SublimeLinter-contrib-vale) is upgraded.

## Installation

SublimeLinter 3 must be installed to use this plugin. To install SublimeLinter, please follow [the SublimeLinter install instructions](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation

**Note**: This plugin requires `vale` **0.5.0** or later. Vale runs on Windows, macOS, and Linux. It can be installed by downloading an executable from the [Vale releases](https://github.com/errata-ai/vale/releases) page.


### Linter configuration

In order for `vale` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in "[Finding a linter executable](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable)" through "Validating your PATH" in the documentation.

Once you have installed and configured `vale`, you can install the `SublimeLinter-contrib-vale` plugin.

### Plugin installation

Here's how to install this custom fork of `SublimeLinter-contrib-vale`.

1. In the Command Palette, enter `Package Control: Add Repository`.
2. When prompted, enter the URL `git@github.com:dylan-k/SublimeLinter-contrib-vale.git`.
3. In the Command Palette, enter `Package Control: Install Package`.
4. Search for ``Vale`` and you install the option for `SublimeLinter-contrib-vale`.
5. Quit Sublime.
6. Open Sublime and try to use.

## Settings

No extra settings required, but just in case:

For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.io/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.io/en/latest/linter_settings.html).

You can configure Vale for your project using a configuration file named `.vale` or `_vale`. For more information, see [Vale's documentation](https://valelint.github.io/docs/config).

## Contributing

Contribute to [the original package](https://packagecontrol.io/packages/SublimeLinter-contrib-vale), since this is a fork.
