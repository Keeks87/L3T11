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

print()
print(spacy.explain("LOC"))
print(spacy.explain("NORP"))

'''
Q-  At the bottom of your file, write a comment about two entities that you
    looked up. For each entity answer the following questions:

        What was the entity and its explanation that you looked up?

        Did the entity make sense in terms of the word associated with it?

A-  Two entities that I looked up are:

    LOC

        Explanation:
        
            Non-GPE locations, mountain ranges, bodies of water 
        
        Yes, the entity makes sense in terms of the words associated with it.
        For example, in the sentence "John went hiking in the mountains," 
        "mountains" would be categorized as a LOC entity.

    NORP

        Explanation:
        
            Nationalities or religious or political groups
            
        Yes, the entity makes sense in terms of the words associated with it.
        For example, in the sentence "The Irish team won the game," 
        "Irish" would be categorized as a NORP entity.
'''
