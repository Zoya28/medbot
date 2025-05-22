import streamlit as st
from backend import qa_chain


@st.cache_resource
def init():
    return qa_chain


def main():
    st.set_page_config(
        page_title="🩺 MedChat - Your AI Medical Assistant", layout="wide"
    )

    st.markdown("<h1 style='color:#2d6a4f;'>💬 MedChat</h1>", unsafe_allow_html=True)
    st.markdown(
        "<h4 style='color:#588157;'>Your friendly AI medical assistant 🩺💛</h4>",
        unsafe_allow_html=True,
    )

    st.sidebar.title("🧾 Chat History")
    if "all_sessions" not in st.session_state:
        st.session_state.all_sessions = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if st.sidebar.button("🗑️ New Chat"):
        if st.session_state.chat_history:
            st.session_state.all_sessions.append(st.session_state.chat_history)
        st.session_state.chat_history = []

    for idx, session in enumerate(st.session_state.all_sessions[::-1]):
        with st.sidebar.expander(
            f"Session {len(st.session_state.all_sessions) - idx}", expanded=False
        ):
            for role, message in session:
                icon = "🧍" if role == "user" else "🩺"
                st.markdown(f"{icon} **{role.title()}:** {message}")

    bot = init()

    user_input = st.chat_input("Type your symptoms or question here...")

    if user_input:
        st.session_state.chat_history.append(("user", user_input))
        with st.spinner("MedBot is diagnosing your symptoms...🧠💊"):
            response = bot.invoke({"query": user_input})
            bot_answer = response["result"]
        st.session_state.chat_history.append(("bot", bot_answer))

    for role, message in st.session_state.chat_history:
        with st.container():
            if role == "user":
                with st.chat_message("user", avatar="🧍"):
                    st.markdown(f"**You:**  {message}")
            else:
                with st.chat_message("assistant", avatar="🩺"):
                    st.markdown(f"**MedBot:** {message}")


if __name__ == "__main__":
    main()
