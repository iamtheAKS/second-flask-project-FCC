from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
   {
  "id": 1,
  'title': "Data Analyst",
  "location": "Bengluru, India",
  "salary": "Rs 10,00,000",
},
   {
  "id": 2,
  'title': "Software Engineer",
  "location": "California, USA",
  "salary": "$ 10,00,000",
},
   {
  "id": 3,
  'title': "CyberSecurity Expert",
  "location": "Delhi, India",
  "salary": "Rs 10,00,000",
},
   {
  "id": 4,
  'title': "Web Developer",
  "location": "Hydrabad, India",
  "salary": "Rs 10,00,000",
},
   {
  "id": 5,
  'title': "App Developer (Android)",
  "location": "Bengluru, India",
  "salary": "Rs 10,00,000",
},
   {
  "id": 6,
  'title': "App Developer (Ios)",
  "location": "Bengluru, India",
  "salary": "Rs 10,00,000",
},
   {
  "id": 5,
  'title': "Database Desginer",
  "location": "Bengluru, India",
  "salary": "Rs 10,00,000",
},
   {
  "id": 5,
  'title': "System Desginer",
  "location": "Amsterdam, Germany",
  "salary": "$ 90,00,000",
},
  
]

@app.route("/")
def helloWorld():
  return render_template("home.html", jobs=JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)