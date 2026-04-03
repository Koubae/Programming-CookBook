"""

----------------
    GET
----------------

- If-None-Match
    - 200 OK                    => ETag Doesn't Match | Send data
    - 304 Not Modified          => ETag Match | Don't send data use cache inst4ead

- If-Match
    - 200 OK Or 204 No Content  => successful update
    - 428 Precondition Required => server refuses to updated, missing `If-Match` header
    - 412 Precondition Failed   => the object does not have that ETag anymore

"""
import hashlib
from flask import Flask, request, jsonify, make_response, abort

app = Flask(__name__)

# Simulated database
resource_db = {"id": 101, "content": "Initial System State", "version": 1}

def generate_etag(data):
    """Generates a strong ETag based on the content hash."""
    # Using double quotes for the ETag string as per HTTP spec
    content_hash = hashlib.md5(str(data).encode('utf-8')).hexdigest()
    return f'"{content_hash}"'

@app.route('/resource', methods=['GET'])
def get_resource():
    current_etag = generate_etag(resource_db)

    # 1. Version: GET with If-None-Match (Caching)
    # If the client already has this version, don't resend the data.
    if request.headers.get('If-None-Match') == current_etag:
        return '', 304  # Not Modified

    # Otherwise, send the full data with the new ETag
    response = make_response(jsonify(resource_db))
    response.headers['ETag'] = current_etag
    return response

@app.route('/resource', methods=['PUT'])
def update_resource():
    global resource_db
    current_etag = generate_etag(resource_db)

    # 2. Version: PUT with If-Match (Concurrency Control)
    # Ensure the client is updating the version they actually saw.
    client_match_header = request.headers.get('If-Match')

    if not client_match_header:
        abort(428, description="Precondition Required: Missing If-Match header")

    if client_match_header != current_etag:
        # The data changed on the server while the client was editing.
        abort(412, description="Precondition Failed: Resource has changed")

    # Perform the update
    new_content = request.json.get('content')
    resource_db['content'] = new_content
    resource_db['version'] += 1

    # Send back the updated resource with its brand-new ETag
    new_etag = generate_etag(resource_db)
    response = make_response(jsonify(resource_db))
    response.headers['ETag'] = new_etag
    return response

if __name__ == '__main__':
    app.run(debug=True)


