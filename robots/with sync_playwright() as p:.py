with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://playwright.dev')
    image_element = page.locator('.main-wrapper img').nth(0)
    image_b64 = image_element.evaluate("""element => {
      var cnv = document.createElement('canvas');
      cnv.width = element.naturalWidth;
      cnv.height = element.naturalHeight;
      cnv.getContext('2d').drawImage(element, 0, 0, element.naturalWidth, element.naturalHeight);
      return cnv.toDataURL().substring(22)
    }""")
    with open('playwright.png', 'wb') as f:
        f.write(base64.b64decode(image_b64))
        
    browser.close()
    import base64
from playwright.sync_api import sync_playwright



    r1 = requests.get("https://thispersondoesnotexist.com/image")
    r1.raise_for_status()

    print(r1.status_code, r1.reason)

    tts_url = 'https://thispersondoesnotexist.com/image'

    r2 = requests.get(tts_url, timeout=100, cookies=r1.cookies)
    print(r2.status_code, r2.reason)

    try:
        with open('test.jpeg', "w+b") as f:
            f.write(r2.content)
    except IOError:
        print("IOError: could not write a file")