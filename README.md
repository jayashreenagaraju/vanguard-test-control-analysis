# Week 5-6 Individual Project

## Data sets
There are three datasets that will guide your journey:

Client Profiles [df_final_demo](data/raw/df_final_demo.csv): Demographics like age, gender, and account details of our clients.

Digital Footprints [df_final_web_data](data/raw/df_final_web_data_combined.csv): A detailed trace of client interactions online.
Experiment Roster [df_final_experiment_clients]((data/raw/df_final_experiment_clients.csv)): A list revealing which clients were part of the grand experiment

## Metadata
This comprehensive set of fields will guide your analysis, helping you unravel the intricacies of client behavior and preferences.

* client_id: Every client’s unique ID.
* variation: Indicates if a client was part of the experiment.
* visitor_id: A unique ID for each client-device combination.
* visit_id: A unique ID for each web visit/session.
* process_step: Marks each step in the digital process.
* date_time: Timestamp of each web activity.
* clnt_tenure_yr: Represents how long the client has been with Vanguard, measured in years.
* clnt_tenure_mnth: Further breaks down the client’s tenure with Vanguard in months.
* clnt_age: Indicates the age of the client.
* gendr: Specifies the client’s gender.
* num_accts: Denotes the number of accounts the client holds with Vanguard.
* bal: Gives the total balance spread across all accounts for a particular client.
* calls_6_mnth: Records the number of times the client reached out over a call in the past six months.
* logons_6_mnth: Reflects the frequency with which the client logged onto Vanguard’s platform over the last six months.

## Client behavior analysis

Answered the following questions about demographics:

* Who are the primary clients using this online process?
* Are the primary clients younger or older, new or long-standing?

## Performance Metrics & Hypothesis Testing

Performance Metrics and hypothesis testing can be seen in the presentation [here](slides/ppt.pdf)

* Completion rate
* Average time spent on each process step
* Average time spent on entire process
* Farthest Step
* Error rate
* Average client tenure
* Gender differences


Tableau file can be found [here](slides/Tableau.twb)

Miro board can be found [here](https://miro.com/app/board/uXjVK-e1Sk8=/)

And for the code you can see the notebook [here](notebooks/Customer-Experience.ipynb)
