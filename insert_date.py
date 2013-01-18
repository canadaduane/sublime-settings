import datetime
import sublime_plugin

class InsertDateCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # Generate the timestamp
    timestamp_str = datetime.datetime.now().strftime("[%Y-%m-%d]")

    # For region in the selection (i.e. if you have multiple regions selected,
    # insert the timestamp in all of them)
    for r in self.view.sel():
      if r.size() > 0:
        self.view.replace(edit, r, timestamp_str)
      else:
        self.view.insert(edit, r.begin(), timestamp_str)