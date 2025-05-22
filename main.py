import requests
import time
from article import extract_wechat_article_content

def fetch_album_articles(biz, album_id, start_msgid, path, is_reverse):
    urls = []
    while True:
        api_url = f"https://mp.weixin.qq.com/mp/appmsgalbum"
        params = {
            "action": "getalbum",
            "__biz": biz,
            "album_id": album_id,
            "count": 20,
            "begin_msgid": start_msgid,
            "begin_itemidx": 1,
            "wxtoken": "",
            "f": "json",
            "x5": "0",
            "devicetype": "Windows 11 x64",
            "clientversion": "63090c33",
            "appmsg_token": "",
            "is_reverse": is_reverse
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
            # 你可能还需要 Cookie 才能成功访问，视情况而定
        }

        response = requests.get(api_url, params=params, headers=headers)
        if response.status_code != 200:
            print("请求失败:", response.status_code)
            break

        data = response.json()

        # 检查返回状态
        if data.get("base_resp", {}).get("ret") != 0:
            print("接口返回异常:", data["base_resp"])
            break

        article_list = data.get("getalbum_resp", {}).get("article_list", [])
        if not article_list:
            print("没有更多文章")
            break

        # 提取每篇文章的 URL
        for article in article_list:
            print("文章标题:", article["title"])
            print("time", article["create_time"])
            extract_wechat_article_content(article["url"], int(article["create_time"]), path)
            urls.append(article["url"])

        # 获取下一页的起始 msgid
        last_msgid = article_list[-1]["msgid"]
        start_msgid = last_msgid

        # 判断是否还有下一页
        if data.get("getalbum_resp", {}).get("continue_flag") != "1":
            print("已到最后一页")
            break

        time.sleep(1)  # 避免过快请求被封

    return urls


if __name__ == "__main__":
    __biz = "Mzg2NTkwNTM4MA=="
    album_id = "3896715541905326087"
    start_msgid = "2247484267"  # 初始 msgid  金渐成 # 2025-05-08
    path = "articles/金渐成"
    is_reverse = 1

    # album_id = "3932943505567170582"  # 金渐成 -- 育儿
    # start_msgid = "2247485143"

    # path = "articles/天机奇谈"
    # is_reverse = 0
    # __biz = "Mzg2OTkwNzE4MA=="
    # album_id = "2861896433740955648"
    # start_msgid = "2247492939"  # 初始 msgid  天机奇谈 -- 地产随笔 2025-05-09
 
    
    # album_id = "2861890111381323779"
    # start_msgid = "2247492948" # # 初始 msgid  天机奇谈 -- 地产透视  2025-05-09 

    # album_id = "3715248304800841730"
    # start_msgid = "2247492843" # # 初始 msgid  天机奇谈 -- 日常随想  2025-05-09 

    # __biz = "Mzg5ODgxNDE0NQ==" # 精算学习交流圈 -- 北美精算师
    # album_id = "2482089104038428675"
    # start_msgid = "2247506776"
    # path = "articles/北美精算师"
    # is_reverse = 0
    
    urls = fetch_album_articles(__biz, album_id, start_msgid, path, is_reverse)
    print("\n总共抓取文章数:", len(urls))

