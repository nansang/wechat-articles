# 统一配置中心（新增）
album_configs = [
    {
        "biz": "Mzg2NTU3NjEwMw==",
        "album_id": "3671102465178337283",
        "path": "articles/真视研究/财务分析",
        "is_reverse": 0
    },
    # CFA
    {
        "biz": "MjM5ODg1Njk1Mw==",
        "album_id": "4035873491378192388",
        "path": "articles/品职在线/CFA学科攻略",
        "is_reverse": 1
    },
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
    {
        "biz": "Mzg2NTkwNTM4MA==",
        "album_id": "3896708264536227856",
        "path": "articles/金渐成/投资心得",
        "is_reverse": 1
    },
    # 匹夫老六说财税
    {
        "biz": "MzUyNTI2NTY0MQ==",
        "album_id": "3683658408122351627",
        "path": "articles/匹夫老六说财税/我做尽调这些年",
        "is_reverse": 0
    },
    # 康治本伤寒论
    {
        "biz": "MzkwNDM4NDMyMw==",
        "album_id": "4005680930332409861",
        "path": "articles/凌若云/康治本伤寒论",
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
    # 房圳探
    {
        "biz": "MjM5NTI0NjE1Mg==",
        "album_id": "2509480863978520577",
        "path": "articles/房圳探/西丽",
        "is_reverse": 0
    },
    {
        "biz": "MjM5NTI0NjE1Mg==",
        "album_id": "2828563609906610176",
        "path": "articles/房圳探/汇城茗院",
        "is_reverse": 0
    },
    # 其他系列
    {
        "biz": "Mzg5NzkwMTMzMA==",
        "album_id": "2804960172988448769",
        "path": "articles/精算屋/精算考试",
        "is_reverse": 0
    },
    {
        "biz": "Mzg5NzkwMTMzMA==",
        "album_id": "2809916434738069507",
        "path": "articles/精算屋/招聘信息",
        "is_reverse": 0
    },
    {
        "biz": "MjA1ODMxMDQwMQ==",
        "album_id": "3954806586270433294",
        "path": "articles/丁香医生/较真生活",
        "is_reverse": 0
    },
    # {
    #     "biz": "MzUyMTcxODYyMw==",
    #     "album_id": "3002213374534926339",
    #     "path": "articles/大道问答录/段永平投资问答录",
    #     "is_reverse": 0
    # },
    # {
    #     "biz": "MzUyMTcxODYyMw==",
    #     "album_id": "2558808176826040323",
    #     "path": "articles/大道问答录/段永平",
    #     "is_reverse": 0
    # },
    # {
    #     "biz": "MzUyMTcxODYyMw==",
    #     "album_id": "3335787608588730369",
    #     "path": "articles/大道问答录/巴菲特股东信",
    #     "is_reverse": 0
    # },
    # {
    #     "biz": "MzUyMTcxODYyMw==",
    #     "album_id": "2532315030176972800",
    #     "path": "articles/大道问答录/巴菲特",
    #     "is_reverse": 0
    # },
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