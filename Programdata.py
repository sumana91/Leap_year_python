'''
Created on October 10, 2018
Install "requests" library before running this script :
pip install requests

'''

import datetime
import requests
from pathlib import Path
import calendar
import os
import csv

def is_downloadable(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

def download(url,location,file=None):
    if not file:
        file = url.split('/')[-1]
        print(file)

    location = location+"/"+file
    r = requests.get(url, allow_redirects=True)
    open(location, 'wb').write(r.content)

def writeCSV(csvLocation,csvContent):
    fieldnames = ['FILENAME', 'DATE']
    with open(csvLocation, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(fieldnames)
        for c in csvContent:
            csv_writer.writerow(c)

# PREPARE DOWNLOAD FOLDER
home = str(Path.home())
folder = "/bhavcopy"
downloadFolder = home+folder.replace("\\", "/")
if not os.path.exists(downloadFolder):
    os.makedirs(downloadFolder)

## PREPARE CSV
csvFile = "FileDownloadStatus.csv"
csvLocation = downloadFolder+"/"+csvFile
csvContent = []


#PREPARE URL
URL = "https://nseindia.com/content/historical/EQUITIES/YYYY/MMM/cmDDDDDbhav.csv.zip"

#PREPARE DATES
base = datetime.datetime.today()
numdays = 365
date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]

for a in date_list:
    SEND_URL = URL
    year = str(a.year)
    month = calendar.month_abbr[a.month].upper()
    day = str(a.day)
    SEND_URL = SEND_URL.replace("YYYY",year).replace("MMM",month).replace("DDDDD",day+month+year)
    #print(SEND_URL)
    if is_downloadable(SEND_URL):
        file = SEND_URL.split('/')[-1]
        csvContent.append([file,a.date()])
        download(SEND_URL,downloadFolder,file)

writeCSV(csvLocation,csvContent)

print("CSV list of files and all reports for last one year donwloaded into your user directory, \"bhavcopy\" folder ")
