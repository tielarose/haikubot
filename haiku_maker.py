import spacy
nlp = spacy.load("en_core_web_sm")

file = "hitchhikers_guide.txt"
doc = nlp(open(file).read())

pattern = [{'POS': 'ADJ'},
           {'POS': 'NOUN'}]
