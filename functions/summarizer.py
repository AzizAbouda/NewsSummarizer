from transformers import pipeline, BartTokenizer

# Load BART model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
MAX_TOKENS = 1024  # maximum tokens per chunk

def chunk_text(text, max_tokens=MAX_TOKENS):
    words = text.split()
    chunks = []
    current_chunk = []
    current_len = 0

    for word in words:
        token_len = len(tokenizer.encode(word, add_special_tokens=False))
        if current_len + token_len > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_len = token_len
        else:
            current_chunk.append(word)
            current_len += token_len

    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def summarize_long_text(text):
    if not text or len(text.strip()) == 0:
        return "No content to summarize"
    
    chunks = chunk_text(text)
    summary = ""
    from transformers import pipeline, BartTokenizer

# Load BART model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
MAX_TOKENS = 1024  # maximum tokens per chunk

def chunk_text(text, max_tokens=MAX_TOKENS):
    words = text.split()
    chunks = []
    current_chunk = []
    current_len = 0

    for word in words:
        token_len = len(tokenizer.encode(word, add_special_tokens=False))
        if current_len + token_len > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_len = token_len
        else:
            current_chunk.append(word)
            current_len += token_len

    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def summarize_long_text(text):
    if not text or len(text.strip()) == 0:
        return "No content to summarize"
    
    chunks = chunk_text(text)
    summary = ""
    for chunk in chunks:
        input_len = len(tokenizer.encode(chunk, add_special_tokens=False))
        # Set max_length to half of input tokens or at least 20 tokens
        max_len = max(20, input_len // 2)
        summary_chunk = summarizer(chunk, max_length=max_len, min_length=10, do_sample=False)[0]['summary_text']
        summary += summary_chunk + " "
    return summary.strip()

