import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize

# Download tokenizer (only first time)
nltk.download('punkt')

def extractive_summary(text, num_sentences=3):
    sentences = sent_tokenize(text)

    if len(sentences) == 0:
        return ""

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)

    scores = tfidf_matrix.sum(axis=1)

    # Create list of (index, score)
    sentence_scores = [
        (i, scores[i, 0])
        for i in range(len(sentences))
    ]

    # Sort by score descending
    ranked = sorted(sentence_scores, key=lambda x: x[1], reverse=True)

    # Pick top N sentence indices
    top_indices = sorted(
        [ranked[i][0] for i in range(min(num_sentences, len(ranked)))]
    )

    # Join sentences in original order
    summary = " ".join([sentences[i] for i in top_indices])

    return summary

