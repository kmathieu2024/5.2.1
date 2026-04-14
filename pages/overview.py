import streamlit as st
from utils import render_sidebar

st.set_page_config(page_title="Overview")

st.markdown("# Overview")
st.sidebar.header("Overview")
render_sidebar()

st.write(
    """Here is a page with a site overview.

    This site has one main page (app) and three pages (about, overview, and report).

    All of them have some redundant code that can be abstracted out to make changes easier in the future.
    """
)

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
