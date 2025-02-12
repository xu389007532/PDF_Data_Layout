import datetime
import sqlite3
import os


def PDFLicense_bs(company, year):
    b = company.encode()
    # print(b)
    passkey = ""
    for en1 in b:
        key = en1 * (year + 1981)
        passkey = passkey + str(key)
        decode_key = int(key / (year + 1981))
        # print(en1, 'key: ', key, 'decode_key:', decode_key)

    print(year,'补数_注册码:',passkey)
    return passkey

def PDFLicense_pb(company,year):
    b = company.encode()
    # print(b)
    passkey = ""
    for en1 in b:
        key = en1 * (year + 2012)
        passkey = passkey + str(key)
        decode_key = int(key / (year + 2012))
        # print(en1, 'key: ', key, 'decode_key:', decode_key)

    print(year,'排版_注册码:',passkey)
    return passkey

if __name__ == '__main__':
    PDFLicense_pb("公司A1",datetime.date.today().year-1)
    PDFLicense_bs("公司A1",datetime.date.today().year-1)
    PDFLicense_pb("公司A1",datetime.date.today().year)
    PDFLicense_bs("公司A1",datetime.date.today().year)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
