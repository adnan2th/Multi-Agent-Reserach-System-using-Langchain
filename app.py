
import streamlit as st
from src.pipelines.piplines import run_research_pipeline
from datetime import datetime
import inspect

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔬",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
.main {
    background-color: #0e1117;
}

.block-container {
    padding-top: 2rem;
}

.hero {
    padding: 25px;
    border-radius: 15px;
    background: linear-gradient(120deg, #172554, #312e81);
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 38px;
}

.hero p {
    color: #cbd5e1;
    font-size: 17px;
}

.stButton button {
    width: 100%;
    border-radius: 10px;
    height: 45px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SESSION STATE ----------------

if "research_data" not in st.session_state:
    st.session_state.research_data = None

if "history" not in st.session_state:
    st.session_state.history = []


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🔬 Research AI")

    st.markdown("---")

    st.subheader("Research Pipeline")

    st.markdown("""
    1. 🔎 Search Agent
    2. 🌐 Scrape Agent
    3. ✍️ Writer Agent
    4. 🧠 Critic Agent
    """)

    st.markdown("---")

    st.subheader("About")

    st.write(
        "An AI-powered multi-agent research system "
        "that searches, extracts, writes and reviews "
        "research reports automatically."
    )

    st.markdown("---")

    if st.button("Clear Results"):
        st.session_state.research_data = None
        st.rerun()


# ---------------- HEADER ----------------

st.markdown("""
<div class="hero">
    <h1>🔬 AI Research Assistant</h1>
    <p>Multi-Agent Research Automation System</p>
</div>
""", unsafe_allow_html=True)


# ---------------- METRICS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AI Agents", "4")

with col2:
    st.metric("Pipeline", "Automated")

with col3:
    st.metric("Report Format", "Markdown")

st.markdown("---")


# ---------------- INPUT ----------------

st.subheader("Start New Research")

topic = st.text_input(
    "Research Topic",
    placeholder="e.g. Latest developments in Agentic AI"
)

run_button = st.button(
    "🚀 Start Research",
    type="primary"
)


# ---------------- RUN PIPELINE ----------------

if run_button:

    if not topic.strip():

        st.warning("Please enter a research topic.")

    else:

        progress_bar = st.progress(0)
        status_text = st.empty()
        agent_status = st.empty()

        steps = {
            1: "🔎 Search Agent",
            2: "🌐 Scrape Agent",
            3: "✍️ Writer Agent",
            4: "🧠 Critic Agent",
            5: "✅ Completed"
        }

        def progress_callback(step, message):

            progress_bar.progress(min(step / 5, 1.0))

            status_text.info(message)

            agent_status.markdown(
                f"### {steps.get(step, 'Processing')}"
            )

        try:

            with st.spinner("AI agents are working..."):

                # Check whether pipeline accepts callback
                parameters = inspect.signature(
                    run_research_pipeline
                ).parameters

                if "progress_callback" in parameters:

                    result = run_research_pipeline(
                        topic,
                        progress_callback=progress_callback
                    )

                else:

                    status_text.info(
                        "Running research pipeline..."
                    )

                    result = run_research_pipeline(topic)

                    progress_bar.progress(1.0)

                    agent_status.markdown(
                        "### ✅ Completed"
                    )

            st.session_state.research_data = result

            st.session_state.history.append({
                "topic": topic,
                "date": datetime.now().strftime(
                    "%Y-%m-%d %H:%M"
                )
            })

            st.success("Research completed successfully!")

        except Exception as e:

            st.error(f"Pipeline Error: {str(e)}")


# ---------------- DISPLAY RESULTS ----------------

data = st.session_state.research_data

if data:

    st.markdown("---")

    st.title("📊 Research Results")

    tab1, tab2, tab3, tab4 = st.tabs([
        "🔎 Search Results",
        "🌐 Scraped Content",
        "📄 Final Report",
        "🧠 Critic Feedback"
    ])

    with tab1:

        st.subheader("Search Agent Output")

        st.write(data.get("search_result", "No search results available."))

    with tab2:

        st.subheader("Scraped Website Content")

        st.write(data.get("scraped_content", "No scraped content available."))

    with tab3:

        st.subheader("Generated Research Report")

        st.markdown(str(data.get("report", "")))

        report_text = str(data.get("report", ""))

        st.download_button(
            label="⬇️ Download Research Report",
            data=report_text,
            file_name="research_report.md",
            mime="text/markdown"
        )

    with tab4:

        st.subheader("Critic Agent Review")

        st.markdown(str(data.get("feedback", "")))


# ---------------- HISTORY ----------------

if st.session_state.history:

    st.markdown("---")

    st.subheader("📚 Research History")

    st.dataframe(
        st.session_state.history,
        use_container_width=True
    )


# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "AI Research Assistant | Multi-Agent Research Automation"
)
