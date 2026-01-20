import streamlit as st
st.set_page_config(page_title="Multi-language Dictionary",
layout="centered")

st.title("Multi-Language Dictionary App")

dictionary = {
    "jukun":{
    "Water" : "Jyape",
    "School" : "Manta",
    "Good evening" : "Kyebara",
    "How are you" : "Foni",
    "One" : "Zum",
    "Help" : "Sa-zam",
    "Girl" : "Wa'a",
    "Write" : "Ba",
    "Town" : "Sunwan",
    "Fire" : "Puru",
    "Please" : "Sa'akuri",
    "Good morning" : "Kyabeni",
    "Hand" :"Avoo",
    "Come" : "Bi'",
    "Mountain" : "Akwen",
    "Stomach" : "Afin",
    "Foot" : "Abee",
    "Take" : "Pann",
    "House" : "Ta'an",
    "Forget" : "Mujin"
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
    "I/me" : "Àm",
   "you" : "Owò",
   "we/us" : "Alò",
   "eye" : "Eyì",
   "Mouth" : "Ókònú",
   "Ear" : "Àhò",
   "breast" : "Àmé",
   "hand" : "Ìgàlà",
   " Good evening " : "Nma chi",
   "we" : "Alo",
   "one" : "Áyà",
   "how is the day" : "Iche be",
   "thank you" : "Ahinya",
   "water" : "Enyi",
   "Fire" : "Èlé",
   "my child" : "Oyìm",
   "person" : "Ótú",
   "Chair" : "Egà",
   "queen" : "òchànyà",
   "house" : "òfi"

}
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

