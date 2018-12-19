from datetime import datetime, timedelta
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()

def convert_to_datetime(line):
    date_raw = line.split()[1]
    format_date = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(date_raw, format_date)


def time_between_shutdowns(loglines):
    date = []
    for line in loglines:
        if 'Shutdown initiated' in line:
            date_raw = line.split()[1]
            format_date = '%Y-%m-%dT%H:%M:%S'
            date.append(datetime.strptime(date_raw, format_date))
    print(date[1] - date[0])

time_between_shutdowns(loglines)
