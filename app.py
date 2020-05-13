from flask import Flask, render_template, request, json
import random
import pprint

app = Flask(__name__)
app.secret_key = "secure_code_string"


# ---- ... ---
@app.route('/')
def render_main():
   # Грузим данные
   with open("teachers.json", "r") as f:
      teachers_data = json.load(f)
   with open("goals.json", "r") as f:
      goals_data = json.load(f)
   with open("logos.json", "r") as f:
      logo = json.load(f)
   # Берем случайных 6 преподователей
   teachers_data = random.sample(teachers_data, 6)
   return render_template('index.html', goals_data=goals_data, teachers_data=teachers_data, logo=logo)



# ---- Страница цели ----
@app.route('/goals/<id_goal>/')
def render_goals(id_goal):
   # Грузим данные
   teachers_filtered = []
   teachers_tmp = []
   with open("teachers.json", "r") as f:
      teachers_data = json.load(f)
   with open("goals.json", "r") as f:
      goals_data = json.load(f)
   with open("logos.json", "r") as f:
      logo_tmp = json.load(f)
   # Оставляем только нужных учитилей
   for teacher in teachers_data:
      for goal in teacher["goals"]:
         if goal == id_goal:
            teachers_tmp.append(teacher)
   teachers_filtered = sorted(teachers_tmp, key=lambda x: x['rating'], reverse=True)
   # Логотип
   logo = logo_tmp[id_goal]
   return render_template('goal.html', id_goal=id_goal, goals_data=goals_data, teachers_filtered=teachers_filtered, logo=logo)



# ---- Профиль преподователя ----
@app.route('/profiles/<int:id_teacher>/')
def render_profiles(id_teacher):
   # Грузим данные об учителе
   with open("teachers.json", "r") as f:
      teachers_data = json.load(f)
   # Грузим цели
   with open("goals.json", "r") as f:
      goals_data = json.load(f)
   # Грузим названия дней
   with open("days.json", "r") as f:
      days = json.load(f)
   tmp = teachers_data[id_teacher]
   teacher_free = tmp["free"]
   return render_template('profile.html', id_teacher = id_teacher, teacher_info = teachers_data[id_teacher], teacher_free = teacher_free, goals_data = goals_data, days = days)



# ---- Страница запроса ----
@app.route('/request/')
def render_request():
   return render_template('request.html')



# ---- Страница подтверждения запроса ----
@app.route('/request_done/', methods=['GET','POST'])
def render_request_done():
   new_request = {}
   if request.method == "POST":
      new_request["goal"] = request.form["goal"]
      new_request["time"] = request.form["time"]
      new_request["clientName"] = request.form["clientName"]
      new_request["clientPhone"] = request.form["clientPhone"]
      # Добавляем заявку в базу
      with open("request.json", "r") as f:
         data = json.load(f)
      data.append(new_request)
      with open("request.json", "w") as f:
         json.dump(data, f, indent=4, ensure_ascii=False)
      return render_template('request_done.html', new_request=new_request)
   else:
      return "Вы не ввели данные на форме. Попробуйте снова"



# ---- Страница бронирования ----
@app.route('/booking/<int:id_teacher>/<date>/<time>/')
def render_booking(id_teacher,date,time):
   # Грузим данные об учителе
   with open("teachers.json", "r") as f:
      teachers_data = json.load(f)
   # Грузим названия дней
   with open("days.json", "r") as f:
      days = json.load(f)
   return render_template('booking.html', id_teacher = id_teacher, teacher_info = teachers_data[id_teacher], date = date, time = time, days = days)



# ---- Принимаем данные с формы и сохраняем заявку ----
@app.route('/booking_done/', methods=['GET','POST'])
def render_booking_done():
   new_request = {}
   if request.method == "POST":
      new_request["clientWeekday"] = request.form["clientWeekday"]
      new_request["clientWeekday_rus"] = request.form["clientWeekday_rus"]
      new_request["clientTime"] = request.form["clientTime"]
      new_request["clientTeacher"] = request.form["clientTeacher"]
      new_request["clientName"] = request.form["clientName"]
      new_request["clientPhone"] = request.form["clientPhone"]
      # Добавляем заявку в базу
      with open("booking.json", "r") as f:
         data = json.load(f)
      data.append(new_request)
      with open("booking.json", "w") as f:
         json.dump(data, f, indent=4, ensure_ascii=False)
      return render_template('booking_done.html', new_request=new_request)
   else:
      return "Вы не ввели данные на форме. Попробуйте снова"


if __name__ == '__main__':
    app.run()