"# NLP-Sentiment-analysis" 
FastAPI Email Extractor
Overview
This FastAPI application extracts information from an email file (.eml) and returns the extracted data in JSON format. The extracted information includes the email's subject, sender's name and organization, recipient address, timestamp, and body content.

Prerequisites
Python 3.6 or higher
FastAPI
Uvicorn
Installation
Clone the Repository

If the project is in a repository, clone it to your local machine. If it's a standalone script, ensure it's saved in a directory on your local machine.

Create a Virtual Environment

Navigate to the project directory and create a virtual environment using the following commands:

sh
Copy code
python3 -m venv env
Activate the Virtual Environment

On Windows:

sh
Copy code
.\env\Scripts\activate
On Linux/Mac:

sh
Copy code
source env/bin/activate
Install Dependencies

Install the necessary dependencies by running the following command in the terminal:

sh
Copy code
pip install fastapi uvicorn
Usage
Start the Application

Navigate to the directory where your FastAPI script (main.py) is located. Start the application using the following command:

sh
Copy code
uvicorn main:app --reload
Access the API

Once the server is running, you can access the FastAPI application at:

arduino
Copy code
http://127.0.0.1:8000
You can also access the automatic interactive API documentation at:

arduino
Copy code
http://127.0.0.1:8000/docs
Using the API

Use the /extract_email endpoint to extract information from an .eml file. You'll need to provide the path to the .eml file as input.

Stopping the Server

To stop the server, use Ctrl+C in the terminal where the server is running.

API Endpoint
POST /extract_email
Request Body:

eml_path (string): The path to the .eml file.
Response:

A JSON object containing the following fields:

subject: The subject of the email.
person_from: The name of the person who sent the email.
organization: The organization of the person who sent the email.
to_address: The recipient's email address.
timestamp: The timestamp of the email.
body: The body content of the email.
Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request.
