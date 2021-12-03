list_of_books = ('Romeo and Juliet': 'William Shakespeare',
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
'I Giorni Dell Eternita' : 'Ken Follet',
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
'Il Nome Della Rosa' : 'Umberto Eco',
'Intelligenza Emotiva' : 'Daniel Goleman',
'Cosa vuoi davvero?' : 'Roberto Re',
'Intelligenza emotiva' : 'Daniel Goleman',
'Madame Bovary' : 'Gustave Flaubert',
'Jane Eyre' : 'Charlotte Brontë',
'Little Women' : 'Louisa May Alcott',
'Anna Karenina' : 'Leo Tolstoy',
'The Alchemist' : 'Paulo Coelho',
'The Da Vinci Code' : 'Dan Brown',
'The Three Musketeers' : 'Alexandre Dumas',
'Les Miserables' : 'Victor Hugo',
'War and Peace' : 'Leo Tolstoy',
'Treasure Island' : ' Robert Louis Stevenson',
'David Copperfield' : 'Charles Dickens',
'Charlie And The Chocolate Factory' : 'Roald Dahl',
'Jane Eyre' : 'Charlotte Brontë',
'Crime And Punishment' : 'Fyodor Dostoyevsky',
'Memoirs Of A Geisha' : 'Arthur Golden',
'Matilda' : 'Roald Dahl',
'Dracula' : 'Bram Stoker',
'The Green Mile' : 'Stephen King',
'It' : 'Stephen King',
'Thief Of Time' : 'Terry Pratchett',
'Moby Dick' : 'Herman Melville',
'Oliver Twist' : 'Charles Dickens',
'The Witches' : 'Roald Dahl',
'Frankenstein' : 'Mary Shelley',
'American Psycho' : 'Bret Easton Ellis',
<<<<<<< HEAD
)


=======
'People We Meet on Vacation': 'Emily Henry',
'Malibu Rising' : 'Taylor Jenkins Reid',
'The Four Winds' : 'Kristin Hannah',
'The Last Thing He Told Me' : 'Laura Dave',
'The Lincoln Highway' : 'Amor Towles',
'Project Hail Mary' : 'Andy Weir',
'Klara and the Sun' : 'Kazuo Ishiguro',
'The Push' : 'Ashley Audrain',
'Beautiful World, Where Are You' : 'Sally Rooney',
'Apples Never Fall' : 'Laine Moriarty',
'Under the Whispering Door' : 'T.J. Klune',
'Cloud Cuckoo Land' : 'Anthony Doerr',
'Crying in H Mart: A Memoir' : 'Michelle Zauner',
'Think Again: The Power of Knowing What You Dont Know' : 'Adam Grant',
'Between Two Kingdoms: A Memoir of a Life Interrupted' : 'Suleika Jaquad',
'The Anthropocene Reviewed' : 'John Green',
'How To Avoid A Climate Disaster: The Solutions We Have and the Breakthroughs We Need' : 'Bill Gates',
'What Happened To You?: Conversations on Trauma, Resilience, and Healing' : 'Oprah Winfrey',
'Empire of Pain: The Secret History of the Sackler Dynasty' : 'Patrick Radden Keefe,
'The Sum of Us: What Racism Costs Everyone and How We Can Prosper Together' : 'Heather McGhee',
}
>>>>>>> 82d7f56682c4018841e88a23541bf83f8b757c1d



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
