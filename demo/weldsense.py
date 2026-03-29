from google import genai
from google.genai import types
from PIL import Image
import sys
import os

client = genai.Client(api_key="AIzaSyDaqelwQ68tTBeYFaJ04H4BKGXeL1qsPbs")

def inspect_weld(image_path):

    print("")
    print("========================================")
    print("         WELDSENSE AI")
    print("   AI Weld Quality Inspection System")
    print("========================================")
    print("")
    print("Analysing image: " + image_path)
    print("Please wait...")
    print("")

    image = Image.open(image_path)

    prompt = """You are an expert weld quality inspector with 20 years of experience.

Carefully examine this weld image and provide your inspection result.

Respond in EXACTLY this format with no extra text:

VERDICT: PASS or FAIL
DEFECT: porosity or undercut or crack or spatter or overlap or none
CONFIDENCE: a number from 0 to 100
REASON: one clear sentence explaining your decision

Rules:
- VERDICT must be either PASS or FAIL only
- DEFECT must be one of the listed types or none
- CONFIDENCE must be a number only
- REASON must be one sentence only"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt, image]
    )

    print("========================================")
    print("         INSPECTION RESULT")
    print("========================================")
    print("")

    result_text = response.text.strip()
    lines = result_text.split('\n')

    verdict = ""
    defect = ""
    confidence = ""
    reason = ""

    for line in lines:
        if line.startswith("VERDICT:"):
            verdict = line.replace("VERDICT:", "").strip()
        elif line.startswith("DEFECT:"):
            defect = line.replace("DEFECT:", "").strip()
        elif line.startswith("CONFIDENCE:"):
            confidence = line.replace("CONFIDENCE:", "").strip()
        elif line.startswith("REASON:"):
            reason = line.replace("REASON:", "").strip()

    print("VERDICT    : " + verdict)
    print("DEFECT TYPE: " + defect)
    print("CONFIDENCE : " + confidence + "%")
    print("REASON     : " + reason)
    print("")

    if "PASS" in verdict.upper():
        print(">>> STATUS: GOOD WELD - NO ACTION NEEDED <<<")
    else:
        print(">>> STATUS: DEFECT FOUND - SEND FOR REWORK <<<")

    print("")
    print("========================================")
    print("")

if len(sys.argv) < 2:
    print("")
    print("Usage: python weldsense.py path_to_image.jpg")
    print("Example: python weldsense.py porosity-1.jpg")
    print("")
else:
    image_path = sys.argv[1]
    if os.path.exists(image_path):
        inspect_weld(image_path)
    else:
        print("")
        print("ERROR: Image file not found: " + image_path)
        print("Check the file name and try again.")
        print("")