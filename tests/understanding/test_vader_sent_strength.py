import pytest

# Explicitly set path so don't need to run setup.py - if we have multiple copies of the code we would otherwise need
# to setup a separate environment for each to ensure the code pointers are correct.
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from enlp.understanding.sentiment import vader_sentiment_strength
import pandas as pd

def test_sent_strength_simple():

    # arange
    text = 'happy'
    textlist = [text]

    # act
    sent_scores = vader_sentiment_strength(textlist)

    # assert
    asserted_scores_dicts = [{'text': 'happy',
                              'compound': 0.5719,
                              'negative': 0.0,
                              'positive': 1.0,
                              'neutral': 0.0},
                             ]
    asserted_scores = pd.DataFrame(asserted_scores_dicts)

    assert sent_scores.equals(asserted_scores)
