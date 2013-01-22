import datetime
import sublime_plugin
import re
from sublime import Region

class InsertDateCommand(sublime_plugin.TextCommand):
  date_sample = "[2013-01-01]"
  date_size = len(date_sample)

  def run(self, edit):

    # For region in the selection (i.e. if you have multiple regions selected,
    # insert the timestamp in all of them)
    for r in self.view.sel():
      if r.size() > 0:
        self.view.replace(edit, r, self.get_date())
      else:
        if self.is_point_after_date(r):
          date_region = Region(r.begin() - InsertDateCommand.date_size, r.end())
          self.view.replace(edit, date_region, self.get_datetime())
        else:
          self.view.insert(edit, r.begin(), self.get_date())

  def get_date(self):
    return datetime.datetime.now().strftime("[%Y-%m-%d]")

  def get_datetime(self):
    return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M]")

  def is_point_after_date(self, region):
    if region.begin() <= InsertDateCommand.date_size:
      return False
    else:
      date_region = Region(region.begin() - InsertDateCommand.date_size, region.end())
      text = self.view.substr(date_region)
      if re.match("\[\d+-\d+-\d+\]$", text):
        return True
      else:
        return False
