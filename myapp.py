import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")
col1, col2 = st.columns(2)
with col1:
  st.subheader("Aprilia")
  st.image("./aprilia.jpg", caption="Aprilia", width=300,use_column_width=True)
  st.write("Aprilia bike")
with col2:
  st.subheader("Car")
  st.image("./download.jpg", caption="Car", width=300,use_column_width=True)
  st.write("mercedes")
