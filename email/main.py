# coding=utf-8
# @Time : 2022/6/22 15:07 
# @Author : hh
# @File : main.py 
# @Software: PyCharm

from readEmail import ReadEmail


host = 'imap.qq.com'  # 主机IP或者域名
port = '993'  # 端口
username = '********'  # 用户名
password = '********'  # 密码
mail_box = '*********@qq.com'  # 邮箱名


# 使用pop邮箱服务器实例化一个对象，如下为163的pop邮箱服务器
# read_email = ReadEmail("pop.163.com")
read_email = ReadEmail(host)
# 登录邮箱，密码使用授权码，需要到邮箱设置里点击授权，并将授权码拷贝至此
read_email.login(username, password)
# 获取emails对象列表，按照时间顺序倒序获取，同时可以设置过滤条件，过滤条件可以通过邮件标题，发件人名，发件人邮箱过滤，支持正则表达式过滤，返回结果是一个列表，如果没有满足条件的为空列表，如果n设置多个，则返回满足条件的n封邮件，每一封邮件即为一个对象，通过对象属性可以获取到邮件的发送人、发送人邮箱，收件人，收件人邮箱，时间，邮件标题，邮件文本内容，还可以获取回复邮件html格式的邮件内容，此时的属性即为html
# 如下为获取最新的，邮件标题中有‘测试’字样的一封邮件
emails = read_email.get_latest_n_email(n=3, subject="2")
# emails = read_email.get_latest_n_email(n=1, subject="测试")
for obj in emails:
    print('from name: ', obj.from_name)
    print('from addr: ', obj.from_addr)
    print('toto name: ', obj.to_name)
    print('toto addr: ', obj.to_addr)
    print('from date: ', obj.date)
    print('from subj: ', obj.subject)
    print('from text: ', obj.context)
    print('--------------end ----------------------')
