import csv

import pandas as pd

tweets = pd.read_csv('ExtractedTweets.csv')

col = ['Party', 'Tweet']
tweets = tweets[col]
tweets = tweets[pd.notnull(tweets['Tweet'])]
tweets.columns = ['Party', 'Tweet']

tweets['Party'] = ['__label__' + s.replace(' or ', '$').replace(', or ', '$').replace(',', '$').replace(' ', '_')
    .replace(',', '__label__').replace('$$', '$').replace('$', ' __label__').replace('___', '__') for s in
                   tweets['Party']]
tweets['Party']

tweets['Tweet'] = tweets['Tweet'].replace('\n', ' ', regex=True).replace('\t', ' ', regex=True)

tweets.to_csv(r'tweets.txt', index=False, sep=' ', header=False, quoting=csv.QUOTE_NONE, quotechar="", escapechar=" ")
