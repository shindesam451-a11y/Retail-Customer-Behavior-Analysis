import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load Dataset
df = pd.read_csv("Mall_Customers.csv")

print(df.head())

print(df.info())

print(df.describe())

# Basic Visualizations

plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=20)
plt.title("Customer Age Distribution")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(
    data=df,
    x='Annual Income (k$)',
    y='Spending Score (1-100)'
)
plt.title("Income vs Spending")
plt.show()

# Feature Selection

X = df[['Annual Income (k$)',
        'Spending Score (1-100)']]

# Scaling

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method

wcss = []

for i in range(1,11):
    kmeans = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)

    wcss.append(kmeans.inertia_)

plt.plot(range(1,11), wcss)
plt.xlabel("Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# KMeans

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

df['Cluster'] = kmeans.fit_predict(X_scaled)

# Cluster Visualization

plt.figure(figsize=(10,6))

sns.scatterplot(
    data=df,
    x='Annual Income (k$)',
    y='Spending Score (1-100)',
    hue='Cluster',
    palette='Set1'
)

plt.title("Customer Segmentation")
plt.show()

# Save Results

df.to_csv(
    "Customer_Segmentation_Output.csv",
    index=False
)

print("Analysis Complete")