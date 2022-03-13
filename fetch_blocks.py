import requests
import datetime
import time

# Using https://btc.com/btc/adapter?type=api-doc
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




# Using blockchair API:

# URL_BASE = "https://api.blockchair.com/bitcoin/blocks?q=time(2009-01-01..2009-12-31)&limit=100800&export=csv"

# resp = requests.get(URL_BASE)
# print(resp)
# print(resp.json())
# print(len(resp.json()["data"]))

# Using chainAPI.com API:


# latest_block_data = query_btc("/721054") # "/latest")
# current_height = int(latest_block_data["data"]["height"])
prev = datetime.datetime.now()
block_counter = 0
for i in range(1,100800):
    # print(f"Processing block: {current_height-i}")
    print(f"Processing block: {i}")
    time.sleep(10) # sleep to prevent rate limiting
    # response = query_btc(f"/{current_height-i}") 
    response = query_btc(f"/{i}") 
    if not response:
        print("error from btc api: Empty response")
        continue
    curr_ts = datetime.datetime.fromtimestamp(response["data"]["timestamp"])
    # tdelta = prev - curr_ts
    tdelta = curr_ts - prev
    if tdelta >= datetime.timedelta(hours=2):
        block_counter += 1
    print("Block counter: " + str(block_counter) + "\nFound block mined " + str(tdelta) + " after previous")
    prev = curr_ts
print(block_counter)