import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Shiv CineExtract AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# MODERN UI CSS
# ============================================================

st.markdown("""
<style>

    /* ================================
       GLOBAL
    ================================= */

    .stApp {
        background-color: #0b0d12;
        color: #f5f5f5;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }


    /* ================================
       TEXT
    ================================= */

    h1, h2, h3, h4 {
        color: #ffffff !important;
    }

    p {
        color: #a7aab3;
    }


    /* ================================
       BUTTONS
    ================================= */

    div.stButton > button {

        width: 100%;

        height: 50px;

        border-radius: 12px;

        border: 1px solid #303642;

        background: #151922;

        color: #ffffff;

        font-size: 14px;

        font-weight: 600;

        transition: all 0.2s ease;

    }

    div.stButton > button:hover {

        border-color: #3b82f6;

        background: #1a2030;

        transform: translateY(-1px);

    }


    /* Main extraction button */

    div.stButton > button[kind="primary"] {

        background: linear-gradient(
            90deg,
            #2563eb,
            #7c3aed
        );

        border: none;

    }


    /* ================================
       TEXT AREA
    ================================= */

    textarea {

        background-color: #11141b !important;

        color: #f5f5f5 !important;

        border: 1px solid #292e38 !important;

        border-radius: 14px !important;

        padding: 16px !important;

        font-size: 15px !important;

        line-height: 1.7 !important;

    }

    textarea:hover {

        border-color: #3b82f6 !important;

    }

    textarea:focus {

        border-color: #3b82f6 !important;

        box-shadow:
            0 0 0 1px #3b82f6 !important;

    }


    /* ================================
       METRIC CARDS
    ================================= */

    [data-testid="stMetric"] {

        background: #11141b;

        border: 1px solid #292e38;

        border-radius: 14px;

        padding: 18px;

        min-height: 120px;

    }

    [data-testid="stMetricLabel"] {

        color: #858a96 !important;

    }

    [data-testid="stMetricValue"] {

        color: #ffffff !important;

        font-size: 20px !important;

    }


    /* ================================
       EXPANDER
    ================================= */

    .streamlit-expanderHeader {

        background: #11141b !important;

        border: 1px solid #292e38 !important;

        border-radius: 12px !important;

        color: #ffffff !important;

    }


    /* ================================
       CODE
    ================================= */

    pre {

        border-radius: 12px !important;

        background-color: #090b10 !important;

        border: 1px solid #292e38 !important;

    }


    /* ================================
       ALERTS
    ================================= */

    [data-testid="stAlert"] {

        border-radius: 12px;

    }


    /* ================================
       DIVIDER
    ================================= */

    hr {

        border-color: #252932 !important;

        margin-top: 30px;

        margin-bottom: 30px;

    }


    /* ================================
       ABOUT SECTION
    ================================= */

    .about-box {

        background: #11141b;

        border: 1px solid #292e38;

        border-radius: 16px;

        padding: 22px;

        margin-top: 15px;

    }


    /* ================================
       MOBILE
    ================================= */

    @media (max-width: 768px) {

        .block-container {

            padding-left: 1rem;

            padding-right: 1rem;

        }

        h1 {

            font-size: 32px !important;

        }

    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# SETUP
# ============================================================

load_dotenv()


@st.cache_resource
def get_model():

    return ChatMistralAI(
        model="mistral-small-2506"
    )


model = get_model()


# ============================================================
# SCHEMA
# ============================================================

class Movie(BaseModel):

    title: str

    release_year: Optional[int]

    genre: List[str]

    director: Optional[str]

    cast: List[str]

    rating: Optional[float]

    summary: str


parser = PydanticOutputParser(
    pydantic_object=Movie
)


prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
        Extract movie information from the paragraph.
        {format_instructions}
        """
    ),

    (
        "human",
        "{paragraph}"
    )

])


# ============================================================
# HEADER
# ============================================================

header_col1, header_col2 = st.columns(
    [4, 1],
    vertical_alignment="center"
)


with header_col1:

    st.markdown(
        "# 🎬 Shiv CineExtract AI"
    )

    st.caption(
        "AI-powered movie information extraction"
    )


with header_col2:

    st.info(
        "🤖 Mistral AI"
    )


st.divider()


# ============================================================
# HERO
# ============================================================

st.markdown(
    "### 🎞️ Movie Information Extractor"
)

st.markdown(
    """
    Transform movie descriptions, scenes, and stories into
    clean and structured information using AI.
    """
)

st.write("")


# ============================================================
# INPUT
# ============================================================

st.markdown(
    "#### 📝 Movie Description"
)

st.caption(
    "Paste your movie story or description below."
)


paragraph = st.text_area(

    "Movie Description",

    height=250,

    placeholder="""
Example:

The story follows Arjun Mehta, a 28-year-old
investigative journalist who travels to Riverton
to investigate the mysterious disappearance of
a famous scientist.

Paste your complete movie story here...
""",

    label_visibility="collapsed"

)


st.write("")


# ============================================================
# EXTRACT BUTTON
# ============================================================

extract_button = st.button(
    "🎬  Extract Movie Information",
    type="primary"
)


# ============================================================
# EXTRACTION
# ============================================================

if extract_button:

    if not paragraph.strip():

        st.warning(
            "⚠️ Please enter a movie paragraph first."
        )

    else:

        with st.spinner(
            "🎬 Analyzing movie information..."
        ):

            try:

                # ==================================================
                # ORIGINAL LOGIC — UNCHANGED
                # ==================================================

                final_prompt = prompt.invoke({

                    "paragraph": paragraph,

                    "format_instructions":
                        parser.get_format_instructions()

                })


                response = model.invoke(
                    final_prompt
                )


                movie_data = parser.parse(
                    response.content
                )


                # ==================================================
                # SUCCESS
                # ==================================================

                st.success(
                    "✓ Movie information extracted successfully!"
                )

                st.divider()


                # ==================================================
                # OUTPUT
                # ==================================================

                st.markdown(
                    "### ✨ Extracted Information"
                )


                # ==================================================
                # TOP INFORMATION
                # ==================================================

                col1, col2, col3 = st.columns(3)


                with col1:

                    st.metric(

                        label="🎬 Movie Title",

                        value=movie_data.title

                    )


                with col2:

                    st.metric(

                        label="📅 Release Year",

                        value=(
                            movie_data.release_year
                            if movie_data.release_year
                            else "N/A"
                        )

                    )


                with col3:

                    st.metric(

                        label="⭐ Rating",

                        value=(
                            movie_data.rating
                            if movie_data.rating
                            else "N/A"
                        )

                    )


                st.write("")


                # ==================================================
                # GENRE + DIRECTOR
                # ==================================================

                col1, col2 = st.columns(2)


                with col1:

                    st.markdown(
                        "##### 🎭 Genre"
                    )

                    genre_text = (

                        ", ".join(movie_data.genre)

                        if movie_data.genre

                        else "Not available"

                    )

                    st.info(
                        genre_text
                    )


                with col2:

                    st.markdown(
                        "##### 🎥 Director"
                    )

                    director_text = (

                        movie_data.director

                        if movie_data.director

                        else "Not available"

                    )

                    st.info(
                        director_text
                    )


                # ==================================================
                # CAST
                # ==================================================

                st.markdown(
                    "##### 👥 Cast"
                )


                cast_text = (

                    ", ".join(movie_data.cast)

                    if movie_data.cast

                    else "Not available"

                )


                st.info(
                    cast_text
                )


                # ==================================================
                # SUMMARY
                # ==================================================

                st.markdown(
                    "##### 📖 Summary"
                )


                st.write(
                    movie_data.summary
                )


                # ==================================================
                # DEVELOPER OUTPUT
                # ==================================================

                st.divider()


                st.markdown(
                    "### 🔧 Developer Output"
                )


                st.caption(
                    "Technical output for testing and development"
                )


                with st.expander(
                    "🔍 View Raw Model Output"
                ):

                    st.code(

                        response.content,

                        language="json"

                    )


                with st.expander(
                    "📦 View Structured JSON"
                ):

                    st.json(

                        movie_data.model_dump()

                    )


            except Exception as e:

                st.error(

                    "❌ Failed to parse response. "
                    "Model did not follow the required schema."

                )

                with st.expander(
                    "View technical error"
                ):

                    st.exception(e)


# ============================================================
# ABOUT DEVELOPER
# ============================================================

st.divider()

st.markdown(
    "### 👨‍💻 About the Developer"
)


about_col1, about_col2 = st.columns(
    [3, 1],
    vertical_alignment="center"
)


with about_col1:

    st.markdown(
        "#### Shiv Shankar Tiwari"
    )

    st.caption(
        "Data Science | Data Analytics | AI/ML |  Prompt Engineer"
    )

    st.write(
        """
        CineExtract AI is an AI-powered project designed to
        convert unstructured movie descriptions and stories
        into structured information using Mistral AI,
        LangChain, and Pydantic.
        """
    )


with about_col2:

    st.markdown(
        "**Built with**"
    )

    st.write(
        "🐍 Python"
    )

    st.write(
        "🤖 Mistral AI"
    )

    st.write(
        "🔗 LangChain"
    )

    st.write(
        "📦 Pydantic"
    )

    st.write(
        "⚡ Streamlit"
    )


# ============================================================
# SOCIAL LINKS
# ============================================================

st.write("")


link_col1, link_col2, link_col3 = st.columns(
    [1, 1, 2]
)


with link_col1:

    st.link_button(
        "💻 GitHub",
        "https://github.com/sandilyashivshankar"
    )


with link_col2:

    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/in/shiv-shankar-tiwari-a4054a282/"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🎬 CineExtract AI  •  Built by Shiv Shankar Tiwari  •  © 2026"
)

st.caption(
    "LangChain  •  Mistral AI  •  Pydantic  •  Streamlit"
)
