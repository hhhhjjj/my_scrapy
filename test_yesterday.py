from datetime import datetime, date, timedelta
yesterday = (date.today() + timedelta(days = -1)).strftime("%Y-%m-%d")[5:].replace("0", "").replace("-", "月") + "日"
print(yesterday)