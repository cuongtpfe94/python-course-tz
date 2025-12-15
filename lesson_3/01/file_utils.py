# Bài tập 1: Dict tần suất từ trong file (Module + File I/O + Exception)

## Đề bài:
# Viết chương trình phân tích một file text (ví dụ: `article.txt`) và in ra tần suất xuất hiện của từng từ

from collections import Counter

def read_file_content(filename: str) -> str:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")
    except Exception as e:
        raise RuntimeError(f"Error reading file '{filename}': {e}")


def count_word_frequency(text: str) -> dict[str, int]:
    words = text.split()
    return dict(Counter(words))
