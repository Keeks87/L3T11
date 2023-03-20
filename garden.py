import spacy

# Load the small English model
nlp = spacy.load("en_core_web_sm")

# Define the garden path sentences
gardenpathSentences = [
    "The old man the boat.",
    "The horse raced past the barn fell.",
    "The chicken is ready to eat.",
    "The lettuce was too hot to eat.",
    "The dog that I had really loved bones."
]

# Loop through each sentence and tokenize it
for sentence in gardenpathSentences:
    doc = nlp(sentence)

    # Loop through each token in the sentence and print its text and entity label
    for token in doc:
        print(token.text, token.ent_type_)

        # If the entity label is not recognized, look it up using spacy.explain
        if token.ent_type_ == "":
            print(spacy.explain(token.ent_type_))

    # Print a blank line to separate each sentence
    print()
