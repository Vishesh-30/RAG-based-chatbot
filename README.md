# WordPress Chatbot with Retrieval-Augmented Generation (RAG) and Chain of Thought (CoT) Strategy

## Overview

This project aims to develop a versatile and intelligent chatbot that utilizes a Retrieval-Augmented Generation (RAG) system enhanced with a Chain of Thought (CoT) strategy. The chatbot is designed to be integrated into various WordPress blogs and sites, handling and adapting to a wide range of topics while maintaining logical and contextually relevant interactions.

## Features

- **Adaptable Interactions:** The chatbot adjusts its interaction style and content based on the specific WordPress site it is deployed on.
- **Retrieval-Augmented Generation:** Combines retrieval of relevant content from WordPress sites with generative AI to produce accurate and contextually appropriate responses.
- **Chain of Thought:** Enhances responses with a logical progression and continuity to improve user engagement and satisfaction.

## Project Structure

```
chatbot/
│
├── data/
│   └── embeddings/
├── models/
│   └── fine-tuned/
├── src/
│   ├── __init__.py
│   ├── data_retrieval.py
│   ├── embedding_generator.py
│   ├── rag_processor.py
│   ├── cot_module.py
│   ├── app.py
│   └── config.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

```


## Setup Instructions
1. Local Development Environment
Clone the Repository:
```
https://github.com/Vishesh-30/RAG-based-chatbot
```

3. Set Up Virtual Environment:
```
  python -m venv chatbot-env
  chatbot-env\Scripts\activate  # Windows
  source chatbot-env/bin/activate  # Mac/Linux
```

4. Install Dependencies:
```
pip install -r requirements.txt
```

5. Setup config file
```
import os


class Config:

    EMBEDDING_MODEL = ''
    SUMMARIZATION_MODEL = ''
    HUGGINGFACE_TOKEN = ''

```

6. Run the streamlit based frontend
```
streamlit run app.py
````




