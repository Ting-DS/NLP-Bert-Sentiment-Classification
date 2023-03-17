# Sentiment analysis by BERT in PyTorch
BERT is state-of-the-art natural language processing model from Google. Using its latent space, it can be repurpossed for various NLP tasks, such as sentiment analysis.

This simple wrapper based on [Transformers](https://github.com/huggingface/transformers) (for managing BERT model) and PyTorch achieves 92% accuracy on guessing positivity / negativity on IMDB reviews.

# How to use

## Prepare data

For amazon
download the data from https://www.kaggle.com/datasets/bittlingmayer/amazonreviews

`python read-amazon.py`

For imdb
download the data from https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

`python split_data.py`


## Train weights

Training with default parameters can be performed simply by.

`python script.py --train`

Optionally, you can change output dir for weights or input dir for dataset.

## Evaluate weights

You can find out how great you are (until your grandma gets her hands on BERT as well) simply by running

`python script.py --evaluate`

Of course, you need to train your data first or get them from my drive.

## Predict text

`python script.py --predict "It was truly amazing experience."`

or

`python script.py --predict "It was so terrible and disgusting as coffee topped with ketchup."`
