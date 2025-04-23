import streamlit as st
import time

st.set_page_config(page_title="Lettera per Francesco", page_icon="❤️", layout="centered")

st.markdown("<h1 style='text-align: center;'>Lettera per Francesco 💖</h1>", unsafe_allow_html=True)
st.markdown("---")

testo = """
Ciao amore mio... eccomi qui... a tentare di entrare nel tuo mondo da IT per esprimerti il mio amore ❤️.

Oggi il mio Francescolo compie 26 anni ed è quindi un'ottima occasione per esprimerti i miei sentimenti.

Il 30 Maggio 2024 è stata la prima volta che siamo usciti insieme... doveva essere un semplice aperitivo e invece ci siamo ritrovati a parlare per 4 ore...

Da quel giorno è cominciato tutto...

E non dimenticherò mai quel 26 luglio, quando a notte fonda mi hai detto: "vuoi essere la mia ragazza?" ❤️

Poi a settembre è arrivato il nostro primo viaggio insieme, e quella è stata la conferma ufficiale che insieme stiamo benissimo.

Sei la mia pace, la mia sicurezza... sei la persona che voglio vedere quando non ho voglia di vedere nessuno, la persona che mi ha capita, la persona che mi fa sentire amata ogni giorno

Spero di poter presto condividere la quotidianita con te, per poterci godere la vita insieme... è il mio sogno.

Anche se te l'ho già detto voglio ripetertelo... averti nella vita mi ha migliorata e mi sta migliorando tantissimo, hai un impatto enorme... ho trovato l'amore e si sei proprio tu

Oggi voglio farti un mondo di auguri amore, ti amo davvero tantissimo, sei speciale e unico ❤️ 

Buon compleanno amore mio. ❤️
  
Giada 💖

Ps. non ci sto capendo nulla con sti linguaggi, spero tutto funzioni lol ti amo ciaociao

"""

for riga in testo.split("\n"):
    st.write(riga)
    time.sleep(0.4)

st.markdown("---")
st.markdown("```\n      ******       ******\n    **********   **********\n  ************* *************\n ******************************\n ******************************\n ******************************\n  ****************************\n    ************************\n      ********************\n        ****************\n          ************\n            ********\n              ****\n               **\n```")
