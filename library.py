list_of_books = {
'Romeo And Juliet': ['William Shakespeare', 1964, 'Tragedy'],
'1984': ['George Orwell', 1949, 'Science Fiction'],
'2001: A Space Odissey': ['Arthur C. Clarke', 1968, 'Science Fiction'],
'Pride And Prejudice' : ['Jane Austen', 1813, 'Romance'],
'The Great Gatsby' : ['F.Scott Fitzgerald', 1925, 'Tragedy'],
'The Lord Of The Rings' : ['J. R. R. Tolkien', 1937, 'Fantasy'],
'The Old Man And The Sea' : ['Ernest Hemingway', 1951, 'Fiction'],
'The Picture Of Dorian Gray' : ['Oscar Wilde', 1890, 'Philosophy'],
'A Christmas Carol' : ['Charles Dickens',1843, 'Drama'],
'I Promessi Sposi' : ['Alessandro Manzoni', 1827, 'Romance'],
'Awaken The Giant Within' : ['Anthony Robbins', 1995, 'Self growth'],
'La Divina Commedia' : ['Dante Allighieri', 1909, 'Epic poem'],
'Odyssey' : ['Omero', 1937, 'Epic poem'],
'Lo Scudo Di Talos' : ['Valerio Massimo Manfredi', 1988, 'Romance'],
'Delitto E Castigo' : ['Dostoevskij', 1967, 'Tragedy'],
'I Giorni Dell Eternita' : ['Ken Follet', 2019, 'Fition'],
'Fu Sera Fu Mattina' : ['Ken Follet', 2021, 'Fiction'],
'La Caduta Dei Giganti' : ['Ken Follet', 2017, 'Romance'],
'La Cruna Dell Ago' : ['Ken Follet', 2002, 'Thriller'],
'Mondo Senza Fine' : ['Ken Follet', 2000, 'Fiction'],
'L Arte Della Guerra' : ['Sun Tzu', 1948, 'Treaty'],
'Alla Ricerca Del Tempo Perduto' : ['Marcel Proust', 1967, 'Romance'],
'La Coscienza Di Zeno' : ['Italo Svevo', 1965, 'Romance'],
'Il Processo' : ['Franz Kafka', 1924, 'Romance'],
'Uno, Nessuno, Centomila' : ['Luigi Pirandello', 1929, 'Romance'],
'Gita Al Faro' : ['Virginia Wolf', 1980, 'Romance'],
'Il Processo' : ['Franz Kafka', 1989, 'Romance'],
'La Fabbrica Di Cioccolato' : ['Roald Dahl', 1988, 'Adventure'],
'Billy Elliot' : ['Melvin Burgess', 1999, 'Musical'],
'Il Nome Della Rosa' : ['Umberto Eco', 1979, 'Romance'],
'Intelligenza Emotiva' : ['Daniel Goleman', 2001, 'Self growth'],
'Cosa Vuoi Davvero?' : ['Roberto Re', 2004, 'Empowerment'],
'Madame Bovary' : ['Gustave Flaubert', 1968, 'Romance'],
'Jane Eyre' : ['Charlotte Bronte', 1974, 'Fiction'],
'Little Women' : ['Louisa May Alcott', 1954, 'Romance'],
'Anna Karenina' : ['Leo Tolstoy', 1968, 'Romance'],
'The Alchemist' : ['Paulo Coelho', 2001, 'Romance'],
'The Da Vinci Code' : ['Dan Brown', 2004, 'Romance'],
'The Three Musketeers' : ['Alexandre Dumas', 1922, 'Romance'],
'Les Miserables' : ['Victor Hugo', 1933, 'Romance'],
'War And Peace' : ['Leo Tolstoy', 1931, 'Romance'],
'Treasure Island' : ['Robert Louis Stevenson', 1967, 'Romance'],
'David Copperfield' : ['Charles Dickens', 1975, 'Romance'],
'Jane Eyre' : ['Charlotte Bronte', 1996, 'Romance'],
'Memoirs Of A Geisha' : ['Arthur Golden', 1966, 'Memoire'],
'Matilda' : ['Roald Dahl', 1977, 'Humor'],
'Dracula' : ['Bram Stoker', 1966, 'Thriller'],
'The Green Mile' : ['Stephen King', 1979, 'Documentary'],
'It' : ['Stephen King', 1986, 'Science fiction'],
'Thief Of Time' : ['Terry Pratchett', 1965, 'Fantasy'],
'Moby Dick' : ['Herman Melville', 1851, 'Epic'],
'Oliver Twist' : ['Charles Dickens', 1923, 'Adventure'],
'The Witches' : ['Roald Dahl', 1945, 'Commedy'],
'Frankenstein' : ['Mary Shelley', 1890, 'Science fiction'],
'American Psycho' : ['Bret Easton Ellis', 1967, 'Horror'],
'People We Meet On Vacation': ['Emily Henry', 1959, 'Romance'],
'Malibu Rising' : ['Taylor Jenkins Reid', 2004, 'Fiction'],
'The Four Winds' : ['Kristin Hannah', 2009, 'Thriller'],
'The Last Thing He Told Me' : ['Laura Dave', 2017, 'Thriller'],
'The Lincoln Highway' : ['Amor Towles', 1970, 'Fiction'],
'Project Hail Mary' : ['Andy Weir', 1957, 'Romance'],
'Klara And The Sun' : ['Kazuo Ishiguro', 1995, 'Romance'],
'The Push' : ['Ashley Audrain', 1992, 'Thriller'],
'Beautiful World, Where Are You' : ['Sally Rooney', 1986, 'Romance'],
'Apples Never Fall' : ['Laine Moriarty', 1984, 'Thriller'],
'Under The Whispering Door' : ['T.J. Klune', 1998, 'Romance'],
'Cloud Cuckoo Land' : ['Anthony Doerr', 1957, 'Science fiction'],
'Crying In H Mart: A Memoir' : ['Michelle Zauner', 1924, 'Momoir'],
'Think Again: The Power Of Knowing What You Dont Know' : ['Adam Grant', 1990, 'Self growth'],
'Between Two Kingdoms: A Memoir Of A Life Interrupted' : ['Suleika Jaquad', 2007, 'Memoir'],
'The Anthropocene Reviewed' : ['John Green', 2004, 'Commentary'],
'How To Avoid A Climate Disaster: The Solutions We Have And The Breakthroughs We Need' : ['Bill Gates', 2018, 'Essay'],
'What Happened To You?: Conversations On Trauma, Resilience, And Healing' : ['Oprah Winfrey', 2012, 'Self growth'],
'Empire Of Pain: The Secret History Of The Sackler Dynasty' : ['Patrick Radden Keefe', 2003, 'Crime'],
'The Sum Of Us: What Racism Costs Everyone And How We Can Prosper Together' : ['Heather McGhee', 2007, 'Commedy'],
}

def check_book(title):
    if title in list_of_books:
        field = list_of_books[title]
        author = field[0]
        year = field[1]
        genre = field[2]
        
        print("The title {} is written by {}, and it was published in {}".format(title, author, year,))
        #print ("The title {} is a {} book written by {}, published in year {} and counts {} words".format(title, author, genre, year, words,))
        
    else:
        print("The title {} is not present in our catalogue".format(title))

def check_author(author_name):
    found = False
    for title, field in list_of_books.items():
        author = field[0]
        year = field[1]
        genre = field[2]
        if author == author_name:
            print("{} published {} in {} ".format(author_name, title, year))
            found = True

    if not found:
        print("Sorry we don't have any book by {} ".format(author_name))

def check_year(year):
    found = False
    for title, field in list_of_books.items():
        author = field[0]
        pub_year = field[1]
        genre = field[2]
        if year == pub_year:
            print("{} published {} in {} ".format(author, title, year))
            found = True

    if not found:
        print("Sorry we don't have any books published in the year {} ".format(year))
        
def check_genre(book_genre):
    found = False
    for title, field in list_of_books.items():
        author = field[0]
        pub_year = field[1]
        genre = field[2]
        if genre == book_genre:
            print("{} of {} is a {} ".format(title, author, genre))
            found = True

    if not found:
        print("Sorry there aren't books in the {} category, try again".format(genre))
