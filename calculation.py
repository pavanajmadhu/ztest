import plotly.figure_factory as ff
import pandas as pd
import csv
import random
import statistics
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()


populationmean=statistics.mean(data)
stddeviation=statistics.stdev(data)
print("standard deviation is : ", stddeviation)
print("mean is : ",populationmean)

def randommeans(counter):
    dataset=[]
    for i in range(0,counter):
       randomindex=random.randint(0,len(data))
       value=data[randomindex]
       dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def showfig(meanlist):
    df=meanlist
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        setofmeans=randommeans(30)
        mean_list.append(setofmeans)
    showfig(mean_list)
    mean=statistics.mean(mean_list)
    print("mean of sampling distribution : ",mean)

meanlist=[]
for i in range(0,100):
     setofmeans=randommeans(30)
     meanlist.append(setofmeans)
     std_devtion=statistics.stdev(meanlist)
     print("standard deviation of sampling distribution : ",std_devtion)


setup()
std_deviation = statistics.stdev(meanlist)
mean = statistics.mean(meanlist)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
print("std1",first_std_deviation_start, first_std_deviation_end)
print("std2",second_std_deviation_start, second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)



mean_of_sample1 = statistics.mean(data)
fig = ff.create_distplot([meanlist], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="reading time"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


z_score=(mean_of_sample1-mean)/std_deviation
print("the z-score is ",z_score)