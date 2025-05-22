from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from markdownify import markdownify as md
from bs4 import BeautifulSoup
import os
import time
import re


def extract_wechat_article_content(url, timestamp=1692452567, save_dir="articles"):
    chrome_options = Options()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    service = Service(executable_path="D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "js_content")))
        html_content = driver.find_element(By.ID, "js_content").get_attribute("innerHTML")
        title = driver.find_element(By.ID, "activity-name").text.strip()
        formatted_time = time.strftime("%Y-%m-%d", time.localtime(timestamp))

        # 用 BeautifulSoup 处理 html
        soup = BeautifulSoup(html_content, "html.parser")

        # 插入 # 标题用于分片
        # for tag in soup.find_all(['strong', 'b', 'h1', 'h2', 'h3']):
        #     if tag.name in ['h1', 'h2', 'h3']:
        #         tag.insert_before(f"\n\n#{'#' * (int(tag.name[1]) - 1)} {tag.get_text(strip=True)}\n\n")
        #     elif tag.name in ['strong', 'b']:
        #         tag.insert_before(f"\n\n## {tag.get_text(strip=True)}\n\n")

        # 转为 Markdown
        markdown_content = md(str(soup), heading_style="ATX")

        # enhanced_lines = []
        # for line in markdown_content.splitlines():
        #     stripped = line.strip()

        #     # 匹配以 **数字 或 **数字. 开头的段落（数字后面可选点）
        #     match = re.match(r'^(\*\*\s*\d+\.?)\s*(.*)', stripped)
        #     if match:
        #         full_number = match.group(1)  # "**33" 或 "**33."
        #         rest = match.group(2)         # 后续内容
        #         enhanced_lines.append(f"# {full_number} {rest}".strip())
        #     else:
        #         enhanced_lines.append(line)

        # markdown_content = "\n".join(enhanced_lines)

        # 清理多余空行
        # cleaned_lines = []
        # for line in markdown_content.splitlines():
        #     if line.strip() == "" and (not cleaned_lines or cleaned_lines[-1].strip() == ""):
        #         continue
        #     cleaned_lines.append(line)
        # markdown_content = "\n".join(cleaned_lines)

        # 保存为 .md 文件
        os.makedirs(save_dir, exist_ok=True)
        safe_title = title.replace('/', '_').replace('\\', '_').replace('|', '_')
        filename = f"{formatted_time} - {safe_title}.md".replace('/', '_').replace('\\', '_')
        file_path = os.path.join(save_dir, filename)
        if os.path.exists(file_path):
            print(f"⚠️ 文件已存在: {filename}")
            return True

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {formatted_time} - {safe_title}\n\n")
            f.write(markdown_content)

        print(f"✅ 已保存为 Markdown: {filename}")
        return filename
    except Exception as e:
        print("❌ 提取失败：", e)
        return None
    finally:
        driver.quit()

# 示例使用
# article_url = ""
# extract_wechat_article_content(article_url)
