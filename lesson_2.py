'''
# Bài tập 1: Quản lý học viên & khóa học
'''

# Danh sách học viên (list các tuple)
students = [
    ("SV01", "Nguyen Van A", 20),
    ("SV02", "Tran Thi B", 21),
    ("SV03", "Le Van C", 19),
]

# a. Dùng vòng lặp + unpacking tuple để in ra danh sách học viên theo format

for student in students:
  id, name, age = student
  print(f"{id} - {name} ({age})")

# b. Tạo một list mới `python_scores` chỉ chứa tuple `(student_id, name, python_score)

# Dict lưu điểm từng môn cho từng sinh viên
scores = {
    "SV01": {"math": 8.0, "python": 7.5},
    "SV02": {"math": 6.5, "python": 8.5},
    "SV03": {"math": 9.0, "python": 9.5},
}

python_scores = [(id, name, scores[id]["python"]) for id, name, _ in students]
print('\n', python_scores)

#  c. Tìm học viên có điểm Python cao nhất từ `python_scores` và in ra: `Top Python: <name> - <score>`

top_python_score = python_scores[0]
for score in python_scores:
  if score[2] > top_python_score[2]:
    top_python_score = score

print(f'\nTop Python: {top_python_score[1]} - {top_python_score[2]}')

# d. Thêm môn mới `"database"` vào `courses` (dùng set) và gán tạm điểm `database = 0` cho tất cả sinh viên trong `scores`

# Set các môn học hiện có
courses = {"math", "python"}

courses.add("database")
print('\n', courses)

# Gán điểm database = 0 cho tất cả sinh viên trong scores
for id, _, _ in students:
  scores[id]["database"] = 0

print('\n', scores)

'''
# Bài tập 2: Thống kê sản phẩm & hóa đơn
'''


# Mỗi sản phẩm là 1 tuple (product_id, name, price)
products = [
    (1, "Ban Phim", 250_000),
    (2, "Chuot", 150_000),
    (3, "Man Hinh", 3_000_000),
    (4, "Tai Nghe", 500_000),
]

# Danh sách đơn hàng (list dict)
orders = [
    {"order_id": "HD01", "items": [1, 2, 4]},
    {"order_id": "HD02", "items": [2, 3]},
    {"order_id": "HD03", "items": [1, 4]},
]

# a. Tạo một dict `product_map` từ `products` để tra cứu nhanh theo `product_id` với dạng:

product_map = {product[0]: {"name": product[1], "price": product[2]} for product in products}
print('\n', product_map)

# b. Với mỗi hóa đơn trong `orders`, hãy tính tổng tiền của hóa đơn đó, lưu vào key mới `"total"` trong từng dict hóa đơn

for order in orders:
  total = 0
  for id in order["items"]:
    total += product_map[id]["price"]
  order["total"] = total

print('\n', orders)

# c. In ra danh sách hóa đơn theo format:
print('\n')
for order in orders:
  print(f'{order["order_id"]}: - {len(order["items"])} san pham, Tong tien = {order["total"]}')


'''
# Bài tập 3: Hệ thống tag bài viết & người dùng
'''

# Danh sách user: list tuple (user_id, name)
users = [
    ("U01", "Alice"),
    ("U02", "Bob"),
    ("U03", "Charlie"),
]

# Dict bài viết: key là post_id, value là dict thông tin
posts = {
    "P01": {
        "title": "Hoc Python co ban",
        "author_id": "U01",
        "tags": {"python", "beginner"},
    },
    "P02": {
        "title": "Lam viec voi List va Dict",
        "author_id": "U01",
        "tags": {"python", "data-structure"},
    },
    "P03": {
        "title": "Gioi thieu HTML CSS",
        "author_id": "U02",
        "tags": {"web", "frontend"},
    },
}

# a. Tạo một dict `user_map` từ `users`, map `user_id` sang `name`

user_map = {user[0]: user[1] for user in users}
print('\n', user_map)

# b. Dùng vòng lặp duyệt `posts.items()` để in ra:

for post_id, post in posts.items():
  print(f'[{post_id}] {post["title"]} - {user_map[post["author_id"]]} - Tags: {", ".join(sorted(post["tags"]))}')

# c. Tạo một set `all_tags` chứa toàn bộ tag xuất hiện trong mọi bài viết
all_tags = set()

for post in posts.values():
  all_tags.update(post["tags"])

print('\n', all_tags)

# * d. Tạo một dict `tag_counter` để đếm số bài viết chứa mỗi tag

tag_counter = {tag: 0 for tag in all_tags}

for post in posts.values():
  for tag in post["tags"]:
    tag_counter[tag] += 1

print('\n', tag_counter)
