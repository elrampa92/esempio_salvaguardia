import streamlit as st

# Dati di esempio per i menu a tendina
opzioni_menu1 = ["Opzione 1A", "Opzione 1B", "Opzione 1C"]
opzioni_menu2 = ["Opzione 2A", "Opzione 2B", "Opzione 2C"]
opzioni_menu3 = ["Opzione 3A", "Opzione 3B", "Opzione 3C"]

# Titolo dell'applicazione
st.title("Webapp con 3 Menu a Tendina")

# Menu a tendina 1
scelta_menu1 = st.selectbox("Seleziona un'opzione dal Menu 1", opzioni_menu1)

# Menu a tendina 2
scelta_menu2 = st.selectbox("Seleziona un'opzione dal Menu 2", opzioni_menu2)

# Menu a tendina 3
scelta_menu3 = st.selectbox("Seleziona un'opzione dal Menu 3", opzioni_menu3)

# Visualizzazione delle scelte effettuate
st.write("Hai selezionato:")
st.write(f"- Menu 1: {scelta_menu1}")
st.write(f"- Menu 2: {scelta_menu2}")
st.write(f"- Menu 3: {scelta_menu3}")
