import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset (replace 'your_file.csv' with the actual file path)
data = pd.read_csv("./data/shopping_trends.csv")  # Asegúrate de poner la ruta correcta

# Display basic information about the dataset
print("Dataset Info:")
print(data.info())

# Check for null values
print("\nNull Values:")
print(data.isnull().sum())

# Check for unique values in each column to identify "rare" or unexpected values
print("\nUnique Values in Each Column:")
for column in data.columns:
    print(f"{column}: {data[column].unique()}")

# Example cleaning steps (customize as needed):
# 1. Fill or drop null values
data['Age'] = data['Age'].fillna(data['Age'].median())  # Fill null ages with median
data = data.dropna(subset=['Customer ID'])  # Drop rows with null Customer ID

# 2. Handle "rare" or unexpected values
data = data[data['Age'] > 0]  # Remove rows with invalid ages (e.g., negative values)
data = data[data['Review Rating'].between(1, 5)]  # Ensure ratings are between 1 and 5

# 3. Normalize categorical values (e.g., Gender)
data['Gender'] = data['Gender'].str.strip().str.capitalize()  # Standardize gender values

# Save the cleaned dataset
cleaned_file_path = 'cleaned_data.csv'
data.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned data saved to {cleaned_file_path}")

# Create a folder for results if it doesn't exist
results_folder = './results.julian'
os.makedirs(results_folder, exist_ok=True)

# Plot example: Age distribution
plt.figure(figsize=(10, 6))
plt.hist(data['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot as a PNG file
plot_file_path = os.path.join(results_folder, 'age_distribution.png')
plt.savefig(plot_file_path)
plt.close()
print(f"Plot saved to {plot_file_path}")