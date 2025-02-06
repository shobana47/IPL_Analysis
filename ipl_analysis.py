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
