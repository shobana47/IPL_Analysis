IPL Analysis Project

📌 Overview

This project focuses on analyzing Indian Premier League (IPL) data to extract meaningful insights and patterns. Using data visualization and machine learning techniques, the project aims to explore player performance, team statistics, match outcomes, and trends over different seasons.

📂 Dataset

The dataset contains IPL match details from multiple seasons.

It includes information on teams, players, runs, wickets, venues, and match results.

Data is sourced from publicly available IPL datasets.

🛠️ Technologies Used

Programming Language: Python

Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn

VS Code for development and execution

🎯 Features & Analysis

Data Preprocessing: Cleaning and structuring the raw IPL data.

Exploratory Data Analysis (EDA):

Team-wise performance over the years.

Top run-scorers and wicket-takers.

Toss decisions and their impact on match results.

Venue-based performance trends.

Machine Learning Predictions:

Win predictions based on historical data.

Player performance forecasting.

Data Visualization:

Interactive graphs and heatmaps for insights.

🚀 How to Run the Project

Clone the repository:

git clone https://github.com/shobana47/IPL_Analysis

Navigate to the project directory:

cd ipl-analysis

Install dependencies:

pip install -r requirements.txt

Open the project in VS Code:

code .

Run the script in VS Code:

Open the .py file containing the analysis script.

Click on the "Run" button or press Shift + Enter if using an interactive window.

Alternatively, run the script in the terminal:

python script_name.py

📊 Sample Visualizations

Number of Matches Won by Each Team

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r'C:\Users\SHOBANA G\Desktop\Project\AIML with DS\dataset\ipldata\file 2.csv'

# Load data from the CSV file
ipl_df = pd.read_csv(file_path)

# column names to verify
print("Columns in the DataFrame:\n", ipl_df.columns)

# first few rows of the DataFrame
print("First few rows of the DataFrame:\n", ipl_df.head())
print("Information about the DataFrame:\n")
ipl_df.info()

# number of matches won by each team
team_wins = ipl_df['winner'].value_counts()
print("\nTeam Wins:\n", team_wins)
player_of_match_counts = ipl_df['player_of_match'].value_counts()
print("\nPlayer of the match counts:\n", player_of_match_counts)

plt.figure(figsize=(12, 8))
sns.countplot(x='winner', data=ipl_df)
plt.title('Number of Wins by Team')
plt.xlabel('Team')
plt.ylabel('Number of Wins')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.
