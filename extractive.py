import nltk
import numpy as np
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

def extractive_summary(text, num_sentences=5):
    sentences = sent_tokenize(text)

    if len(sentences) == 0:
        return ""

    # Convert sentences to TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # Compute cosine similarity matrix
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Create graph
    nx_graph = nx.from_numpy_array(similarity_matrix)

    # Apply PageRank (TextRank)
    scores = nx.pagerank(nx_graph)

    # Rank sentences
    ranked_sentences = sorted(
        ((scores[i], s, i) for i, s in enumerate(sentences)),
        reverse=True
    )

    # Select top N
    selected = sorted(ranked_sentences[:num_sentences], key=lambda x: x[2])

    summary = " ".join([s[1] for s in selected])

    return summary
