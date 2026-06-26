import streamlit as st

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="Wiki-Style Page")

# 2. Sidebar Navigation ("Others")
with st.sidebar:
    st.markdown("### Contents")
    st.markdown("[Top](#top)")
    st.markdown("[Introduction](#introduction)")
    st.markdown("[Section 1](#section-1)")
    st.markdown("[Section 2](#section-2)")
    
    st.markdown("---")
    
    st.markdown("### Others")
    # Add your navigation links here
    st.button("Another Page Link")
    st.button("More Cult Lore")
    st.button("The Archives")

# 3. Main Content Layout
# We split the page: 70% for text, 30% for the side image
col1, col2 = st.columns([3, 1])

with col1:
    st.title("Main Article Title")
    st.markdown("_From the encyclopedia_")
    st.write("---")
    
    st.header("Introduction")
    st.write("Write your introductory paragraph here...")
    
    st.header("Section 1")
    st.write("Write your first main section here...")
    
    st.header("Section 2")
    st.write("Write your second main section here...")

with col2:
    # This acts as the side image box like in image_abab59.jpg
    st.image("https://via.placeholder.com/300", caption="Subject Name")
    st.markdown("""
    **Born:** [Date]  
    **Died:** [Date]  
    **Location:** [Place]  
    """)
