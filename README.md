sublime-spec-focuser
====================

Sublime Text plugin for toggling focus on currently selected spec

**NOTE:** This is *NOT* a Sublime plugin for yet-another Rspec runner.
This plugin assumes you use a existing continuous testing framework
(ex: guard) to act as your test-runner.  This is a *much* more stable
solution than trying to run Rspec from within the context of SublimeText.

## Features
* shortcut for toggling focus on currently highlighted spec (`CMD+ALT+CTRL+F`)
* searches for closest defined spec
* re-runnable to remove the focus keywords after complete

## Installation
TODO: Package Control integration

## Usage
* Open control panel (ex: CMD+SHIFT+P)
* select "Toggle Focus on currently selected spec" command
* `focus: true` will be automatically added to the currently selected spec
* Re-run command to remove the focus keywords
