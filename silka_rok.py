import csv
import matplotlib.pyplot as plt
from datetime import datetime



file = "data/csv/sitka_weather_2018_full.csv"
with open(file) as f:
    reader = csv.reader(f)
    head = next(reader)
    header = []
    for i , h in enumerate(head):
        print(i,h)
    tmax, tmin, date_name= [],[],[]
    for row in reader:
        try:
            tempmax = int(row[8])
            tempmin = int(row[9])
        except ValueError:
            print(f'Lack of value {row[2]}.')
        else:
            tmax.append(tempmax)
            tmin.append(tempmin)
            timeline = datetime.strptime(row[2], "%Y-%m-%d")
            date_name.append(timeline)

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.set_xlabel('date')
ax.set_ylabel('temperature in (F)')
fig.autofmt_xdate()
ax.plot(date_name,tmax, c='red', alpha=0.8, linewidth=1)
ax.plot(date_name,tmin, c='blue', alpha=0.8, linewidth=1)
ax.fill_between(date_name,tmax,tmin, facecolor='yellow', alpha=0.3)


if __name__ == '__main__':
    plt.title('Sitka_temperature_2018')
    plt.show()



