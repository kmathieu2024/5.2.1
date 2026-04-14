import streamlit as st
from utils import render_sidebar, render_common_info


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

render_common_info()
