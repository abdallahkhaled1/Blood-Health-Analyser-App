# 🩸 AI Blood Health Analyser & Localized Diet Planner

A production-ready, interactive Streamlit web application that automates the pipeline of extracting biomarkers from raw clinical blood reports and synthesizing culturally localized dietary recommendations using Google Gemini LLMs.

This project bridges the gap between raw medical text and patient-centric, actionable guidance tailored to traditional Egyptian cuisine.

---

## 🚀 Key Features

* **Instant Document Parsing:** Upload raw plain-text (`.txt`) blood work reports directly via a clean, modern UI.
* **Intelligent Entity Extraction (Stage 1):** Uses LangChain and Google Gemini to extract precise lab values and categorize them dynamically into **HIGH**, **LOW**, or **NORMAL** classes.
* **Interactive Data Dashboard:** Automatically parses LLM output into a dynamic, color-coded Pandas DataFrame with high/low alert metrics.
* **Cultural Dietary Synthesis (Stage 2):** Acts as an Egyptian-specialized clinical nutritionist to map biomarker flags to practical, local dietary choices (e.g., managing *Samna*, *Gibna Roumy*, and optimizing *Ful Medames* or *Molokhia*).
* **Exportable Reports:** Generates a comprehensive plain-text clinical summary available for one-click download.

---

## 🏗️ System Architecture

The application follows a modular, secure, and stateful architecture:
1. **User Input:** Secure sidebar configuration for Google API Keys (fully decoupled, ensuring no hardcoded credentials) and model selection (`gemini-2.5-flash`, `gemini-1.5-pro`, etc.).
2. **Extraction Engine:** LangChain orchestration transforms unstructured text into structured, delimited outputs.
3. **Parsing Engine:** Regex-free robust string splitting transforms markdown text into safe tabular `pd.DataFrame` structures.
4. **Presentation Layer:** Styled Streamlit components combined with scoped custom CSS for a premium medical-dashboard feel.

---

## 🛠️ Tech Stack

* **Frontend & UI:** Streamlit (Custom CSS, Inter & DM Serif Display Fonts)
* **LLM Framework:** LangChain (`langchain-google-genai`)
* **Core Model:** Google Gemini (Default: `gemini-2.5-flash`)
* **Data Processing:** Pandas
* **Environment:** Python 3.x

---
