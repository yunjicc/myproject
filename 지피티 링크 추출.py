"""
AI 인라인 인용 뱃지 추출기
============================
텍스트 옆에 붙는 출처 뱃지/칩만 골라서 추출합니다.
지원: Google AI Overview, ChatGPT, Perplexity, Gemini

설치:
    pip install playwright
    playwright install chromium

사용법:
    python ai_citation_extractor.py
"""

import asyncio
import csv
from datetime import datetime
from urllib.parse import urlparse, unquote

from playwright.async_api import async_playwright


SERVICE_CONFIGS = {
    "google_ai_overview": {
        "name": "Google AI Overview",
        "domains": ["google.com", "google.co.kr"],
        "badge_selectors": [
            "a.BVG0Nb",
            "a[jsname='UWckNb']",
            "cite-chip a",
            "a.B6fmyf",
            "[data-ved] a[ping]",
            "a[class*='source-chip']",
            "[id*='kp-wp-tab'] a[href*='http']:not([href*='google'])",
            "block-component a[href*='http']:not([href*='google'])",
        ],
        "wait_selector": "body",
        "need_login": False,
    },
    "google_gemini": {
        "name": "Google Gemini",
        "domains": ["gemini.google.com"],
        "badge_selectors": [
            "browse-chip a",
            "[class*='browse-chip'] a",
            "a.citation-chip",
            "[class*='citation-chip']",
            "message-content a[href*='http']:not([href*='google'])",
            "model-response a[href*='http']:not([href*='google'])",
        ],
        "wait_selector": "model-response, message-content",
        "need_login": True,
    },
    "chatgpt": {
        "name": "ChatGPT",
        "domains": ["chatgpt.com", "chat.openai.com"],
        "badge_selectors": [
            "a[data-footnote-ref]",
            "sup a[href*='http']",
            "[class*='citation'] a[href*='http']",
            "a[class*='footnote']",
            "[data-testid*='citation'] a",
            ".group\\/citation a",
            "[class*='source-card'] a[href*='http']",
        ],
        "wait_selector": "[data-message-author-role='assistant']",
        "need_login": True,
    },
    "perplexity": {
        "name": "Perplexity",
        "domains": ["perplexity.ai"],
        "badge_selectors": [
            "a[data-testid='citation-link']",
            "a.citation",
            "[class*='CitationButton'] a",
            "[class*='citation-button']",
            "[class*='SourceItem'] a[href*='http']",
            "[class*='source-item'] a[href*='http']",
        ],
        "wait_selector": ".prose, [class*='answer']",
        "need_login": False,
    },
}

EXCLUDE_DOMAINS = {
    "google.com", "google.co.kr", "accounts.google.com",
    "support.google.com", "policies.google.com",
    "chatgpt.com", "chat.openai.com", "openai.com",
    "perplexity.ai", "gemini.google.com",
}


def detect_service(url):
    domain = urlparse(url).netloc.lower().replace("www.", "")
    for key, cfg in SERVICE_CONFIGS.items():
        for d in cfg["domains"]:
            if d in domain:
                return key
    return None


def clean_google_url(url):
    if "/url?q=" in url:
        return unquote(url.split("/url?q=")[1].split("&")[0])
    return url


def is_valid(url):
    if not url or not url.startswith("http"):
        return False
    domain = urlparse(url).netloc.lower().replace("www.", "")
    return not any(excl in domain for excl in EXCLUDE_DOMAINS)


async def extract_badges(url, service_key):
    cfg = SERVICE_CONFIGS[service_key]
    results = []
    seen = set()

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            ),
        )
        page = await context.new_page()

        print(f"\n🌐 [{cfg['name']}] 로딩 중...")
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        except Exception as e:
            print(f"  ❌ 로드 실패: {e}")
            await browser.close()
            return []

        await asyncio.sleep(2)

        # 로그인 감지
        if any(kw in page.url for kw in ["login", "signin", "auth", "accounts"]):
            print("  ⚠️  로그인 필요 — 브라우저에서 로그인 후 Enter 누르세요...")
            input("  ✅ 완료 후 Enter: ")
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(3)

        try:
            await page.wait_for_selector(cfg["wait_selector"], timeout=15000)
        except Exception:
            pass

        await asyncio.sleep(2)

        for selector in cfg["badge_selectors"]:
            try:
                elements = await page.query_selector_all(selector)
                for el in elements:
                    href = clean_google_url(await el.get_attribute("href") or "")
                    text = (await el.inner_text()).strip()[:80]
                    if not text:
                        text = urlparse(href).netloc.replace("www.", "")
                    if href and is_valid(href) and href not in seen:
                        seen.add(href)
                        results.append({
                            "service": cfg["name"],
                            "badge_label": text,
                            "domain": urlparse(href).netloc.replace("www.", ""),
                            "url": href,
                            "source_url": url,
                        })
            except Exception:
                continue

        await browser.close()

    print(f"  → {len(results)}개 인용 추출")
    return results


def save_csv(results, path):
    fields = ["service", "badge_label", "domain", "url", "source_url"]
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(results)
    print(f"\n💾 저장 완료: {path}  ({len(results)}개)")


async def main():
    print("=" * 55)
    print("  AI 인라인 인용 뱃지 추출기")
    print("  Google AI / Gemini / ChatGPT / Perplexity")
    print("=" * 55)
    print("\nURL을 한 줄에 하나씩 입력 → 빈 줄 Enter로 시작\n")

    urls = []
    while True:
        line = input("URL: ").strip()
        if not line:
            break
        urls.append(line)

    if not urls:
        print("❌ URL 없음")
        return

    all_results = []
    for url in urls:
        key = detect_service(url)
        if not key:
            print(f"\n⚠️  지원하지 않는 서비스: {url}")
            continue
        results = await extract_badges(url, key)
        all_results.extend(results)

    if not all_results:
        print("\n추출된 뱃지 없음")
        return

    print("\n" + "=" * 55)
    for r in all_results:
        print(f"  [{r['service']}] {r['badge_label'][:20]:20s} → {r['domain']}")
    print("=" * 55)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_csv(all_results, f"ai_citations_{ts}.csv")


if __name__ == "__main__":
    asyncio.run(main())