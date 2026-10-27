import os
from datetime import datetime

import streamlit as st
from langchain_core.messages import HumanMessage
from main import app


st.set_page_config(
    page_title="AI Travel Booking System",
    page_icon="✈️",
    layout="wide"
)


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, .stApp {
    font-family: 'Inter', sans-serif;
    background-color: #080d14;
}

.stApp {
    color: #e0edf8;
}

.hero-wrapper {
    position: relative;
    border-radius: 20px;
    overflow: hidden;
    margin-bottom: 2rem;
    height: 280px;
}

.hero-bg {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    filter: brightness(0.35);
    position: absolute;
    top: 0;
    left: 0;
}

.hero-content {
    position: relative;
    z-index: 2;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 2rem;
}

.hero-badge {
    background: rgba(58,123,213,0.25);
    border: 1px solid rgba(58,123,213,0.5);
    color: #7ab8f5;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 0.3rem 0.9rem;
    border-radius: 20px;
    margin-bottom: 0.9rem;
}

.hero-title {
    font-size: 2.6rem;
    font-weight: 700;
    color: #ffffff;
    margin: 0 0 0.6rem;
    line-height: 1.2;
}

.hero-sub {
    color: #b4c9df;
    font-size: 1rem;
    max-width: 560px;
}

.input-label {
    color: #7ab8f5;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #1a6bbf 0%, #0d4a8a 50%, #0a3d75 100%);
    color: #ffffff;
    border: 1px solid #2a5080;
    border-radius: 10px;
    font-weight: 600;
    transition: all 0.2s ease;
}

div[data-testid="stButton"] > button:hover {
    border-color: #7ab8f5;
    color: #ffffff;
}

[data-testid="stStatusWidget"] {
    background: #0e1a2e;
    border: 1px solid #1e3050;
    border-radius: 12px;
}

.sec-head {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin: 2rem 0 0.75rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #29415b;
}

.sec-head span {
    font-size: 1.15rem;
    font-weight: 600;
    color: #e0edf8;
}

.metric-row {
    display: flex;
    gap: 1rem;
    margin: 1.5rem 0;
}

.metric-box {
    flex: 1;
    background: #0e1623;
    border: 1px solid #1e2e44;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    text-align: center;
}

.metric-val {
    font-size: 1.8rem;
    font-weight: 700;
    color: #4ea8f0;
}

.metric-lbl {
    font-size: 0.78rem;
    color: #a0c4e0;
    margin-top: 0.2rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.final-card {
    background: linear-gradient(160deg, #0c1a2e 0%, #0a1520 100%);
    border: 1px solid #294766;
    border-left: 4px solid #3a7bd5;
    border-radius: 14px;
    padding: 1.8rem;
    line-height: 1.8;
    color: #d5e7f8;
    font-size: 0.95rem;
}

.save-bar {
    background: #0e1623;
    border: 1px solid #1e2e44;
    border-radius: 10px;
    padding: 0.85rem 1.2rem;
    color: #a0c4e0;
    font-size: 0.88rem;
    margin-top: 0.5rem;
}

section[data-testid="stSidebar"] {
    background: #090e18;
    border-right: 1px solid #1a2e44;
}

.sidebar-title {
    color: #e0edf8;
    font-size: 1rem;
    font-weight: 600;
    margin: 1rem 0 0.5rem;
}

.sidebar-chip {
    background: #0e1a2b;
    border: 1px solid #1a2e44;
    border-radius: 8px;
    padding: 0.45rem 0.75rem;
    margin-bottom: 0.4rem;
    font-size: 0.83rem;
    color: #a0c4e0;
}

.stTextArea textarea,
.stTextInput input {
    background: #0a1520;
    border: 1px solid #29415b;
    border-radius: 10px;
    color: #e8f4ff;
    font-size: 0.95rem;
}

.stTextArea textarea:focus,
.stTextInput input:focus {
    border-color: #3a7bd5;
    box-shadow: 0 0 0 2px rgba(58,123,213,0.2);
}

.stTextArea label,
.stTextInput label {
    color: #7ab8f5;
}

.stMarkdown p,
.stMarkdown li,
.stMarkdown td,
.stMarkdown th {
    color: #cce0f5;
}

.stMarkdown h1,
.stMarkdown h2,
.stMarkdown h3 {
    color: #e8f4ff;
}

.stAlert {
    background: #0e1a2b;
    border-radius: 10px;
}

div[data-testid="stDownloadButton"] > button {
    background: #1a3a5c;
    color: #e8f4ff;
    border: 1px solid #2a5080;
    border-radius: 10px;
}

#MainMenu, footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.markdown(
        "<div class='sidebar-title'>🌍 AI Travel Planner</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    thread_id = st.text_input(
        "👤 User ID",
        value="user_1",
        help="Your session ID keeps travel history separate."
    )

    st.markdown(
        "<div class='sidebar-title'>Powered by</div>",
        unsafe_allow_html=True
    )

    technologies = [
        "🔗 LangGraph",
        "🧠 Groq · GPT-OSS 120B",
        "🐘 PostgreSQL",
        "🔍 Tavily Search",
        "✈️ AviationStack"
    ]

    for tech in technologies:
        st.markdown(
            f"<div class='sidebar-chip'>{tech}</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        "<div class='sidebar-title'>Agent Pipeline</div>",
        unsafe_allow_html=True
    )

    pipeline_steps = [
        "① Flight Agent",
        "② Hotel Agent",
        "③ Itinerary Agent",
        "④ Final Agent"
    ]

    for step in pipeline_steps:
        st.markdown(
            f"<div class='sidebar-chip'>{step}</div>",
            unsafe_allow_html=True
        )


# Hero section
st.markdown("""
<div class="hero-wrapper">
    <img class="hero-bg"
         src="https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1400&q=80"
         alt="Airplane above clouds"/>
    <div class="hero-content">
        <div class="hero-badge">✦ Multi-Agent AI System</div>
        <div class="hero-title">✈️ AI Travel Booking System</div>
        <div class="hero-sub">
            Four specialized agents work together to search flights,
            find hotels, build an itinerary, and create your travel plan.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# Destination images
st.markdown(
    "<div class='sec-head'><span>🌎 Explore Destinations</span></div>",
    unsafe_allow_html=True
)

destinations = [
    (
        "🇯🇵 Tokyo",
        "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=300&q=70"
    ),
    (
        "🇫🇷 Paris",
        "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=300&q=70"
    ),
    (
        "🇹🇭 Bangkok",
        "https://images.unsplash.com/photo-1508009603885-50cf7c579365?w=300&q=70"
    ),
    (
        "🇮🇹 Rome",
        "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=300&q=70"
    ),
    (
        "🇦🇪 Dubai",
        "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=300&q=70"
    )
]

columns = st.columns(5)

for column, (name, image_url) in zip(columns, destinations):
    with column:
        st.markdown(
            f"""
            <div style="border-radius:10px;overflow:hidden;
                        position:relative;height:100px;">
                <img src="{image_url}"
                     style="width:100%;height:100%;object-fit:cover;
                            filter:brightness(0.65);"/>
                <div style="position:absolute;bottom:8px;left:0;right:0;
                            text-align:center;color:#fff;
                            font-size:0.8rem;font-weight:600;">
                    {name}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# Trip input
st.markdown(
    "<div class='sec-head'><span>🗺️ Plan Your Trip</span></div>",
    unsafe_allow_html=True
)

quick_options = [
    "7-day Japan trip under ₹2 lakh",
    "5-day Paris trip",
    "3-day Dubai trip from Delhi",
    "10-day Bali backpacking trip"
]

selected_option = st.selectbox(
    "Choose a sample request",
    ["Custom trip"] + quick_options
)

default_query = ""

if selected_option != "Custom trip":
    default_query = selected_option

user_query = st.text_area(
    "Describe your trip",
    value=default_query,
    placeholder=(
        "Example: Plan a 3-day trip from Delhi to Dubai "
        "for 2 adults with a budget of ₹80,000."
    ),
    height=120
)

generate = st.button(
    "🚀 Generate My Travel Plan",
    use_container_width=True
)


# Agent pipeline
agent_meta = {
    "flight_agent": ("✈️", "Flight Agent"),
    "hotel_agent": ("🏨", "Hotel Agent"),
    "itinerary_agent": ("🗓️", "Itinerary Agent"),
    "final_agent": ("🧠", "Final Agent")
}


if generate:
    if not user_query.strip():
        st.warning("Please describe your trip first.")

    elif not thread_id.strip():
        st.warning("Please enter a User ID.")

    else:
        config = {
            "configurable": {
                "thread_id": thread_id.strip()
            }
        }

        collected = {
            "flight_results": "",
            "hotel_results": "",
            "itinerary": "",
            "final_response": "",
            "llm_calls": 0
        }

        st.markdown("---")
        st.markdown(
            "<div class='sec-head'><span>🤖 Agent Pipeline</span></div>",
            unsafe_allow_html=True
        )

        try:
            with st.spinner("Your travel agents are working..."):
                for chunk in app.stream(
                    {
                        "messages": [
                            HumanMessage(content=user_query.strip())
                        ],
                        "user_query": user_query.strip(),
                        "flight_results": "",
                        "hotel_results": "",
                        "itinerary": "",
                        "llm_calls": 0
                    },
                    config=config,
                    stream_mode="updates"
                ):
                    for node_name, state_update in chunk.items():
                        icon, label = agent_meta.get(
                            node_name,
                            ("🔧", node_name)
                        )

                        with st.status(
                            f"{icon} {label}",
                            state="complete",
                            expanded=True
                        ):
                            if node_name == "flight_agent":
                                text = state_update.get(
                                    "flight_results", ""
                                )
                                collected["flight_results"] = text
                                st.markdown(
                                    text or "_No flight data returned._"
                                )

                            elif node_name == "hotel_agent":
                                text = state_update.get(
                                    "hotel_results", ""
                                )
                                collected["hotel_results"] = text
                                st.markdown(
                                    text or "_No hotel data returned._"
                                )

                            elif node_name == "itinerary_agent":
                                text = state_update.get("itinerary", "")
                                collected["itinerary"] = text
                                st.markdown(
                                    text or "_No itinerary generated._"
                                )

                            elif node_name == "final_agent":
                                messages = state_update.get("messages", [])
                                text = (
                                    messages[-1].content
                                    if messages
                                    else ""
                                )
                                collected["final_response"] = text
                                st.markdown(
                                    text or "_No final response returned._"
                                )

                            collected["llm_calls"] = state_update.get(
                                "llm_calls",
                                collected["llm_calls"]
                            )

            # Metrics
            st.markdown(f"""
            <div class="metric-row">
                <div class="metric-box">
                    <div class="metric-val">4</div>
                    <div class="metric-lbl">Agents Run</div>
                </div>
                <div class="metric-box">
                    <div class="metric-val">{collected['llm_calls']}</div>
                    <div class="metric-lbl">LLM Calls</div>
                </div>
                <div class="metric-box">
                    <div class="metric-val">✅</div>
                    <div class="metric-lbl">Status</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Final response
            if collected["final_response"]:
                st.markdown(
                    "<div class='sec-head'>"
                    "<span>🧠 Final Travel Plan</span></div>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    collected["final_response"]
                )

            # Save travel plan
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"travel_plan_{timestamp}.md"

            save_dir = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "travel_plans"
            )

            os.makedirs(save_dir, exist_ok=True)

            file_content = f"""# Travel Plan

**Query:** {user_query}
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**User ID:** {thread_id}

---

## Flight Information

{collected['flight_results'] or 'N/A'}

---

## Hotel Information

{collected['hotel_results'] or 'N/A'}

---

## Itinerary

{collected['itinerary'] or 'N/A'}

---

## Final Travel Plan

{collected['final_response'] or 'N/A'}

---

LLM Calls: {collected['llm_calls']}
"""

            with open(
                os.path.join(save_dir, filename),
                "w",
                encoding="utf-8"
            ) as file:
                file.write(file_content)

            download_column, info_column = st.columns([1, 3])

            with download_column:
                st.download_button(
                    "⬇️ Download Travel Plan",
                    data=file_content,
                    file_name=filename,
                    mime="text/markdown",
                    use_container_width=True
                )

            with info_column:
                st.markdown(
                    f"""
                    <div class="save-bar">
                        📁 Saved to travel_plans/{filename}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        except Exception as error:
            st.error(f"Travel planning failed: {error}")
            st.info(
                "Check the VS Code terminal for the complete error message."
            )
