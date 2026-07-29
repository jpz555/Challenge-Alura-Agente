import streamlit as st


def render_input(app):
    """
    Llama a app.ask() -> no conoce nada de LangGraph
    """

    question = st.chat_input(
        "Haz una pregunta..."
    )

    if not question:
        return

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    response = app.ask(question)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response.response,
            "agent":response.current_agent,
            "time":response.execution_time
        }
    )

    st.rerun()