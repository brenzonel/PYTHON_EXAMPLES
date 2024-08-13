import win32api, win32con
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0) #Click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)   #Release

def move(x,y):
    win32api.SetCursorPos((x,y))

#click(200,200)
move(200,200)
for i in range(100):
    move(200+i,200)
    time.sleep(0.1)