.model small
.stack 100h
.data

how_to_do db 'welcome to history test: to answer the questions press a for answer a, \n b for answer b, c for answer c or d for answer d \n$'
grade db 0

ahadot db 0
asarot db 1
meot db 0
number db ?
your_grade_message db 'Your grade is: $'
congrats_message db '\n Congrats! $'
correct db 'correct! \n$'
not_correct db '\n false! the answer was: $'
answer db 'enter your answer: $'

question1 db 'When did the Christian era begin? \n$'
answers_q1 db 'a.in the creation of the world \n b.at the birth of jesus \n c.when moses recieved the torah \n d.when jesus died \n $'
correct_answer_q1 db 'b.at the birth of jesus \n$'


question2 db 'What had in the city of Polis? \n$'
answers_q2 db 'a. A king \n b. Army \n c. Court \n d. All the asnwers are correct \n$'
correct_answer_q2 db 'd. All the asnwers are correct \n$'

question3 db 'What is the rule of the people? \n$'
answers_q3 db 'a. A government where the one who rules only decides \n b. A goverment where the people who rules \n c. A goverment where the goverment decides \n d. A goverment where everyone decides \n$'
correct_answer_q3 db 'b. A goverment where the people who rules \n$'

question4 db 'What is the principle of equality? \n$'
answers_q4 db 'a. Everyone has one vote \n b. Everyone has two votes \n c. The ruler has two votes \n d. The minister of military has two votes \n$'
correct_answer_q4 db 'a. Everyone has one vote \n$'

question5 db 'Who are the participants of "the civil assembly"? \n$'
answers_q5 db 'a. Israeli citizens aged 30 and over  \n b. Sparta citizens aged 18 and over \n c. Sparta citizens aged 30 and over \n d. Athens citizens aged 30 and over \n$'
correct_answer_q5 db 'c. Sparta citizens aged 30 and over \n$'

question6 db 'Which of the following was part of \n the education system in Sparta? \n$'
answers_q6 db 'a. Ecourage them to steal food  \n b. To study every day from 8 at morning until 3 in the noon \n c. To serve in the army fron the age of 18 until age of 60 \n d. To draft disabled people into the army \n$'
correct_answer_q6 db 'a. Ecourage them to steal food \n$'

question7 db 'Who was the goddess of the hunt and the moon? \n$'
answers_q7 db 'a. Afrodita  \n b. Athena \n c. Artemis \n d. Hera \n$'
correct_answer_q7 db 'c. Artemis \n$'

question8 db 'What is the mythology? \n$'
answers_q8 db 'a. Old Testament  \n b. Ancient Greek stories \n c. Ancient Roman stories \n d. Noah stories \n$'
correct_answer_q8 db 'b. Ancient Greek stories \n$'

question9 db 'What is the Acropolis? \n$'
answers_q9 db 'a. Synagogue \n b. Church \n c. A high place where the religious and \n public places in Rome are concentrated \n d. A high place where the religious and \n public places in Greece are concentrated \n$'
correct_answer_q9 db 'd. A high place where the religious and \n public places in Greece are concentrated \n$'

question10 db 'What are the three classes? \n$'
answers_q10 db 'a. The upper class - the citizens, the middle class - the peasants,\n the lower class - the slaves \n b. The upper class - the ruler, the middle class - the citizens,\n the lower class - the peasants and slaves \n c. The upper class - the ruler, the middle class - the \n citizens and peasants, the lower class - the slaves \n d. The upper class - the ruler, the middle class - the \n minister of the army,\n the lower class - the citizens, peasants and slaves \n$'
correct_answer_q10 db 'a. The upper class - the citizens, the middle class - the peasants,\n the lower class - the slaves \n$'

question11 db 'What is a legion? \n$'
answers_q11 db 'a. Synonymous with a football league in ancient Rome \n b. Synonymous with a football league in ancient Greece \n c. A military unit of the Roman army \n d. A military unit of the Greek army \n$'
correct_answer_q11 db 'c. A military unit of the Roman army \n$'

question12 db 'What does the word "imperium" mean? \n$'
answers_q12 db 'a. The authority to rule over countries \n b. The authority to commant the army \n c. The authority to be part of the decisions of the people \n d. The authority to be a citizen of the country \n$'
correct_answer_q12 db 'b. The authority to commant the army \n$'

question13 db 'Who is it hordus? \n$'
answers_q13 db 'a. The king of Greece from 37 before \n the Common Era until his death \n b. The king of Yehuda from 38 before \n the Common Era until his death \n c. The king of Yehuda from 37 before \n the Common Era until his death \n d. The king of Yehuda from 37 according to \n the Christian counting of years until his death \n$'
correct_answer_q13 db 'c. The king of Yehuda from 37 before \n the Common Era until his death \n$'

question14 db 'Who were the philosophers? \n$'
answers_q14 db 'a. People who explored the world around them \n b. People who studied the human brain \n c. People who studied human behavior \n d. Answers a and c are correct \n$'
correct_answer_q14 db 'd. Answers a and c are correct \n$'

question15 db 'Which of hte following is a written source? \n$'
answers_q15 db 'a. A draw \n b. A statue \n c. A letter \n d. All the answers are correct \n$'
correct_answer_q15 db 'c. A letter \n$'

question16 db 'What is the current year according to the jewish count? \n$'
answers_q16 db 'a. 5782 \n b. 5783 \n c. 5784 \n d. 5785 \n$'
correct_answer_q16 db 'b. 5783 \n$'

question17 db 'What is the democracy? \n$'
answers_q17 db 'a. A government where only the ruler makes decisions \n related to the state \n b. A government where the ruler and the people jointly \n decide decisions related to the state \n c. A government where only the people make decisions \n related to the state \n d. A government where only the courts decide decisions \n related to the state \n$'
correct_answer_q17 db 'c. A government where only the people make decisions \n related to the state \n$'

question18 db 'What does the regime in Sparta consist of? \n$'
answers_q18 db 'a. Knesset, Council of Elders and Citizens meeting \n b. Municipal Council and Citizens meeting \n c. Monarchy and city council \n d. Monarchy, Council of Elders and Citizens meeting  \n$'
correct_answer_q18 db 'a. A government where only the ruler makes decisions \n related to the state \n$'

question19 db 'What does the monarchy consist of? \n$'
answers_q19 db 'a. Of one king \n b. Of two kings \n c. Two kings who were army ministers and  \n priests to the gods  \n d.One king who was army ministers and  \n priests to the gods  \n$'
correct_answer_q19 db 'c. Two kings who were army ministers and  \n priests to the gods \n$'

question20 db 'How many greek gods were there? \n$'
answers_q20 db 'a. 10 \n b. 1 \n c.  5 \n d. 12 \n$'
correct_answer_q20 db 'd. 12 \n$'

ZERO dw 0
random_number db ?
ADDR EQU 1132
ip_addr dw ?
counter_q1 db 0
counter_q2 db 0
counter_q3 db 0
counter_q4 db 0
counter_q5 db 0
counter_q6 db 0
counter_q7 db 0
counter_q8 db 0
counter_q9 db 0
counter_q10 db 0
counter_q11 db 0
counter_q12 db 0
counter_q13 db 0
counter_q14 db 0
counter_q15 db 0
counter_q16 db 0
counter_q17 db 0
counter_q18 db 0
counter_q19 db 0
counter_q20 db 0
numbers_counter db 0
flag db 0

waiting dw 0
.code

mov ax,@data
mov ds, ax

call welcome_message

start:
call Random

search:
mov waiting, 0
mov flag ,0
call wait
call cleaning
call search_for_questions
cmp flag,1
je start
call check_return_to_main

; here your program ends

mov ah,4ch
mov al,0
int 21h

welcome_message:
lea dx, how_to_do
mov ah, 09h
int 21h
ret


Random:
mov  ah, 00h                        
int  1ah                                 
mov  ax, dx
xor  dx, dx
mov  cx, 20
div  cx
inc dx
ret

search_for_questions:
cmp random_number, 1
je check_question_number_1
cmp random_number, 2
je check_question_number_2
cmp random_number, 3
je check_question_number_3
cmp random_number, 4
je check_question_number_4
cmp random_number, 5
je check_question_number_5
cmp random_number, 6
je check_question_number_6
cmp random_number, 7
je check_question_number_7
cmp random_number, 8
je check_question_number_8
cmp random_number, 9
je check_question_number_9
cmp random_number, 10
je check_question_number_10
cmp random_number, 11
je check_question_number_11
cmp random_number, 12
je check_question_number_12
cmp random_number, 13
je check_question_number_13
cmp random_number, 14
je check_question_number_14
cmp random_number, 15
je check_question_number_15
cmp random_number, 16
je check_question_number_16
cmp random_number, 17
je check_question_number_17
cmp random_number, 18
je check_question_number_18
cmp random_number, 19
je check_question_number_19
cmp random_number, 20
je check_question_number_20


check_question_number_1:
inc counter_q1
cmp counter_q1, 1
jne restart

calling_question_1:
inc numbers_counter
call question_number_1
jmp returning

check_question_number_2:
inc counter_q2
cmp counter_q2, 1
jne restart

calling_question_2:
inc numbers_counter
call question_number_2
jmp returning

check_question_number_3:
inc counter_q3
cmp counter_q3, 1
jne restart

calling_question_3:
inc numbers_counter
call question_number_3
jmp returning

check_question_number_4:
inc counter_q4
cmp counter_q4, 1
jne restart

calling_question_4:
inc numbers_counter
call question_number_4
jmp returning

check_question_number_5:
inc counter_q5
cmp counter_q5, 1
jne restart

calling_question_5:
inc numbers_counter
call question_number_5
jmp returning

check_question_number_6:
inc counter_q6
cmp counter_q6, 1
jne restart

calling_question_6:
inc numbers_counter
jmp question_number_6
jmp returning

check_question_number_7:
inc counter_q7
cmp counter_q7, 1
jne restart

calling_question_7:
inc numbers_counter
call question_number_7
jmp returning 

check_question_number_8:
inc counter_q8
cmp counter_q8, 1
jne restart

calling_question_8:
inc numbers_counter
call question_number_8
jmp returning

check_question_number_9:
inc counter_q9
cmp counter_q9, 1
jne restart

calling_question_9:
inc numbers_counter
call question_number_9
jmp returning

check_question_number_10:
inc counter_q10
cmp counter_q10, 1
jne restart

calling_question_10:
inc numbers_counter
call question_number_10
jmp returning

check_question_number_11:
inc counter_q11
cmp counter_q11, 1
jne restart

calling_question_11:
inc numbers_counter
call question_number_11
jmp returning

check_question_number_12:
inc counter_q12
cmp counter_q12, 1
jne restart

calling_question_12:
inc numbers_counter
call question_number_12
jmp returning

check_question_number_13:
inc counter_q13
cmp counter_q13, 1
jne restart

calling_question_13:
inc numbers_counter
call question_number_13
jmp returning

check_question_number_14:
inc counter_q14
cmp counter_q14, 1
jne restart

calling_question_14:
inc numbers_counter
call question_number_14
jmp returning

check_question_number_15:
inc counter_q15
cmp counter_q15, 1
jne restart

calling_question_15:
inc numbers_counter
call question_number_15
jmp returning

check_question_number_16:
inc counter_q16
cmp counter_q16, 1
jne restart

calling_question_16:
inc numbers_counter
call question_number_16
jmp returning

check_question_number_17:
inc counter_q17
cmp counter_q17, 1
jne restart

calling_question_17:
inc numbers_counter
call question_number_17
jmp returning

check_question_number_18:
inc counter_q18
cmp counter_q18, 1
jne restart

calling_question_18:
inc numbers_counter
call question_number_18
jmp returning

check_question_number_19:
inc counter_q19
cmp counter_q19, 1
jne restart

calling_question_19:
inc numbers_counter
call question_number_19
jmp returning

check_question_number_20:
inc counter_q20
cmp counter_q20, 1
jne restart

calling_question_20:
inc numbers_counter
call question_number_20
jmp returning

restart:
mov flag, 1

returning:
ret


questions:
question_number_1:
lea dx, question1
mov ah, 09h
int 21h

lea dx, answers_q1
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h

cmp al, 98 
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q1 
mov ah, 09h
int 21h
ret

question_number_2:
lea dx, question2
mov ah, 09h
int 21h

lea dx, answers_q2
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 100
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q2
mov ah, 09h
int 21h
ret

question_number_3:
lea dx, question3
mov ah, 09h
int 21h

lea dx, answers_q3
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 98
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q3
mov ah, 09h
int 21h
ret

question_number_4:
lea dx, question4
mov ah, 09h
int 21h

lea dx, answers_q4
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 97
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q4
mov ah, 09h
int 21h
ret

question_number_5:
lea dx, question5
mov ah, 09h
int 21h

lea dx, answers_q5
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 99
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q5
mov ah, 09h
int 21h
ret


question_number_6:
lea dx, question6
mov ah, 09h
int 21h

lea dx, answers_q6
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 97 
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q6
mov ah, 09h
int 21h
ret

question_number_7:
lea dx, question7
mov ah, 09h
int 21h

lea dx, answers_q7
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 99 
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q7
mov ah, 09h
int 21h
ret

question_number_8:
lea dx, question8
mov ah, 09h
int 21h

lea dx, answers_q8
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 98 
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q8
mov ah, 09h
int 21h
ret

question_number_9:
lea dx, question9
mov ah, 09h
int 21h

lea dx, answers_q9
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 100 
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q9
mov ah, 09h
int 21h
ret

question_number_10:
lea dx, question10
mov ah, 09h
int 21h

lea dx, answers_q10
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 97
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q10
mov ah, 09h
int 21h
ret

question_number_11:
lea dx, question11
mov ah, 09h
int 21h

lea dx, answers_q11
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 99
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q11
mov ah, 09h
int 21h
ret


question_number_12:
lea dx, question12
mov ah, 09h
int 21h

lea dx, answers_q12
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 98 
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q12
mov ah, 09h
int 21h
ret

question_number_13:
lea dx, question13
mov ah, 09h
int 21h

lea dx, answers_q13
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 99
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q13 
mov ah, 09h
int 21h
ret

question_number_14:
lea dx, question14
mov ah, 09h
int 21h

lea dx, answers_q14
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 100
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q14
mov ah, 09h
int 21h
ret

question_number_15:
lea dx, question15
mov ah, 09h
int 21h

lea dx, answers_q15
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 99
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q15
mov ah, 09h
int 21h
ret

question_number_16:
lea dx, question16
mov ah, 09h
int 21h

lea dx, answers_q16
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 98 
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q16
mov ah, 09h
int 21h
ret

question_number_17:
lea dx, question17
mov ah, 09h
int 21h

lea dx, answers_q17
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 99 
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q17
mov ah, 09h
int 21h
ret

question_number_18:
lea dx, question18
mov ah, 09h
int 21h

lea dx, answers_q18
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 97
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q18
mov ah, 09h
int 21h
ret

question_number_19:
lea dx, question19
mov ah, 09h
int 21h

lea dx, answers_q19
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 99
je you_right
lea dx, not_correct
mov ah, 09h
int 21h
lea dx, correct_answer_q19
mov ah, 09h
int 21h
ret

question_number_20:
lea dx, question20
mov ah, 09h
int 21h

lea dx, answers_q20
mov ah, 09h
int 21h

lea dx, answer
mov ah, 09h
int 21h

mov ah, 01h
int 21h


cmp al, 100
je you_right
lea dx, not_correct 
mov ah, 09h
int 21h
lea dx, correct_answer_q20
mov ah, 09h
int 21h
ret

you_right:
call right
ret

right: 
lea dx, correct
mov ah, 09h
int 21h
add grade, 5
ret

ascii_grade:
mov al, grade
mov ahadot, al
mov number, al
call divisor_for_ahadot
cmp ahadot, 10
je grade_100
mov al, ahadot
sub number, al
call divisor_for_asarot
add asarot, '0'
add ahadot, '0'

lea dx, your_grade_message
mov ah, 09h
int 21h

mov dl, asarot
mov ah, 02h
int 21h

mov dl, ahadot
mov ah, 02h
int 21h

lea dx, congrats_message
mov ah, 09h
int 21h
ret

grade_100:
mov asarot, 0
mov ahadot, 1
mov meot, 0
add ahadot, '0'
add asarot, '0'
add meot, '0'

lea dx, your_grade_message
mov ah, 09h
int 21h

mov dl, ahadot
mov ah, 02h
int 21h

mov dl, asarot
mov ah, 02h
int 21h

mov dl, meot
mov ah, 02h
int 21h

lea dx, congrats_message
mov ah, 09h
int 21h
ret

divisor_for_ahadot:
sub ahadot, 10
cmp ahadot, 10
ja divisor_for_ahadot
ret

divisor_for_asarot:
inc asarot
sub number, 10
cmp number, 10
jne divisor_for_asarot
ret

cleaning:
mov ah, 06h
mov al, 0h
mov bh, 07
xor cx, cx
mov dh, 24
mov dl, 79
int 10h
ret

check_return_to_main:
cmp numbers_counter, 20
jnb return_grade

return_to_main:
push ip_addr
ret

return_grade:
call cleaning
call ascii_grade
ret

wait:
inc waiting
cmp waiting, 20000
jbe wait
ret



; here your sub-programs end
end
