sublime-spec-focuser
====================

Sublime Text plugin for toggling focus on currently selected spec.

http://stackoverflow.com/questions/5069677/how-do-i-run-only-specific-tests-in-rspec

**NOTE:** This is *NOT* a Sublime plugin for yet-another Rspec runner.
This plugin assumes you use a existing continuous testing framework
(ex: guard) to act as your test-runner.  This is a *much* more stable
solution than trying to run Rspec from within the context of SublimeText.

## Features
* searches for closest defined spec
* adds `focus: true` configuration to closest `it`, `context`, or `describe` block
* shortcut for toggling focus on currently highlighted spec (`CMD+ALT+CTRL+F`)
* re-runnable to remove the focus keywords after complete
* clears all `focus: true` tags from the current file
* shortcut for clearing focus tags on current file (`CMD+ALT+CTRL+C`)

## Installation

Install via the great [Package Control Plugin Manager](https://sublime.wbond.net/)

## Usage

**Add `focus: true` tag**
* Open control panel (ex: CMD+SHIFT+P)
* select "Toggle Focus on currently selected spec" command
* `focus: true` will be automatically added to the currently selected spec
* Re-run command to remove the focus keywords

**Clear all `focus: true` tags from the current file**
* Open control panel (ex: CMD+SHIFT+P)
* select "Remove all focus tags from current file" command
* all instances of `focus: true` will be removed from the current file
