# import os
# # print(os.getcwd())

# for i in range(1,6):
#     week_name = "week" + str(i)
#     os.mkdir(week_name)
#     for j in range(1,6):
#         day_name = "day" + str(j)
#         day_path = os.path.join(week_name, day_name)
#         os.mkdir(day_path)
#         lesson = "lesson"
#         homework = "homework"
#         lesson_path = os.path.join(day_path, lesson)
#         os.mkdir(lesson_path)
#         homework_path = os.path.join(day_path, homework)
#         os.mkdir(homework_path)