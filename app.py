import streamlit as st
from dotenv import load_dotenv
import replicate
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from streamlit_google_auth import Authenticate

AUTHORIZATION_CODE = "code"

load_dotenv()
replicate_api_token = os.getenv("REPLICATE_API_TOKEN")
oauth_client_id = os.getenv("GMAIL_CLIENT_ID")

authenticator = Authenticate(
    secret_credentials_path='oauth2_secret.json',
    cookie_name='cookie_name',
    cookie_key='one',
    redirect_uri='http://localhost:8501',
)


def main():
    authenticator.check_authentification()
    if not st.session_state['connected']:
        st.write('Hello, welcome to Cherry Mail. Please login to continue.')
    authenticator.login()
    if st.session_state['connected']:
        st.image(st.session_state['user_info'].get('picture'))
        st.write(f"Hello, {st.session_state['user_info'].get('name')}")
        st.write(f"Your email is {st.session_state['user_info'].get('email')}")
        if st.button('Log out'):
            authenticator.logout()


if __name__ == "__main__":
    main()

