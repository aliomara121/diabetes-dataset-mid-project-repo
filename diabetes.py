
import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(layout= 'wide', page_title= 'diabetes_dataset')
st.markdown("<h1 style='text-align: center; color: white;'>diabetes dataset with Analysis</h1>", unsafe_allow_html=True)
st.image('https://elfagr-med.com/media/rokanthemes/blog/images/f/i/file_25.jpg')
df = pd.read_csv('cleaned_df.csv',index_col=0)
page = st.sidebar.radio('Pages', ['Introduction', 'Analysis Questions', 'Reporting'])
if page == 'Introduction':

    st.dataframe(df.head())

    st.header('diabetes_dataset Description')

    st.write('''The dataset contains 10,000 entries and 21 columns. Here's a summary of the columns:

Unnamed: 0 : Index column (can likely be dropped).

Age : Age of the individual (integer).

Sex : Gender: Male or Female.

Ethnicity : Ethnic background (categorical).

BMI : Body Mass Index (float).

Waist_Circumference : Waist size in cm (float).

Fasting_Blood_Glucose : Fasting blood sugar level (float).

HbA1c : Hemoglobin A1c percentage, used to assess blood sugar control (float).

Blood_Pressure_Systolic : Systolic BP (integer).

Blood_Pressure_Diastolic : Diastolic BP (integer).

Cholesterol_Total : Total cholesterol level (float).

Cholesterol_HDL : HDL (good) cholesterol (float).

Cholesterol_LDL : LDL (bad) cholesterol (float).

GGT : Gamma-glutamyl transferase, a liver enzyme (float).

Serum_Urate : Uric acid level in blood (float).

Physical_Activity_Level : Level of physical activity: e.g., Low, Moderate, etc. (categorical).

Dietary_Intake_Calories : Daily caloric intake (integer).

Alcohol_Consumption : Alcohol consumption level (categorical).

Smoking_Status : Smoking status: Never, Former, Current (categorical).

Family_History_of_Diabetes : Binary: 1 if family history exists, 0 otherwise (integer).

Previous_Gestational_Diabetes : Binary: 1 if individual had gestational diabetes previously (integer).''')

elif page == 'Analysis Questions':

    st.header(' Q1 What is the relationship between BMI and fasting blood glucose levels?')
    relation_BMI_Glucose = df[['BMI','Fasting_Blood_Glucose']].corr()
    st.write(df[['BMI','Fasting_Blood_Glucose']].corr())
    st.write(px.scatter(data_frame = df ,x='BMI',y ='Fasting_Blood_Glucose' ,title='relationship between BMI and fasting blood glucose'))
    st.header('Q1 What is the relationship between BMI and HbA1c levels?')
    relation_BMI_HBA1c =df[['BMI','HbA1c']].corr()
    st.write(df[['BMI','HbA1c']].corr())
    st.write(px.scatter(data_frame= df ,x='BMI',y ='HbA1c' ,title='relationship between BMI and HbA1c'))
    st.write('## insight Q1')
    st.write('#### insight from Q1 that the relationship between BMI and fasting blood glucose or HbA1c levels is very weak negative relationship')
    st.header('Q2 Do individuals with a family history of diabetes show higher average HbA1c or glucose levels?')
    family_history_HBA1c = df.groupby('Family_History_of_Diabetes')['HbA1c'].mean().round(3).reset_index()
    st.write(df.groupby('Family_History_of_Diabetes')['HbA1c'].mean().round(3).reset_index())
    st.write(px.bar(data_frame=family_history_HBA1c, x= 'Family_History_of_Diabetes' ,y = 'HbA1c',text_auto=True ,title='Do individuals with a family history of diabetes show higher average HbA1c or glucose levels'))
    st.write('## insight Q2')
    st.write('#### insight from Q2 after comparing the averge HBA1C for both the individuals with a family history of diabetes and the individuals with a no family history of diabete i didnt show higher average HbA1c But the percentages are very close')
    st.header(' Q3 Is there a significant difference in diabetes markers (like HbA1c) between males and females?')
    df_sex_HbA1c = df.groupby('Sex')['HbA1c'].mean().round(2).reset_index()
    st.write(df.groupby('Sex')['HbA1c'].mean().round(2).reset_index())
    st.write(px.bar(data_frame=df_sex_HbA1c,x='Sex',y ='HbA1c' ,text_auto=True ,title='difference in diabetes markers (like HbA1c) between males and females'))
    st.write('## insight Q3')
    st.write('#### insight from Q3 after comparing the averge HBA1C for both males and females there is no a significant difference in diabetes markers')
    st.header('Q4 How does physical activity level impact blood sugar levels or BMI?')
    ph_activity_level_Glucose = df.groupby('Physical_Activity_Level')['Fasting_Blood_Glucose'].mean().round(2).reset_index()
    st.write(df.groupby('Physical_Activity_Level')['Fasting_Blood_Glucose'].mean().round(2).reset_index())
    st.write(px.bar(data_frame=ph_activity_level_Glucose,x='Physical_Activity_Level',y ='Fasting_Blood_Glucose',text_auto=True,title='How does physical activity level impact blood sugar levels'))
    st.write('## insight Q4')
    st.write('#### insight from Q4 after comparing Physical_Activity_Level impact for BMI There is no noticeable effect on BMI')
    st.header('Q5 Are there differences in HBA1C levels among different ethnic groups?')
    Ethnicity_HBA1C = df.groupby('Ethnicity')['HbA1c'].mean().round(2).reset_index()
    st.write( df.groupby('Ethnicity')['HbA1c'].mean().round(2).reset_index())
    st.plotly_chart(px.bar(data_frame=Ethnicity_HBA1C,x='Ethnicity',y ='HbA1c' ,text_auto=True ,title='differences in HBA1C levels among different ethnic groups?'))
    st.write('## insight Q5')
    st.write('#### insight from Q5 after comparing HbA1c impact for each Ethnicity There is no noticeable effect on HBA1C')
    st.header('Q6 Is smoking status linked to higher LDL or lower HDL cholesterol?')
    smoking_LDL = df.groupby('Smoking_Status')[['Cholesterol_LDL','Cholesterol_HDL']].mean().round(2).reset_index()
    smoking_HDL = df.groupby('Smoking_Status')['Cholesterol_HDL'].mean().round(2).reset_index()
    st.write(df.groupby('Smoking_Status')[['Cholesterol_LDL','Cholesterol_HDL']].mean().round(2).reset_index())
    st.plotly_chart(px.bar(data_frame=smoking_LDL,x='Smoking_Status',y ='Cholesterol_LDL' ,text_auto=True,title=' Is smoking status linked to higher LDL ?'))
    st.plotly_chart(px.bar(data_frame=smoking_HDL,x='Smoking_Status',y ='Cholesterol_HDL' ,text_auto=True,title=' Is smoking status linked to Lower HDL ?'))
    st.write('## insight Q6')
    st.write('#### insight from Q6 after comparing Smoking_Status impact for each Cholesterol_LDL and Cholesterol_HDL There is no noticeable effect on higher LDL or lower HDL cholesterol')
    st.header(' Q7 How does previous gestational diabetes affect current glucose control among females?')
    st.write(df[df.Sex =='Female'][['Previous_Gestational_Diabetes','Fasting_Blood_Glucose']].corr())
    female_pr_ge_di__Glucose = df[df.Sex =='Female'][['Previous_Gestational_Diabetes','Fasting_Blood_Glucose']].corr()
    st.plotly_chart(px.line(data_frame=female_pr_ge_di__Glucose,x='Previous_Gestational_Diabetes',y = 'Fasting_Blood_Glucose' ,title='How does previous gestational diabetes affect current glucose control among females?,text'))
    st.write('## insight Q7')
    st.write('#### insight from Q7 after comparing Previous_Gestational_Diabetes impact for Fasting_Blood_Glucose for females There is a weak negative relationship between Previous_Gestational_Diabetes and Fasting_Blood_Glucose')
elif page == 'Reporting':
    sex = st.sidebar.selectbox('Sex' ,df['Sex'].unique())
    ethnicity = st.sidebar.selectbox('Ethnicity', df['Ethnicity'].unique())
    physical_activity_level = st.sidebar.selectbox('physical_activity_level',df['Physical_Activity_Level'].unique())
    smoking_status = st.sidebar.selectbox('Smoking_Status', df['Smoking_Status'].unique())
    df2 = df[(df['Sex']== sex) & (df['Ethnicity'] == ethnicity) &(df['Physical_Activity_Level']== physical_activity_level) & (df['Smoking_Status']==smoking_status) ]
    st.dataframe(df2.head(50))
  
