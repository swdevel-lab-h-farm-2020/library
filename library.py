list_of_books = {'Romeo and Juliet': 'William Shakespeare',
'1984': 'George Orwell',
'2001: a Space Odissey': 'Arthur C. Clarke',
'Pride and Prejudice' : 'Jane Austen',
'The Great Gatsby' : 'F.Scott Fitzgerald',
'The Lord of the Rings' : 'J. R. R. Tolkien',
'The Old Man and the Sea' : 'Ernest Hemingway',
'The Picture of Dorian Gray' : 'Oscar Wilde',
'A Christmas Carol' : 'Charles Dickens',
'The Name Of The Rose' : 'Umberto Eco',

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
