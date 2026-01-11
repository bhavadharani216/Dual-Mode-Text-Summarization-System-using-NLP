from transformers import pipeline

# Load summarization model (first run will download it)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def abstractive_summary(text, max_length=130, min_length=30):
    if not text or len(text.strip()) == 0:
        return ""
    
    result = summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )
    return result[0]["summary_text"]
