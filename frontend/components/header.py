import streamlit as st

from api.enums import SearchMode


def render_header(app):
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏢 Empresa", use_container_width=True):
            app.set_search_mode(SearchMode.COMPANY)
    with col2:
        if st.button("📄 Personal", use_container_width=True):
            app.set_search_mode(SearchMode.DOCUMENTS)