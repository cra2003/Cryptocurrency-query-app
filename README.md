
# Cryptocurrency Query App

This application provides users with cryptocurrency price-related information, powered by FastAPI and Streamlit, while also supporting multilingual input via translation. It utilizes a classification system to identify if a query is related to cryptocurrency prices, rate limiting to avoid excessive requests, and caching for efficient price lookups. Additionally, Redis manages conversation history and rate limits.

## Table of Contents

1. [Architecture](#architecture)
2. [Requirements](#requirements)
3. [Environment Variables](#environment-variables)
4. [Setup and Installation](#setup-and-installation)
5. [Running the Application](#running-the-application)
6. [Components Overview](#components-overview)



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
GOOGLE_PROJECT_ID=your_google_project_id
GOOGLE_PRIVATE_KEY_ID=your_google_private_key_id
GOOGLE_PRIVATE_KEY="your_google_private_key"
GOOGLE_CLIENT_EMAIL=your_google_client_email
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_AUTH_URI=your_google_auth_uri
GOOGLE_TOKEN_URI=your_google_token_uri
GOOGLE_CERT_URL=your_google_cert_url
GOOGLE_CLIENT_CERT_URL=your_google_client_cert_url
```

## Setup and Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/cra2003/Sarvam-assignment.git
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
- **final_reply.py**: Processes user queries and manages conversation context with Redis.
- **translate.py**: Uses Google translate for translating queries.
- **crypto_price.py**: Fetches cryptocurrency prices from the CoinGecko API and uses caching to store results temporarily.
- **classify_query.py**: Identifies if a query is price-related using the TogetherAI API.
- **ui.py**: Provides a Streamlit user interface for interacting with the app.


--- 
