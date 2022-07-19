#!/usr/bin/env python
# coding: utf-8

# In[237]:


import pandas as pd
import os

school_data_to_load = os.path.join("." , "Resources", "schools_complete.csv")
student_data_to_load = os.path.join("." , "Resources", "students_complete.csv")


# In[238]:


school_data_df = pd.read_csv(school_data_to_load)
student_data_df = pd.read_csv(student_data_to_load)


# In[239]:


student_data_df.count()


# In[240]:



prefixes_suffixes = ["Dr.", "Mr.","Ms.", "Mrs.", "Miss", "MD", "DDS", "DVM", "PhD"]
 
for word in prefixes_suffixes:
        student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")


# In[241]:


student_data_df.head(25)


# In[242]:


thomas_high_school_student_data_df = student_data_df[(student_data_df["school_name"] == "Thomas High School") & (student_data_df["grade"] == "9th")].index


# In[243]:


student_data_df.drop(thomas_high_school_student_data_df, inplace=False)
student_data_df


# In[244]:


student_data_df.count()


# In[245]:


# Install numpy using conda install numpy or pip install numpy. 
# Step 1. Import numpy as np.
import numpy as np


# In[246]:


student_data_df


# In[247]:


student_data_df.loc[
    (student_data_df ["school_name"] == "Thomas High School") 
    & (student_data_df ["grade"] == "9th") & (student_data_df ["reading_score"] > 0) ,"reading_score"] =np.nan 


# In[248]:


student_data_df


# In[249]:


student_data_df


# In[250]:


student_data_df.loc[
    (student_data_df ["school_name"] == "Thomas High School") 
    & (student_data_df ["grade"] == "9th") & (student_data_df ["math_score"] > 0) ,"math_score"] =np.nan 


# In[251]:


# Combine the data into a single dataset
school_data_complete_df = pd.merge(student_data_df, school_data_df, how="left", on=["school_name", "school_name"])
school_data_complete_df.head()


# In[252]:


school_count = len(school_data_complete_df ["school_name"].unique())
student_count = school_data_complete_df ["Student ID"].count()


# In[253]:


total_budget = school_data_df ["budget"]. sum()


# In[254]:


average_reading_score = school_data_complete_df["reading_score"].mean()
average_math_score = school_data_complete_df["math_score"].mean()


# In[255]:


passing_math_count = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)].count()["student_name"]

passing_reading_count = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)].count()["student_name"]

student_count = school_data_complete_df ["Student ID"].count()
                                          
passing_math_percentage = passing_math_count/ float(student_count) * 100
passing_reading_percentage = passing_reading_count/ float(student_count) * 100    


# In[256]:


passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)
                                               & (school_data_complete_df["reading_score"] >= 70)]

overall_passing_math_reading_count = passing_math_reading["student_name"].count()
overall_passing_percentage = overall_passing_math_reading_count / student_count * 100


# In[257]:


district_summary_df = pd.DataFrame(
          {
            "Total Schools": [school_count], 
          "Total Students": [student_count], 
          "Total Budget": [total_budget],
          "Average Math Score": [average_math_score], 
          "Average Reading Score": [average_reading_score],
          "% Passing Math": [passing_math_percentage],
         "% Passing Reading": [passing_reading_percentage],
        "% Overall Passing": [overall_passing_percentage]
          }
)


# In[258]:


district_summary_df 


# In[259]:


district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)
district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("${:,.1f}".format)
district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("${:,.1f}".format)
district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("${:,.1f}".format)
district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("${:,.1f}".format)
district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("${:,.1f}".format)
district_summary_df


# In[260]:


per_school_types = school_data_df.set_index(["school_name"])["type"]

per_school_counts = school_data_complete_df["school_name"].value_counts()


# In[261]:


per_school_budget = school_data_complete_df.groupby(["school_name"]).mean()["budget"]

per_school_capita = per_school_budget / per_school_counts


# In[262]:


per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]
per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]


# In[263]:


per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]
per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]


# In[264]:


per_school_passing_reading


# In[265]:


per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]


# In[266]:


per_school_passing_math


# In[270]:


per_school_passing_math = per_school_passing_math / per_school_counts * 100
per_school_passing_reading = per_school_passing_reading / per_school_counts * 100


# In[272]:


per_school_passing_math


# In[274]:


per_school_math_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70) & 
                                                  (school_data_complete_df["math_score"] >= 70)]


# In[278]:


per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]

per_overall_passing_percentage = per_passing_math_reading/per_school_counts *100


# In[ ]:


per_school_summary_df = pd.DataFrame({
    "School Type": per_school_types,
    "Total Students":per_school_counts,
    "Total School Budget": per_school_budget,
    "Per Student Budget": per_school_capita,
    "Average Math Score": per_school_math,
    "Average Reading Score": per_school_reading,
    "% Passing Math": per_school_passing_math,
    "% Passing Reading": per_school_passing_reading,
    "% Overall Passing": per_overall_passing_percentage
})


# In[ ]:


per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)
per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)


# In[269]:


top_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending =False)
top_schools.head(10)


# In[284]:


ninth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "9th")]
tenth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "10th")]
eleventh_graders = school_data_complete_df[(school_data_complete_df["grade"] == "11th")]
twelfth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "12th")]

ninth_graders_math_scores = ninth_graders.groupby(["school_name"]).mean()["math_score"]
tenth_graders_math_scores = tenth_graders.groupby(["school_name"]).mean()["math_score"]
eleventh_graders_math_scores = eleventh_graders.groupby(["school_name"]).mean()["math_score"]
twelfth_graders_math_scores = twelfth_graders.groupby(["school_name"]).mean()["math_score"]


# In[288]:


math_scores_by_grade=pd.DataFrame({
    "9th": ninth_graders_math_scores,
    "10th": tenth_graders_math_scores,
    "11th": eleventh_graders_math_scores,
    "12th": twelfth_graders_math_scores
})
math_scores_by_grade


# In[293]:


spending_bins = [0,585,630,645,675]
group_names = ["<$584", "$585-$629", "$630-644","$645-675"]
per_school_summary_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita, spending_bins, lables=group_names)
per_school_summary_df


# In[ ]:





# In[ ]:




