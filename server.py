from flask import Flask, request, make_response, jsonify, send_file, send_from_directory
app = Flask(__name__, static_url_path="/static")

# Always return minified JSON
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False

# Static content
@app.route("/static/<path:filename>")
def send_static(filename):
    return send_from_directory("/static", filename)

# Root
@app.route("/", methods=["GET"])
def root():
    return send_file("static/index.html")

# Graph API
@app.route("/api/graph", methods=["GET"])
def graph():
    dataset = request.args.get("dataset")
    graphtype = request.args.get("graphtype")

    if dataset is None or dataset not in ["social", "other"]:
        return make_response(jsonify({"error": "Invalid dataset."})), 400

    if graphtype is None or graphtype not in ["normal", "confluent"]:
        return make_response(jsonify({"error": "Invalid graph type."})), 400

    return "TODO"

if __name__ == "__main__":
    app.run()