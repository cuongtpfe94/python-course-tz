from datetime import datetime

class Task:
  def __init__(self, description: str, due_date: datetime, status: str = "todo"):
    self.description = description
    self.due_date = due_date # datetime
    self.status = status # "todo" hoặc "done"

  def is_overdue(self, now: datetime) -> bool:
    return self.due_date < now and self.status != "done"

  def __str__(self) -> str:
    status_display = "DONE" if self.status == "done" else "TODO"
    date_str = self.due_date.strftime("%Y-%m-%d")
    return f"[{status_display}] {self.description} (Hạn: {date_str})"

