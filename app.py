import streamlit as st

from api.logimind import LogiMindAI

from frontend.components.sidebar import render_sidebar
from frontend.components.header import render_header
from frontend.components.chat import render_chat
from frontend.components.input_box import render_input

from frontend.utils.session import initialize_session


st.set_page_config(
    page_title="LOGBOT",
    layout="wide"
)

initialize_session()

render_sidebar(st.session_state.app)
render_header(st.session_state.app)
render_chat()
render_input(st.session_state.app)