import streamlit as st

from api.logimind import LogiMindAI


def initialize_session():
    if "app" not in st.session_state:
        st.session_state.app = LogiMindAI()

    if "messages" not in st.session_state:
        st.session_state.messages = []