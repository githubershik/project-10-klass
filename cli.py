import random
import cv2
import speech_recognition as sr
import time
import psycopg2

conn = psycopg2.connect(dbname="project_db", user="postgres",
                        password="17042008", host="localhost", port="5433")
cursor = conn.cursor()
login = ""
password = ""
registred = False
# картинки
chem_pics = {
    1: "src/img/chem_pics/avogadro.png",
    2: "src/img/chem_pics/carbon.jpg",
    3: "src/img/chem_pics/Mercury.jpg",
    4: "src/img/chem_pics/natrii.jpg",
    5: "src/img/chem_pics/plumbum.jpg",
    6: "src/img/chem_pics/plutonium.jpg",
    7: "src/img/chem_pics/silicium.jpg",
    8: "src/img/chem_pics/mishyak.jpg",
    9: "src/img/chem_pics/molibden.jpg",
    10: "src/img/chem_pics/aurum.jpg"
}

bio_pics = {
    1: "src/img/bio_pics/",
    2: "src/img/bio_pics/",
    3: "src/img/bio_pics/",
    4: "src/img/bio_pics/",
    5: "src/img/bio_pics/",
    6: "src/img/bio_pics/",
    7: "src/img/bio_pics/",
    8: "src/img/bio_pics/",
    9: "src/img/bio_pics/",
    10: "src/img/bio_pics/"
}

math_pics = {
    1: "src/img/math_pics/",
    2: "src/img/math_pics/",
    3: "src/img/math_pics/",
    4: "src/img/math_pics/",
    5: "src/img/math_pics/",
    6: "src/img/math_pics/",
    7: "src/img/math_pics/",
    8: "src/img/math_pics/",
    9: "src/img/math_pics/",
    10: "src/img/math_pics/"
}

it_pics = {
    1: "src/img/it_pics/",
    2: "src/img/it_pics/",
    3: "src/img/it_pics/",
    4: "src/img/it_pics/",
    5: "src/img/it_pics/",
    6: "src/img/it_pics/",
    7: "src/img/it_pics/",
    8: "src/img/it_pics/",
    9: "src/img/it_pics/",
    10: "src/img/it_pics/"
}

eng_pics = {
    1: "src/img/eng_pics/",
    2: "src/img/eng_pics/",
    3: "src/img/eng_pics/",
    4: "src/img/eng_pics/",
    5: "src/img/eng_pics/",
    6: "src/img/eng_pics/",
    7: "src/img/eng_pics/",
    8: "src/img/eng_pics/",
    9: "src/img/eng_pics/",
    10: "src/img/eng_pics/"
}
# ответы
chem_ans = {
    1: "число авогадро",
    2: "углерод",
    3: "ртуть",
    4: "натрий",
    5: "свинец",
    6: "плутоний",
    7: "кремний",
    8: "мышьяк",
    9: "молибден",
    10: "золото"
}

bio_ans = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",
    10: ""
}

math_ans = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",
    10: ""
}

it_ans = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",
    10: ""
}

eng_ans = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",
    10: ""
}
# хранение использованных заданий
used_chem = []
used_bio = []
used_math = []
used_it = []
used_eng = []

# распознавание ответа


def voice_recog(mode):
    r = sr.Recognizer()
    if mode == 1:
        lang = "ru-RU"
    elif mode == 2:
        lang = "en-US"
    with sr.Microphone() as source:
        try:
            print("Говорите...")
            audio_data = r.record(source, duration=7)
            print("Распознаю...")
            text = r.recognize_google(audio_data, language=lang)
            print("Ваш ответ:", text)
            return text
        except sr.UnknownValueError:
            print("Не удалось распознать голос\n")
            return "err"


def chem_task_gen(correct_answers):
    while len(used_chem) != 10:
        num = random.randint(1, 10)
        if num not in used_chem:
            used_chem.append(num)
            img_gen(1, num)
            answer = voice_recog(1)
            if answer == "err":
                continue
            if chem_ans[num] == answer.lower():
                print("Верно!")
                correct_answers += 1
                a = int(input("Продолжить?\n1.Да 2.Нет"))
                if a == 1:
                    continue
                elif a == 2:
                    main(correct_answers)
                    break
            else:
                print("Неверно! Ответ:", chem_ans[num])
                a = int(input("Продолжить?\n1.Да 2.Нет"))
                if a == 1:
                    continue
                elif a == 2:
                    main(correct_answers)
                    break
    main(correct_answers)


def bio_task_gen(correct_answers):
    while len(used_bio) != 10:
        num = random.randint(1, 10)
        if num not in used_bio:
            used_bio.append(num)
            img_gen(2, num)
            answer = voice_recog(1)
            if bio_ans[num] == answer.lower():
                print("Верно!")
                correct_answers += 1
            else:
                print("Неверно! Ответ:", bio_ans[num])
                continue
    main(correct_answers)


def math_task_gen(correct_answers):
    while len(used_math) != 10:
        num = random.randint(1, 10)
        if num not in used_math:
            used_math.append(num)
            img_gen(3, num)
            answer = voice_recog(1)
            if math_ans[num] == answer.lower():
                print("Верно!")
                correct_answers += 1
                a = int(input("Продолжить?\n1.Да 2.Нет"))
                if a == 1:
                    continue
                elif a == 2:
                    main(correct_answers)
                    break
            else:
                print("Неверно! Ответ:", math_ans[num])
                a = int(input("Продолжить?\n1.Да 2.Нет"))
                if a == 1:
                    continue
                elif a == 2:
                    main(correct_answers)
                    break
    main(correct_answers)


def it_task_gen(correct_answers):
    while len(used_it) != 10:
        num = random.randint(1, 10)
        if num not in used_it:
            used_it.append(num)
            img_gen(4, num)
            answer = voice_recog(1)
            if it_ans[num] == answer.lower():
                print("Верно!")
                correct_answers += 1
            else:
                print("Неверно! Ответ:", it_ans[num])
                continue
    main(correct_answers)


def eng_task_gen(correct_answers):
    while len(used_eng) != 10:
        num = random.randint(1, 10)
        if num not in used_eng:
            used_eng.append(num)
            img_gen(5, num)
            answer = voice_recog(2)
            if eng_ans[num] == answer.lower():
                print("Верно!")
                correct_answers += 1
            else:
                print("Неверно! Ответ:", eng_ans[num])
                continue
    main(correct_answers)


def check_results(correct_answers):
    print(
        f"Ваше количество правильных ответов за данную сессию:{correct_answers}")
    cursor.execute(f"SELECT top_result FROM users WHERE nickname='{login}'")
    record = cursor.fetchone()
    if record and record[0] is not None:
        top_result = record[0]
        print(f"Ваш лучший результат: {top_result}")
    else:
        print("У вас пока нет сохраненных результатов.")

    if correct_answers > (top_result if record and record[0] is not None else 0):
        cursor.execute(
            f"UPDATE users SET top_result = {correct_answers} WHERE nickname='{login}'")
        conn.commit()
        print(f"Поздравляем! Вы установили новый рекорд: {correct_answers}")
    main(correct_answers)


def register():
    global login
    global password
    global registred
    q = int(input("Вы зарегестрированы?\n1.Да 2.Нет\n"))
    if q == 1:
        login = input("Логин:")
        password = input("Пароль:")
        cursor.execute(
            f"SELECT * FROM users WHERE nickname = '{login}' AND password = {password}")
        record = cursor.fetchall()
        if record != []:
            print("Вход выполнен успешно!\n")
            registred = True
        else:
            print("Логин или пароль неверны!")
    elif q == 2:
        login = input("Логин:")
        password = input("Пароль:")
        cursor.execute(f"SELECT * FROM users WHERE nickname = '{login}'")
        record = cursor.fetchall()
        if record == []:
            cursor.execute(
                f"INSERT INTO users (nickname,password) VALUES ('{login}', {password})")
            conn.commit()
            res = cursor.execute(
                f"SELECT * FROM users WHERE nickname = '{login}'")
            record = cursor.fetchall()
            if record != []:
                print("Вы зарегистрированы!\n")
                registred = True
        else:
            print("Такой логин уже существует")
    elif q == 99:
        pass
    else:
        print("Неверный ввод!")
        register()


def img_gen(index, num):
    if index == 1:
        pics = chem_pics
    elif index == 2:
        pics = bio_pics
    elif index == 3:
        pics = math_pics
    elif index == 4:
        pics = it_pics
    elif index == 5:
        pics = eng_pics
    img = cv2.imread(pics[num])
    img = cv2.resize(img, (960, 540))
    cv2.imshow("image", img)
    print("Ожидайте...")
    cv2.waitKey(5000)


def main(correct_answers):
    if not registred:
        register()
    t_choice = int(input(
        "Выберите тему:\n1.Химия\n2.Биология\n3.Математика\n4.Информатика\n5.Английский язык\n6.Просмотреть результаты\n0.Выход\n"))
    if t_choice == 1:
        chem_task_gen(correct_answers)
    elif t_choice == 2:
        bio_task_gen(correct_answers)
    elif t_choice == 3:
        math_task_gen(correct_answers)
    elif t_choice == 4:
        it_task_gen(correct_answers)
    elif t_choice == 5:
        eng_task_gen(correct_answers)
    elif t_choice == 6:
        check_results(correct_answers)
    elif t_choice == 0:
        print("Выход...")
        cv2.destroyAllWindows()
        exit(0)
    elif t_choice == 99:
        print(login, password)
    else:
        print("Неверный ввод\n")
        main(correct_answers)


if __name__ == "__main__":
    main(0)
