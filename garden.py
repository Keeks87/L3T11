import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define a list of garden path sentences
gardenpathSentences = ["John Smith lives in New York.",
                       "The cat chased the mouse.",
                       "The Eiffel Tower is in Paris.",
                       "Albert Einstein was a brilliant physicist.",
                       "The government plans to raise taxes were met with resistance."]

# Loop through each sentence in the list
for sentence in gardenpathSentences:
    # Parse the sentence using the loaded language model
    doc = nlp(sentence)
    # Print the original sentence
    print("\nSentence: ", sentence)
    # Print the entities found in the sentence
    print("Entities: ")
    for ent in doc.ents:
        # Print the text of the entity and the entity label
        print(ent.text, ent.label_)
