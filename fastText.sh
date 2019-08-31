#!/usr/bin/env bash

python dataPreprocess.py
head -n 69168 tweets.txt > tweets.train.txt
head -n 17292 tweets.txt > tweets.valid.txt
fastText/fasttext supervised -input tweets.train.txt -output model_tweets
fastText/fasttext test model_tweets.bin tweets.valid.txt