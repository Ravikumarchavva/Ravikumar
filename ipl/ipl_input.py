from flask import *
import requests
from pycaret.regression import *
import tempfile
import pandas as pd
import os
from google.cloud import storage
# Set the path to your service account key file
key_file = "/workspace/Ravikumar/healthy-genre-391115-f36176b04acf.json"

# Set the environment variable for the key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file

# Create a client using the provided credentials
client = storage.Client()

# Specify the GCS URI for the model
gcs_uri = 'gs://githubml_models/ipl_models/ipl_pycaret.pkl'

# Get the bucket and blob names from the GCS URI
bucket_name, blob_name = gcs_uri[5:].split("/", 1)
# Get the bucket
bucket = client.get_bucket(bucket_name)

# Get the blob
blob = bucket.blob(blob_name)

# Download the model file as bytes
model_data = blob.download_as_bytes()
# Create the file.
with tempfile.NamedTemporaryFile(suffix='.pkl', delete=False) as temp_file:
    # Write the model data to the file.
    temp_file.write(model_data)
    # Load the model from the file.
    model = load_model(temp_file.name[:-4])  # Remove the ".pkl" extension

# Close the file.
temp_file.close()

# Now you can use the model for predictions or other tasks
app=Flask(__name__)

with app.app_context():
#    model_db=sqlite3.connect(par['db_uri'])
#    model_cur=model_db.cursor()
#    slug_name="ipl_fsp"
#    model_cur.execute(f"SELECT * FROM ml_models WHERE slug='{slug_name}'")
#    mc=model_cur.fetchone()
#    model={
#       'name':mc[1],
#       'slug':mc[2],
#       'date':mc[3]
#    }

    batting_teams=['batting_team_Chennai Super Kings','batting_team_Delhi Capitals','batting_team_Gujarat Lions','batting_team_Kings XI Punjab','batting_team_Kolkata Knight Riders',
                'batting_team_Mumbai Indians','batting_team_Pune Warriors','batting_team_Rajasthan Royals','batting_team_Royal Challengers Bangalore','batting_team_Sunrisers Hyderabad']
   
    bowling_teams=['bowling_team_Chennai Super Kings','bowling_team_Delhi Capitals','bowling_team_Gujarat Lions','bowling_team_Kings XI Punjab','bowling_team_Kolkata Knight Riders',
                'bowling_team_Mumbai Indians','bowling_team_Pune Warriors','bowling_team_Rajasthan Royals','bowling_team_Royal Challengers Bangalore','bowling_team_Sunrisers Hyderabad']
    toss_teams=['toss_winner_Chennai Super Kings','toss_winner_Delhi Capitals','toss_winner_Gujarat Lions','toss_winner_Kings XI Punjab','toss_winner_Kolkata Knight Riders',
                'toss_winner_Mumbai Indians','toss_winner_Pune Warriors','toss_winner_Rajasthan Royals','toss_winner_Royal Challengers Bangalore','toss_winner_Sunrisers Hyderabad']
    city_names=['Ahmedabad','Bangalore','Chandigarh','Chennai','Delhi','Dharamsala','Hyderabad','Jaipur','Kolkata','Mohali','Mumbai','Pune']
    m=model
    inning=1
    bat="batting_team_Chennai Super Kings"
    bowl="bowling_team_Delhi Capitals"
    ba_t=[1 if x==bat else 0 for x in batting_teams ]
    bo_t=[1 if x==bowl else 0 for x in bowling_teams ]
    city_input='Delhi'
    city=[1 if x==city_input else 0 for x in city_names ]
    toss_winner='toss_winner_Chennai Super Kings'
    toss=[1 if x==toss_winner else 0 for x in toss_teams]
    toss_decisions=["feild","bat"]
    toss_taken="feild"
    if(toss_taken=="feild"):
        toss_decision=1
    else:
        toss_decision=0
    current_runs=112
    current_wickets=3
    current_ball=12.4
    current_run_rate=int(current_runs)/int(current_ball)
    print(inning,ba_t,bo_t,city,toss,toss_decision,current_ball,current_runs,current_wickets,current_run_rate)
    values=[int(inning)]+ba_t+bo_t+city+toss+[int(toss_decision),int(current_ball),int(current_runs),int(current_wickets),float(current_run_rate)]
    print(values)
    keys=['inning', 'batting_team_Chennai Super Kings', 'batting_team_Delhi Capitals', 'batting_team_Gujarat Lions', 'batting_team_Kings XI Punjab', 'batting_team_Kolkata Knight Riders', 
            'batting_team_Mumbai Indians', 'batting_team_Pune Warriors', 'batting_team_Rajasthan Royals', 'batting_team_Royal Challengers Bangalore', 'batting_team_Sunrisers Hyderabad', 
            'bowling_team_Chennai Super Kings', 'bowling_team_Delhi Capitals', 'bowling_team_Gujarat Lions', 'bowling_team_Kings XI Punjab', 'bowling_team_Kolkata Knight Riders', 'bowling_team_Mumbai Indians', 
            'bowling_team_Pune Warriors', 'bowling_team_Rajasthan Royals', 'bowling_team_Royal Challengers Bangalore', 'bowling_team_Sunrisers Hyderabad', 'city_Ahmedabad', 'city_Bangalore', 'city_Chandigarh', 
            'city_Chennai', 'city_Delhi', 'city_Dharamsala', 'city_Hyderabad', 'city_Jaipur', 'city_Kolkata', 'city_Mohali', 'city_Mumbai', 'city_Pune', 'toss_winner_Chennai Super Kings', 'toss_winner_Delhi Capitals', 
            'toss_winner_Gujarat Lions', 'toss_winner_Kings XI Punjab', 'toss_winner_Kolkata Knight Riders', 'toss_winner_Mumbai Indians', 'toss_winner_Pune Warriors', 'toss_winner_Rajasthan Royals', 
            'toss_winner_Royal Challengers Bangalore', 'toss_winner_Sunrisers Hyderabad', 'toss_decision', 'balls', 'current_runs', 'wickets', 'current_run_rate']
    input_list = {k: {1: v} for k, v in zip(keys,values)}
    s=m.predict(input_list)
    print(s)