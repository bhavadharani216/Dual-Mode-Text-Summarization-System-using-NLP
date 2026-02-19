from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def chunk_text(text, max_chunk=1000):
    chunks = []
    for i in range(0, len(text), max_chunk):
        chunks.append(text[i:i + max_chunk])
    return chunks

def abstractive_summary(text):

    chunks = chunk_text(text)
    final_summary = ""

    for chunk in chunks:
        result = summarizer(
            chunk,
            max_length=150,
            min_length=50,
            do_sample=False
        )
        final_summary += result[0]['summary_text'] + " "

    return final_summary.strip()
