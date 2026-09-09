import streamlit as st
from groq import Groq

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI Workflow Generator By ASZ",
    page_icon="🚀",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}
h1, h2, h3 {
    text-align: center;
}
.stButton>button {
    background-color: #00c6ff;
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1>🚀 AI Workflow Generator By ASZ</h1>", unsafe_allow_html=True)
st.markdown("<h3>Create complete execution systems using AI</h3>", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.header("⚙️ Controls")

api_key = st.sidebar.text_input("Groq API Key", type="password")

industry = st.sidebar.selectbox(
    "Industry",
    ["Freelancing", "Marketing", "Real Estate", "Healthcare", "Education", "Startup", "Custom"]
)

mode = st.sidebar.selectbox(
    "Mode",
    ["Quick Workflow", "Deep Strategy", "Automation Plan"]
)

level = st.sidebar.selectbox(
    "User Level",
    ["Beginner", "Intermediate", "Advanced"]
)

# ---------- INPUT ----------
st.subheader("🧠 Enter Your Goal")

user_input = st.text_area("Example: I want to build a Fiverr income system")

generate = st.button("🔥 Generate Advanced Workflow")

# ---------- BUILT-IN KNOWLEDGE BASE (RAG STYLE) ----------
knowledge_base = {
    "Freelancing": "Client acquisition, proposal optimization, gig SEO, portfolio building, repeat clients.",
    "Marketing": "Funnel building, ad optimization, content strategy, analytics tracking.",
    "Real Estate": "Lead generation, property analysis, ROI calculation, negotiation.",
    "Healthcare": "Patient workflow, diagnosis assistance, documentation automation.",
    "Education": "Course creation, student engagement, content delivery systems.",
    "Startup": "Idea validation, MVP, scaling, funding strategies."
}

# ---------- FUNCTION ----------
def generate_ai_workflow(prompt):
    client = Groq(api_key=api_key)

    context = knowledge_base.get(industry, "")

    full_prompt = f"""
    You are an elite AI business strategist.

    USER GOAL:
    {prompt}

    INDUSTRY CONTEXT:
    {context}

    USER LEVEL:
    {level}

    MODE:
    {mode}

    Generate a HIGH-LEVEL EXECUTION SYSTEM:

    1. Step-by-step workflow (clear and structured)
    2. Tools for each step
    3. Automation opportunities
    4. Common mistakes to avoid
    5. Growth & scaling plan

    Keep it practical, strategic, and actionable.
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": full_prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content

# ---------- OUTPUT ----------
if generate:
    if not api_key:
        st.error("❌ Enter API Key")
    elif not user_input.strip():
        st.warning("⚠️ Enter goal")
    else:
        with st.spinner("Building your system..."):
            try:
                result = generate_ai_workflow(user_input)

                st.success("✅ Your AI System is Ready")

                st.markdown("## 📊 Generated Workflow System")
                st.markdown(result)

                st.download_button(
                    "📥 Download Plan",
                    result,
                    file_name="ASZ_Workflow.txt"
                )

            except Exception as e:
                st.error(f"Error: {e}")
