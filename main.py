import streamlit as st
from streamlit_option_menu import option_menu

import about, account, home, Ayurvedic_Plants

# Set page configuration
st.set_page_config(page_title="AyurVedic Plant Detection")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title='Menu',
                options=['Home', 'Account', 'Ayurvedic Plants', 'About','Predict'],
                icons=['house-fill', 'person-circle', 'book-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "black"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": "orange"},
                }
            )
        if app == 'Home':
            home.app()
        elif app == 'Account':
            account.app()
        elif app == 'Ayurvedic Plants':
            Ayurvedic_Plants.app()
        elif app == 'About':
            about.app()
        elif app === 'Predict':
            predict.app()

    run()
