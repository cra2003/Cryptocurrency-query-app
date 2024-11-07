
# Cryptocurrency Query App

This application provides users with cryptocurrency price-related information, powered by FastAPI and Streamlit, while also supporting multilingual input via translation. It utilizes a classification system to identify if a query is related to cryptocurrency prices, rate limiting to avoid excessive requests, and caching for efficient price lookups. Additionally, Redis manages conversation history and rate limits.

## Table of Contents
1. [Features](#features)
2. [Architecture](#architecture)
3. [Requirements](#requirements)
4. [Environment Variables](#environment-variables)
5. [Setup and Installation](#setup-and-installation)
6. [Running the Application](#running-the-application)
7. [Components Overview](#components-overview)
8. [Usage](#usage)

---

## Features
- **Cryptocurrency Price Fetching**: Fetches real-time cryptocurrency prices from CoinGecko API.
- **Multilingual Support**: Utilizes translation to allow input queries in multiple languages.
- **Classification**: Determines if a query is specifically about cryptocurrency prices.
- **Context-Based Answering**: Leverages conversation history for context in responses.
- **Caching**: Stores cryptocurrency prices in memory to avoid repeated API calls.
- **Rate Limiting**: Controls request frequency using Redis to ensure fair usage.
- **User Interface**: Streamlit UI for a user-friendly query input and response.

---

## Architecture
The application is divided into several components:
- **FastAPI** (`main.py`): Handles API requests and routes them to appropriate processing functions.
- **Streamlit UI** (`ui.py`): Provides a frontend interface for users to interact with the app.
- **Redis**: Manages rate limits and conversation history.
- **TogetherAI API**: Used for classification and translation.

---

## Requirements
- **Python** 3.8 or higher
- **Redis** server
- **CoinGecko API** for cryptocurrency prices
- **TogetherAI API** for language translation and classification
- **Packages**: Listed in `requirements.txt`

## Environment Variables
Create a `.env` file in the root of the project to store sensitive data:

```plaintext
TOGETHER_API_KEY=your_togetherai_api_key
```

## Setup and Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/crypto-query-app.git
    cd crypto-query-app
    ```

2. **Install Python Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Install Redis**
    - **Linux**:
      ```bash
      sudo apt update
      sudo apt install redis-server
      ```
    - **MacOS** (using Homebrew):
      ```bash
      brew install redis
      ```
    - **Windows**:
      Follow instructions on the [Redis official website](https://redis.io/download).

4. **Start Redis Server**
    ```bash
    redis-server
    ```

5. **Set Up Environment Variables**
    - Create a `.env` file in the project directory and add your TogetherAI API key.

---

## Running the Application

### 1. Run FastAPI
Start the FastAPI server to serve backend functionality.

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

### 2. Run Streamlit
Start the Streamlit server to provide a user interface.

```bash
streamlit run ui.py
```

---

## Components Overview

- **main.py**: Defines the FastAPI application, rate limiting, and routing logic.
- **final_reply.py**: Processes user queries, classifies cryptocurrency-related questions, and manages conversation context with Redis.
- **translate.py**: Uses TogetherAI for translating queries.
- **crypto_price.py**: Fetches cryptocurrency prices from the CoinGecko API and uses caching to store results temporarily.
- **classify_query.py**: Identifies if a query is price-related using the TogetherAI API.
- **ui.py**: Provides a Streamlit user interface for interacting with the app.

---

## Usage

### 1. Input in Streamlit
- Enter a **Session ID** to track conversations.
- Type a query, such as *"What is the price of Bitcoin?"*.
- Select a source language for the query (default is English).
- Press **Submit** to see the result.

### 2. API Endpoint (for FastAPI)
The FastAPI server has an endpoint for handling cryptocurrency queries:

**POST /query**

**Payload**:
```json
{
    "session_id": "your_unique_session_id",
    "query": "Your cryptocurrency-related question",
    "source_language": "Your language (e.g., English, Spanish)"
}
```

**Response**:
- For cryptocurrency-related queries, it returns the price.
- For non-cryptocurrency queries, it provides a general response.

### Example Command for Rate Limiting
To test rate limiting, send multiple queries quickly:

```bash
for i in {1..9}; do curl -X POST http://127.0.0.1:8001/query -H "Content-Type: application/json" -d '{"session_id": "test_session", "query": "What is the price of Bitcoin?", "source_language": "English"}'; done
```

After six requests per minute, you should receive a **429 Rate Limit Exceeded** response.

---

## Assumptions and Limitations

1. **Assumptions**:
   - Users provide a valid cryptocurrency name.
   - API rate limiting is per unique IP.
2. **Limitations**:
   - Classification model might misinterpret ambiguous queries.
   - IP-based rate limiting could restrict users sharing the same IP.
   - Maximum history length may impact very long conversations.

## License

This project is open-source under the MIT license.

--- 
