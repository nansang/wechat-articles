import re
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from article import extract_wechat_article_content
from second import fetch_album_articles
from urllib.parse import urlencode
from config import album_configs

def get_first_msgid(url, __biz, album_id, path, is_reverse):
    """通过浏览器自动化获取首个msgid"""

    params = {
        "__biz": __biz,  # 公众号标识（必填）[6](@ref)
        "action": "getalbum",          # 固定值（必填）[6](@ref)
        "album_id": album_id,  # 合集ID（必填）[6](@ref)
        "is_reverse": is_reverse,            # 1倒序/0正序（必填）[6](@ref)
        "count": "10",                # 每页文章数（默认10）[6](@ref)
    }

    url = url + urlencode(params)

    # 配置无头浏览器
    chrome_options = Options()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    service = Service(executable_path="D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get(url)
        # 等待JS加载完成（可调整时长）
        driver.implicitly_wait(5)
        
        # 提取window.cgiData对象
        script_content = driver.execute_script("return JSON.stringify(window.cgiData);")
        cgi_data = json.loads(script_content)
        index_urls = []
        # 提取首个msgid
        if cgi_data.get('articleList'):
            driver.quit()
            article_list = cgi_data['articleList']
            # 提取每篇文章的 URL
            # for article in article_list:
            #     time.sleep(1)
            #     print("文章标题index:", article["title"], article["url"])
            #     print("time", article["create_time"])
            #     extract_wechat_article_content(article["url"], int(article["create_time"]), path)
            #     index_urls.append(article["url"])

            # 获取下一页的起始 msgid
            last_msgid = article_list[0]["msgid"]
            start_msgid = last_msgid

            urls = fetch_album_articles(__biz, album_id, start_msgid, path, is_reverse)
            print("\n总共抓取文章数:", len(urls) + len(index_urls))

            return cgi_data['articleList'][0]['msgid']
        else:
            raise ValueError("文章列表为空")
            
    except Exception as e:
        print(f"抓取失败：{str(e)}")
        return None
    # finally:
    #     driver.quit()


if __name__ == "__main__":
    # __biz = "Mzg2NTkwNTM4MA=="
    # album_id = "3896715541905326087"
    # start_msgid = "2247484267"  # 初始 msgid  金渐成 # 2025-05-08
    # path = "articles/金渐成"
    # is_reverse = 1

    test_url = "https://mp.weixin.qq.com/mp/appmsgalbum?"

    for config in album_configs:
        first_msgid = get_first_msgid(
            url=test_url,
            __biz=config["biz"],
            album_id=config["album_id"],
            # start_msgid=config["start_msgid"],
            path=config["path"],
            is_reverse=config["is_reverse"]
        )
        print(f"获取到的首个msgid：{first_msgid}, {config["path"]}") 
        # pass
    # first_msgid = get_first_msgid(test_url, __biz, album_id, path, is_reverse)
    # print(f"获取到的首个msgid：{first_msgid}")  # 输出：2657974094
