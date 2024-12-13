# CSV Processing Application
This application allows users to upload a CSV file, input a message, and use OpenAI's API to generate Python code that processes the CSV data based on the given message. The generated Python code is executed dynamically, and the result is returned to the user.

# Features:
Upload a CSV file.
Enter a user message describing the task to be performed on the CSV data.
Generate and execute Python code based on the input message.
Display the generated code and its execution result.

# Requirements
Python 3.7 or higher
Flask web framework
OpenAI Python SDK
Pandas for data manipulation
dotenv for environment variable management

Installation & Setup
1. Clone the repository
#bash

git clone https://github.com/Preranasiddiraju/csv-processing-app.git
cd csv-processing-app

3. Set up a virtual environment (optional but recommended)
#bash

python -m venv venv
venv\Scripts\activate

5. Install the required dependencies
Once the virtual environment is activated, install the necessary Python packages by running:

#bash

pip install -r requirements.txt

4. Set up your OpenAI API key

You will need an OpenAI API key to use the OpenAI models. Follow these steps:

Visit OpenAI API Keys.

Create a new API key and copy it.

Create a .env file in the project root directory and add the following line:

#bash

OPENAI_API_KEY=your-api-key-here

Ensure that your .env file is added to your .gitignore to prevent it from being uploaded to version control.

5. Install Pandas
Pandas is required to handle the CSV file. Install it by running:

#bash

pip install pandas

Running the Application

Once everything is set up, you can run the Flask development server.

#bash

python app.py

ex:By default, the server will start on http://127.0.0.1:5000/. Open this URL in your browser to interact with the application.

# How to Use:
1.Upload a CSV File: Choose a CSV file from your local system (e.g., employee data with columns like Name, Age, Salary).

2.Enter a Task: Provide a short message describing the task you want to perform on the CSV data. Example: "Calculate the average salary of employees."

3.Submit the Form: Click the Submit button to send the data.

4.View the Result: The application will generate Python code based on the input message and execute it. The generated code and the execution output will be displayed on the page.



# Troubleshooting
1.Common Errors:

"No API key provided":

Make sure you have added your OpenAI API key to the .env file and that it's properly loaded into the app.

2."Quota exceeded":

If you exceed your API quota, check your OpenAI account for usage limits or upgrade your plan to increase your usage.

3."The model gpt-4 does not exist":

If you're using a model that your account doesn't have access to, switch to gpt-3.5-turbo.


# Contributing

If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request.

Contact
For any questions, feel free to reach out to Mail id: siddirajuprerana@gmail.com.
