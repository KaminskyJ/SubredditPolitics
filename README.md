# SubredditPolitics
A quick spring break project which analyzes r/the_donald and r/politics.

By no means is the scientific data, but I did try to make it as scientific as possible.

Methodology: 
Initially, I was using every book in Google’s database to generate “normal” word frequencies and then comparing that to subreddit frequencies. Reddit writes way too differently to get good data. Also, I couldn’t figure out a good way to deal with fake words like “ur” and other internet slang. Scratch that. If you want that code, it’s in the old versions folder.

I then used r/all to determine differences in frequency (“RedditFrequency.txt”. I took the percent difference of frequencies to determine the most overused words of r/politics and r/the_donald. I saved those in “RepubsData.txt” and “DemsData.txt”. The top 10 are shown in OverusedWords.png. This turned out to be pretty good looking data. The top words are stereotypically democratic/republican.

I then took subreddits and parsed every word and put them through a calculator. If they were found in either the republican or democratic dictionaries, their percent difference score would be added to the republican or democratic totals (these are not necessarily mutually exclusive). Then I divided by the total number of words and got my “similarity indexes”.

Subreddits that were know to be republican were calculated to be more like r/the_donald and subreddits that were know to be democratic were calculated to be more like r/politics.

So I’m pretty happy with the results!

If you’re from reddit and have any questions, just pm me.
