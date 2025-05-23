# 统一配置中心（新增）
album_configs = [
    # 金渐成系列
    {
        "biz": "Mzg2NTkwNTM4MA==",
        "album_id": "3896715541905326087",
        "path": "articles/金渐成/投资",
        "is_reverse": 1
    },
    {
        "biz": "Mzg2NTkwNTM4MA==",
        "album_id": "3932943505567170582",
        "path": "articles/金渐成/育儿",
        "is_reverse": 1
    },
    
    # 天机奇谈系列
    {
        "biz": "Mzg2OTkwNzE4MA==",
        "album_id": "2861896433740955648",
        "path": "articles/天机奇谈/地产随笔",
        "is_reverse": 0
    },
    {
        "biz": "Mzg2OTkwNzE4MA==",
        "album_id": "2861890111381323779",
        "path": "articles/天机奇谈/地产透视", 
        "is_reverse": 0
    },
    {
        "biz": "Mzg2OTkwNzE4MA==",
        "album_id": "3715248304800841730",
        "path": "articles/天机奇谈/日常随想", 
        "is_reverse": 1
    },
    
    # 其他系列
    {
        "biz": "Mzg5ODgxNDE0NQ==",
        "album_id": "2482089104038428675",
        "path": "articles/精算学习圈/北美精算师",
        "is_reverse": 0
    },
    {
        "biz": "MjA1ODMxMDQwMQ==",
        "album_id": "3954806586270433294",
        "path": "articles/丁香医生/较真生活",
        "is_reverse": 0
    }
]

# 批量执行函数（修改原代码）
# if __name__ == "__main__":
#     for config in album_configs:
        # urls = fetch_album_articles(
        #     biz=config["biz"],
        #     album_id=config["album_id"],
        #     start_msgid=config["start_msgid"],
        #     path=config["path"],
        #     is_reverse=config["is_reverse"]
        # )
        # print(f"【{config['path'].split('/')[-1]}】抓取完成，共获取{len(urls)}篇文章")
        # pass