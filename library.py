list_of_books = {
'Romeo And Juliet': ['William Shakespeare', 1964],
'1984': ['George Orwell', 1949],
'2001: A Space Odissey': ['Arthur C. Clarke', 1968],
'Pride And Prejudice' : ['Jane Austen', 1813],
'The Great Gatsby' : ['F.Scott Fitzgerald', 1925],
'The Lord Of The Rings' : ['J. R. R. Tolkien', 1937],
'The Old Man And The Sea' : ['Ernest Hemingway', 1951],
'The Picture Of Dorian Gray' : ['Oscar Wilde', 1890],
'A Christmas Carol' : ['Charles Dickens',1843],
'I Promessi Sposi' : ['Alessandro Manzoni', 1827],
'Awaken The Giant Within' : ['Anthony Robbins', 1995],
'La Divina Commedia' : ['Dante Allighieri', 1909],
'Odyssey' : ['Omero', 1937],
'Lo Scudo Di Talos' : ['Valerio Massimo Manfredi', 1988],
'Delitto E Castigo' : ['Dostoevskij', 1967],
'I Giorni Dell Eternita' : ['Ken Follet', 2019],
'Fu Sera Fu Mattina' : ['Ken Follet', 2021],
'La Caduta Dei Giganti' : ['Ken Follet', 2017],
'La Cruna Dell Ago' : ['Ken Follet', 2002],
'Mondo Senza Fine' : ['Ken Follet', 2000],
'L Arte Della Guerra' : ['Sun Tzu', 1948],
'Alla Ricerca Del Tempo Perduto' : ['Marcel Proust', 1967],
'La Coscienza Di Zeno' : ['Italo Svevo', 1965],
'Il Processo' : ['Franz Kafka', 1924],
'Uno, Nessuno, Centomila' : ['Luigi Pirandello', 1929],
'Gita Al Faro' : ['Virginia Wolf', 1980],
'Il Processo' : ['Franz Kafka', 1989],
'La Fabbrica Di Cioccolato' : ['Roald Dahl', 1988],
'Billy Elliot' : ['Melvin Burgess', 1999],
'Il Nome Della Rosa' : ['Umberto Eco', 1979],
'Intelligenza Emotiva' : ['Daniel Goleman', 2001],
'Cosa Vuoi Davvero?' : ['Roberto Re', 2004],
'Intelligenza Emotiva' : ['Daniel Goleman', 2007],
'Madame Bovary' : ['Gustave Flaubert', 1968],
'Jane Eyre' : ['Charlotte Bronte', 1974],
'Little Women' : ['Louisa May Alcott', 1954],
'Anna Karenina' : ['Leo Tolstoy', 1968],
'The Alchemist' : ['Paulo Coelho', 2001],
'The Da Vinci Code' : ['Dan Brown', 2004],
'The Three Musketeers' : ['Alexandre Dumas', 1922],
'Les Miserables' : ['Victor Hugo', 1933],
'War And Peace' : ['Leo Tolstoy', 1931],
'Treasure Island' : ['Robert Louis Stevenson', 1967],
'David Copperfield' : ['Charles Dickens', 1975],
'Jane Eyre' : ['Charlotte Bronte', 1996],
'Memoirs Of A Geisha' : ['Arthur Golden', 1966],
'Matilda' : ['Roald Dahl', 1977],
'Dracula' : ['Bram Stoker', 1966],
'The Green Mile' : ['Stephen King', 1979],
'It' : ['Stephen King', 1986],
'Thief Of Time' : ['Terry Pratchett', 1965],
'Moby Dick' : ['Herman Melville', 1851],
'Oliver Twist' : ['Charles Dickens', 1923],
'The Witches' : ['Roald Dahl', 1945],
'Frankenstein' : ['Mary Shelley', 1890],
'American Psycho' : ['Bret Easton Ellis', 1967],
'People We Meet On Vacation': ['Emily Henry', 1959],
'Malibu Rising' : ['Taylor Jenkins Reid', 2004],
'The Four Winds' : ['Kristin Hannah', 2009],
'The Last Thing He Told Me' : ['Laura Dave', 2017],
'The Lincoln Highway' : ['Amor Towles', 1970],
'Project Hail Mary' : ['Andy Weir', 1957],
'Klara And The Sun' : ['Kazuo Ishiguro', 1995],
'The Push' : ['Ashley Audrain', 1992],
'Beautiful World, Where Are You' : ['Sally Rooney', 1986],
'Apples Never Fall' : ['Laine Moriarty', 1984],
'Under The Whispering Door' : ['T.J. Klune', 1998],
'Cloud Cuckoo Land' : ['Anthony Doerr', 1957],
'Crying In H Mart: A Memoir' : ['Michelle Zauner', 1924],
'Think Again: The Power Of Knowing What You Dont Know' : ['Adam Grant', 1990],
'Between Two Kingdoms: A Memoir Of A Life Interrupted' : ['Suleika Jaquad', 2007],
'The Anthropocene Reviewed' : ['John Green', 2004],
'How To Avoid A Climate Disaster: The Solutions We Have And The Breakthroughs We Need' : ['Bill Gates', 2018],
'What Happened To You?: Conversations On Trauma, Resilience, And Healing' : ['Oprah Winfrey', 2012],
'Empire Of Pain: The Secret History Of The Sackler Dynasty' : ['Patrick Radden Keefe', 2003],
'The Sum Of Us: What Racism Costs Everyone And How We Can Prosper Together' : ['Heather McGhee', 2007],
}

def check_book(title):
    if title in list_of_books:
        field = list_of_books[title]
        author = field[0]
        #genre = field[1]
        year = field[2]
        #words = field[3]
        
        print("The title {} is written by {}, and it was published in {}".format(title, author, year,))
        #print ("The title {} is a {} book written by {}, published in year {} and counts {} words".format(title, author, genre, year, words,))
        
    else:
        print("The title {} is not present in our catalogue".format(title))

def check_author(author_name):
    found = False
    for title, field in list_of_books.items():
        author = field[0]
        year = field [1]
        if author == author_name:
            print("{} published {} in {} ".format(author_name, title, year))
            found = True
    if not found:
        print("Sorry we don't have any book by {} ".format(author_name))
