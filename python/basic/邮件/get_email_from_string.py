# coding=utf-8
import Pandas_ as pd
import tkFileDialog
import re
import time

city_list = ['北京', '上海', '广州', '深圳', '杭州']

# 获取当前时间用来为excel文件命名
# today_ = map(lambda x: str(x), time.localtime())[:-3]
today = map(lambda x: str(x), time.localtime())
today_ = today[0]+u'年'+today[1]+u'月'+today[2]+u'日'
# excel_path = 'C:\\Users\\xiligey\\Desktop\\'+'-'.join(today_)+u'-企业邮箱.txt'
txt_path = 'C:\\Users\\xiligey\\Desktop\\'+today_+u'-企业邮箱.txt'
dict_path = r'C:\Study\Python\Data\email_dict2.txt'
# dict_backup_path = r'D:\Python\Python_Program\Python_Data\email_dict_backup.txt'
# feedback_dict_path = r'D:\Python\Python_Program\Python_Data\email_feedback_dict.txt'
# email正则表达式
pattern = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b")

# 1 选择需要解析的多个文件
# 返回包含多个文件的目录组成的元组
file_names = sorted(tkFileDialog.askopenfilenames(initialdir=r'C:/Users/xiligey/Desktop/'))

# email_dict_ = pd.read_csv(r'C:\Study\Python\Data\email_dict2.txt', header=None)
# email_dict = list(email_dict_[0])
email_dict = []
for i, document in enumerate(file_names):
    data = pd.read_csv(document, header=None, sep='$$$$')[0]
    for j in range(len(data)):
        email = re.findall(pattern, data[j])
        if len(email) > 0:
            for k in range(len(email)):
                if email[k] not in email_dict:
                    # if '@qq.com' not in email[k] and '@126.com' not in email[k] and '@163.com' not in email[k] \
                    #         and '@QQ.com' not in email[k]:
                    email_dict.append(email[k])
                    print email[k]
# email_feedback_dict = pd.read_csv(feedback_dict_path, header=None)[0]
# for email in email_feedback_dict:   # 删除已反馈的邮箱
#     if email in email_dict:
#         email_dict.remove(email)
pd.Series(email_dict).to_csv(dict_path, header=False, index=False)      # 邮箱字典
# pd.Series(email_dict).to_csv(dict_backup_path, header=False, index=False)   # 邮箱字典备份
print 'End'
