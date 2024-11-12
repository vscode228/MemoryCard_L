from memo___card_layout import (app, layout_card, ib_question, ib_correct, ib_result, rbtn_1, rbtn_2, rbtn_3, rbtn_4, btn_Ok, show_question, show_result)
from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle, choice 
from data import questions

card_width, card_height = 600, 500  
text_wrong = 'Неправильно'
text_correct = 'Правильно'

frm_q = "Are you english?"
frm_ans1 = "Yes"
frm_ans2 = "Si"
frm_ans3 = "Sim"
frm_correct_ans = "Я з України!"

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)
answer = radio_list[0]
wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]

def show_data():
    ''' показывает на экране нужную информацию '''
    ib_question.setText(frm_q)
    ib_correct.setText(frm_correct_ans)
    answer.setText(frm_correct_ans)
    wrong_answer1.setText(frm_ans1)
    wrong_answer2.setText(frm_ans2)
    wrong_answer3.setText(frm_ans3)

def check_result():
    ''' проверка, правильный ли ответ выбран '''
    correct = answer.isChecked()
    if correct:
        ib_result.setText(text_correct)
        show_result()
    else:
        incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
        if incorrect:
            ib_result.setText(text_wrong)
            show_result()

def click_OK(self):
    if btn_Ok.text() != 'Наступне питання':
        check_result()
    else:
        next_question()

def next_question():
    global frm_q, frm_ans1, frm_ans2, frm_ans3, frm_correct_ans
    random_key = choice(list(questions.keys()))
    frm_q = questions[random_key]["question"]
    frm_ans1 = questions[random_key]["wrong_ans1"]
    frm_ans2 = questions[random_key]["wrong_ans2"]
    frm_ans3 = questions[random_key]["wrong_ans3"] 
    frm_correct_ans = questions[random_key]["correct_ans"]
    show_data()
    show_question()
    btn_Ok.setText('Ок')

win_card = QWidget()
win_card.resize(card_height, card_width)
win_card.move(600, 540)
win_card.setWindowTitle('Memory Card')

win_card.setLayout(layout_card)
show_data()
show_question()
btn_Ok.clicked.connect(click_OK)

win_card.show()
app.exec_()
