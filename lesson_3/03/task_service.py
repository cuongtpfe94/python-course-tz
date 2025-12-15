from datetime import datetime
from models import Task

def load_tasks(filename: str) -> list[Task]:
  tasks = []

  try:
    with open(filename, "r", encoding="utf-8") as file:
      for line_num, line in enumerate(file, 1):
        line = line.strip()
        if not line:
          continue

        try:
          parts = line.split(";")
          if len(parts) != 3:
            raise ValueError("Thiếu cột dữ liệu")

          description = parts[0]
          due_date = datetime.strptime(parts[1], "%Y-%m-%d")
          status = parts[2]

          if status not in ["todo", "done"]:
            raise ValueError(f"Status không hợp lệ: {status}")

          tasks.append(Task(description, due_date, status))
        except ValueError as e:
          print(f"Bỏ qua dòng {line_num} '{line}' - Lỗi: {e}")
        except Exception as e:
          print(f"Bỏ qua dòng {line_num} '{line}' - Lỗi không xác định: {e}")

  except FileNotFoundError:
    print(f"File '{filename}' không tồn tại.")
  except Exception as e:
    print(f"Lỗi khi đọc file: {e}")

  return tasks

def save_tasks(filename: str, tasks: list[Task]) -> None:
  try:
    with open(filename, "w", encoding="utf-8") as file:
      for task in tasks:
        date_str = task.due_date.strftime("%Y-%m-%d")
        file.write(f"{task.description};{date_str};{task.status}\n")
  except Exception as e:
    print(f"Lỗi khi lưu file: {e}")

def get_overdue_tasks(tasks: list[Task]) -> list[Task]:
  now = datetime.now()
  return [task for task in tasks if task.is_overdue(now)]

def get_todo_tasks(tasks: list[Task]) -> list[Task]:
  return [task for task in tasks if task.status == "todo"]

def mark_task_done(tasks: list[Task], index: int) -> bool:
  if 0 <= index < len(tasks):
    tasks[index].status = "done"
    return True
  return False

