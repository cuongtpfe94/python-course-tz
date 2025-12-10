"""
# Bài tập 1: Kiểm tra và tìm ngày kế tiếp, ngày trước đó
"""

def is_year_leap(year: int) -> bool:
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    return True
  else:
    return False

def month_days(month: int, year: int) -> int:
  if month in [1, 3, 5, 7, 8, 10, 12]:
    return 31
  elif month in [4, 6, 9, 11]:
    return 30
  elif month == 2:
    return 29 if is_year_leap(year) else 28
  else:
    return 0

def is_valid_date(day: int, month: int, year: int) -> bool:
  if month_days(month, year) == 0:
    return False
  if day < 1 or day > month_days(month, year):
    return False
  return True

def next_day(day: int, month: int, year: int) -> tuple[int, int, int]:
  if is_valid_date(day, month, year):
    current_month_days = month_days(month, year)

    if day < current_month_days:
      return day + 1, month, year
    else:
      if month == 12:
        return 1, 1, year + 1
      else:
        return day, month + 1, year
  else:
    return day, month, year

def previous_day(day: int, month: int, year: int) -> tuple[int, int, int]:
  if is_valid_date(day, month, year):
    current_month_days = month_days(month, year)

    if day > 1:
      return day - 1, month, year
    else:
      if month > 1:
        return current_month_days, month - 1, year
      else:
        return current_month_days, 12, year - 1
  else:
    return day, month, year

while True:
  ngay = int(input("Nhap ngay: "))
  thang = int(input("Nhap thang: "))
  nam = int(input("Nhap nam: "))

  print(f"\nNgay da nhap: {ngay}/{thang}/{nam}")
  if is_valid_date(ngay, thang, nam):
    break
  else:
    print("Ngay khong hop le")

next_day = next_day(ngay, thang, nam)
print(f"\nNgay ke tiep: {next_day[0]}/{next_day[1]}/{next_day[2]}")

previous_day = previous_day(ngay, thang, nam)
print(f"\nNgay truoc do: {previous_day[0]}/{previous_day[1]}/{previous_day[2]}")


"""
# Bài tập 2: Viết chương trình tính `S = 1 + 1/3! + 1/5! + ... + 1/(2n−1)!`, với n được nhập từ bàn phím
"""

def factorial(n: int) -> int:
  if n == 0:
    return 1
  return n * factorial(n - 1)

def sum_of_series(n: int) -> float:
  sum = 0
  for i in range(1, n + 1):
    sum += 1 / factorial(2 * i - 1)
  return sum

while True:
  n = int(input("Nhap n: "))
  if n > 0:
    break
  else:
    print("n phai lon hon 0")

print(f"S = {sum_of_series(n)}")


"""
# Bài tập 3: Thao tác chuỗi
"""

def normalize_sentence(sentence: str) -> str:
  sentence = sentence.strip()
  sentence = sentence.capitalize()
  sentence = sentence.replace('..', '.')
  return sentence

print(normalize_sentence("Hello worlD, this Is python.. "))
