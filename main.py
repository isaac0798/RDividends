import csv
from datetime import datetime
from collections import defaultdict

dividendsByYear = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

def get_month_key(date):
    """Convert datetime to YYYY-MM format for grouping"""
    dateFormatted = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    return dateFormatted.strftime('%m')

def get_year_key(date):
    """Convert datetime to YYYY-MM format for grouping"""
    dateFormatted = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    return dateFormatted.strftime('%Y')

with open('orders.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    print(spamreader.fieldnames)
    
    tickers = defaultdict(int)
    for row in spamreader:
        if row['Action'] == 'Dividend (Dividend)':
            year = get_year_key(row['Time'])
            month = get_month_key(row['Time'])

            dividendsByYear[year][month][row['Ticker']] = row['Total']

            print(row['Time'], row['Ticker'], row['Total'], get_month_key(row['Time']))
            tickers[row['Name']] += float(row['Total'])

    print(tickers)
    print(sum(tickers.values()))
    print(dividendsByYear)
