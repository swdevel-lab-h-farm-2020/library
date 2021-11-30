list_of_books = {'Romeo and Juliet': 'William Shakespeare',
'1984': 'George Orwell',
'2001: a Space Odissey': 'Arthur C. Clarke',
'Pride and Prejudice' : 'Jane Austen',
'The Great Gatsby' : 'F.Scott Fitzgerald',
'The Lord of the Rings' : 'J. R. R. Tolkien',
'The Old Man and the Sea' : 'Ernest Hemingway',
'The Picture of Dorian Gray' : 'Oscar Wilde',
'A Christmas Carol' : 'Charles Dickens',
'Intelligenza emotiva' : 'Daniel Goleman',

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
