from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("data/your_new_dataset.csv", encoding="latin1")  # Change to your new CSV filename and encoding if needed
df = df.dropna(subset=['Brand', 'Model', 'Review Summary'])

df.columns = df.columns.str.strip()

print('DataFrame columns:', list(df.columns))

# 
@app.route("/")
def home():
    brands = sorted(df['Brand'].dropna().unique().tolist())
    return render_template("index.html", brands=brands)

@app.route("/get_models", methods=["POST"])
def get_models():
    data = request.json
    brand = data.get("brand", "").strip().lower()
    models = df[df['Brand'].str.strip().str.lower() == brand]['Model'].dropna().unique().tolist()
    if not models:
        models = df[df['Brand'].str.strip().str.lower().str.contains(brand)]['Model'].dropna().unique().tolist()
    return jsonify(models)

@app.route("/get_reviews", methods=["POST"])
def get_reviews():
    data = request.json
    brand = data.get("brand", "").strip().lower()
    model = data.get("model", "").strip().lower()
    reviews = df[
        (df['Brand'].str.strip().str.lower() == brand) &
        (df['Model'].str.strip().str.lower() == model)
    ][['Review Summary', 'Star Rating']].head(5).to_dict(orient='records')
    return jsonify(reviews)

@app.route("/compare_devices", methods=["POST"])
def compare_devices():
    data = request.json
    brand1 = data.get("brand1", "").strip().lower()
    model1 = data.get("model1", "").strip().lower()
    brand2 = data.get("brand2", "").strip().lower()
    model2 = data.get("model2", "").strip().lower()
    device1_reviews = df[
        (df['Brand'].str.strip().str.lower() == brand1) &
        (df['Model'].str.strip().str.lower() == model1)
    ][['Brand', 'Model', 'Review Summary', 'Star Rating']].head(5).to_dict(orient='records')
    device2_reviews = df[
        (df['Brand'].str.strip().str.lower() == brand2) &
        (df['Model'].str.strip().str.lower() == model2)
    ][['Brand', 'Model', 'Review Summary', 'Star Rating']].head(5).to_dict(orient='records')
    return jsonify({"device1": device1_reviews, "device2": device2_reviews})

@app.route("/compare")
def compare():
    brands = sorted(df['Brand'].dropna().unique().tolist())
    return render_template("compare.html", brands=brands)

@app.route("/get_reviews_with_avg", methods=["POST"])
def get_reviews_with_avg():
    data = request.json
    brand = data.get("brand", "").strip().lower()
    model = data.get("model", "").strip().lower()
    reviews_df = df[
        (df['Brand'].str.strip().str.lower() == brand) &
        (df['Model'].str.strip().str.lower() == model)
    ][['Review Summary', 'Star Rating']].head(5)
    reviews = reviews_df.to_dict(orient='records')
    avg_rating = reviews_df['Star Rating'].astype(float).mean() if not reviews_df.empty else None
    return jsonify({"reviews": reviews, "average_rating": avg_rating})

if __name__ == "__main__":
    app.run(debug=True)
