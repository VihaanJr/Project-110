import statistics
from cv2 import mean
import pandas as pd
import csv
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

f = pd.read_csv('medium_data.csv')
read = f['reading_time'].tolist()

population_mean = statistics.mean(read)
print('The population mean is ' , population_mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(read)-1)
        value = read[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list , sampling_mean):
        df = mean_list
        fig = ff.create_distplot([df] , ['Reading Time'] , show_hist=False)
        fig.add_trace(go.Scatter(x=[sampling_mean, sampling_mean], y=[0, 0.7], mode="lines", name="Sampling Mean"))
        fig.add_trace(go.Scatter(x=[population_mean, population_mean], y=[0, 0.7], mode="lines", name="Population Mean"))
        fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        mean = random_set_of_mean(30)
        mean_list.append(mean)
    sampling_mean = statistics.mean(mean_list)
    show_fig(mean_list , sampling_mean)
    print('The sampling mean is ', sampling_mean)

setup()