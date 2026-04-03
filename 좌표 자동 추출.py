from pynput import mouse

print("--- ⏺️ 좌표 녹화 시작 ---")
print("클릭하는 지점의 좌표가 아래에 기록됩니다.")
print("다 끝났으면 이 창에서 Ctrl+C를 눌러 종료하세요.\n")

# 클릭 횟수를 세기 위한 변수
count = 1

def on_click(x, y, button, pressed):
    global count
    if pressed: # 마우스를 누르는 순간만 기록
        print(f"좌표 {count}: ({int(x)}, {int(y)})")
        count += 1

# 마우스 리스너 시작
with mouse.Listener(on_click=on_click) as listener:
    listener.join()