# 🎬 Shiv Movie Scout — AI Movie Information Extractor

> Transform unstructured movie stories and descriptions into clean, structured movie information using AI.

Shiv Movie Scout is an AI-powered movie information extraction application built with **Python, Streamlit, LangChain, Mistral AI, and Pydantic**.

The application accepts a natural-language movie description, scene, or story and uses a Large Language Model (LLM) to extract important movie-related information into a structured format.

Instead of manually reading a long movie paragraph and searching for individual details, users can simply paste the text and let the AI identify the available information automatically.

---
# 🛠️ Tools & Technologies

Shiv Movie Scout is built using modern technologies across **Generative AI, Natural Language Processing, Python development, structured data validation, and web application deployment**.

---

## 🐍 Programming Language

### Python

Python is the primary programming language used to develop the complete application.

**Used for:**
- Application development
- AI model integration
- Data processing
- Schema definition
- Error handling
- Backend application logic

---

## 🤖 Generative AI

### Mistral AI

Mistral AI provides the Large Language Model used for understanding movie descriptions and extracting relevant information.

**Model used:**

```text
mistral-small-2506
## 🚀 Live Demo

Try the deployed application here:

**Shiv Movie Scout — Live Demo**

https://shivmoviescout.streamlit.app/

---

## 📌 Project Overview

Movie descriptions are usually written as unstructured natural language.

For example:

> "The story follows Arjun Mehta, a 28-year-old investigative journalist who travels to Riverton to investigate the disappearance of a famous scientist..."

Although this paragraph contains useful information, extracting individual fields manually can be time-consuming.

Shiv Movie Scout converts this type of unstructured content into structured information such as:

- 🎬 Movie Title
- 📅 Release Year
- 🎭 Genre
- 🎥 Director
- 👥 Cast
- ⭐ Rating
- 📖 Summary

The extracted information is validated using a **Pydantic schema**, helping the application maintain a consistent output structure.

---

# ✨ Features

## 🤖 AI-Powered Information Extraction

Uses **Mistral AI** to understand natural-language movie descriptions and identify relevant movie information.

## 🧠 Structured Output

The AI response is parsed into a predefined Pydantic model rather than being displayed only as plain text.

## 🎬 Movie Information Extraction

The application extracts:

| Field | Description |
|---|---|
| Movie Title | Name of the movie |
| Release Year | Year in which the movie was released |
| Genre | Movie genres |
| Director | Director of the movie |
| Cast | Actors associated with the movie |
| Rating | Movie rating |
| Summary | Short movie description |

## 📊 JSON Output

The extracted information can also be viewed as structured JSON, which makes the project useful for:

- Data processing
- NLP experimentation
- Dataset creation
- Information extraction
- AI application development
- API/backend integration

## 🔍 Raw Model Output

For development and debugging purposes, the application also provides access to the original model response.

## 🎨 Modern User Interface

The application provides a clean, responsive Streamlit interface designed around a modern AI/movie experience.

## ⚡ Fast Interaction

Users can paste a movie description and receive structured information without manually processing the text.

## 🛡️ Schema Validation

Pydantic is used to validate the model output against the expected movie structure.

---

# 🏗️ Application Architecture

The overall processing pipeline is:

```text
                    ┌───────────────────────┐
                    │    User Input         │
                    │ Movie Description     │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │ ChatPromptTemplate    │
                    │ Prompt Construction   │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │      Mistral AI       │
                    │   LLM Processing      │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │ PydanticOutputParser  │
                    │ Response Validation   │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   Movie Data Model    │
                    │ Structured Information│
                    └───────────┬───────────┘
                                │
                                ▼
              ┌─────────────────────────────────┐
              │       Streamlit Interface       │
              │                                 │
              │  Title | Year | Genre | Rating │
              │  Director | Cast | Summary     │
              │                                 │
              └─────────────────────────────────┘
