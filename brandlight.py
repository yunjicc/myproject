from playwright.sync_api import sync_playwright

def check_connection():
    try:
        with sync_playwright() as p:
            # 9222 포트에 접속 시도
            browser = p.chromium.connect_over_cdp("http://localhost:9222")
            
            # 현재 열려 있는 탭들 확인
            context = browser.contexts[0]
            pages = context.pages
            
            print("✅ 브라우저 연결 성공!")
            print(f"📄 현재 열린 탭 개수: {len(pages)}개")
            
            for i, page in enumerate(pages):
                print(f"   [{i}] 탭 제목: {page.title()}")
                
            browser.close()
    except Exception as e:
        print("❌ 브라우저 연결 실패!")
        print(f"💡 원인: {e}")
        print("💡 팁: 크롬을 완전히 종료한 후 --remote-debugging-port=9222 명령어로 다시 켜세요.")

if __name__ == "__main__":
    check_connection()