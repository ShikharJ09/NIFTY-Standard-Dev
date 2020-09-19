#importing packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#loading the csv file into a dataframe
nifty = pd.read_csv(r'')

#creating daily returns column
nifty['Daily Returns'] = nifty['Close'].pct_change(1)

#Calculate daily mean
daily_mean = nifty['Daily Returns'].mean(axis=0,skipna=True)
daily_sd = nifty['Daily Returns'].std(axis=0,skipna=True)

print(daily_mean)
print(daily_sd)

#Seek what day is today as this will affect the mean and standard deviation
t = input('Enter what day is today? Thursday or Friday: ')
expiry = float(input('Enter the closing price of NIFTY: '))

if t.lower() == 't':
    first_week_mean = daily_mean*7
    first_week_sd = daily_sd*np.sqrt(7)
    first_week_1sd_upper = expiry*(1 + first_week_mean + first_week_sd)
    first_week_1sd_lower = expiry*(1 + first_week_mean - first_week_sd)
    first_week_2sd_upper = expiry*(1 + first_week_mean + 2*first_week_sd)
    first_week_2sd_lower = expiry*(1 + first_week_mean - 2*first_week_sd)
    first_week_3sd_upper = expiry*(1 + first_week_mean + 3*first_week_sd)
    first_week_3sd_lower = expiry*(1 + first_week_mean - 3*first_week_sd)
    second_week_mean = daily_mean * 14
    second_week_sd = daily_sd * np.sqrt(14)
    second_week_1sd_upper = expiry*(1 + second_week_mean + second_week_sd)
    second_week_1sd_lower = expiry*(1 + second_week_mean - second_week_sd)
    second_week_2sd_upper = expiry*(1 + second_week_mean + 2*second_week_sd)
    second_week_2sd_lower = expiry*(1 + second_week_mean - 2*second_week_sd)
    second_week_3sd_upper = expiry*(1 + second_week_mean + 3*second_week_sd)
    second_week_3sd_lower = expiry*(1 + second_week_mean - 3*second_week_sd)
    result = pd.DataFrame(data=[[first_week_1sd_upper,first_week_2sd_upper,first_week_3sd_upper],
                                [first_week_1sd_lower,first_week_2sd_lower,first_week_3sd_lower],
                                [second_week_1sd_upper, second_week_2sd_upper, second_week_3sd_upper],
                                [second_week_1sd_lower, second_week_2sd_lower, second_week_3sd_lower]],
                          index=['First Week Upper Limit','First Week Lower Limit','Second Week Upper Limit','Second Week Lower Limit'],
                          columns=['68%','95%','99.7%'])
elif t.lower() == 'f':
    first_week_mean = daily_mean*6
    first_week_sd = daily_sd*np.sqrt(6)
    first_week_1sd_upper = expiry*(1 + first_week_mean + first_week_sd)
    first_week_1sd_lower = expiry*(1 + first_week_mean - first_week_sd)
    first_week_2sd_upper = expiry*(1 + first_week_mean + 2*first_week_sd)
    first_week_2sd_lower = expiry*(1 + first_week_mean - 2*first_week_sd)
    first_week_3sd_upper = expiry*(1 + first_week_mean + 3*first_week_sd)
    first_week_3sd_lower = expiry*(1 + first_week_mean - 3*first_week_sd)
    second_week_mean = daily_mean * 13
    second_week_sd = daily_sd * np.sqrt(13)
    second_week_1sd_upper = expiry*(1 + second_week_mean + second_week_sd)
    second_week_1sd_lower = expiry*(1 + second_week_mean - second_week_sd)
    second_week_2sd_upper = expiry*(1 + second_week_mean + 2*second_week_sd)
    second_week_2sd_lower = expiry*(1 + second_week_mean - 2*second_week_sd)
    second_week_3sd_upper = expiry*(1 + second_week_mean + 3*second_week_sd)
    second_week_3sd_lower = expiry*(1 + second_week_mean - 3*second_week_sd)
    result = pd.DataFrame(data=[[first_week_1sd_upper,first_week_2sd_upper,first_week_3sd_upper],
                                [first_week_1sd_lower,first_week_2sd_lower,first_week_3sd_lower],
                                [second_week_1sd_upper, second_week_2sd_upper, second_week_3sd_upper],
                                [second_week_1sd_lower, second_week_2sd_lower, second_week_3sd_lower]],
                          index=['First Week Upper Limit','First Week Lower Limit','Second Week Upper Limit','Second Week Lower Limit'],
                          columns=['68%','95%','99.7%'])
print(result)
