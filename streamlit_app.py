import streamlit as st

# Dati di esempio per i menu a tendina
opzioni_menu1 = ["Opzione 1A", "Opzione 1B", "Opzione 1C"]
opzioni_menu2 = ["Opzione 2A", "Opzione 2B", "Opzione 2C"]

# Titolo dell'applicazione
st.title("Che quota vuoi controllare?")

# Menu a tendina 1
scelta_menu1 = st.selectbox("Tipo di materiale", opzioni_menu1)

# Menu a tendina 2
scelta_menu2 = st.selectbox("Paese di origine", opzioni_menu2)

# Visualizzazione delle scelte effettuate
st.write("Hai selezionato:")
st.write(f"- Materiale: {scelta_menu1}")
st.write(f"- Paese di origine: {scelta_menu2}")
