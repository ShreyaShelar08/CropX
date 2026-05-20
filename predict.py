import pandas as pd
import mysql.connector 
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
    'land_area': [1.5, 2.0, 3.5, 1.2, 4.0, 2.5, 3.0, 1.8, 2.2, 3.8, 2.7, 1.0],
    'soil_color': ['brown', 'black', 'red', 'brown', 'black', 'red', 'black', 'brown', 'red', 'black', 'brown', 'red'],
    'region': ['north', 'south', 'east', 'west', 'north', 'south', 'east', 'west', 'north', 'south', 'east', 'west'],
    'past_crop_details': ['wheat', 'rice', 'maize', 'rice', 'wheat', 'maize', 'rice', 'wheat', 'maize', 'rice', 'wheat', 'maize'],
    'predicted_crop': ['wheat', 'rice', 'maize', 'rice', 'wheat', 'maize', 'rice', 'wheat', 'maize', 'rice', 'wheat', 'maize']
}

df = pd.DataFrame(data)
df_dummies = pd.get_dummies(df, columns=['soil_color', 'region', 'past_crop_details'])
X = df_dummies.drop('predicted_crop', axis=1)
y = df_dummies['predicted_crop']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

model_filename = 'crop_prediction_model.pkl'
columns_filename = 'model_columns.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model, file)
with open(columns_filename, 'wb') as file:
    pickle.dump(X.columns.tolist(), file)

print("Model and columns saved successfully.\n")

def fetch_farmer_data(farmer_id, db_config):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT land_area, soil_color,region, past_crop_details FROM farmer_details WHERE id = %s"
        cursor.execute(query, (farmer_id,))
        record = cursor.fetchone()
        
        if record:
                # Use past_crop_details directly from the record
                new_data_dict = {
                    'land_area': record['land_area'],
                    'soil_color': record['soil_color'],
                    'region': record['region'],
                    'past_crop_details': record['past_crop_details']
                }
                return new_data_dict
        else:
            print("Farmer not found.")
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def predict_crop_from_db(farmer_id, db_config):
    # Load the trained model and the list of columns
    with open('crop_prediction_model.pkl', 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    with open('model_columns.pkl', 'rb') as columns_file:
        model_columns = pickle.load(columns_file)

    # Fetch the data for the specified farmer
    farmer_data = fetch_farmer_data(farmer_id, db_config)
    
    if farmer_data:
        # Convert the fetched data into a DataFrame with one-hot encoding
        df_new_data = pd.DataFrame([farmer_data])
        df_new_data_dummies = pd.get_dummies(df_new_data, columns=['soil_color', 'region', 'past_crop_details'])
        
        # Ensure the columns match the training data
        final_df = df_new_data_dummies.reindex(columns=model_columns, fill_value=0)
        
        # Make the prediction
        prediction = loaded_model.predict(final_df)
        return prediction[0]
    else:
        return None
    
db_config = {
    'user': 'root',
    'password': 'SIH@2025',
    'host': 'localhost',
    'database': 'user_auth_db'
}

farmer_to_predict = 1  
predicted_crop = predict_crop_from_db(farmer_to_predict, db_config)

if predicted_crop:
    print(f"Predicted crop for farmer ID {farmer_to_predict}: {predicted_crop}")
else:
    print("Could not make a prediction.")

