# btc-consecutive-blocks

# Data Exploration
My first step was to gain an intuition of the problem. The average block time is 10 minutes- how often does it really happen that block times are greater than 2 hours?
I looked at https://bitinfocharts.com/comparison/bitcoin-confirmationtime.html#alltime. 
We can see that the majority of network delays occurred in the first year. This makes sense- bitcoin block time is dependent on the network difficulty and hash rate. Perhaps at launch, the Bitcoin network experienced a very unstable hash rate which steadied over the years. 
# Solution
To solve this problem completely we must download all block data and take the timestamp difference of every two consecutive blocks. However, downloading the entire history of Bitcoin requires >1TB which I don't have- so we approximate. 
I will count the first year's worth of block times greater than 2 hours. 
After that, will assume an error rate of 0.1%- so we take the worst case where 0.1% of all blocks mined after the first year have a block time greater than 2 hours. 
We use 0.1% because the first year had 439 blocks fitting the criteria, which is about 1% of blocks within that year.  Based on the data exploration phase, block times greater than 2 hours occured at least 10x more in the first year. 
# Result
Adding these two yields a final result of 1113. 
