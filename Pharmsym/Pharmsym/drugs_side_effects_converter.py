import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Cargar el dataset
df = pd.read_csv('drugs_side_effects_drugs_com.csv')

# Inicializar el codificador de etiquetas
le = LabelEncoder()

# Convertir columnas de síntomas a categorías
sickness_columns = ['medical_condition']  # Añadir todas las columnas de síntomas
for col in sickness_columns:
    df[col] = le.fit_transform(df[col])

# Guardar el nuevo dataset
df.to_csv('drugs_side_effects_drugs_com.csv', index=False)