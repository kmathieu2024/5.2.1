import streamlit as st
from utils import render_sidebar


st.set_page_config(page_title="About")

st.markdown("# About")
st.sidebar.header("About")
render_sidebar()

st.markdown(
    """
    Fake Company LLC Inc. is a fake company created in 2024 for the purposes of making a website with a lot of redundant code.

    It produces nothing and has $0 a year in revenue.

    Usually, companies are not called both "LLC" and "Inc." and must choose one, but this is a fake company so it has both just to be funny.

    Here is a logo that I created with Gemini. It has too many "L"s.
    """
)

st.image("./assets/fake_company.png")

with st.expander("Company Info"):
    st.write(
        """
        Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043
    """
    )

with st.expander("Links"):
    st.markdown(
        """
        [Google](https://google.com)

        [Gemini](https://gemini.google.com)

        [Streamlit Docs](https://docs.streamlit.io/)
    """
    )
