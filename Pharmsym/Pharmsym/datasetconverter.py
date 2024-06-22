import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Cargar el dataset
df = pd.read_csv('dataset.csv')

# Inicializar el codificador de etiquetas
le = LabelEncoder()

# Convertir columnas de síntomas a categorías
symptom_columns = ['Symptom_1' ,'Symptom_2' ,'Symptom_3' ,'Symptom_4' ,'Symptom_5' ,'Symptom_6' ,
                   'Symptom_7' , 'Symptom_8' ,'Symptom_9' ,'Symptom_10' ,'Symptom_11' ,'Symptom_12' ,
                   'Symptom_13' ,'Symptom_14' ,'Symptom_15' ,'Symptom_16' ,'Symptom_17']  # Añadir todas las columnas de síntomas
for col in symptom_columns:
    df[col] = le.fit_transform(df[col])

# Guardar el nuevo dataset
df.to_csv('dataset.csv', index=False)
