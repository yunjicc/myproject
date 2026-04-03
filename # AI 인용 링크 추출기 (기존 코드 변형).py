import asyncio
import pandas as pd
from playwright.async_api import async_playwright

urls = [
    "https://www.google.com/search?q=%EC%B2%98%EC%9D%8C+%EA%B8%88+%ED%88%AC%EC%9E%90%EB%A5%BC+%EC%8B%9C%EC%9E%91%ED%95%98%EB%A0%A4%EB%8A%94%EB%8D%B0+%EC%8B%A0%ED%95%9C%EC%9D%80%ED%96%89+%EA%B3%A8%EB%93%9C%EB%A6%AC%EC%8A%88%EA%B0%80+%EC%A0%81%ED%95%A9%ED%95%9C%EA%B0%80%EC%9A%94+"
]

async def scrape_exact_citations(url_list):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True) # 눈으로 확인하려면 False
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )
        
        results = []

        for i, url in enumerate(url_list):
            page = await context.new_page()
            print(f"[{i+1}/{len(url_list)}] 분석 중: {url}")

            try:
                await page.goto(url, wait_until="networkidle", timeout=60000)
                await asyncio.sleep(10) # 답변 생성 대기

                # 🎯 이미지에서 확인된 클래스 기반 추출 로직
                citation_links = await page.evaluate("""() => {
                    const links = [];
                    
                    // 1. 이미지에 나온 'button.rBl3me' 형태나 그 안의 링크를 모두 찾습니다.
                    // Perplexity는 버튼을 누르면 레이어가 뜨거나, 버튼 자체가 링크를 포함합니다.
                    const elements = document.querySelectorAll('button, a, [role="button"]');
                    
                    elements.forEach(el => {
                        // 클래스명에 이미지에서 본 'rBl3me'나 'pjvauc' 등이 포함되어 있는지 확인
                        const className = el.className || "";
                        const isCitation = /rBl3me|pjvauc|lWyTpf/.test(typeof className === 'string' ? className : "");
                        
                        // 직접적인 href가 있는 경우
                        if (el.href && el.href.startsWith('http')) {
                             links.push(el.href);
                        } 
                        // 버튼 안에 링크가 숨겨진 경우 (data-url 등)
                        else if (isCitation && el.getAttribute('data-url')) {
                             links.append(el.getAttribute('data-url'));
                        }
                    });

                    // 2. 불필요한 서비스 링크 제외 필터링
                    const excludeList = [
                        'google.com/policies', 'support.google', 'perplexity.ai', 
                        'facebook.com', 'twitter.com', 'apple.com'
                    ];

                    return [...new Set(links)].filter(link => 
                        !excludeList.some(ex => link.includes(ex))
                    );
                }""")

                print(f"   ✅ {len(citation_links)}개의 실제 인용 링크를 찾았습니다.")

                results.append({
                    "번호": i + 1,
                    "원본URL": url,
                    "인용링크": "\n".join(citation_links)
                })

            except Exception as e:
                print(f"   ❌ 에러: {e}")
                results.append({"번호": i + 1, "원본URL": url, "인용링크": "추출 실패"})
            finally:
                await page.close()

        df = pd.DataFrame(results)
        df.to_excel("final_precise_citations.xlsx", index=False)
        await browser.close()
        print("\n✨ 작업 완료! 'final_precise_citations.xlsx'를 확인하세요.")

if __name__ == "__main__":
    asyncio.run(scrape_exact_citations(urls))