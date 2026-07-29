import streamlit as st

def render_chat():
    """
    Mostrar el Historial
    """
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if message["role"] == "assistant":

                st.caption(
                    f'{message["agent"]} • {message["time"]:.2f} s'
                )
                
                
    # SOLO si hay una respuesta pendiente
    if st.session_state.get("pending_question"):

        with st.chat_message("assistant"):
            st.markdown("Pensando...")