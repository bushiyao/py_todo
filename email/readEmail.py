# coding=utf-8
# @Time : 2022/6/22 15:07 
# @Author : hh
# @File : readEmail.py 
# @Software: PyCharm
import re
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


class Email(object):
    def __init__(self):
        self.__subject = ""
        self.__from_addr = ""
        self.__from_name = ""
        self.__to_name = ""
        self.__to_addr = ""
        self.__context = ""
        self.__html = ""
        self.__date = ""

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subj):
        self.__subject = subj

    @property
    def from_addr(self):
        return self.__from_addr

    @from_addr.setter
    def from_addr(self, from_addr):
        self.__from_addr = from_addr

    @property
    def from_name(self):
        return self.__from_name

    @from_name.setter
    def from_name(self, from_name):
        self.__from_name = from_name

    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, ctx):
        self.__context = ctx

    @property
    def to_name(self):
        return self.__to_name

    @to_name.setter
    def to_name(self, to_name):
        self.__to_name = to_name

    @property
    def to_addr(self):
        return self.__to_addr

    @to_addr.setter
    def to_addr(self, to_addr):
        self.__to_addr = to_addr

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date


class ReadEmail(object):
    def __init__(self, mail_server):
        self.__pop_server = mail_server
        self.__username = ""
        self.__password = ""
        self.__pop = None

    def get_latest_n_email(self, n=1, subject="", from_addr="", from_name=""):
        resp, mails, octets = self.__pop.list()
        index = len(mails)
        results = []
        count = 0
        for i in range(index, 0, -1):
            resp, lines, octets = self.__pop.retr(i)
            print("lines: ", lines)
            msg_content = b'\r\n'.join(lines).decode('utf-8')
            print("msg_content: ", msg_content)

            msg_obj = Parser().parsestr(msg_content)
            print("msg_obj: ", msg_obj)

            obj = Email()
            email_subject = self.__decode_header_msg(msg_obj["subject"])
            if subject.strip() and subject.strip() != email_subject and not re.search(subject.strip(), email_subject):
                continue
            obj.subject = email_subject
            email_from_name, email_from_addr = parseaddr(msg_obj["From"])
            email_from_name = self.__decode_header_msg(email_from_name)
            email_from_addr = self.__decode_header_msg(email_from_addr)
            if from_name.strip() and from_name.strip() != email_from_name and not re.search(from_name, email_from_name):
                continue
            if from_addr.strip() and from_addr.strip() != email_from_addr and not re.search(from_addr, email_from_addr):
                continue
            obj.from_name = email_from_name
            obj.from_addr = email_from_addr
            email_to_name, email_to_addr = parseaddr(msg_obj["To"])
            email_to_name = self.__decode_header_msg(email_to_name)
            email_to_addr = self.__decode_header_msg(email_to_addr)
            obj.to_name = email_to_name
            obj.to_addr = email_to_addr
            email_date = self.__decode_header_msg(msg_obj["Date"])
            obj.date = email_date

            context = []
            if msg_obj.is_multipart():
                for part in msg_obj.get_payload():
                    ctx = self.__decode_body(part)
                    if ctx:
                        context.append(ctx)
            else:
                ctx = self.__decode_body(msg_obj)
                if ctx:
                    context.append(ctx)
            if context:
                obj.context = "\n".join(context)

            count += 1
            results.append(obj)
            if count >= n:
                return results

        return results

    def login(self, username, password):
        self.__username = username
        self.__password = password
        self.__pop = poplib.POP3(self.__pop_server)
        self.__pop.set_debuglevel(1)
        self.__pop.user(username)
        self.__pop.pass_(password)

    def __decode_header_msg(self, header):
        value, charset = decode_header(header)[0]
        if charset:
            value = value.decode(charset)
        return value

    def __decode_body(self, part):
        content_type = part.get_content_type()
        txt = ""
        if content_type == "text/plain" or content_type == 'text/html':
            content = part.get_payload(decode=True)
            charset = part.get_charset()
            if charset is None:
                content_type_get = part.get('Content-Type', '').lower()
                position = content_type_get.find('charset=')
                if position >= 0:
                    charset = content_type_get[position + 8:].strip()
                    if charset:
                        txt = content.decode(charset)
        return txt
