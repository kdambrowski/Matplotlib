import csv
import matplotlib.pyplot as plt
from datetime import datetime

file_name= 'data/csv/sitka_weather_07-2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    header_title=[[i, h] for i, h in enumerate(header_row)]
    print(header_title)
    for index, header in enumerate(header_row):
        print(index, header)

    tmax = []
    date = []
    tmin = []
    for row in reader:
        try:
            tempmax = int(row[5])
            tempmin = int(row[6])
        except ValueError:
            print(f'brak danych dla daty {row[2]}.')
        else:
            dat = datetime.strptime(row[2], "%Y-%m-%d")
            tmax.append(tempmax)
            tmin.append(tempmin)
            date.append(dat)

print(date)


plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.set_xlabel('data')
ax.set_ylabel('max temp')
ax.set_title('weather fo max temp')
fig.autofmt_xdate()
ax.plot(date,tmax, c='red', linewidth= 4)
ax.plot(date,tmin,c='blue', linewidth= 4)
ax.fill_between(date,tmax,tmin, alpha=0.2, facecolor='yellow')

plt.show()
