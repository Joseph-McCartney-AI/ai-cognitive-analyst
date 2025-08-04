# app.py

import streamlit as st
import openai
import os

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit App UI
st.set_page_config(page_title="AI Cognitive Analyst", layout="centered")
st.title("AI Cognitive Analyst")
st.write("Enter a paragraph below to receive a structured analysis of its logic, assumptions, bias, and persuasiveness — powered by GPT-4.")

# User input
user_input = st.text_area("Enter a paragraph of text for analysis:", height=200)

# Define the prompt template
system_prompt = """
You are a critical thinking assistant trained in argument analysis, logic, and ethical NLP. Your job is to analyze any paragraph of text submitted by the user by performing the following:

1. Logical Breakdown – Identify the main claim, supporting evidence, and conclusion.
2. Assumptions – Highlight any assumptions made by the author, both explicit and implicit.
3. Potential Bias – Point out emotionally charged language, framing techniques, or selective evidence.
4. Argument Structure – Analyze the coherence of the reasoning. Note any fallacies (e.g. appeal to emotion, slippery slope, false cause).
5. Scoring:
   - Clarity: Score out of 10 with brief explanation.
   - Persuasiveness: Score out of 10 with brief explanation.

Be structured, objective, and concise. Use markdown formatting in your response.

Example output format:

**Logical Breakdown**
• Main Claim: ...
• Evidence: ...
• Conclusion: ...

**Assumptions**
• ...

**Potential Bias**
• ...

**Argument Structure**
• ...

**Clarity Score**: 8/10 – [reason]
**Persuasiveness Score**: 6/10 – [reason]
"""

# Button logic
if st.button("Analyze Text") and user_input.strip():
    with st.spinner("Analyzing with GPT-4..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.4
            )
            result = response['choices'][0]['message']['content']
            st.subheader("Analysis Results")
            st.markdown(result)
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Example section
with st.expander("Example Paragraphs to Try"):
    st.markdown("""
**Example 1**
> Climate change is the most urgent problem facing humanity. Anyone who denies this is simply ignoring the science. We must take drastic action now to avoid catastrophe.

**Example 2**
> Increasing taxes on the wealthy will inevitably lead to economic downturn. When the rich are taxed more, they invest less, leading to fewer jobs and lower growth.

**Example 3**
> Veganism is the healthiest lifestyle choice. Meat causes disease and inflammation, while plants provide everything your body needs.
""")

