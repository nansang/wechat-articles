import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def extract_wechat_article_content(url, timestamp=1692452567, save_dir="articles"):
    chrome_options = Options()
    # 打开真实浏览器，不使用 headless
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(executable_path="D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe", options=chrome_options)

    driver.get(url)

    try:
        # 等待正文加载
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "js_content")))
        content = driver.find_element(By.ID, "js_content").get_attribute("innerHTML")
        title = driver.find_element(By.ID, "activity-name").text.strip()
        # 格式化时间为 yyyy-mm-dd
        formatted_time = time.strftime("%Y-%m-%d", time.localtime(timestamp))
        # formatted_time = time.strftime("%Y-%m-%d", time.strptime(publish_time, "%Y年%m月%d日"))

        # 保存为 Markdown
        os.makedirs(save_dir, exist_ok=True)
        safe_title = title.replace('/', '_').replace('\\', '_').replace('|', '_')
        filename = f"{formatted_time} - {safe_title}.md".replace('/', '_').replace('\\', '_')  # 防止非法字符
        with open(os.path.join(save_dir, filename), "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(content)

        print(f"✅ 已保存为 Markdown: {filename}")
        return filename
    except Exception as e:
        print("❌ 提取失败：", e)
        return None
    finally:
        driver.quit()


# 示例使用
article_url = "https://mp.weixin.qq.com/s?__biz=Mzg2NTkwNTM4MA==&mid=2247484159&idx=1&sn=0ef01696732b24176b85498be4f74cf5"
extract_wechat_article_content(article_url)
