from flask import Flask, jsonify, request
from sqs import send_message_sqs
from db import insert_message_into_db, get_db_connection

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def message():
    # Extract the message from the request
    data = request.json  # Assuming the message is sent as JSON
    message = data.get('message', '')
    message_id = insert_message_into_db(message)
    message = {
        "message": message,
        "id": message_id
    }
    #send_message_sqs(message)
    # Here, you would add your logic to handle the message,
    # such as sending it to your application's processing module or saving it to a database.

    print(f"Received message: {message}")
    return jsonify({'status': 'success', 'message': 'Message received successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
