from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# 🔐 API KEY
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# ---------- Serve Frontend ----------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            return redirect("/dashboard")
        else:
            return "Invalid login"

    return render_template("login.html")

@app.route("/editor")
def editor():
    return render_template("editor.html")

@app.route("/html")
def html_page():
    return render_template("html_home.html")


# ---------- HTML SIDEBAR ROUTES (NEW ADDED) ----------

@app.route("/html-home")
def html_home():
    return render_template("html_home.html")

@app.route("/html-introduction")
def html_intro():
    return render_template("html_introduction.html")

@app.route("/html-editors")
def html_editors():
    return render_template("html_editors.html")

@app.route("/html-basic")
def html_basic():
    return render_template("html_basic.html")

@app.route("/html-elements")
def html_elements():
    return render_template("html_elements.html")

@app.route("/html-attributes")
def html_attributes():
    return render_template("html_attributes.html")

@app.route("/html-headings")
def html_headings():
    return render_template("html_headings.html")

@app.route("/html-paragraphs")
def html_paragraphs():
    return render_template("html_paragraphs.html")

@app.route("/html-styles")
def html_styles():
    return render_template("html_styles.html")

@app.route("/html-formatting")
def html_formatting():
    return render_template("html_formatting.html")

@app.route("/html-quotations")
def html_quotations():
    return render_template("html_quotations.html")

@app.route("/html-comments")
def html_comments():
    return render_template("html_comments.html")

@app.route("/html-colors")
def html_colors():
    return render_template("html_colors.html")

@app.route("/html-css")
def html_css():
    return render_template("html_css.html")

@app.route("/html-links")
def html_links():
    return render_template("html_links.html")

@app.route("/html-images")
def html_images():
    return render_template("html_images.html")

@app.route("/html-favicon")
def html_favicon():
    return render_template("html_favicon.html")

@app.route("/html-title")
def html_title():
    return render_template("html_title.html")

@app.route("/html-tables")
def html_tables():
    return render_template("html_tables.html")

@app.route("/html-lists")
def html_lists():
    return render_template("html_lists.html")

@app.route("/html-block-inline")
def html_block():
    return render_template("html_block.html")

@app.route("/html-div")
def html_div():
    return render_template("html_div.html")

@app.route("/html-classes")
def html_classes():
    return render_template("html_classes.html")

@app.route("/html-id")
def html_id():
    return render_template("html_id.html")

@app.route("/html-buttons")
def html_buttons():
    return render_template("html_buttons.html")

@app.route("/html-iframes")
def html_iframes():
    return render_template("html_iframes.html")

@app.route("/html-javascript")
def html_js():
    return render_template("html_js.html")

@app.route("/html-filepaths")
def html_paths():
    return render_template("html_paths.html")

@app.route("/html-head")
def html_head():
    return render_template("html_head.html")

@app.route("/html-layout")
def html_layout():
    return render_template("html_layout.html")

@app.route("/html-responsive")
def html_responsive():
    return render_template("html_responsive.html")

@app.route("/html-computercode")
def html_code():
    return render_template("html_code.html")

@app.route("/html-semantics")
def html_semantics():
    return render_template("html_semantics.html")

@app.route("/html-style-guide")
def html_style():
    return render_template("html_style.html")

@app.route("/html-entities")
def html_entities():
    return render_template("html_entities.html")

@app.route("/html-symbols")
def html_symbols():
    return render_template("html_symbols.html")

@app.route("/html-emojis")
def html_emojis():
    return render_template("html_emojis.html")

@app.route("/html-charset")
def html_charset():
    return render_template("html_charset.html")

@app.route("/html-urlencode")
def html_url():
    return render_template("html_url.html")

@app.route("/html-vs-xhtml")
def html_vs():
    return render_template("html_vs.html")


# ---------- AI CHAT ----------

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "No message received"}), 400

    user_message = data["message"]

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openrouter/auto",
                "messages": [
                    {"role": "user", "content": user_message}
                ]
            }
        )

        print("STATUS:", response.status_code)
        print("RAW RESPONSE:", response.text)

        result = response.json()

        if "choices" in result:
            reply = result["choices"][0]["message"]["content"]
        else:
            reply = "⚠️ ERROR: " + str(result)

    except Exception as e:
        reply = "Error: " + str(e)

    return jsonify({"reply": reply})


# ---------- RUN ----------

if __name__ == "__main__":
    app.run(debug=True)
