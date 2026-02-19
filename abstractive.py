from transformers import pipeline

# Load smaller but high-quality model
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def abstractive_summary(text):

    # Limit input size for efficiency
    text = text[:1500]

    result = summarizer(
        text,
        max_length=180,
        min_length=60,
        do_sample=False
    )

    return result[0]['summary_text']
