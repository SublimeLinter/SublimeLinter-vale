# SublimeLinter-contrib-vale

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [vale](https://valelint.github.io/docs). It will be used with files that have the `plain text` or `markdown` syntaxes.

## Installation

SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation

Before using this plugin, you must ensure that `vale` is installed on your system.

**Note**: This plugin requires `vale` **0.5.0** or later.

#### Windows

Visit the [releases page](https://github.com/ValeLint/vale/releases) and download and install the latest `.msi` installer for Vale.

#### macOS

You can install Vale using [Homebrew](https://brew.sh/):

```
brew tap ValeLint/vale
brew install vale
```

#### Linux

You can install Vale using [snap](https://snapcraft.io):

```
snap install vale
```

### Linter configuration

In order for `vale` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `vale`, you can proceed to install the SublimeLinter-contrib-vale plugin if it is not yet installed.

### Plugin installation

Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `vale`. Among the entries you should see `SublimeLinter-contrib-vale`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings

For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

You can configure Vale for your project using `.vale` configuration files. For more information, see [Vale's documentation](https://valelint.github.io/docs/config).

## Contributing

If you would like to contribute enhancements or fixes, please do the following:

1. Fork this repository.
2. Work on a separate topic branch created from the latest `master`.
3. Commit and push the topic branch.
4. Make a pull request.

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass `flake8` and `pep257` linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are well known.

Thank you for helping out!