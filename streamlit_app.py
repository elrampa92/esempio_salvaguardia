import streamlit as st
import random

st.image("https://github.com/elrampa92/esempio_salvaguardia/blob/main/GetAttachmentThumbnail.jpg?raw=true", use_column_width=True)

# Dati di esempio per i menu a tendina
opzioni_menu1 = ["Coils a caldo/decapati", "Coils a freddo", "Coils zincati 4A", "Coils zincati 4B", "Coils preverniciati"]
opzioni_menu2 = ["India", "Turchia", "Korea", "Taiwan", "Altri paesi terzi ..."]

# Titolo dell'applicazione
st.title("Che quota vuoi controllare?")

# Menu a tendina 1
scelta_menu1 = st.selectbox("Tipo di materiale", opzioni_menu1)

# Menu a tendina 2
scelta_menu2 = st.selectbox("Paese di origine", opzioni_menu2)

quota_iniziale = random.randint(5000, 66000)
spesa = random.randint(3000, min(29999, quota_iniziale))
quota_disponibile = quota_iniziale - spesa
percentuale_disponibile = (quota_disponibile / quota_iniziale) * 100


# Visualizzazione delle scelte effettuate
st.write("Hai selezionato:")
st.write(f"- Materiale: {scelta_menu1}")
st.write(f"- Paese di origine: {scelta_menu2}")


st.write(f"Quota iniziale: {quota_iniziale} tons")
st.write(f"Quota utilizzata: {spesa} tons")
st.write(f"Quota disponibile: {quota_disponibile} tons")
st.write(f"Percentuale disponibile: {percentuale_disponibile:.2f}%")

# Barra di avanzamento
st.progress(int(percentuale_disponibile))


# Messaggio in base alla percentuale disponibile
if percentuale_disponibile > 90:
    st.markdown("<h3 style='color:red;'>ATTENZIONE, QUOTA CRITICA!</h3>", unsafe_allow_html=True)
else:
    st.markdown("<h3 style='color:green;'>QUOTA DISPONIBILE, NON CRITICA</h3>", unsafe_allow_html=True)


if st.button("Genera PDF"):
    # Qui dovresti inserire la logica per generare il PDF
    # Esempio (richiede l'installazione di reportlab):
    # from reportlab.pdfgen import canvas
    # c = canvas.Canvas("output.pdf")
    # c.drawString(100, 750, f"Quota iniziale: {quota_iniziale} tons")
    # c.drawString(100, 730, f"Quota disponibile: {quota_disponibile} tons")
    # c.save()
    st.write("PDF generato!")  # Sostituisci con la tua logica










