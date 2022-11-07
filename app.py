import streamlit as st


import Crypto_Dashboard

pages = {'Crypto_Dashboard': Crypto_Dashboard}

choice = st.sidebar.radio("Choice your page: ",tuple(pages.keys()))
page = pages[choice]
page.main()




