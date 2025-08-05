# AI Cognitive Analyst

AI Cognitive Analyst is a GPT-4-powered application that analyzes any paragraph of text for logical structure, assumptions, bias, and persuasiveness. Built with Streamlit and OpenAI's API, it demonstrates applied NLP, argument mining, and responsible AI design.

## What This Project Does

This tool critically evaluates short-form written content by:

- Breaking down the logical components:
  - Main claim
  - Supporting evidence
  - Conclusion
- Identifying stated and unstated assumptions
- Detecting potential bias, including:
  - Emotional language
  - Framing techniques
  - Selective or polarizing language
- Evaluating argument structure:
  - Logical coherence
  - Detection of common fallacies (e.g., appeal to emotion, false dichotomy)
- Scoring the paragraph's:
  - Clarity (1–10)
  - Persuasiveness (1–10)

Output is formatted using structured markdown for easy reading and analysis.

## Purpose and Motivation

This project explores how large language models can be used to support critical thinking, argument literacy, and high-trust AI applications. It was designed to demonstrate practical use of advanced NLP in a way that goes beyond basic prompting, with a focus on structure, reasoning, and ethical deployment.

The tool reflects a broader interest in building real-world AI systems that are not only functional but responsible, explainable, and aligned with human-centered design principles.

## Key Technologies Used

- Python 3.10+
- Streamlit for the front-end interface
- OpenAI GPT-4 for language understanding and reasoning
- Markdown formatting for clean, structured output

## How to Run This App Locally

1. Clone this repository or download the files

2. Install dependencies:
   ```bash
   pip install streamlit openai
   ```

3. Set your OpenAI API key:

   On Windows:
   ```bash
   set OPENAI_API_KEY=your_key_here
   ```

   On macOS/Linux:
   ```bash
   export OPENAI_API_KEY=your_key_here
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Your browser will open to localhost:8501 with the full interface

## Example Input

Climate change is the most urgent problem facing humanity. Anyone who denies this is simply ignoring the science. We must take drastic action now to avoid catastrophe.

## Example Output (Excerpt)

Logical Breakdown  
• Main Claim: Climate change is the most urgent problem facing humanity.  
• Evidence: The claim that deniers are ignoring the science.  
• Conclusion: We must take drastic action now to avoid catastrophe.

Assumptions  
• That science is in full agreement about urgency.  
• That drastic action is the only way to avoid catastrophe.

Potential Bias  
• Emotionally charged terms like “most urgent” and “ignoring the science”.  
• Framing opponents as irrational or ignorant.

Argument Structure  
• Appeal to emotion  
• False dichotomy

Clarity Score: 7/10 – The message is clear but lacks detail.  
Persuasiveness Score: 5/10 – Limited evidence and some bias reduce effectiveness.

## Future Improvements

- Allow analysis of multi-paragraph or full-article inputs
- Highlight specific phrases contributing to bias or fallacy
- Add PDF export or CSV reporting functionality
- Build a dataset of analyzed examples for training

## References and Related Work

- Allen AI – ArguAna: A Benchmark for Argument Quality  
  https://arxiv.org/abs/2106.11363

- Stanford HAI – Language Model Fairness and Evaluation  
  https://hai.stanford.edu/news/ai-language-models-are-changing-our-world-can-we-make-them-fair

- The Alan Turing Institute – AI Ethics Guidelines  
  https://www.turing.ac.uk/research/research-projects/ai-ethics

- IBM Project Debater – Argument Mining and Computational Rhetoric  
  https://www.research.ibm.com/artificial-intelligence/project-debater/
