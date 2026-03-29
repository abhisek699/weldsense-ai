from flask import Flask, render_template, request, jsonify
from google import genai
from PIL import Image
import io

app = Flask(__name__)

# This matches the "Client" logic from your working weldsense.py
client = genai.Client(api_key=" ")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inspect', methods=['POST'])
def inspect():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    file = request.files['image']
    image_bytes = file.read()
    image = Image.open(io.BytesIO(image_bytes))
    
    prompt = """You are an expert weld quality inspector.
    Analyse this weld image and provide:
    VERDICT: PASS or FAIL
    DEFECT: type or none
    CONFIDENCE: percentage
    REASON: one sentence"""
    
    try:
        # We are using gemini-2.0-flash because your script likes it!
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[prompt, image]
        )
        
        # This part cleans up the answer to show on your website
        result_text = response.text.strip()
        lines = result_text.split('\n')
        parsed = {}
        for line in lines:
            if ':' in line:
                key, val = line.split(':', 1)
                parsed[key.strip()] = val.strip()
        
        return jsonify(parsed)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
