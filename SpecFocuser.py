import sublime, sublime_plugin, re

# toggle focus on Rspec examples to the closest defined assertion or context
# Running the command once will add `focus: true` and running again will remove
# it back to the original state.
#
# NOTE: this is *NOT* intended to be a test runner. This command relies on
# an external process (ex: guard) to monitor the specs and run the specific
# focused spec.
#
# api docs: http://www.sublimetext.com/docs/api-reference#sublime.View
#
# TODO: add support for detecting inline examples (ex: it { should be_true } )
class SpecFocusCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    selection = self.view.sel()[0]
    current_line = self.view.line(selection)
    while current_line.begin() >= 0:
      line_text = self.view.substr(current_line)

      focused_spec_matcher = '(it|describe|context).+, focus: true\s+do'
      match = re.search(focused_spec_matcher, line_text)
      if match:
        print("Removing focused spec definition...")
        self.view.replace(edit, current_line, re.sub(', focus: true ', ' ', line_text))
        break

      spec_matcher = '(it|describe|context)\s?(.*)\sdo'
      match = re.search(spec_matcher, line_text)
      if match:
        print("Adding focused spec definition...")
        self.view.replace(edit, current_line, re.sub(spec_matcher, r'\1 \2, focus: true do', line_text))
        break

      selection = sublime.Region(current_line.begin() - 1, current_line.begin() - 1)
      current_line = self.view.line(selection)
