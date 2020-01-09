# SubredditPolitics
A quick spring break project which tries to classify political leaning of various subreddits. Some short results can be found here: https://imgur.com/a/xhyvJ


Methodology: 
The overarching idea is to use r/the_donald as the example of a conserative subreddit and r/politics as the example of a liberal subreddit. Then, we can determine the political leaning of various subreddits by seeing how similar the language of a particular subreddit is to r/the_donald and r/politics.

The first step is to determine which words are "overused" in r/the_donald and r/politics. Initially, I was using every book in Google’s database to generate “normal” word frequencies and then comparing that to r/the_donald and r/politics frequencies. But Reddit has way too much slang and alternative spellings for that to work properly. Words like "ur" and "lol" were considered to be political. So I needed to find how r/the_donald and r/politics differed from *normal internet language*.

So I decided to use r/all to determine differences in frequency (“RedditFrequency.txt”). I took the percent difference of frequencies to determine the most overused words of r/politics and r/the_donald. I saved those in “RepubsData.txt” and “DemsData.txt”. The top 10 are shown in OverusedWords.png. This turned out to be pretty reasonable looking. The most overused words are stereotypically liberal/conserative.

I then took subreddits and parsed every word and put them through a calculator. If they were found in either the republican or democratic dictionaries, their percent difference score would be added to the republican or democratic totals (these are not necessarily mutually exclusive). Then I divided by the total number of words and got my “similarity indexes”.

Subreddits that were known to be republican were calculated to be more like r/the_donald and subreddits that were known to be democratic were calculated to be more like r/politics.

So I’m pretty happy with the results!

If you’re from reddit and have any questions, just pm me.

IF YOU WOULD LIKE TO USE THIS CODE:
Delete all the txt documents and run the scripts in the described order. You can just use my reddit credentials that are in the code, but if those get revoked you will have to create a reddit account and register the bot through their website.
