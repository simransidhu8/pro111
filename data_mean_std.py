import statistics
from cv2 import mean
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("The population mean is ", population_mean)

population_stdev = statistics.stdev(data)
print("The population standard deviation is", population_stdev)

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0, 100):
    set_of_means= random_set_of_means(30)
    mean_list.append(set_of_means)

sampling_mean = statistics.mean(mean_list)
print("The mean of the sampling data is", sampling_mean)

sampling_stdev = statistics.stdev(mean_list)
print("The sampling standard deviation is", sampling_stdev)

first_std_start, first_std_end = sampling_mean - sampling_stdev, sampling_mean + sampling_stdev
second_std_start, second_std_end = sampling_mean - 2*sampling_stdev, sampling_mean + 2*sampling_stdev
third_std_start, third_std_end = sampling_mean - 3*sampling_stdev, sampling_mean + 3*sampling_stdev
print("std1", first_std_start, first_std_start)
print("std2", second_std_start, second_std_end)
print("std3", third_std_start, third_std_end)

fig = ff.create_distplot([mean_list], ["reading time"], show_hist= False)
fig.add_trace(go.Scatter(x = [sampling_mean, sampling_mean], y = [0, 0.7], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_std_start, first_std_start], y=[0, 0.7], mode = "lines", name = "first stdev start"))
fig.add_trace(go.Scatter(x = [first_std_end, first_std_end], y=[0, 0.7], mode = "lines", name = "first stdev end"))
fig.add_trace(go.Scatter(x = [second_std_start, second_std_start], y=[0, 0.7], mode = "lines", name = "second stdev start"))
fig.add_trace(go.Scatter(x = [second_std_end, second_std_end], y=[0, 0.7], mode = "lines", name = "second stdev end"))
fig.add_trace(go.Scatter(x = [third_std_start, third_std_start], y=[0, 0.7], mode = "lines", name = "third stdev start"))
fig.add_trace(go.Scatter(x = [third_std_end, third_std_end], y=[0, 0.7], mode = "lines", name = "third stdev end"))
fig.show()

z_score = (mean-sampling_mean)/sampling_stdev