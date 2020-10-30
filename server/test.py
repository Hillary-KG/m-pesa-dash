import csv
import pandas as pd
from itertools import islice
def read_data():
    # post_data = request.get_json()
    # csv_file = post_data.get('upload_file')
    return_obj = {}

    with open('spread.csv', 'r') as csvfile:
        # reader = pd.read_csv(csvfile)
        reader = csv.DictReader(csvfile)
        for row in reader:
            # complete_times = []
            # complete_times.append(datetime.strptime(row['Completion Time'], '%d/%m/%y %H:%M:%S'))
            # latest_time = max(complete_times)
            # latest_time = row['Completion Time']
            # latest_balance = row['Balance']
            # return_obj['latest_time'] = latest_time
            # return_obj['latest_balance'] = latest_balance
            print(row)
    return return_obj


# check if this is the main module
# if __name__ == '___main__':
print(read_data())
