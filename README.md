# Mutual-Fund-Broker-Web-Application

## Getting Started

Follow the steps below to set up and run the **Mutual Fund Broker Web Application** on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/BroCodeByMinds/Mutual-Fund-Broker-Web-Application.git
```

Navigate to `Mutual-Fund-Broker-Web-Application/backend` and open the folder in VS Code or your preferred code editor.

### 2. Environment Setup

Please obtain the `.env` file from the project owner or refer to the provided `.env.example` file to create your own. Ensure the `.env` file is placed in the root directory of the project.

### 3. Running the Application

**Note:** Before running the `run_app.bat` file, please ensure that no other server is currently using port 8000.

Open a terminal in the root directory of the project and execute the `run_app.bat` file:

```powershell
PS C:\Path\To\Mutual-Fund-Broker-Web-Application> .\run_app.bat
```

**Description of `run_app.bat` steps:**

- Creates a virtual environment if it does not already exist.
- Activates the virtual environment.
- Installs the dependencies listed in `requirements.txt`.
- Runs the FastAPI application using Uvicorn.

> A cron job is configured to run at application startup to fetch data from RapidAPI. However, since the provided API key has already exhausted its allowed number of requests under the current subscription, you may encounter an error message, as shown in the screenshot below.

![API Error](https://github.com/user-attachments/assets/c8f9aa73-447f-4a93-b2dc-4c8cf97cd1df)

### 4. Configure Environment Variables

Update the `.env` file with your specific credentials and configuration:

- FastAPI secret key
- API host
- Database URL

### 5. Database Setup

**Note:**

1. Before running the migration script, ensure that you have created a database in PostgreSQL. The same database name must also be specified in the `.env` file.
2. While the server is running, make sure it’s using the correct Python interpreter (i.e., the intended virtual environment); using the wrong one can trigger `ModuleNotFoundError` issues.
3. Activate the virtual environment by running the following command:

```bash
C:\Path\To\Mutual-Fund-Broker-Web-Application\backend> .\venv\Scripts\activate
```

Execute the migrations script using the following command:

```powershell
PS C:\Path\To\Mutual-Fund-Broker-Web-Application\backend> python .\migrations.py
```

### 6. Accessing the Application

Once the application is running successfully, open your browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs). This will launch the built-in FastAPI Swagger UI, where you can explore and test all available APIs. Alternatively, you can use the Postman collection provided in the `backend` folder for testing.

### 7. Using the API

- Register a new user using the Register API endpoint.
- In the response, you will receive an authentication token.
- Authorize the token in the FastAPI UI using the **Authorize** button.
- After authorization, you can access other secured API endpoints, such as **Open Ended Schemes** and **Fund Families**.

---

## Note

Due to time constraints, the frontend is partially implemented. However, all backend APIs are functional and testable via Swagger UI (`/docs`).
