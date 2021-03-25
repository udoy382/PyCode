# Coroutines In Python #77

def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("next mothod run")
search.send("harry")

search.close()

# input("Press any key")
# search.send("joker")
# input("Press any key")
# search.send("like this vide")
# input("Press any key")
# search.send("hello last")