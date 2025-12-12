**FastAPI Wedding Project – Multi-Organization Management API**
This project is a FastAPI-based backend built to manage organizations, admin login, authentication, and CRUD operations using MongoDB as the database.
It is fully modular, beginner-friendly, and structured for real-world API development.

**⭐ Features**
Organization registration
Organization admin login
JWT-based authentication
CRUD operations
MongoDB integration
Modular file structure
Fully tested API routes
Environment-variable based configuration
Easy local setup (beginner friendly)

**📁 Project Folder Structure**
/wedding
│── app
│   │── main.py
│   │── config.py
│   │── models.py
│   │── auth.py
│   │── crud.py
│   │── utils.py
│   └── routes
│       │── admin.py
│       │── org.py
│       └── __init__.py
│── venv/
│── .env
│── requirements.txt
│── README.md

**⚙️ Tech Stack**
Component	Technology
Backend Framework	FastAPI
Language	Python
Database	MongoDB
Authentication	JWT
Server	Uvicorn
Environment Loader	python-dotenv
🔧 Installation & Setup
1. Clone the Repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2. Create a Virtual Environment
python -m venv venv

3. Activate the Virtual Environment
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

**🛠️ Environment Setup**
Create a .env file in the project root:
MONGO_URI=mongodb://localhost:27017
MASTER_DB=master_db
JWT_SECRET=mysecret123
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

Make sure you have MongoDB running locally.

**🚀 Run the FastAPI Server**

Inside the project root:
uvicorn app.main:app --reload
Server will run on:
👉 http://127.0.0.1:8000
Swagger Docs:
👉 http://127.0.0.1:8000/docs
🧪 Testing the API
✔️ 1. Create Organization
POST /org/create
{
  "org_name": "My Studio",
  "email": "studio@gmail.com",
  "password": "test123"
}

✔️ 2. Admin Login

POST /admin/login

{
  "email": "studio@gmail.com",
  "password": "test123"
}


Response Example:

{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}

✔️ 3. Get Organization by ID

GET /org/{org_id}

✔️ 4. Delete Organization

DELETE /org/{org_id}

🧩 Requirements File

Your requirements.txt should include:

fastapi
uvicorn
pydantic
python-dotenv
pymongo
passlib[bcrypt]
python-jose
email-validator

🤝 Contributing

Feel free to submit pull requests or open issues if you want to add new features or report bugs.

📜 License

This project is open-source and available under the MIT License.
