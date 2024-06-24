def chain_of_thought(retrieved_texts, summarizer):
    # Split the retrieved texts into parts to simulate intermediate steps
    parts = [retrieved_texts[i:i + 1000] for i in range(0, len(retrieved_texts), 1000)]
    
    intermediate_summaries = []
    for part in parts:
        summary = summarizer(part, max_length=100, min_length=50, do_sample=False)
        intermediate_summaries.append(summary[0]['summary_text'])

    # Combine intermediate summaries into a final summary
    final_summary_text = " ".join(intermediate_summaries)
    final_summary = summarizer(final_summary_text, max_length=200, min_length=50, do_sample=False)
    return final_summary[0]['summary_text']

def generate_summary(query, retriever, encoder, summarizer):
    query_embedding = encoder.encode(query)
    retrieved_chunks = retriever.retrieve(query_embedding)
    retrieved_texts = " ".join([chunk.page_content for chunk, _ in retrieved_chunks])

    # Use chain of thought for summarization
    summary = chain_of_thought(retrieved_texts, summarizer)
    return summary
