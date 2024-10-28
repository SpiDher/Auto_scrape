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
    
    # Extract headers from the first job in the response
    headers = list(response[0].keys())
    
    # Write headers
    for i in range(len(headers)):
        job_sheet.write(0, i, headers[i])
    
    # Write job data
    for i in range(len(response)):
        jobs = response[i]
        values = list(jobs.values())
        
        for x in range(len(values)):
            job_sheet.write(i + 1, x, str(values[x])[:32767])
    
    wb.save('remoteok.xls')

email_params = {
    'send_to':['penivera655@gmail.com'],
    'send_from': 'charlesocean2023@gmail.com',
    'subject':'TEstin smtp servers',
    'text': 'This is a simple test of gmail smtp server',
    'files': None
    }
def send_email(send_to,send_from,subject,text,files):
    assert isinstance(send_to,list)
    msg = MIMEMultipart()
    msg['From']= send_from
    msg['To']= COMMASPACE.join(send_to)
    msg['Date']= formatdate(localtime=True)
    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()
if __name__ == '__main__':
    main()