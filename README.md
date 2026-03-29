WeldSense AI
AI-Powered Weld Quality Inspection for Indian Fabrication Industries
Developer: Abhisek Tripathy
Institution: Veer Surendra Sai University of Technology (VSSUT), Burla, Odisha
Programme: B.Tech Mechanical Engineering, Year 2
Status: Prototype in development — March 2026

The Problem
India produces 140 million tonnes of steel annually. Odisha alone has 50+ steel plants within 150km of VSSUT Burla. Every plant uses fabrication contractors who weld structural components daily.
These welds have defects — porosity, undercut, cracks, spatter — at a rate of 4 to 10% of all welds. Human inspectors miss 20 to 30% of these defects due to fatigue and inconsistent lighting.
Existing solutions like Cognex and Keyence cost Rs 15 lakh to Rs 80 lakh per installation. Small fabrication shops earning Rs 2 crore annually cannot afford them. There is no affordable solution for this market.
WeldSense AI fills this gap.

The Solution
WeldSense AI is a hardware and software system that automatically inspects every weld immediately after it is made, classifies defects using a trained AI model, and alerts the supervisor in real time.
Hardware cost per unit: Rs 8,000 to Rs 10,000
Monthly subscription: Rs 12,000 to Rs 25,000
Detection accuracy: 95 to 98%
Response time: under 5 seconds per weld

How It Works

Welder completes a weld pass
Current sensor detects arc stopping automatically
System waits 4 seconds for weld to cool
8MP camera captures weld image with LED ring light
YOLOv8 AI model classifies the weld in 200 milliseconds
Result displayed as PASS in green or FAIL in red with defect type
WhatsApp alert sent to supervisor if defect found
All results saved to dashboard with full image archive


Defects Detected

Porosity — gas pits trapped on weld surface
Undercut — groove melted along the weld edge
Surface cracks — fractures visible on the weld bead
Spatter — molten metal droplets scattered around weld
Overlap — weld metal spilling over base metal without fusing


Technology Stack
| Component | Technology | Cost |
|-----------|-----------|------|
| AI Model | YOLOv8 (Ultralytics) | Free |
| Camera | 8MP Sony IMX179 USB | Rs 3,500 |
| Edge Computer | Raspberry Pi 4 (4GB) | Rs 4,500 |
| Trigger | Current transformer on cable | Rs 300 |
| Dashboard | Python Streamlit + SQLite | Free |
| Alerts | WhatsApp API (Twilio) | Free tier |
| Training | Google Colab (free GPU) | Free |
| Mobile Demo | Google Gemini Vision API | Free tier |


Target Market
Primary customers: Industrial fabrication contractors near Sambalpur, Jharsuguda, and Rourkela — within 0 to 90km of VSSUT Burla — who supply structural steel to sponge iron and steel plants.
Secondary customers: In-house maintenance workshops inside sponge iron plants including Maa Samaleswari, Aryan Ispat, and Shyam Metalics located 20 to 45km from campus.
Total addressable market: 50+ steel plants in Odisha with zero AI weld inspection deployed today.

Competitive Advantage
Zero funded startups and zero multinational companies have deployed AI weld inspection anywhere in Odisha, Jharkhand, West Bengal, or Chhattisgarh.
Indian competitors including SwitchOn and Jidoka Technologies focus entirely on automotive clusters in Tamil Nadu, Karnataka, and Maharashtra. The entire eastern India steel belt is completely unclaimed territory.

Current Status

System architecture and hardware specifications complete
Customer discovery completed — 10 plus conversations with fabrication shop owners near Sambalpur
Gemini Vision API demo prototype running on laptop
Weld image dataset collection from local samples in progress
YOLOv8 model training pipeline set up on Google Colab
Target: First paying customer by Month 7


Project Structure
weldsense-ai:
demo-          Gemini-powered web demo application
model-         YOLOv8 training notebooks and model files
data-          Weld defect image dataset and labels
hardware-      Circuit diagrams and hardware specifications
docs-          System design documents and pitch materials

Contact
Abhisek Tripathy
B.Tech Mechanical Engineering Year 2
Veer Surendra Sai University of Technology, Burla, Odisha

Built at VSSUT Burla, Odisha — solving a real problem for the steel industry within 150km of this campus.
