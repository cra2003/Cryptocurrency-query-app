# Sarvam-assignment

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

Setup and Installation
Clone the Repository

bash
Always show details

Copy code
git clone https://github.com/yourusername/crypto-query-app.git
cd crypto-query-app
