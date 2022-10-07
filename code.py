import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv
import pandas as pd

df = pd.read_csv('medium_data.csv')
data = df["reading_time"].tolist()
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)
std_deviation = statistics.stdev(mean_list)

first_std_deviation_start,first_std_deviation_end = mean - std_deviation,mean + std_deviation
second_std_deviation_start,second_std_deviation_end = mean -(2* std_deviation),mean +(2* std_deviation)
third_std_deviation_start,third_std_deviation_end = mean -(3* std_deviation),mean +(3* std_deviation)

df = pd.read_csv('sample_2.csv')
data = df['reading_time'].tolist()
mean_of_sample3 = statistics.mean(data)
print("mean of sample3:-",mean_of_sample3)
fig = ff.create_distplot([mean_list],["student marks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample3,mean_of_sample3],y = [0,0.17],mode = "lines",name = "MEAN OF STUDENTS WHO GOT FUN SHEETS"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end],y = [0,0.17],mode = "lines",name = "STANDARD DEVIATION TO END"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end,third_std_deviation_end],y = [0,0.17],mode = "lines",name = "STANDARD DEVIATION OF 3 END "))
fig.show()

z_score = ( mean - mean_of_sample3)/std_deviation
print("The z score is =",z_score)