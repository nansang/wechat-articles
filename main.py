import requests
import time
from article import extract_wechat_article_content

def fetch_album_articles(biz, album_id, start_msgid):
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
            "appmsg_token": ""
        }

        headers = {
            "User-Agent": "Mozilla/5.0",
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
            extract_wechat_article_content(article["url"], int(article["create_time"]))
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
    start_msgid = "2247484044"  # 初始 msgid

    urls = fetch_album_articles(__biz, album_id, start_msgid)
    print("\n总共抓取文章数:", len(urls))
