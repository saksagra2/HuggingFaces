import requests
import csv
import time

while True:
    response = requests.get("https://huggingface.co/api/models")
    data = response.json()
    top_models = sorted(data, key=lambda x: x['downloads'], reverse=True)[:10]
    filename = "report_" + time.strftime("%Y%m%d_%H%M%S")+".csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Model Name", "Downloads"])
        for model in top_models:
            writer.writerow([model['id'], model['downloads']])
    time.sleep(3600)