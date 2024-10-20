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
    ...

base_url = 'https://remoteok.com/api/'
user_agent = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36'

request_header = {
    'user-agent': user_agent,
    'language': 'en-us, en;q=0.5'
}

def get_jobs():
    response = requests.get(base_url,headers = request_header)
    return json.dumps(response.json(), indent = 2)
    
def spread(response):
    wb = Workbook()
    job_sheet = wb.add_sheet('Tetsing')
    headers = list(response[0].keys())
    
if __name__ == '__main__':
    main()