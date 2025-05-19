# Mutual-Fund-Broker-Web-Application

## Getting Started

Follow the steps below to set up and run the **Mutual Fund Broker Web Application** on your local machine:

### 1. Clone the Repository
git clone https://github.com/BroCodeByMinds/Mutual-Fund-Broker-Web-Application.git

### 2. Environment Setup
Please obtain the .env file from the project owner and place it in the root directory of the project.

### 3. Running the Application
Open a terminal in the root directory of the project and execute the run_app.bat file:

PS C:\Users\YourUsername\Path\To\Mutual-Fund-Broker-Web-Application> .\run_app.bat

Description of run_app.bat steps:

Creates a virtual environment if it does not already exist.

Activates the virtual environment.

Installs the dependencies listed in requirements.txt.

Runs the FastAPI application using Uvicorn.

### 4. Configure Environment Variables
Update the .env file with your specific credentials and configuration:
--> FastAPI secret key
--> API host
--> Database URL

### 5. Database Setup
Initialize Alembic migrations by running the following command:
alembic init alembic

alembic revision --autogenerate -m "Initial migration"

alembic upgrade head

### 6. Accessing the Application
Once the application is running successfully, open your browser and navigate to:http://localhost:8000/docs.
This will open the built-in FastAPI Swagger UI, where you can explore and test the available APIs.

### 7. Using the API
Register a new user using the Register API endpoint.

In the response, you will receive an authentication token.

Authorize the token in the FastAPI UI using the Authorize button.

After authorization, you can access other secured API endpoints, such as Open Ended Schemes and Fund Families.