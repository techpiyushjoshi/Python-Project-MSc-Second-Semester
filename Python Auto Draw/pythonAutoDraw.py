#Name : Piyush Joshi
#Topic: Python Auto Draw (Square Maze using pyautogui module)

#Instructions
# Open the Paint Application 
# Run the Program then switch over to the paint screen the cursor will form maze automatically

#----Code-----

#Importing modules
import pyautogui
import time

# Drawing a spiral drawing
time.sleep(3)
distance =400

while distance>0:
    pyautogui.dragRel(distance,0,1, button = "left")
    # moving the length = distance on x axis, 0 movement on y axis, using left mousebutton
    distance = distance -20
    pyautogui.dragRel(0,distance,1,button="left")
    pyautogui.dragRel(-distance,0,1,button="left")
    distance = distance -20
    pyautogui.dragRel(0,-distance,1,button="left") 
    time.sleep(2)