import requests
import datetime
from datetime import datetime, timedelta
import pandas as pd
import gzip
import shutil
import os


# author: @odrori1997
# Please check out the README for the intuition behind this code. 


# Using https://gz.blockchair.com/bitcoin/blocks/
URL_BASE = f"https://gz.blockchair.com/bitcoin/outputs/blockchair_bitcoin_outputs_"
APIKEY = os.environ("APIKEY")

start_date = "2009/01/02" # date of bitcoin inception
start_dt = datetime.strptime(start_date, "%Y/%m/%d")

def download_files(start_dt):
    for _ in range(365):
        start_dt += timedelta(days=1)
        endpoint = URL_BASE + start_dt.strftime("%Y%m%d") +".tsv.gz?key=" + APIKEY
        print(endpoint)
        fname = start_dt.strftime("%Y%m%d") + '.csv'
        resp = requests.get(endpoint, verify=False)
        try:
            with open("temp.tsv.gz", 'wb') as f:
                f.write(resp.content)
            with gzip.open("temp.tsv.gz", 'rb') as f_in:
                with open(fname, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        except Exception as e:
            print(f"Error: {e}")
            continue


def count_block_intervals(start_dt):
    prev = datetime.now()
    block_counter = -1 # first block will count as >2 hours
    for _ in range(365):
        start_dt += timedelta(days=1)
        fname = start_dt.strftime("%Y%m%d") + '.csv'
        with open(fname, "rb") as f:
            try: 
                df = pd.read_csv(fname,delimiter="\t")
                print(df)
            except Exception as e:
                print(f"Error: {e}")
                continue
            for _, row in df.iterrows():
                row_time = datetime.strptime(row["time"], "%Y-%m-%d %H:%M:%S")
                tdelta = row_time - prev
                if tdelta >= timedelta(hours=2):
                    block_counter += 1
                print("Block counter: " + str(block_counter) + "\nFound block mined " + str(tdelta) + " after previous")
                prev = datetime.strptime(row["time"], "%Y-%m-%d %H:%M:%S")
    return block_counter

download_files(start_dt)

print(" -- Final count -- ")
# Final count = year 1 of block times > 2 hours + 1% of blocks in remaining years
# Current block height = 727167
# 2,016 blocks mined every 2 weeks
final_count = count_block_intervals(start_dt) + 0.01 * (727167 - (2016 * 26))
print(final_count)