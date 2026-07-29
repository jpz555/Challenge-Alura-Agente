import streamlit as st


def render_input(app):
    """
    Llama a app.ask() -> no conoce nada de LangGraph
    """
    if "pending_question" in st.session_state:
        question = st.session_state.pending_question
        
        del st.session_state.pending_question
        
        response = app.ask(question)
        
        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":response.response,
                "agent": response.current_agent,
                "time": response.execution_time
                
            }
        )
        st.rerun()
    
    
    question = st.chat_input("Haz una pregunta...")

    if question:   
        st.session_state.messages.append(
            {
                "role":"user",
                "content":question
            }
        )
        st.session_state.pending_question = question
        # Refrescar la pantalla para que aparezca la pregunta de usuario en el inicio
        st.rerun()

