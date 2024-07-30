import datetime

now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S") 

with open("index.html", "w") as f:
    f.write(f"Last updated at (current_time")
    