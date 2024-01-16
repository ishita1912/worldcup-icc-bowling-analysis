#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np #help in work on numbers or arrays
import pandas as pd   # help for data frame or table
import matplotlib.pyplot as plt # visualizing data charts or graphs
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv('C:\\Users\\Lenovo\\Downloads\\icc_wc_23_bowl.csv', encoding= 'unicode_escape')
# it was giving error so we used double back slash instead of single\


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.isnull().sum()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df['team'].value_counts() #how many teams and kitne over kie har team ne


# In[9]:


#Data Analysis
# maximun overs?  
#max maiden? 
#max runs? and from which bowler
# max wickets? and from which bowler
# max min runrate?


# In[10]:


player_name = df.loc[df['runs'].idxmax(),'player']
team_name = df.loc[df['runs'].idxmax(),'team']
highest_runs = df.loc[df['runs'].idxmax(),'runs']
opponent = df.loc[df['runs'].idxmax(),'opponent']

print("------> Highest runs were given by the bowler ", player_name, " from the team of ", team_name,' in one spell which are ',highest_runs, ' against team ', opponent)


player_name = df.loc[df['wickets'].idxmax(),'player']
team_name = df.loc[df['wickets'].idxmax(),'team']
highest_runs = df.loc[df['wickets'].idxmax(),'wickets']
opponent = df.loc[df['wickets'].idxmax(),'opponent']

print("------> Highest wickets were given by the bowler ", player_name, " from the team of ", team_name,' in one spell which are ',highest_runs, ' against team ', opponent)

player_name = df.loc[df['6s'].idxmax(),'player']
team_name = df.loc[df['6s'].idxmax(),'team']
highest_runs = df.loc[df['6s'].idxmax(),'6s']
opponent = df.loc[df['6s'].idxmax(),'opponent']

print("------> Highest 6s were given by the bowler ", player_name, " from the team of ", team_name,' in one spell which are ',highest_runs, ' against team ', opponent)

player_name = df.loc[df['4s'].idxmax(),'player']
team_name = df.loc[df['4s'].idxmax(),'team']
highest_runs = df.loc[df['4s'].idxmax(),'4s']
opponent = df.loc[df['4s'].idxmax(),'opponent']

print("------> Highest 4s were given by the bowler ", player_name, " from the team of ", team_name,' in one spell which are ',highest_runs, ' against team ', opponent)

player_name = df.loc[df['maidens'].idxmax(),'player']
team_name = df.loc[df['maidens'].idxmax(),'team']
highest_runs = df.loc[df['maidens'].idxmax(),'maidens']
opponent = df.loc[df['maidens'].idxmax(),'opponent']

print("------> Highest maidens were given by the bowler ", player_name, " from the team of ", team_name,' in one spell which are ',highest_runs, ' against team ', opponent)



# In[11]:


# group the players by the overs, runs, wickets, ...
df_player_overs = df.groupby('player').agg({'overs':'sum', 'maidens': 'sum','runs': 'sum','wickets': 'sum' , 'run_rate': 'mean', '4s':'sum','wd':'sum', '6s': 'sum'}).reset_index()


# In[30]:


# sort the dataset by the overs
sorted_df_player_overs = df_player_overs.sort_values(by = 'overs', ascending = False).reset_index()


# In[31]:


sorted_df_player_overs


# In[32]:


df_player_overs_top_30 = sorted_df_player_overs.head(30)

# Plotting
plt.figure(figsize = (20, 6))
plt.bar(df_player_overs_top_30['player'], df_player_overs_top_30['overs'])
plt.xlabel('Player')
plt.ylabel('overs')
plt.title('overs by the top 30 players')
plt.xticks(rotation = 45)  # Rotate player names for better visibility
plt.tight_layout()

#Show the plot
plt.show()


# In[33]:


df_player_overs_top_30 = sorted_df_player_overs.head(30)

# Plotting
plt.figure(figsize = (15, 6))
plt.bar(df_player_overs_top_30['player'], df_player_overs_top_30['runs'], color = 'violet')
plt.xlabel('Player')
plt.ylabel('runs')
plt.title('runs given by the top 30 bowlers')
plt.xticks(rotation = 45, ha = 'right')  # Rotate player names for better visibility
plt.tight_layout()

#Show the plot
plt.show()


# In[34]:


# Run_rate from the top 30 bowlers

df_player_overs_top_30 = sorted_df_player_overs.head(30)

# Plotting
plt.figure(figsize = (15, 6))
plt.bar(df_player_overs_top_30['player'], df_player_overs_top_30['run_rate'], color = 'orange')
plt.xlabel('Player')
plt.ylabel('run_rate')
plt.title('run_rate from the top 30 bowlers')
plt.xticks(rotation = 45, ha = 'right')  # Rotate player names for better visibility
plt.tight_layout()

#Show the plot
plt.show()


# In[35]:


# Wide balls from the top 30 bowlers

df_player_wickets_top_30 = sorted_df_player_overs.head(30)

# Plotting
plt.figure(figsize = (20, 8))
plt.bar(df_player_overs_top_30['player'], df_player_overs_top_30['wd'], color = 'pink')
plt.xlabel('Player')
plt.ylabel('Wide balls')
plt.title('Wide balls from the top 30 players')
plt.xticks(rotation = 45, ha = 'right')  # Rotate player names for better visibility
plt.tight_layout()

#Show the plot
plt.show()


# In[26]:


fig, ax1 = plt.subplots(figsize=(12,6))

# Plot bars for 'overs' on the primary y-axis (ax1)

index = np.arange(len(df_player_overs_top_30))
bars = ax1.bar(index, df_player_overs_top_30['overs'], label = 'Overs', color ='skyblue')

# Plot line for 'maidens' on the same y-axis (ax1)
line = ax1.plot(index, df_player_overs_top_30['maidens'], color = 'orange', marker = 'o', label = 'maidens')

# Set labels and titles
ax1.set_xlabel('Player')
ax1.set_ylabel('Overs', color = 'skyblue')
ax1.tick_params(axis = 'y', labelcolor = 'skyblue')  # Make sure y-axis labels are in blue

plt.title('Maiden overs and Overs for the top 30 players')

# Combine legends
bar_legends = [bar for bar in bars]
line_legends = [line[0]]
plt.legend(bar_legends + line_legends, ['Overs', 'Maiden'], loc = 'upper left')

# Set x-axis ticks and labels
plt.xticks(index, df_player_overs_top_30['player'], rotation = 45, ha = 'right')

# Show the plot
plt.tight_layout()
plt.show()


# In[27]:


# Bowlers are sorted on the wickets taken by them

sorted_df_player_wickets = df_player_overs.sort_values(by = 'wickets', ascending = False).reset_index()
sorted_df_player_wickets


# In[36]:


# Wickets taken by the top 30 bowlers

df_player_wickets_top_30 = sorted_df_player_wickets.head(30)

# Plotting
plt.figure(figsize = (20, 6))
plt.bar(df_player_overs_top_30['player'], df_player_wickets_top_30['wickets'], color = 'violet')
plt.xlabel('Player')
plt.ylabel('wickets')
plt.title('wickets taken by the top 30 bowlers')
plt.xticks(rotation = 45, ha = 'right')  # Rotate player names for better visibility
plt.tight_layout()

#Show the plot
plt.show()


# In[37]:


# Wickets and Overs for the top 30 players

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(12,6))

# Plot bars for 'overs' on the primary y-axis (ax1)

index = np.arange(len(df_player_wickets_top_30))
bars = ax1.bar(index, df_player_wickets_top_30['overs'], label = 'Overs', color ='skyblue')

# Plot line for 'wickets' on the same y-axis (ax1)
line = ax1.plot(index, df_player_wickets_top_30['wickets'], color = 'orange', marker = 'o', label = 'Wickets')

# Set labels and titles
ax1.set_xlabel('Player')
ax1.set_ylabel('Overs', color = 'skyblue')
ax1.tick_params(axis = 'y', labelcolor = 'skyblue')  # Make sure y-axis labels are in blue

plt.title('Wickets and Overs for the top 30 players')

# Combine legends
bar_legends = [bar for bar in bars]
line_legends = [line[0]]
plt.legend(bar_legends + line_legends, ['Overs', 'Wickets'], loc = 'upper left')

# Set x-axis ticks and labels
plt.xticks(index, df_player_wickets_top_30['player'], rotation = 45, ha = 'right')

# Show the plot
plt.tight_layout()
plt.show() 


# In[38]:


# 4s given by the top 30 bowlers

# Plotting 
plt.figure(figsize= (15,6))
plt.bar(df_player_wickets_top_30['player'], df_player_wickets_top_30['4s'], color='cyan')
plt.xlabel('Player')
plt.ylabel('4s')
plt.title('4s given by the top 30 bowlers')
plt.xticks(rotation = 45, ha= 'right')  # Rotate player names for better visibility
plt.tight_layout()

# Show the plot
plt.show()


# In[39]:


#6s given by the top 30 bowlers

# Plotting 
plt.figure(figsize= (15,6))
plt.plot(df_player_wickets_top_30['player'], df_player_wickets_top_30['6s'], marker = 'o', linestyle = '--')
plt.grid()
plt.gray()
plt.xlabel('Player')
plt.ylabel('6s')
plt.title('6s given by the top 30 bowlers')
plt.xticks(rotation = 45, ha= 'right')  # Rotate player names for better visibility
plt.tight_layout()

# HSow the plot
plt.show()


# In[40]:


# Group by Team

df_team_overs = df.groupby('team').agg({'overs': 'sum', 'maidens': 'sum', 'runs': 'sum', 'wickets': 'sum', 'run_rate' : 'mean', '4s' : 'sum', '6s' : 'sum', 'wd': 'sum'})
df_team_overs


# In[41]:


# Overs by each team
plt.figure(figsize = (10,6))
plt.bar(df_team_overs.index, df_team_overs['overs'], color = 'magenta')
plt.xlabel('Team')
plt.ylabel('overs')
plt.title('overs by each Team')
plt.xticks(rotation = 45, ha = 'right')  # Rotate player names for better visibility
plt.tight_layout()

# SHow the plot
plt.show()


# In[42]:


# Maiden overs by each team 

plt.figure(figsize = (10, 6))
plt.bar(df_team_overs.index, df_team_overs['maidens'])
plt.xlabel('Team')
plt.ylabel('maiden overs')
plt.title('maiden overs by each Team')
plt.xticks(rotation = 45, ha = 'right')  # Rotate player names for better visibility
plt.tight_layout()

plt.show()


# In[43]:


print(df_team_overs.head())


# In[44]:


# Run_rate by the Team Bowlers

plt.figure(figsize = (12,6))
plt.plot(df_team_overs.index, df_team_overs['run_rate'], marker = 'o', linestyle = '--')
plt.grid()
plt.gray()
plt.xlabel('Teams')
plt.ylabel('run_rate')
plt.title('run_rate by the Team bowlers')
plt.xticks(rotation= 45, ha = 'right')   
plt.tight_layout()

plt.show()


# In[45]:


# Runs Scored by Each Team

plt.figure(figsize = (4,4))
plt.pie(df_team_overs['wickets'], labels = df_team_overs.index)
plt.title('Runs Scored by Each Team')
#plt.axis('equal') # Equal aspect ratio ensures that the pie is drawn as a circle

plt.show()


# In[46]:


plt.figure(figsize = (12,6))
plt.plot(df_team_overs.index, df_team_overs['runs'], marker = 'o', linestyle = '--')
plt.grid()
plt.gray()
plt.xlabel('Teams')
plt.ylabel('run')
plt.title('runs given by the Team bowlers')
plt.xticks(rotation= 45, ha = 'right')   
plt.tight_layout()

plt.show()


# In[47]:


# Wides by Each Team
plt.figure(figsize = (6,6))
plt.pie(df_team_overs['wd'], labels = df_team_overs.index)
plt.title('Wides by Each Team')

plt.show()


# In[ ]:





# In[ ]:




