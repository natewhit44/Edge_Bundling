from flask import Flask, request, make_response, jsonify, send_file, send_from_directory
import data_parser

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

    print dataset

    if dataset is None or dataset not in ["data_file_500_points.csv", "data2.csv"]:
        return make_response(jsonify({"error": "Invalid dataset."})), 400

    parsed = data_parser.parse(dataset)

    return make_response(jsonify(parsed)), 200

if __name__ == "__main__":
    app.run()