from transformers import pipeline

feedbacks = ["I can't say this is a good movie", \
    "this a bad one", \
        "I actually like the movie"]
#create pipeline
Classifier = pipeline("sentiment-analysis")

#preforming sentiment analysis on raw text
print(Classifier(feedbacks))
