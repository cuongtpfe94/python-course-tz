from datetime import datetime
from models import Task
from task_service import load_tasks, save_tasks, get_overdue_tasks, get_todo_tasks

FILENAME = "tasks.txt"

def display_menu():
  print("1. Xem tất cả task")
  print("2. Xem các task quá hạn")
  print("3. Thêm task mới")
  print("4. Đánh dấu task là done")
  print("5. Thoát")

def view_all_tasks(tasks: list[Task]):
  if not tasks:
    print("\nKhông có task nào trong danh sách!")
    return

  for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")

def view_overdue_tasks(tasks: list[Task]):
  overdue = get_overdue_tasks(tasks)

  if not overdue:
    print("\nKhông có task nào quá hạn!")
    return

  for i, task in enumerate(overdue, 1):
    print(f"{i}. {task}")

def add_new_task(tasks: list[Task]):
  description = input("Nhập mô tả task: ").strip()

  if not description:
    print("Mô tả không được để trống!")
    return

  due_date_str = input("Nhập ngày hạn (YYYY-MM-DD): ").strip()

  try:
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")

    new_task = Task(description, due_date, "todo")
    tasks.append(new_task)

    save_tasks(FILENAME, tasks)

    print(f"\nĐã thêm task: {new_task}")
  except ValueError:
    print(f"Ngày không đúng format! Vui lòng nhập theo định dạng YYYY-MM-DD")
  except Exception as e:
    print(f"Lỗi: {e}")

def mark_task_as_done(tasks: list[Task]):
  todo_tasks = get_todo_tasks(tasks)

  if not todo_tasks:
    print("\nKhông có task nào cần hoàn thành!")
    return

  task_indices = []
  for i, task in enumerate(tasks):
    if task.status == "todo":
      task_indices.append(i)
      print(f"{len(task_indices)}. {task}")

  try:
    choice = input("Nhập số thứ tự, đổi `status` của task thành `done`: ").strip()
    index = int(choice) - 1

    if 0 <= index < len(task_indices):
      original_index = task_indices[index]
      tasks[original_index].status = "done"

      save_tasks(FILENAME, tasks)

      print(f"\nĐã đánh dấu hoàn thành: {tasks[original_index]}")
    else:
      print("Số thứ tự không hợp lệ!")
  except ValueError:
    print("Vui lòng nhập số!")
  except Exception as e:
    print(f"Lỗi: {e}")

def main():
  tasks = load_tasks(FILENAME)

  while True:
    print(f"================================================\n")
    display_menu()

    try:
      choice = input("\nNhập lựa chọn (1-5): ").strip()

      if choice == "1":
        view_all_tasks(tasks)
      elif choice == "2":
        view_overdue_tasks(tasks)
      elif choice == "3":
        add_new_task(tasks)
      elif choice == "4":
        mark_task_as_done(tasks)
      elif choice == "5":
        print("\nThoát chương trình.")
        break
      else:
        print("\nLựa chọn không hợp lệ! Vui lòng chọn từ 1-5.")

    except KeyboardInterrupt:
      print("\n\nĐã dừng chương trình.")
      break
    except Exception as e:
      print(f"\nCó lỗi xảy ra: {e}")

if __name__ == "__main__":
  main()

