Farm Expense Tracker

A simple CRUD application built with FastAPI and MySQL to help farmers track their expenses easily.

Features

- Add and list farmers
- Add and list expenses tied to farmers
- RESTful API endpoints

Technologies Used

- Python (FastAPI)
- SQLAlchemy (ORM)
- MySQL
- Uvicorn (ASGI server)

Setup Instructions

1. Clone the repo:  
   git clone https://github.com/Fancy-nateku/data.git

2. Create and activate a virtual environment:  
   python3 -m venv venv  
   source venv/bin/activate

3. Install dependencies:  
   pip install -r requirements.txt

4. Update your MySQL credentials in database.py.

5. Run the FastAPI app:  
   uvicorn main:app --reload

6. Access the API docs at:  
   http://127.0.0.1:8000/docs

API Endpoints

- POST /farmers/ - Create a new farmer
- GET /farmers/ - List all farmers
- POST /expenses/ - Create a new expense linked to a farmer
- GET /expenses/ - List all expenses
