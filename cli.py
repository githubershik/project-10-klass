import random
import cv2
import speech_recognition as sr
import time

#######картинки

chem_pics = {
    1:"src/img/chem_pics/dog.jpg",
    2:"src/img/chem_pics/carbon.jpg",
    3:"src/img/chem_pics/Mercury.png",
    4:"src/img/chem_pics/natrii.png",
    5:"src/img/chem_pics/plumbum.jpg",
    6:"src/img/chem_pics/plutonium.jpg",
    7:"src/img/chem_pics/silicium.jpg",
    8:"src/img/chem_pics/mishyak.webp"
}

biology_pics = {

}

math_pics = {

}

it_pics = {

}

eng_pics = {

}
####### ответы
chem_ans = {
    1:"сабака",
    2:"углерод",
    3:"ртуть",
    4:"натрий",
    5:"свинец",
    6:"плутоний",
    7:"кремний",
    8:"мышьяк"
}

biology_ans = {

}

math_ans = {

}

it_ans = {

}
########хранение использованных заданий
used_chem = []
used_bio = []
used_math = []
used_it = []
used_eng = []

#########распознавание ответа
def voice_recog(mode):
    r = sr.Recognizer()
    if mode == 1:
        lang = "ru-RU"
    elif mode == 2:
        lang = "en-US"
    with sr.Microphone() as source:
        try:
            print("Говорите...")
            audio_data = r.record(source,duration=7)
            print("Распознаю...")
            text = r.recognize_google(audio_data, language=lang)
            print("Ваш ответ:",text)
            return text
        except sr.UnknownValueError:
            print("Не удалось распознать голос")

def chem_task_gen():
    while len(used_chem) != 10:
        num = random.randint(1, 8)
        if num not in used_chem:
            used_chem.append(num)
            img_gen(1,num)
            answer = voice_recog(1)
            if chem_ans[num] == answer.lower():
                print("Верно!")
            else:
                print("Неверно! Ответ:", chem_ans[num])
                break
        

def bio_task_gen():
    pass

def math_task_gen():
    pass

def it_task_gen():
    pass

def eng_task_gen():
    pass
    
def img_gen(index,num):
    if index == 1:
        pics = chem_pics
    elif index == 2:
        pics = biology_pics
    elif index == 3:
        pics = math_pics
    elif index == 4:
        pics = it_pics
    elif index == 5:
        pics = eng_pics
    img = cv2.imread(pics[num])
    img = cv2.resize(img,(960,540))
    cv2.imshow("image",img)
    print("Ожидайте...")
    cv2.waitKey(5000)

def main():
    t_choice = int(input("Выберите тему:\n1.Химия\n2.Биология\n3.Математика\n4.Информатика\n5.Английский язык\n"))
    if t_choice == 1:
        chem_task_gen()
    elif t_choice == 2:
        bio_task_gen()
    elif t_choice == 3:
        math_task_gen()
    elif t_choice == 4:
        it_task_gen()
    elif t_choice == 5:
        eng_task_gen()
    else:
        print("Такой темы нет")
        return 0
main()