import pandas as pd
import matplotlib.pyplot as plt

file_name = 'VEDL.csv'
folder_path = 'C:\\Users\\imdig\\Desktop\\Learning\\Backtesting\\data\\'
file_path = f'{folder_path}{file_name}'

asset_df = pd.read_csv(file_path)

# Making sure everything has the correct datatype
asset_df['Date'] = pd.to_datetime(asset_df['Date'])
asset_df['Ticker'] = asset_df['Ticker'].astype("string")

# Adding a DayName Column next to Date
asset_df.insert(2,"DayName",asset_df['Date'].dt.day_name())
# print(asset_df.head())

volume_df = asset_df.drop(columns={"High","Low","Open"})
# print(volume_df.describe())

fig, ax = plt.subplots()
ax.plot(volume_df['Date'],volume_df['Close'])
ax.bar(volume_df['Date'],volume_df['Volume']/100000)
ax.set_title("Stock Price Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")

plt.show()