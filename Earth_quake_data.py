import json

from plotly.graph_objs import Layout
from plotly import offline

file = 'data/json/data/eq_data_1_day_m1.json'
with open(file) as f:
    all_eq_data = json.load(f)
readable_file = 'readable_eq_data_work.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_disct_features = all_eq_data['features']

mags=[]
szergeog =[]
dlgeog = []
title=[]

for eq_dict in all_eq_disct_features:
    mag = eq_dict['properties']['mag']
    szer = eq_dict['geometry']['coordinates'][1]
    dl = eq_dict['geometry']['coordinates'][0]
    text = eq_dict['properties']['title']
    mags.append(mag)
    szergeog.append(szer)
    dlgeog.append(dl)
    title.append(text)


data = [{
    'type': 'scattergeo',
    'lon': dlgeog,
    'lat': szergeog,
    'text': title,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': [[0, 'rgb(0,255,0)'], [1, 'rgb(255,0,0)']],
        'colorbar': {'title': 'Earth quake scale'},
        'autocolorscale': False,

    },
}]
my_layout = Layout(title='Global Earth Quake in 2018')
fig = {'data': data, 'layout': my_layout}

if __name__ == '__main__':
    offline.plot(fig, filename='global_eq.html')

