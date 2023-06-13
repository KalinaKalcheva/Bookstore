# Bookstore
A Django app that provides basic functionallity for managig a Bookstore. 


How to run it:

1. Create virtual environment: python -m venv venv
2. Activate environment
  - Windows: ./venv/Scripts/activate
  - Linux: source venv/bin/activate
3. Install requirements: pip install -r ./requirements.txt
4. Run it: python manage.py runserver 


Admin: 
  user: admin
  pass: admin
  
In the admin panel you can:
  - perform CRUD operations on Authors and Books;
  - Filter Books;
  - apply a 20% sale/discount on selected books from Action drop down

URLs:
  - http://127.0.0.1:8000/admin/
  - http://127.0.0.1:8000/authors/ 
     [GET, POST]
    - example POST body:
      - http://127.0.0.1:8000/authors/
      -  {
          "first_name": "Elin",
          "last_name": "Pelin"
          }
  - http://127.0.0.1:8000:books/ 
  - http://127.0.0.1:8000/books/<int:id> [GET, PUT, DELETE]
    - example PUT body: 
      - http://127.0.0.1:8000/books/2)    
      - {
          "id": 2,
          "title": "It #1",
          "author": 2,
          "genre": "Thriller",
          "stock": 5,
          "price": 20.0
      }


search books by author's last name; genre or title:
  - example: http://127.0.0.1:8000/books?genre=thriller
  
  

