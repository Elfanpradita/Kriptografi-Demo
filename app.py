import os
import threading
import time
import subprocess
from flask import Flask, render_template, request, send_file, redirect, url_for
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

load_dotenv()

PORT = int(os.getenv("PORT", 5000))
DELETE_AFTER_MINUTES = int(os.getenv("DELETE_AFTER_MINUTES", 5))
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def delete_file_later(filepath, delay_minutes):
    time.sleep(delay_minutes * 60)
    if os.path.exists(filepath):
        os.remove(filepath)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "video" not in request.files:
            return "No file uploaded", 400

        file = request.files["video"]
        if file.filename == "":
            return "No selected file", 400

        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(input_path)

        output_filename = f"compressed_{filename}"
        output_path = os.path.join(app.config["UPLOAD_FOLDER"], output_filename)

        # ffmpeg compress
        cmd = [
            "ffmpeg", "-y",
            "-i", input_path,
            "-vcodec", "libx264",
            "-crf", "28",
            output_path
        ]
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if process.returncode != 0:
            return f"Error during compression: {process.stderr.decode()}", 500

        # Delete both input & output later
        threading.Thread(target=delete_file_later, args=(input_path, DELETE_AFTER_MINUTES), daemon=True).start()
        threading.Thread(target=delete_file_later, args=(output_path, DELETE_AFTER_MINUTES), daemon=True).start()

        return redirect(url_for("download_file", filename=output_filename))

    return render_template("index.html")


@app.route("/download/<filename>")
def download_file(filename):
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if not os.path.exists(filepath):
        return "File not found or deleted", 404
    return send_file(filepath, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
