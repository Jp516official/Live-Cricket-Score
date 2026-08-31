from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.cricbuzz.com/", wait_until="domcontentloaded")
        print(page.title())
        page.screenshot(path="screenshot.png")
        page.wait_for_selector("body > div.bg-cbLightGrayish.dark\:bg-cbBkgDark.wb\:max-w-5xl.wb\:mx-auto.wb\:mt-2.wb\:mb-40.page-wrapper > div.w-full.mb-\[5px\].wb\:block.hidden > div.w-full.text-white.bg-cbGrnCyn.dark\:bg-cbHdrBkgDark.flex.justify-between.items-center.px-3.h-12.relative > div:nth-child(2) > a", timeout=10_000)
        score = page.query_selector("body > div.bg-cbLightGrayish.dark\:bg-cbBkgDark.wb\:max-w-5xl.wb\:mx-auto.wb\:mt-2.wb\:mb-40.page-wrapper > div.w-full.mb-\[5px\].wb\:block.hidden > div.w-full.text-white.bg-cbGrnCyn.dark\:bg-cbHdrBkgDark.flex.justify-between.items-center.px-3.h-12.relative > div:nth-child(2) > a").inner_text()
        page.wait_for_selector("div.carousal-list a")
        live_score = page.locator("div.carousal-list a").first.inner_text(timeout=10_000)
        with open("score.txt", "w") as f:
            f.write(score)
            f.write("\n")
            f.write(live_score)
        browser.close()

if __name__ == "__main__":
    main()