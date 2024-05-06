import streamlit as st
from dotenv import load_dotenv
import replicate
import os

load_dotenv()
replicate_api_token = os.getenv("REPLICATE_API_TOKEN")



