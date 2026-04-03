import os

def rename_global_files():
    # 1. Downloads 폴더 경로 설정 (사용자 계정에 맞게 자동 설정)
    download_path = os.path.join(os.path.expanduser(r"C:\\Users\\yunji\\Downloads"), "")
    
    # 2. 폴더 내 파일 목록 가져오기
    files = os.listdir(download_path)
    
    count = 0
    print(f"조회 시작: {download_path}\n" + "-"*30)

    for filename in files:
        # 3. "Global"로 시작하는 파일 찾기 (대소문자 무시하려면 .lower() 사용 가능)
        if filename.startswith("['Brazil']"):
            # 새 파일명 생성
            
            ###### 글자 옮기기 ######
            # # 1. 언더바(_)를 기준으로 문자열을 분리합니다.
            # name, ext = os.path.splitext(filename)
            # parts = name.split('_')

            # # 2. 맨 마지막 요소('_realme' 부분)를 꺼냅니다 (pop).
            # last_part = parts.pop()

            # # 3. 세 번째 언더바 앞(인덱스 3번 자리)에 삽입합니다.
            # # ['Global', 'Monthly', 'by Model', 'Brand', 'General'] 상태에서 
            # # 3번 인덱스인 'Brand' 자리에 'realme'가 들어갑니다.
            # parts.insert(3, last_part)

            # # 4. 다시 언더바로 합칩니다.
            # new_filename = "_".join(parts) + ext
            
            ###### 글자 교체 ######
            new_filename = filename.replace("['Brazil']", "Brazil", 1)
            old_file = os.path.join(download_path, filename)
            new_file = os.path.join(download_path, new_filename)

            try:
                # 4. 파일 이름 변경 실행
                os.rename(old_file, new_file)
                print(f"[성공] {filename} -> {new_filename}")
                count += 1
            except Exception as e:
                print(f"[오류] {filename} 변경 실패: {e}")

    print("-" * 30)
    print(f"총 {count}개의 파일명이 변경되었습니다.")

if __name__ == "__main__":
    rename_global_files()