import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize

# Download tokenizer (only first time)
nltk.download('punkt')

def extractive_summary(text, num_sentences=3):
    # Split text into sentences
    sentences = sent_tokenize(text)

    if len(sentences) == 0:
        return ""

    # Convert sentences to TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # Score sentences by TF-IDF sum
    scores = tfidf_matrix.sum(axis=1)

    # Rank sentences
    ranked_sentences = sorted(
        ((scores[i, 0], s) for i, s in enumerate(sentences)),
        reverse=True
    )

    # Pick top N sentences
    summary = " ".join(
        ranked_sentences[i][1]
        for i in range(min(num_sentences, len(ranked_sentences)))
    )

    return summary
