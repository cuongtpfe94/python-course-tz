class Student:
  def __init__(self, name: str, age: int, score: float):
    self.name = name
    self.age = age
    self.score = score

  def __str__(self) -> str:
    return f"{self.name} ({self.age} tuổi) - Điểm: {self.score}"

  def is_passed(self) -> bool:
    return self.score >= 5
