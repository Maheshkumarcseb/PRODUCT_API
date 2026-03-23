--> How to Run the FastAPI

1. Clone the Repository
git clone <your-repo-url>
cd Product_Api

2. Create Virtual Environment
Windows (Git Bash / CMD)
python -m venv apienv
source apienv/Scripts/activate
Linux / macOS
python3 -m venv apienv
source apienv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Setup MySQL Database
Open MySQL and run:

-->CREATE DATABASE product_db;
5. Configure Database Connection
Open database.py and update:
DATABASE_URL = "mysql+pymysql://root:password@localhost/product_db"
root → your MySQL username
password → your MySQL password

6. Run the FastAPI Server
uvicorn main:app --reload

8. Access the API
--> Base URL:
http://127.0.0.1:8000
--> Swagger UI (API Testing):
http://127.0.0.1:8000/docs
