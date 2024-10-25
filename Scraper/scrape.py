import requests,json
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def main():
    spread(get_jobs())

base_url = 'https://remoteok.com/api/'
user_agent = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36'

request_header = {
    'user-agent': user_agent,
    'language': 'en-us, en;q=0.5'
}

def get_jobs():
    response = requests.get(base_url,headers = request_header)
    return response.json()
    
def spread(response):
    wb = Workbook()
    job_sheet = wb.add_sheet('Testing')
    headers = list(response[0].keys())
    for i in range(0,len(headers)):
        job_sheet.write(0,i,headers[i])
    for i in range(0,len(response)):
        jobs = response[i]
        value = list(jobs.values())
        for x in range(0,len(value)):
            job_sheet.write(i+1,x,str(value))
    wb.save('remoteok.xls')
if __name__ == '__main__':
    main()