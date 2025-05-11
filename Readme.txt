# 📚 Olist Challenge – Author & Book API

This project is a solution to the [Olist technical challenge](https://github.com/olist/work-at-olist), which requires the development of a RESTful API to manage authors and books.

---

## 🚀 Implemented Features

✅ Author import from a `.csv` file  
✅ Full CRUD operations for authors and books  
✅ Filtering on books by name, author, edition, and publication year  
✅ Pagination on all endpoints  
✅ RESTful structure with Django REST Framework  
✅ Clean, organized code following best practices

---

## 📂 Models Structure

### Author
- `id` (auto)
- `name` (string)

### Book
- `id` (auto)
- `name` (string)
- `edition` (string)
- `publication_year` (integer)
- `authors` (many-to-many with Author)

---

## 🧾 How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/mathorita/Olist-Challenge.git
cd Olist-Challenge
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Import authors from CSV:

bash
Copy
Edit
python manage.py import_authors authors.csv
Run the server:

bash
Copy
Edit
python manage.py runserver
🔗 Available Endpoints
Authors
GET /author/ → paginated list

GET /author/?search=name → filter by name

POST /author/ → create an author

PUT /author/{id}/ → update an author

DELETE /author/{id}/ → delete an author

Books
GET /book/ → paginated list with filters

GET /book/?name=&author=&edition=&publication_year=

POST /book/ → create a book with a list of authors

PUT /book/{id}/ → update a book

DELETE /book/{id}/ → delete a book

🛠️ Technologies Used
Python 3.11+

Django 5.2.1

Django REST Framework

django-filter

SQLite (for development)

📎 Challenge Reference
Original Olist repository:
👉 https://github.com/olist/work-at-olist

