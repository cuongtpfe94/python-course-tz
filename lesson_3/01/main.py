import file_utils
from collections import Counter

def main():
    filename = input("Nhập tên file cần phân tích: ").strip()

    if not filename:
        print("Tên file không được để trống")
        return

    try:
        content = file_utils.read_file_content(filename)

        if not content.strip():
            print("File rỗng")
            return

        frequency = file_utils.count_word_frequency(content)

        print(f"Tổng số từ khác nhau: {len(frequency)}")
        print("Top 10 từ xuất hiện nhiều nhất:")

        for word, count in Counter(frequency).most_common(10):
            print(f"- {word}: {count}")

    except FileNotFoundError:
        print("File không tìm thấy")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")


if __name__ == "__main__":
    main()
