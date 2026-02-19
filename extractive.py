import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def extractive_summary(text, num_sentences=4):
    sentences = sent_tokenize(text)

    if len(sentences) == 0:
        return ""

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # TF-IDF score
    tfidf_scores = np.array(tfidf_matrix.sum(axis=1)).flatten()

    # Add position score (early sentences get slight boost)
    position_scores = np.linspace(1, 0.5, len(sentences))

    # Combine scores
    final_scores = tfidf_scores + position_scores

    ranked_indices = np.argsort(final_scores)[::-1]

    top_indices = sorted(ranked_indices[:num_sentences])

    summary = " ".join([sentences[i] for i in top_indices])

    return summary
