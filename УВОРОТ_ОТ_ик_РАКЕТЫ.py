import keyboard
import time
import random
print("пожалуйста не меняйте язык на клавиатуре после запуска программы")
up = input("кнопка на которую назначен отстрелл лтц: ")
b = input("кнопка на которую назначено отключение двигателя: ")
x = input("кнопка для вверх  на самолете: ")
v = input("кнопка для уворота от ракеты: ")
h = input("кнопка на которую назначена смена режима управления самолетом: ")
g = input("кнопка для маневра кобра: ")
j = input("кнопка центрировать мышь джойстик: ")
print("настройка завершина")
while True:
    time.sleep(0.1)
    if keyboard.is_pressed(v):
        keyboard.press(up)
        time.sleep(random.uniform(0.03, 0.10))
        keyboard.press(x)
        time.sleep(random.uniform(0.05, 0.10))
        keyboard.press(b)
        time.sleep(random.uniform(0.06, 0.10))
        keyboard.release(b)
        time.sleep(random.uniform(0.40, 0.60))
        keyboard.release(up)
        keyboard.release(x)
        time.sleep(random.uniform(2.40, 3.30))
        keyboard.press(b)
        time.sleep(random.uniform(0.10, 0.30))
        keyboard.release(b)
        keyboard.press(up)
        time.sleep(random.uniform(0.10, 0.30))
        keyboard.release(up)
    if keyboard.is_pressed(g):
        #1 НАЖАТИЕ
        keyboard.press(h)
        time.sleep(random.uniform(0.04, 0.10))
        keyboard.release(h)
        
        time.sleep(random.uniform(0.04, 0.10))
        #2 НАЖАТИЕ
        keyboard.press(h)
        time.sleep(random.uniform(0.04, 0.10))
        keyboard.release(h)
        
        time.sleep(random.uniform(0.04, 0.10))
        #3 НАЖАТИЕ
        keyboard.press(h)
        time.sleep(random.uniform(0.04, 0.10))
        keyboard.release(h)
        
        time.sleep(random.uniform(0.04, 0.10))
        
        keyboard.press(j)
        time.sleep(random.uniform(0.04, 0.6))
        keyboard.release(j)
        
        keyboard.press(x)
        time.sleep(random.uniform(0.60, 0.80))
        keyboard.release(x)            
        time.sleep(random.uniform(0.10, 0.15))
        
        
        #4 НАЖАТИЕ
        keyboard.press(h)
        time.sleep(random.uniform(0.04, 0.10))
        keyboard.release(h)
        
