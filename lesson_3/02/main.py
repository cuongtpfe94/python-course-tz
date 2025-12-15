# Bài tập 2: Quản lý điểm sinh viên với File I/O + OOP + Exception

## Đề bài:
# > Viết chương trình quản lý điểm sinh viên, dữ liệu được lưu trong file `students.txt`, mỗi dòng có format:

from student import Student

def load_students_from_file(filename: str) -> list[Student]:
  students = []
  with open(filename, "r", encoding="utf-8") as file:
    for line_num, line in enumerate(file, 1):
      line = line.strip()
      if not line:
        continue

      try:
        parts = line.split(",")
        if len(parts) != 3:
          raise ValueError("Thiếu cột dữ liệu")

        name = parts[0]
        age = int(parts[1])
        score = float(parts[2])

        students.append(Student(name, age, score))
      except ValueError as e:
        print(f"Bỏ qua dòng {line_num} '{line}' - Lỗi: {e}")
      except Exception as e:
        print(f"Bỏ qua dòng {line_num} '{line}' - Lỗi không xác định: {e}")

  return students

def calc_avg_score(students: list[Student]) -> float:
  if not students:
    return 0.0
  return sum(student.score for student in students) / len(students)

def find_top_student(students: list[Student]) -> Student | None:
  if not students:
    return None
  return max(students, key=lambda student: student.score)

def filter_failed(students: list[Student]) -> list[Student]:
  return [student for student in students if not student.is_passed()]

def main():

  filename = input("Nhập tên file điểm sinh viên: ")

  if not filename:
    print("Tên file không được để trống")
    return

  try:
    students = load_students_from_file(filename)

    if not students:
      print("\nKhông có sinh viên nào trong danh sách!")
      return

    print(f"\n================================================")
    print(f"Tổng số sinh viên: {len(students)}")
    print(f"Điểm trung bình lớp: {calc_avg_score(students):.2f}")

    top_student = find_top_student(students)
    if top_student:
      print(f"Sinh viên điểm cao nhất: {top_student}")

    failed_students = filter_failed(students)
    print(f"\nDanh sách sinh viên bị rớt ({len(failed_students)} sinh viên):")

    if failed_students:
      for student in failed_students:
        print(f"  {student}")
    else:
      print("Không có sinh viên nào bị rớt!")

    print(f"================================================\n")

  except FileNotFoundError:
    print(f"Lỗi: File '{filename}' không tìm thấy!")
  except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
  main()
