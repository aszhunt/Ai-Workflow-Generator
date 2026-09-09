import streamlit as st
from openai import OpenAI

# ---------- CONFIG ----------
st.set_page_config(page_title="AI Workflow Generator", page_icon="🚀", layout="wide")

# ---------- TITLE ----------
st.markdown("""
<h1 style='text-align: center; color: #4CAF50;'>🚀 AI Workflow Generator</h1>
<p style='text-align: center;'>Turn your idea into a complete step-by-step execution plan</p>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.header("⚙️ Settings")

api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

industry = st.sidebar.selectbox(
    "Select Industry",
    ["Freelancing", "Marketing", "Real Estate", "Healthcare", "Education", "Business", "Custom"]
)

tone = st.sidebar.selectbox(
    "Workflow Style",
    ["Professional", "Beginner Friendly", "Advanced Strategy"]
)

# ---------- INPUT ----------
st.subheader("🧠 Enter Your Goal / Problem")

user_input = st.text_area(
    "Example: I want to start earning from Fiverr",
    height=120
)

generate = st.button("✨ Generate Workflow")

# ---------- FUNCTION ----------
def generate_workflow(prompt):
    client = OpenAI(api_key=api_key)

    full_prompt = f"""
    You are an expert AI business consultant.

    Create a COMPLETE workflow plan for this goal:
    "{prompt}"

    Industry: {industry}
    Style: {tone}

    Output format:
    1. Step-by-step workflow (numbered)
    2. Tools/Technologies for each step
    3. Automation suggestions
    4. Explanation (WHY this works)
    5. Final success tips

    Make it practical, actionable, and real-world.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": full_prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content

# ---------- OUTPUT ----------
if generate:
    if not api_key:
        st.error("❌ Please enter your OpenAI API Key")
    elif not user_input.strip():
        st.warning("⚠️ Please enter your goal/problem")
    else:
        with st.spinner("Generating powerful workflow..."):
            try:
                result = generate_workflow(user_input)

                st.success("✅ Workflow Generated!")

                st.markdown("## 📋 Your AI-Generated Workflow")
                st.markdown(result)

                st.download_button(
                    label="📥 Download as Text",
                    data=result,
                    file_name="workflow.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error: {e}")
