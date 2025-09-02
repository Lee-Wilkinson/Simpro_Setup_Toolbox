from flask import Flask, request, jsonify

# This is a basic web server using the Flask framework.
# To run this, you need to first install Flask:
# pip install Flask

app = Flask(__name__)

@app.route('/process-data', methods=['POST'])
def process_data():
    """
    This endpoint receives data from the front-end (your webpage)
    and processes it using the API logic from your original script.
    """
    try:
        data = request.json
        base_url = data.get('baseUrl')
        token = data.get('token')
        
        if not base_url or not token:
            return jsonify({"error": "Base URL and Token are required."}), 400

        print(f"Received data from front-end:")
        print(f"Base URL: {base_url}")
        print(f"Token: {token}")

        # The core logic from your original script would go here.
        # For example:
        # companies = get_companies(base_url, token)
        # if companies:
        #     # Logic to select company and process file...
        #     pass
        
        # This is a placeholder for a successful response.
        return jsonify({"message": "Successfully received data. Processing has started."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # To run this server, use the command: flask run
    # For a simple development server, you can also run this file directly.
    app.run(port=5000, debug=True)
