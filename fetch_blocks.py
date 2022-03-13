import requests
import datetime
from datetime import datetime, timedelta
import time
import pandas as pd
import gzip
import shutil
from urllib import request

# Using https://gz.blockchair.com/bitcoin/blocks/
URL_BASE = f"https://chain.api.btc.com/v3/block"

def query_btc(endpoint):
    response = requests.get(URL_BASE+endpoint)
    print(response)
    try:
        parsed_response = response.json()
    except Exception as e:
        print(f"Error parsing json response: {e}")
        return {}
    if parsed_response["err_no"] == 0:
        print(parsed_response)
        return parsed_response
    else:
        print(f"Error: " + str(parsed_response["err_no"]))    
    return {}


start_date = "2009/01/02"
start_dt = datetime.strptime(start_date, "%Y/%m/%d")
for i in range(365):
    start_dt += timedelta(days=1)
    endpoint = "https://gz.blockchair.com/bitcoin/outputs/blockchair_bitcoin_outputs_" + start_dt.strftime("%Y%m%d") +".tsv.gz?key=A___MmrGR8YFGGAeYAfhesqNsQlrPmMD"
    resp = requests.get(endpoint)
    start_dt += timedelta(days=1)
    try:
        parsed_response = resp.json()
    except Exception as e:
        print(f"Error: {e}")
        continue
    fname = start_dt.strftime("%Y%m%d") + '.csv'
    resp = requests.get(endpoint, verify=False)
    try:
        with open("temp.tsv.gz", 'wb') as f:
            f.write(resp.content)
            print("Wrote temp.tsv.gz")
        with gzip.open("temp.tsv.gz", 'rb') as f_in:
            with open(fname, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    except Exception as e:
        print(f"Error: {e}")
        continue

start_date = "2009/01/02"
start_dt = datetime.strptime(start_date, "%Y/%m/%d")
prev = datetime.now()
block_counter = 0
for i in range(365):
    start_dt += timedelta(days=1)
    start_dt += timedelta(days=1)
    fname = start_dt.strftime("%Y%m%d") + '.csv'
    with open(fname, "rb") as f:
        try: 
            df = pd.read_csv(fname,delimiter="\t")
            print(df)
        except Exception as e:
            print(f"Error: {e}")
            continue
        for ind, row in df.iterrows():
            print(row.keys())
            tdelta = datetime.strptime(row["time"], "%Y-%m-%d %H:%M:%S") - prev
            print(tdelta)
            if tdelta >= timedelta(hours=2):
                block_counter += 1
            print("Block counter: " + str(block_counter) + "\nFound block mined " + str(tdelta) + " after previous")
            prev = row["time"]