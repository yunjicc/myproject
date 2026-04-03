import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import os

# 1. 크롤링할 URL 리스트 (여기에 600개를 넣으세요)
urls = [
  "https://gemini.google.com/app/250c77672c49e18a?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/71ae86a351f5979f?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/a07be07459a7f4bb?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/5835e35ff80be79c?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/3aea31347bdd24b1?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/a31c1d0b3ab9a9a2?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/8a82b6a002052e6c?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/78ba500d6fb49434?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/bc3b6663e241f86d?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/0eecb0cd9fbd91f8?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/36a1e02f02884c5b?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/e6c6774832afa250?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/63ec4d071758b973?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/d82ca71bc3039eaa?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/49795a0c9328ae87?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/87c2041bbb52db74?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/33c9e1801b906373?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/0b4967dcd2b52eda?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/737872b2832557b4?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/2dfdebb684536b50?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/57740b798a24499c?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/2660e1be2d3ee59f?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/5b05a0591a073b7a?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/8b6be59b66bb0401?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/b191569703deaf43?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/56cb427b547e743b?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/906b1449075fec41?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/758b8e92a6069176?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/53a2fef6194ac368?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/38544e5aaeed1220?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/63ad437f5ae3d073?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/f4412aced042cd07?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/07cf51d5a4d9db8e?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/c889716b8e8550be?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/b746959b1b5def2b?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/c7b77f4d20f66759?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/442eaf5df5ea6cf1?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/5b0831e5d2195fab?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/a389025b06c14602?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/f19704fe6e3c1fd9?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/f73c9d1fa92411ee?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/82c01d4657f12d36?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/34627388cec1bea0?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/20a43c379d5a4393?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/ced196df9be25a40?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/f726c895c7d9e013?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/5ddcd0b2c9238f55?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/a008bb2e020d1845?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/b735f5e7633c5213?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/0aec76219b9fecf5?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/216fa6432ee07239?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/62be5e878bb2df91?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/38c77956cb286d5d?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/3d5120ae7c11fb3f?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/87cb556212a2211f?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/6b20a7f1c9fbae92?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/576e25fd66f10dbc?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/4063442f22d0b156?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/69ee645696579c10?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/9ab85f4f210d8e1c?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/1fc582e5c918b721?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/4a972f9f8f275eaf?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/a123d34fcb13d3d5?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/a0aa071e6d5b6840?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/e7a94b6d71c1693c?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/2ff75f68f8a90ad3?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/cb85e0cac652b065?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/482bc0a21f6561a3?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/e65590df043e036e?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/8ace4258b22fef20?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/d2cab5330afb2eb8?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/39b11ad745828d1c?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/bdd2e8eea9fcd913?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/9fe91897fa9b9913?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/ed7262c8f1de8f55?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/9965e57661ba8b6a?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/4b154b515cc0b5a2?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/af057a935576b935?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/040b8071dd46f1f0?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/81296b68d0f9614e?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1",
  "https://gemini.google.com/app/f020d9533dbfb0bb?hl=ko&hl=ko&gl=KR&m=0&pc=bard&cm=2&src=1"
]

async def scrape_chatgpt_links(url_list):
    async with async_playwright() as p:
        # 브라우저 실행 (600개니까 효율을 위해 headless=True 권장)
        # 만약 차단이 걱정되면 headless=False로 눈으로 보면서 하세요.
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        results = []
        output_file = "chatgpt_backup_results.xlsx"

        for i, url in enumerate(url_list):
            page = None # 페이지 변수 초기화
            content = ""
            raw_text = ""

            try:
                # 1. 매번 새로운 페이지(탭) 생성
                page = await context.new_page()
                print(f"[{i+1}/{len(url_list)}] 접속 시도: {url}") 

                # 2. 접속 시도 (타임아웃 60초)
                await page.goto(url, wait_until="domcontentloaded", timeout=60000)
                
                # 3. 답변 로딩을 위한 넉넉한 대기 (Perplexity 등 대응)
                await asyncio.sleep(7)
                
                # 🎯 찾으신 <span> 태그와 출처 관련 요소를 실시간 삭제
                await page.evaluate("""() => {
                    // 1. 클래스명에 'max-w-[15ch]'가 포함된 모든 span 요소를 찾아 삭제
                    // 속성 선택자([]) 안에 문자열을 넣는 방식이 가장 안전합니다.
                    const sources = document.querySelectorAll('span[class*="max-w-[15ch]"]');
                    sources.forEach(el => el.remove());

                    // 2. 추가적인 출처 태그 및 하단 쓰레기 데이터 정리
                    const trashSelectors = ['cite', '.citation', 'a[data-index]', 'svg', '.mt-4.flex.flex-col'];
                    trashSelectors.forEach(selector => {
                        const elements = document.querySelectorAll(selector);
                        elements.forEach(el => el.remove());
                    });
                }""")

                # 제목과 대화 내용 추출
                title = await page.title()
                # 공유 페이지의 메인 텍스트 영역 추출
                content_node = await page.query_selector('.markdown, .prose')

                if content_node:
                    # 정밀 클래스가 찾아진 경우
                    raw_text = await content_node.inner_text()
                else:
                    # 클래스를 못 찾은 경우 전체 영역('main' 또는 'body') 긁기
                    raw_text = await page.inner_text('main')


                results.append({
                    "번호": i + 1,
                    "URL": url,
                    "제목": title,
                    "내용": raw_text
                })

                # [중요] 10개마다 중간 저장 (혹시 모를 오류 대비)
                if (i + 1) % 10 == 0:
                    pd.DataFrame(results).to_excel(output_file, index=False)
                    print(f" 중간 저장 완료: {output_file}")

            except Exception as e:
                print(f"❌ {url}에서 에러 발생: {e}")
                results.append({"번호": i + 1, "URL": url, "제목": "에러", "내용": str(e)})

            finally:
                # 8. 반드시 페이지 닫기 (이게 없으면 600개 돌릴 때 컴 터집니다)
                if page:
                    await page.close()
                # 봇 감지 방지를 위한 짧은 휴식
                await asyncio.sleep(2)

        # 최종 저장
        df = pd.DataFrame(results)
        df.to_excel("final_chatgpt_results4.xlsx", index=False)
        await browser.close()
        print("\n✨ 모든 작업이 완료되었습니다! 'final_chatgpt_results.xlsx'를 확인하세요.")

if __name__ == "__main__":
    asyncio.run(scrape_chatgpt_links(urls))