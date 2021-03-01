import os
import re

import markdown
import requests


class BlogSender(object):

    def read_blog(self, blog_path):
        """读取博客内容"""

    def send_blog(self):
        """发送博客"""

    @staticmethod
    def _parse_cookie_string(cookie_string):
        """解析cookie字符串"""
        cookie = {}
        li = cookie_string.replace('\"', '').replace('\t', '').replace(
            '\n', '').replace(' ', '').split(';')
        for i in li:
            try:
                a, b = i.split('=')
                cookie[a] = b
            except Exception as e:
                print(e)
                p = i.find('=')
                cookie[i[:p]] = i[p + 1:]
        return cookie

    @staticmethod
    def md2html(md_string):
        """markdown 转 html
        暂未支持数学公式 TODO
        暂未支持上传本地图片 TODO
        """
        html = '''
                <html lang="zh-cn">
                <head>
                <meta content="text/html; charset=utf-8" http-equiv="content-type" />
                <link href="http://ounix1xcw.bkt.clouddn.com/github.markdown.css" rel="stylesheet">
                </head>
                <body>
                {blog_content}
                </body>
                </html>
               '''
        extensions = ['markdown.extensions.extra', 'markdown.extensions.codehilite',
                      'markdown.extensions.tables', 'markdown.extensions.toc']
        blog_content = markdown.markdown(md_string, extensions=extensions)
        return html.format(blog_content=blog_content)


class CSDNBlogSender(BlogSender):
    def read_blog(self, blog_path):
        """"读取博客内容"""
        from config import default_data
        self.blog_path = blog_path
        file_title, file_type = os.path.splitext(os.path.basename(blog_path))
        self.data = default_data
        self.data["title"] = file_title
        self.file_type = file_type

        with open(blog_path) as f:
            blog_content = f.read()

            pattern = re.compile("---.+?---", re.DOTALL)
            meta_infos = re.match(pattern, blog_content)  # 在文章开头查找元信息
            if meta_infos:  # 如果存在元信息 则需读取元信息 并将元信息从original_blog_content中删除
                blog_content = blog_content.replace(meta_infos.group(), "")  # 将头部信息从原来的blog_content中删除
                meta_infos = meta_infos.group().split("\n")[1:-1]
                for meta_info in meta_infos:
                    if meta_info.count(":") == 1:
                        key, value = meta_info.split(":")
                        if key in self.data:
                            self.data[key] = value
                        else:
                            raise AttributeError("元信息填写错误，没有该字段%s" % key)
            self.data["markdowncontent"] = blog_content  # 点开编辑之后会显示的内容
            self.data['content'] = self.md2html(blog_content)
        return self

    def send_blog(self):
        """发送博客"""
        session = requests.session()
        jar = requests.cookies.RequestsCookieJar()
        from config import cookie_string, url
        cookie_string = cookie_string
        url = url
        cookie = self.parse_cookie_string(cookie_string)
        for a, b in cookie.items():
            jar.set(a, b)
        session.cookies.update(jar)
        print(session.post(url, data=self.data, allow_redirects=False).json())

    @staticmethod
    def parse_cookie_string(cookie_string):
        cookie = {}
        li = cookie_string.replace('\"', '').replace('\t', '').replace(
            '\n', '').replace(' ', '').split(';')
        for i in li:
            try:
                a, b = i.split('=')
                cookie[a] = b
            except Exception as e:
                print(e)
                p = i.find('=')
                cookie[i[:p]] = i[p + 1:]
        return cookie


if __name__ == '__main__':
    from config import websites
    blog_path = "/Users/chenxilin/Code/Python/Machine_Learning/Machine_Learning_And_Deep_Learning_Theories/docs/层次聚类.md"

    if "csdn" in websites:
        blog = CSDNBlogSender()
        blog.read_blog(blog_path)
        blog.send_blog()
    if "jianshu" in websites:  # TODO 支持简书
        """TODO 支持简书"""

