# btc-consecutive-blocks

My first step was to gain an intuition of the problem. The average block time is 10 minutes- how often does it really happen that block times are greater than 2 hours?
I looked at https://bitinfocharts.com/comparison/bitcoin-confirmationtime.html#alltime. 
We can see that the majority of network delays occurred in the first year. This makes sense- bitcoin block time is dependent on the network difficulty and hash rate. Perhaps at launch, the Bitcoin network experienced a very unstable hash rate which steadied over the years. 
To solve this problem completely we must download all block data and take the timestamp difference of every two consecutive blocks. However, downloading the entire history of Bitcoin requires 1TB which I don't have- so we approximate. 
I will count the first year's worth of block times greater than 2 hours. 
After that, will assume an error rate of 1%- so we take the worst case where 1% of all blocks mined after the first year have a block time greater than 2 hours. 
