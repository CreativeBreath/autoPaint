import pyautogui, time


time.sleep(3)
m = pyautogui.click(29,747)

#open paint programme 

pyautogui.typewrite('Paint', 0.5)
time.sleep(1)

pyautogui.typewrite(['enter'])

time.sleep(12)


#maximise the paint programme.......

pyautogui.keyDown('altleft')
pyautogui.press('space')
pyautogui.keyUp('altleft')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')

time.sleep(4)

#draw something 

pyautogui.click(41,175)

distance = 200
x = 0
while distance > 0:
    x = x + 0.2
    pyautogui.dragRel(distance, 0, duration=x)
    distance = distance - 5
    x = x + 0.2
    pyautogui.dragRel(0, distance, duration=x)
    x = x - 0.2
    pyautogui.dragRel(-distance, 0, duration=x)
    distance = distance - 5
    x = x = 0.1
    pyautogui.dragRel(0, -distance, duration=x)


pyautogui.click(250,175)

distance2 = 200


# save the drawing

time.sleep(1)

pyautogui.keyDown('ctrlleft')
pyautogui.press('s')
pyautogui.keyUp('ctrlleft')
time.sleep(2)
pyautogui.typewrite('this is awesome', 1)
time.sleep(1)
pyautogui.press('enter')

