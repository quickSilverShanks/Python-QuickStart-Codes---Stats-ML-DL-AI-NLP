import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map



def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)



def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    # if 'Professional degree' in x or 'Other doctoral' in x:
    if 'Professional degree' in x:
        return 'Post grad'
    return 'Less than a Bachelors'



@st.cache_data
def load_data():
    df_in = pd.read_csv("./data/survey_results_public.csv")
    df = df_in[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]].copy()
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)
    df = df[(df["Salary"] <= 250000) & (df["Salary"] >= 10000) & (df['Country'] != 'Other')]

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    df['EdLevel'] = df['EdLevel'].apply(clean_education)

    return df



df = load_data()



def show_explore_page():
    st.title("Explore Software Developer Salaries")

    st.write("""
                ### Stack Overflow Developer Survey 2023
             """)
    

    data_pie = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data_pie, labels=data_pie.index, autopct="%1.1f%%", shadow=False, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""
                #### Number of data points from different countries
             """)
    st.pyplot(fig1)


    st.write("""
                #### Mean Salary Based On Country
             """)

    data_bar = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data_bar)


    st.write("""
                #### Mean Salary Based On Experience
             """)

    data_line = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data_line)