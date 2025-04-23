import streamlit as st
import time

st.set_page_config(page_title="Lettera per Francesco", page_icon="❤️", layout="centered")

st.markdown("<h1 style='text-align: center;'>Lettera per Francesco 💖</h1>", unsafe_allow_html=True)
st.markdown("---")

testo = """
Ciao amore mio... eccomi qui... a tentare di entrare nel tuo mondo 🌍 per esprimerti il mio amore ❤️.

Oggi il mio Francescolo compie 26 anni ed è quindi un'ottima occasione per esprimerti i miei sentimenti.

Il 30 Maggio 2024 è stata la prima volta che siamo usciti insieme... doveva essere un semplice aperitivo e invece ci siamo ritrovati a parlare per 4 ore...

Da quel giorno è cominciato tutto...

E non dimenticherò mai quel 26 luglio, quando a notte fonda mi hai detto: "vuoi essere la mia ragazza?" ❤️

Poi a settembre è arrivato il nostro primo viaggio insieme, e quella è stata la conferma ufficiale che stiamo benissimo insieme.

Tu sei la mia dolcezza, il mio sorriso, la mia anima gemella.

Ti amo tanto. Buon compleanno amore mio. ❤️

Con amore,  
Giada 💖
"""

for riga in testo.split("\n"):
    st.write(riga)
    time.sleep(0.4)

st.markdown("---")
st.markdown("```\n      ******       ******\n    **********   **********\n  ************* *************\n ******************************\n ******************************\n ******************************\n  ****************************\n    ************************\n      ********************\n        ****************\n          ************\n            ********\n              ****\n               **\n```")
