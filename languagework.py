jukun = {
    "Water" : "Zape",
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



languages = {
    "jukun" : jukun,
    "yoruba" : yoruba,
}

print("Language Translator")
print("choose a Language: jukun,yoruba, ")

language =  input("Enter Language:")

if language not in languages:
    print("Language not found,input right language")
else:
    english_word = input("Enter a English word to translate")

    if english_word in languages[language]:
        print("translation is:",
        languages[language][english_word])
    else:
        print("word not found in the dictionary")



