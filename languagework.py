jukun = {
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
     }

yoruba = {
       "me" : "Emi-I o",
       "Hello" : "E nle",
       "Goodbye" : "O dabo",
       "Thank you" : "o se",
       "How are you" : "Bawo ni",
       "I'm fine" : "Mo wa l'ayo",
       "slowly" : "Jeje",
       "where is..." : "Nibi ni",
       "it's okay" : " O taye",
       "I love you" : "Mo n be o",
       "God" : "Olorun",
       "fire" : "Iná",
       "Water" : "Omi",
       "food" : "On je",
       "mother" : "iya",
       "father" : "Baba",
       "Help" : "Egde",
       "Money" : "owo",
       "work" : "ise",
       "house" : "ile"
          }

idoma = {
    "I/me" : "Àm",
   "you" : "Owò",
   "we/us" : "Alò",
   "eye" : "Eyì",
   "Mouth" : "Ókònú",
   "Ear" : "Àhò",
   "Breast" : "Àmé",
   "Hand" : "Ìgàlà",
   " Good evening " : "Nma chi",
   "we" : "Alo",
   "one" : "Áyà",
   "How is the day" : "Iche be",
   "Thank you" : "Ahinya",
   "Water" : "Enyi",
   "Fire" : "Èlé",
   "My child" : "Oyìm",
   "person" : "Ótú",
   "Chair" : "Egà",
   "Queen" : "òchànyà",
   "house" : "òfi"

}
igala={
"Morning" : "Odudu",
  "When" : "Iko",
  "Where" : "Ugbo",
  "What" : "Ewnu",
  "Evening" : "Ane",
  "God" : "Ojo, Ojowa",
  "Learning" : "Ukoche",
 "Father" : "Attah",
 "Mother" : "Iye",

"Sibling" : "Omaye",
 "Door" : "Ona",
 "Road" : "Ona",
 "Song" : "Eli",
 "Man" : "Onekele",
 "Woman" : "Onobule",
 "light" :" Una",
 "Fire" : "Una",
 "Water" : "Omi",
 "Child" : "Oma",
 "My siblings" : "Amomaye"

}


languages = {
    "jukun" : jukun,
    "yoruba" : yoruba,
    "idoma" : idoma,
    "igala" : igala,
}

print("Language Translator")
print("choose a Language: jukun,yoruba,idoma,igala ")

language =  input("Enter Language:")

if language not in languages:
    print("Language not found,input right language")
else:
    english_word = input("Enter a English word to translate")

    if english_word in languages[language]:
        print("translation is:",
        languages[language][english_word])
    else:
        print("word not found in the dictionary wait for update next year")



