# NIFTY-Standard-Dev
This code is based on the assumption that daily NIFTY returns follow normal distribution.
Hence, we download daily NIFTY data from NSE website for the last 1 year and read the same into python with pandas data reader.
Once the data has been loaded into a dataframe, we calculate daily mean and standard deviation on the basis of past 1 year daily data.
Once the mean and standard deviation has been calculated, we ask the user whether today is Thursday or Friday and what was the expiry level.
On the basis of above, the program returns 1, 2 and 3 standard deviations for NIFTY for next week (Thursday) expiry and next to next week (Thursday expiry).
Hence, positions can be taken basis the same.
