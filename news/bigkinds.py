import time 
import pyautogui
import pyperclip 
import cv2 

def imgClick(filename, t):
        ## fimelname 에 "test.png"와 같이 이미지 파일을 입력하면 클릭하고, t초를 대기하는 함수 

        imgfile = pyautogui.locateOnScreen(filename, confidence=0.9)
        center = pyautogui.center(imgfile)
        pyautogui.moveTo(center) # 이미지의 중간으로 이동하라. 
        pyautogui.click(center)
        time.sleep(t)
        
        
def scroll(line):
        time.sleep(0.5)
        pyautogui.scroll(line)
        time.sleep(0.5)
        

keywords = ["(배당)AND(CJ ENM)", "(배당)"]  ## 검색 

time.sleep(1)

for keyword in keywords :
        #1. 검색어 창을 클릭해서 검색어를 입력 
        imgClick('search_bar.png', 0.2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        pyperclip.copy(keyword)
        pyautogui.hotkey('ctrl', 'v')
        
        #2. 스크롤을 내려서 검색 버튼 클릭 
        while True:
                try:
                        imgClick('search_btn.png', 5)
                        break
                except:
                        scroll(-300)
        

