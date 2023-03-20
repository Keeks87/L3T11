Instructions

In this task you will use spaCy, which is an external Python module that must be
installed as previously described. You’ll be required to use the basic functionalities
of spaCy and give a short explanation.

First, read example.py and run it to check that you have installed spaCy correctly.
Feel free to write and run your own example code before doing this task to
become more comfortable with the topic.

Compulsory Task 1

Follow these steps:

    ● Read the introduction about garden path sentences and explore a few of
    the examples on Wikipedia.
    
    ● Create a new Python file called garden.py.
    
    ● Find at least 5 garden path sentences from the web or think up your own.
    
    ● Store the sentences you have identified or created in a list called
    gardenpathSentences
    
    ● Tokenise each sentence in the list and perform entity recognition.
    
    ● Examine how spaCy has categorised each sentence. Then, use
    spacy.explain to look up and print the meaning of entities that you don’t
    understand. For example: print(spacy.explain("FAC"))
    
    ● At the bottom of your file, write a comment about two entities that you
    looked up. For each entity answer the following questions:
        
        ○ What was the entity and its explanation that you looked up?
        
        ○ Did the entity make sense in terms of the word associated with it?
    
    ● Host your solution on a remote Git repo host such as GitHub or GitLab.
    Ensure your repo includes a Dockerfile and README.md instructions on
    how to run it.
    
        ○ If it doesn’t already, please ensure that your repo includes a file
        named requirements.txt to automate the installation of the project’s
        requirements.
        
        ○ Remember to exclude any venv or virtualenv files from your repo.
    
    ● Link to your public remote Git repo in a file named nlp.txt in your Dropbox
    folder.
    