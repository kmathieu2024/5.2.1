import streamlit as st
from utils import render_sidebar


st.set_page_config(page_title="Report")

st.markdown("# Report")
st.sidebar.header("Report")
render_sidebar()


st.write(
    """
        Here is a page with a report on it.
    """
)

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

st.write(
    """
    Look at those numbers. Amazing.
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
