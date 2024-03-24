import streamlit as st

def app():
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; height: 20vh;">
                <h3>Thatavarthi Tulasiram</h3>
                <p>(Team Lead)</p>
        </div>
        <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; height: 20vh;">
                <h3>Thota SriRam Pavan</h3>
                <p>(Backend Developer)</p>
        </div>
        <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; height: 20vh;">
                <h3>Sypireddy Shanmukha</h3>
                <p>(Frontend Developer)</p>
        </div>
        <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; height: 20vh;">
                <h3>Vangalapudi Abhishek Wesly</h3>
                <p>(Data Scientist)</p>
        </div>
        """,
        unsafe_allow_html=True
    )

