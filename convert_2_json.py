import json
import data

goals = data.goals
teachers = data.teachers
days = {
  "mon" : "Понедельник",
  "tue" : "Вторник",
  "wed" : "Среда",
  "thu" : "Четверг",
  "fri" : "Пятница",
  "sat" : "Суббота",
  "sun" : "Воскресенье"
}

with open("goals.json", "w", encoding="utf-8") as f:
   json.dump(goals, f, indent=4, ensure_ascii=False)

with open("teachers.json", "w", encoding="utf-8") as f:
   json.dump(teachers, f, indent=4, ensure_ascii=False)

with open("days.json", "w", encoding="utf-8") as f:
   json.dump(days, f, indent=4, ensure_ascii=False)

