"""
配置文件
"""
# ----------全局配置----------
websites = ["csdn"]  # 同时发布到多个网站 csdn、简书、博客园等 目前只支持csdn

# ----------csdn相关配置----------
# 通过浏览器,打开发送博客的页面https://mp.csdn.net/mdeditor
# 然后F12,在network中的第一个页面中复制cookie

# csdn的cookies
cookie_string = """
uuid_tt_dd=10_20993211060-1569325503063-565159; dc_session_id=10_1569325503063.984332; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_20993211060-1569325503063-565159!5744*1*xiligey1!1788*1*PC_VC; SESSION=bd136489-e363-4497-87c9-ebad0cebc78d; UserName=xiligey1; UserInfo=0584fd13366c420e945d714d686f929e; UserToken=0584fd13366c420e945d714d686f929e; UserNick=%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AE%B6%E4%BF%AE%E7%82%BC%E4%B9%8B%E9%81%93; AU=158; UN=xiligey1; BT=1569487407977; p_uid=U000000; hasSub=true; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1569487808,1569489375,1569489694,1569563559; notice=1; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1569599562; c_adb=1; dc_tos=pyhys1
"""
url = "https://mp.csdn.net/mdeditor/saveArticle"  # post到csdn的网址
# 默认博客信息
default_data = {
    "title": "Blog Title",  # 文章名
    "content": "<h1>hello, world</h1>",  # 博客内容
    "markdowncontent": '# hello, world~',  # 点击编辑博客后显示的markdown内容
    "categories": "默认分类",  # 分类
    "tags": "",  # 逗号隔开多个标签 如 "python,ml,svm"
    "channel": 28,  # 频道 可选1:移动开发、2:云计算大数据、3:研发管理、6:数据库、12:运维、14:前端、15:架构、16:编程语言、28:人工智能、29:物联网、30:游戏开发、31:后端、32:安全、33:程序人生、34:区块链、35:音视频开发、36:资讯、37:计算机理论与基础
    "articleedittype": "1",
    "type": "orginial",  # orginal原创，report转载，translated翻译
    "private": "0",  # 0公开 1私密
    "status": '0'
}

# ----------简书相关配置----------
