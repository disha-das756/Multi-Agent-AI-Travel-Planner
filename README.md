# 🌍 IntelliTrip AI

### Multi-Agent Travel Planning System

IntelliTrip AI is an advanced multi-agent travel planning system built using **LangGraph, LangChain, and Streamlit**.
It automatically generates structured, personalized, and downloadable travel plans using an orchestrated AI agent pipeline.

The system demonstrates modular agent design, tool-augmented reasoning, evaluation loops, and production-ready UI implementation.

---

# 🚀 Live Demo (Optional)

```
https://your-app-link.streamlit.app
```

---

# 🧠 System Architecture

The project uses a **LangGraph-based multi-agent workflow**:

```
User Input
   ↓
Memory Agent
   ↓
Transport Agent
   ↓
Places Agent (DuckDuckGo Search)
   ↓
Itinerary Agent
   ↓
Budget Agent
   ↓
Evaluator Agent
   ↓
Refinement Agent
   ↓
PDF Generator
```

Each agent has a specific responsibility, ensuring modularity and scalability.

---

# ✨ Features

## 🗺️ Smart Itinerary Generation

* Structured travel plan
* Day-wise breakdown
* Attraction details
* Weather overview
* Visa information

## 🚗 Transport Optimization

* Cheapest option
* Fastest option
* Most comfortable option
* Cost estimation in INR

## 💰 Budget Estimation

* Category-wise breakdown
* Total cost estimation
* Practical travel spending suggestions

## 🧠 AI Evaluation System

* Quality Score
* Coverage Score
* Practicality Score
* Strengths & Improvement suggestions

## 📄 PDF Export

* Automatically generates a downloadable travel plan
* Clean A4 formatted output
* Includes transport + itinerary

## 🎨 Professional UI

* Two-column layout
* Tabs for Travel Plan & Evaluation
* Quality score metric display
* Sidebar branding
* Spinner loading animation

---

# 🛠️ Tech Stack

* Python
* LangChain
* LangGraph
* Streamlit
* ChromaDB (memory)
* DuckDuckGo Search Tool
* ReportLab (PDF generation)
* Groq LLM (LLaMA 3)

---

# 📂 Project Structure

```
intellitrip-ai/
│
├── agents/
│   ├── memory_agent.py
│   ├── transport_agent.py
│   ├── places_agent.py
│   ├── itinerary_agent.py
│   ├── budget_agent.py
│   ├── evaluator_agent.py
│   ├── refinement_agent.py
│
├── prompts/
│   ├── itinerary_prompt.txt
│   ├── budget_prompt.txt
│
├── graph.py
├── app.py
├── trip_memory.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```
git clone https://github.com/disha-das756/Multi-Agent-AI-Travel-Planner.git
cd intellitrip-ai
```

## 2️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

## 4️⃣ Add Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## 5️⃣ Run Application

```
streamlit run app.py
```

---

# 🎯 Example Usage

Input:

* Starting City: Kolkata
* Destination: Goa
* Duration: 5 days
* Budget: Budget
* Travel Style: Adventure
* Interests: Beach, Food, Nightlife

Output:

* Transport comparison
* Structured itinerary
* Budget breakdown
* Accommodation suggestions
* AI quality score
* Downloadable PDF

---

# 🧩 Design Principles

This project demonstrates:

* Modular multi-agent orchestration
* Tool-augmented reasoning
* Evaluation and refinement loop
* Structured output formatting
* Clean UI/UX separation
* Production-ready architecture

---

# 📈 Why This Project Stands Out

Unlike basic LLM chatbots, IntelliTrip AI:

* Uses structured agent orchestration
* Separates responsibilities across agents
* Implements evaluation and refinement stage
* Integrates tool-based search
* Provides exportable outputs
* Demonstrates scalable AI system design

This makes it suitable for:

* AI Engineer portfolios
* LangGraph demonstrations
* Multi-agent architecture case studies
* Resume showcase projects

---

# 🚀 Future Improvements

* Real-time flight API integration
* Distance-based cost calculation
* Crowd prediction system
* Weather API integration
* Carbon footprint estimation
* Chat-style travel assistant
* SaaS deployment with user accounts

---

# 👩‍💻 Author

Disha Das
AI & Multi-Agent Systems Enthusiast

---


