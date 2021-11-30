list_of_books = {'Romeo and Juliet': 'William Shakespeare',
'1984': 'George Orwell',
'2001: A Space Odissey': 'Arthur C. Clarke',
'Pride And Prejudice' : 'Jane Austen',
'The Great Gatsby' : 'F.Scott Fitzgerald',
'The Lord Of The Rings' : 'J. R. R. Tolkien',
'The Old Man And The Sea' : 'Ernest Hemingway',
'The Picture Of Dorian Gray' : 'Oscar Wilde',
'A Christmas Carol' : 'Charles Dickens',
'I Promessi Sposi' : 'Alessandro Manzoni',
'Awake The Giant Within' : 'Tony Robbins',
'La Divina Commedia' : 'Dante Allighieri',
'Odissey' : 'Omero',
'Lo Scudo Di Talos' : 'Valerio Massimo Manfredi',
'Delitto E Castigo' : 'Dostoevskij',
'I Giorni Dell Eternità' : 'Ken Follet',
'It' : 'Stephen King',
'Fu Sera Fu Mattina' : 'Ken Follet',
'La Caduta Dei Giganti' : 'Ken Follet',
'La Cruna Dell Ago' : 'Ken Follet',
'Mondo Senza Fine' : 'Ken Follet',
'L Arte Della Guerra' : 'Sun Tzu',
'Alla Ricerca Del Tempo Perduto' : 'Marcel Proust',
'La Coscienza Di Zeno' : 'Italo Svevo',
'Il Processo' : 'Franz Kafka',
'Uno, Nessuno, Centomila' : 'Luigi Pirandello',
'Gita Al Faro' : 'Virginia Wolf',
'Il Processo' : 'Franz Kafka',
'Matilda' : 'Roald Dahl',
'La Fabbrica Di Cioccolato' : 'Roald Dahl',
'Billy Elliot' : 'Melvin Burgess',

                 }

'Il nome della rosa' : 'Umberto Eco',
'Intelligenza emotiva' : 'Daniel Goleman',

}



def check_book(title):
    if title in list_of_books:
        print("The book {} is written by {}".format(title, list_of_books[title]))
    else:
        print("Sorry, we do not have {}".format(title))

def check_author(author_name):

    found = False
    for title, author in list_of_books.items():
        if author == author_name:
            print("{} wrote {}".format(author_name, title))
            found = True

    if not found:
        print("Sorry, {} is not present.".format(author_name))
