sublime-spec-focuser
====================

Sublime Text plugin for toggling focus on currently selected spec.
http://stackoverflow.com/questions/5069677/how-do-i-run-only-specific-tests-in-rspec

**NOTE:** This is *NOT* a Sublime plugin for yet-another Rspec runner.
This plugin assumes you use a existing continuous testing framework
(ex: guard) to act as your test-runner.  This is a *much* more stable
solution than trying to run Rspec from within the context of SublimeText.

## Features
* shortcut for toggling focus on currently highlighted spec
* adds `focus: true` configuration to closest `it`, `context`, or `describe` block
* re-runnable to remove the focus keywords after complete

## Installation

Install via the great [Package Control Plugin Manager](https://sublime.wbond.net/)

## Usage
* Open control panel (ex: CMD+SHIFT+P)
* select "Toggle Focus on currently selected spec" command
* `focus: true` will be automatically added to the currently selected spec
* Re-run command to remove the focus keywords
