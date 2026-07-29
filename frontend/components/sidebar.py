import streamlit as st

from rag.config import MODELS


def render_sidebar(app):

    with st.sidebar:
        st.title("LOGBOT")

        provider = st.selectbox(
            "Proveedor",
            list(MODELS.keys())
        )

        if provider != app.provider:

            app.set_provider(provider)

        model = st.selectbox(
            "Modelo",
            [MODELS[provider]]
        )

        if model != app.model:

            app.set_model(model)

        api_key = st.text_input(
            "API Key",
            type="password"
        )

        if api_key:

            app.set_api_key(api_key)