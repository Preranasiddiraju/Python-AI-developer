import openai
import pandas as pd
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import io

# Load environment variables
load_dotenv(dotenv_path="D:/python ai/open.env")
openai.api_key = os.getenv("openai.api_key")

# Initialize Flask app
app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")  # Render the template index.html

# Route to handle file upload and user message
@app.route("/process", methods=["POST"])
def process():
    # Get user message from input
    user_message = request.form.get("message")
    if not user_message:
        return jsonify({"error": "Message cannot be empty!"}), 400

    # Get the CSV file from the form (optional)
    csv_file = request.files.get("csv_file")

    # If CSV file is provided, process it
    if csv_file:
        try:
            # Read the CSV file into a pandas DataFrame
            csv_data = pd.read_csv(io.StringIO(csv_file.stream.read().decode("utf-8")))

            # Prepare the prompt for the OpenAI model based on the CSV data and user message
            prompt = f"Generate Python code that processes the following CSV data to fulfill the following instruction: '{user_message}'.\n\nCSV Data:\n{csv_data.head()}"
            
            # Use the OpenAI API to generate Python code
            response = openai.Completion.create(
                model="gpt-3.5-turbo",  # Or another model depending on your needs
                prompt=prompt,
                max_tokens=150
            )

            # Extract the generated Python code from the response
            generated_code = response['choices'][0]['text'].strip()

            # Save the CSV data to a temporary file for the generated code to process
            file_path = "input.csv"
            csv_data.to_csv(file_path, index=False)

            # Execute the generated Python code
            try:
                exec_globals = {"pd": pd, "file_path": file_path}
                exec(generated_code, exec_globals)

                # Return the generated code and execution result
                result = exec_globals.get('result', 'No output generated.')
                return jsonify({
                    "generated_code": generated_code,
                    "execution_output": str(result)
                })

            except Exception as e:
                return jsonify({"error": f"Error executing the generated code: {str(e)}"}), 500

        except Exception as e:
            return jsonify({"error": f"Error processing CSV file: {str(e)}"}), 500

    else:
        # If no CSV file is uploaded, generate Python code based on the user message alone
        try:
            prompt = f"Generate Python code to fulfill the following instruction: '{user_message}'."
            
            # Use the OpenAI API to generate Python code
            response = openai.Completion.create(
                model="gpt-3.5-turbo",  # Or another model depending on your needs
                prompt=prompt,
                max_tokens=150
            )

            # Extract the generated Python code from the response
            generated_code = response['choices'][0]['text'].strip()

            # Return the generated code
            return jsonify({
                "generated_code": generated_code,
                "execution_output": "No CSV file provided. Code generated without execution."
            })

        except Exception as e:
            return jsonify({"error": f"Error generating code: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
