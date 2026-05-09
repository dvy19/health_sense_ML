import pandas as pd 

df = pd.read_csv("data/indian_diseases_dataset.csv")

def get_top_5_diseases_by_state(state_name):
    state_df = df[df['state'].str.lower() == state_name.lower()]
    if state_df.empty:
        return {"error": f"No data found for state: {state_name}"}
    return state_df['disease_name'].value_counts().head(5).to_dict()

def get_top_5_diseases_by_city(city_name):
    city_df = df[df['city'].str.lower() == city_name.lower()]
    if city_df.empty:
        return {"error": f"No data found for city: {city_name}"}
    return city_df['disease_name'].value_counts().head(5).to_dict()
