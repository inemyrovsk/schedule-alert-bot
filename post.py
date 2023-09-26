import datetime

import requests


FormData = {
    "dateStart": datetime.date.today(), "dateEnd": datetime.date.today(), "groupId": "820", "course": "1",
    "facultyID": "1"
}


def getNextLesson():
    with requests.Session() as s:
        res = s.post("https://api.e-rozklad.dut.edu.ua/time-table/group?type=0", data=FormData)
        jsonResponse = res.json()

        return jsonResponse

# response = [{'date': '2023-09-27', 'lessons': [{'number': 2, 'periods': [
#     {'r1': 313640, 'rz14': 585, 'rz15': 680, 'r5': 31, 'disciplineId': 127, 'educationDisciplineId': 64696,
#      'disciplineFullName': 'Вища математика', 'disciplineShortName': 'ВМ', 'classroom': '329', 'timeStart': '09:45',
#      'timeEnd': '11:20', 'teachersName': 'Калинюк А.М.', 'teachersNameFull': 'Калинюк Алла Миколаївна', 'type': 2,
#      'typeStr': 'Prac', 'dateUpdated': '2023-08-30 10:57:28', 'nonstandardTime': False, 'groups': 'ШІД-11',
#      'chairName': 'ВМ', 'extraText': False, 'lessonYear': 2023, 'semester': 0}]}, {'number': 3, 'periods': [
#     {'r1': 313781, 'rz14': 705, 'rz15': 800, 'r5': 18, 'disciplineId': 2071, 'educationDisciplineId': 64713,
#      'disciplineFullName': 'Основи штучного інтелекту', 'disciplineShortName': 'ОШІ-2020', 'classroom': '219',
#      'timeStart': '11:45', 'timeEnd': '13:20', 'teachersName': 'Кисіль Т.М.',
#      'teachersNameFull': 'Кисіль Тетяна Миколаївна', 'type': 2, 'typeStr': 'Prac', 'dateUpdated': '2023-08-10 11:57:48',
#      'nonstandardTime': False, 'groups': 'ШІД-11', 'chairName': 'ШІ', 'extraText': False, 'lessonYear': 2023,
#      'semester': 0}]}]}]
