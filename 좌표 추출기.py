#좌표 추출기
import pyautogui
import time

print("--- 📍 마우스 좌표 추출기 ---")
print("5초 뒤에 현재 마우스의 위치를 알려드립니다.")
print("원하는 버튼 위에 마우스를 가만히 올려두세요.")

time.sleep(2)
print(f"현재 마우스 좌표: {pyautogui.position()}")