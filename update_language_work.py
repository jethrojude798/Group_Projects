import streamlit as st
st.set_page_config(page_title="Multi-language Dictionary",
layout="centered")

st.title("Multi-Language Dictionary App")

dictionary = {
    "jukun":{
    "water" : "Jyape",
    "school" : "Manta",
    "good evening" : "Kyebara",
    "how are you" : "Foni",
    "one" : "Zum",
    "help" : "Sa-zam",
    "girl" : "Wa'a",
    "write" : "Ba",
    "town" : "Sunwan",
    "fire" : "Puru",
    "please" : "Sa'akuri",
    "good morning" : "Kyabeni",
    "hand" :"Avoo",
    "come" : "Bi'",
    "mountain" : "Akwen",
    "stomach" : "Afin",
    "foot" : "Abee",
    "take" : "Pann",
    "house" : "Ta'an",
    "forget" : "Mujin"
     },

    "yoruba": {
       "me" : "Emi-I o",
       "hello" : "E nle",
       "goodbye" : "O dabo",
       "thank you" : "o se",
       "how are you" : "Bawo ni",
       "i'm fine" : "Mo wa l'ayo",
       "slowly" : "Jeje",
       "where is..." : "Nibi ni",
       "it's okay" : " O taye",
       "i love you" : "Mo n be o",
       "God" : "Olorun",
       "fire" : "Iná",
       "Water" : "Omi",
       "food" : "On je",
       "mother" : "iya",
       "father" : "Baba",
       "Help" : "Egde",
       "money" : "owo",
       "work" : "ise",
       "house" : "ile"
    },

"idoma":{
    "i/me" : "Àm",
   "you" : "Owò",
   "we/us" : "Alò",
   "eye" : "Eyì",
   "mouth" : "Ókònú",
   "ear" : "Àhò",
   "breast" : "Àmé",
   "hand" : "Ìgàlà",
   "good evening " : "Nma chi",
   "we" : "Alo",
   "one" : "Áyà",
   "how is the day" : "Iche be",
   "thank you" : "Ahinya",
   "water" : "Enyi",
   "fire" : "Èlé",
   "my child" : "Oyìm",
   "person" : "Ótú",
   "chair" : "Egà",
   "queen" : "òchànyà",
   "house" : "òfi"
    },

"hausa":{
    "hello/Hi": "sannu",
    "thank you": "Na gode",
    "please": "Don Allah",
    "yes": "Ee",
    "girl": "Yarinya",
    "water": "Ruwa",
    "boy": "Yaro",
    "go": "Tafi",
    "money": "kudi",
    "car": "Mota",
    "come": "zo",
    "king": "sarki",
    "market": "kasuwa",
    "teacher": "malam",
    "house": "gida",
    "no": "A'a",
    "food": "abinchi",
    "delicious": "dadi",
    "fine": "lafiya",
    "congratulations": "barka"
    },

}



language = st.selectbox(
    "Select a language",
    list(dictionary.keys())
)

word = st.text_input("Enter a word").strip().lower()

if st.button("search"):
    if word:
        meaning = dictionary[language].get(word)
        if meaning:
            st.subheader("Meaning")
            st.write(meaning)
        else:
            st.error("Word not found in this language dictionary.")
    else:
        st.warning("Please enter a word")

