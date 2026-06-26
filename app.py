import streamlit as st

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="Wiki-Style Page")

# 2. Initialize the "Memory" (Session State)
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# 3. Sidebar Navigation ("Others")
with st.sidebar:
    st.markdown("##### PRIVATE FILES")
    st.markdown("### Contents")
    st.markdown("[Top](#top)")
    st.markdown("[Introduction](#introduction)")
    st.markdown("[Section 1](#section-1)")
    st.markdown("[Section 2](#section-2)")
    
    st.markdown("---")
    
    st.markdown("### Others")
    # Clicking these updates the 'page' variable in memory
    if st.button("Home"):
        st.session_state.page = "Home"
    if st.button("MIR LORE"):
        st.session_state.page = "Lore"
    if st.button("The Archives Balquest vs Napis"):
        st.session_state.page = "Archives"

# 4. Main Content Logic
# This checks the memory and displays only the correct section
if st.session_state.page == "Home":
    col1, col2 = st.columns([3, 1])

    with col1:
        st.title("APA ITU MIE AYAM???")
        st.markdown("-Wise Man-")
        st.write("-Di sudut dunia yang sering kali terasa kelabu dan membosankan, terselip sebuah anugerah kuliner yang mampu membelah awan mendung dalam jiwa, yaitu semangkuk Mie Ayam yang kehadiran fisiknya saja sudah sanggup membuat sejarah kuliner dunia merasa rendah diri. Ini bukanlah sekadar racikan tepung dan bumbu, melainkan sebuah konspirasi rasa yang dirancang secara kosmik untuk meruntuhkan pertahanan emosional siapa pun yang berani menatapnya, sebuah harmoni magis di mana uap kuahnya mengepul membentuk doa-doa kelezatan yang merayu indra penciuman hingga ke titik nadir kesadaran. Tatkala mangkuk itu mendarat di atas meja, semesta seakan berkonspirasi untuk menghentikan waktu, memaksa seluruh alam raya terdiam demi memberikan penghormatan tertinggi kepada mahakarya yang siap mengubah definisi bahagia manusia menjadi sesederhana satu suapan mie yang kenyal dan penuh rahasia ini.-")
        
        st.header("Pemula")
        st.write("Mie ayam ini bukanlah sekadar santapan, melainkan sebuah mahakarya kuliner yang turun langsung dari kayangan untuk memanjakan lidah manusia biasa.")
        
        st.header("Section 1")
        st.write("Potongan ayam kecap yang bertahta di atasnya bukanlah sekadar daging, melainkan bongkahan harta karun rasa yang siap meledak.")
        
        st.header("Section 2")
        st.write("Menyelesaikan semangkuk Mie Ayam ini adalah sebuah pencapaian spiritual yang mengubah hidup selamanya.")

    with col2:
        st.image("https://via.placeholder.com/300", caption="Legacy Mie Ayam")
        st.markdown("""
        **Side story:** [Mie Ayam terkenal akibat OTMAR sang legenda pesawat yang teragisnya tidak tahu pembuat pesawat pertama. website ini berjutuan untuk informasi yang jarang di ketahui orang lain]""")

elif st.session_state.page == "Lore":
    st.title("MIR LORE")
    st.write("Welcome to the secret lore section. Add your stories about the conspiracy here!")

elif st.session_state.page == "Archives":
    st.title("The Archives: Balquest vs Napis")
    st.write("The history of the great battle goes here...")
