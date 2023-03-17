from flask import Flask,render_template,jsonify

app = Flask(__name__)



JOBS = [
  {
    'id':1,
    'role':"Data Analyst",
    'salary':"Rs 1,00,000",
    'location' : "Delhi"
  },
    {
    'id':2,
    'role':"Software Engg",
    'salary':"Rs 9,00,000",
    'location' : "Bangalore"
  },
  {
    'id':3,
    'role':"CA",
    'salary':"Rs 5,00,000",
    'location' : "Mumbai"
  },
  {
    'id':4,
    'role':"Python Developer",
    'salary':"Rs 2,00,000",
    'location' : "UK"
  }
]


@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS, company_name='ITERNAL JOBS')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)





