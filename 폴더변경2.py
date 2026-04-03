import os
import time

# --- 설정 ---
# country_list = ["us", "uk", "ae", "es", "kr", "jp", "it", "id", "in", "de", "fr", "br", "au"]
country_list = ["us","kr"]
# country_list = ["us","uk","kr"]
current_index = 0
DOWNLOAD_PATH = r"C:\Users\yunji\Downloads"
# date_str = ["260308", "260301","260222","260215","260208", "260201","260125","260118"]
date_str = "260329"
print(f"--- 🚀 크롬 다운로드 감시 모드 시작 ---\n")
print(f"📍 현재 대기 국가: [{country_list[0].upper()}]")

# 현재 폴더 상태 스캔 (기존에 있던 파일들은 무시하기 위함)
last_files = set(os.listdir(DOWNLOAD_PATH))

try:
    while current_index < len(country_list):
        current_files = set(os.listdir(DOWNLOAD_PATH))
        new_files = current_files - last_files
        
        if new_files:
            for file_name in new_files:
                # 1. 크롬 임시 파일(.crdownload)은 절대 건드리지 않고 기다림
                if file_name.endswith(".crdownload") or file_name.endswith(".tmp"):
                    continue
                
                # 2. 임시 파일이 사라지고 진짜 파일(예: report.json)이 나타나면 실행
                time.sleep(1) # 파일 쓰기가 완전히 끝날 때까지 1초만 더 대기
                
                old_path = os.path.join(DOWNLOAD_PATH, file_name)
                
                if file_name.startswith("queries"):
                    # 가끔 다운로드 완료 후에도 OS가 파일을 잠그고 있을 수 있어 예외처리
                    try:
                        # date = date_str[current_index]
                        new_filename = f"Airpods-{date_str}-{country_list[current_index]}.json"
                        new_path = os.path.join(DOWNLOAD_PATH, new_filename)
                        
                        os.rename(old_path, new_path)
                        print(f"✅ [{country_list[0].upper()}] 이름 변경 성공!\t\t{file_name} -> {new_filename}")
                        
                        current_index += 1
                        # 현재 폴더 상태를 다시 스캔해서 'last_files' 업데이트
                        last_files = set(os.listdir(DOWNLOAD_PATH))
                        
                        if current_index < len(country_list):
                            print(f"\n👉 다음 대기: [{country_list[current_index].upper()}]")
                        break
                    except PermissionError:
                        # 파일이 아직 브라우저에 의해 사용 중이면 다음 루프에서 재시도
                        continue
                    except Exception as e:
                        print(f"❌ 오류 발생: {e}")
                else:
                    print(f"queries파일 아님: {file_name}")
                    continue
        
        time.sleep(0.5) # 0.5초마다 아주 빠르게 폴더를 훑습니다.

except KeyboardInterrupt:
    print("\n🛑 중단되었습니다.")