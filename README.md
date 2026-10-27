# AI Travel Booking System

An AI-powered travel booking assistant built using Python, LangGraph, and Streamlit.

## Features

- Flight search using AviationStack API
- Hotel search agent
- Travel itinerary generation
- AI-powered responses using Groq
- Conversation memory using PostgreSQL
- Interactive Streamlit interface

## Technologies Used

- Python
- LangGraph
- LangChain
- Groq
- Streamlit
- PostgreSQL
- AviationStack API
- Tavily

## Project Structure

```text
Multi_Agent_System_Demo/
├── main.py
├── frontend.py
├── tools/
│   ├── flight_tool.py
│   └── tavily_tool.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add the required API keys and database connection settings.
5. Run the application:

   ```bash
   streamlit run frontend.py
   ```

## Note

This is a learning project demonstrating a multi-agent workflow. Verify flight, hotel, pricing, and travel information independently before making bookings.