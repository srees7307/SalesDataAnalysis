import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Display basic information
print("Data Overview:")
print(df.head())
print(df.info())
print(df.describe())

# Handle missing values
df.fillna(0, inplace=True)

# Convert date column to datetime format (if applicable)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

# Sales trend over time
if 'Date' in df.columns and 'Sales' in df.columns:
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Sales'], marker='o', linestyle='-')
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.title("Sales Trend Over Time")
    plt.xticks(rotation=45)
    plt.show()

# Sales distribution by category (Fixed Warning)
if 'Category' in df.columns and 'Sales' in df.columns:
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Category', y='Sales', hue='Category', data=df, palette='viridis', legend=False)
    plt.xlabel("Product Category")
    plt.ylabel("Total Sales")
    plt.title("Sales by Category")
    plt.xticks(rotation=45)
    plt.show()

# Correlation heatmap (Fixed Error)
numeric_df = df.select_dtypes(include=['number'])  # Select only numerical columns
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()

print("Analysis Completed! Check the visualizations.")
