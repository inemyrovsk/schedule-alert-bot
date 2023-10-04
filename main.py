import telebot
import datetime
from post import getNextLesson
BOT_TOKEN = ''
bot = telebot.TeleBot(BOT_TOKEN)


currentTime = datetime.datetime.now()
today8am = currentTime.replace(hour=8, minute=0, second=0, microsecond=0)
today9am35 = currentTime.replace(hour=9, minute=35, second=0, microsecond=0)
today11am20 = currentTime.replace(hour=11, minute=20, second=0, microsecond=0)
today13am20 = currentTime.replace(hour=13, minute=20, second=0, microsecond=0)
today15am05 = currentTime.replace(hour=15, minute=5, second=0, microsecond=0)
index = 0

if currentTime < today8am:
    index = 0
elif today8am < currentTime < today9am35:
    index = 1
elif today9am35 < currentTime < today11am20:
    index = 2
elif today11am20 < currentTime < today13am20:
    index = 3
elif today13am20 < currentTime < today15am05:
    index = 4
else:
    index = 5
def start_bot():
    bot.infinity_polling()


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    todayClasses = getNextLesson()
    lessonData = todayClasses[0]['lessons'][index]['periods'][0]
    lessonName = lessonData['disciplineFullName']
    classroom = lessonData['classroom']
    teacherFullName = lessonData['teachersNameFull']
    timeStart = lessonData['timeStart']
    timeEnd = lessonData['timeEnd']
    print("index:", index)
    print(f"""
    Наступна Пара: {lessonName}
        Аудиторія: {classroom}
        Початок: {timeStart}
        Кінець: {timeEnd}
        Викладач: {teacherFullName}""")
    # return {"lessonName": lessonName, "classroomName": classroom, "timeStart": timeStart, "timeEnd": timeEnd}
    bot.reply_to(message, f"""
    
    Наступна Пара: {lessonName}
        Аудиторія: {classroom}
        Початок: {timeStart}
        Кінець: {timeEnd}
        Викладач: {teacherFullName}
    """)


# @bot.message_handler(content_types=['text'])
# def send_alert():
#     bot.send_message(1222, "test")


if __name__ == "__main__":
    print("starting")
    start_bot()
