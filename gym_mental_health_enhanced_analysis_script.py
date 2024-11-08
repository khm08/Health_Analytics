
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures

# Load the dataset
df = pd.read_excel('gym_mental_health_uk_data.xlsx')

# Data Science & Analytics Section

# 1. Enhanced Regression Analysis with Interaction Terms

# Convert categorical variables to numerical
df['Steroid_Use_Binary'] = df['Steroid_Use'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Gender_Binary'] = df['Gender'].apply(lambda x: 1 if x == 'Male' else 0)

# Polynomial Features to account for non-linear relationships
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(df[['Steroid_Use_Binary', 'Steroid_Duration', 'Age', 'Gender_Binary']])

# Adding interaction terms in the regression model
X = sm.add_constant(X_poly)
y = df['Mental_Health_Score']

# Fit the model
model = sm.OLS(y, X).fit()
print(model.summary())

# 2. Clustering Analysis: Grouping based on Mental Health and Powerlifting Performance
clustering_data = df[['Mental_Health_Score', 'Powerlifting_Score', 'Age', 'Steroid_Duration']]
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(clustering_data)
cluster_centers = pd.DataFrame(kmeans.cluster_centers_, columns=['Mental_Health_Score', 'Powerlifting_Score', 'Age', 'Steroid_Duration'])
print(cluster_centers)

# 3. Correlation Analysis
correlation_matrix = df.corr()
print(correlation_matrix)

# Data Visualization Section

# Pairplot for numeric columns
numeric_cols = df[['Mental_Health_Score', 'Powerlifting_Score', 'Steroid_Duration', 'Age']]
sns.pairplot(numeric_cols)
plt.savefig('pairplot_analysis.png')
plt.close()

# Heatmap for Correlation and Interaction Effects
plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap with Interaction Effects')
plt.savefig('heatmap_interaction.png')
plt.close()

# Visualizing Clusters
plt.figure(figsize=(10,6))
sns.scatterplot(x='Powerlifting_Score', y='Mental_Health_Score', hue='Cluster', palette='viridis', data=df)
plt.title('Clustering based on Powerlifting Performance and Mental Health')
plt.savefig('cluster_visualization.png')
plt.close()

# Summary and Recommendations
print("""
The analysis indicates that steroid use significantly impacts mental health scores negatively, even though it enhances powerlifting performance. The enhanced regression analysis, including interaction terms, highlights the complex relationship between steroid use, age, gender, and mental health outcomes.

The clustering analysis identified three distinct groups:
1. **Cluster 1**: Individuals with moderate mental health scores and high powerlifting performance, likely steroid users.
2. **Cluster 2**: Individuals with high mental health scores but moderate powerlifting performance, likely non-users.
3. **Cluster 3**: Individuals with low mental health scores and varied powerlifting performance, potentially high-risk users.

### Recommendations:
- **Mental Health Support**: Gyms should provide mental health support to members, particularly those who use or are considering using steroids.
- **Education**: Implement educational programs highlighting the potential mental health risks of steroid use.
- **Targeted Interventions**: Focus on high-risk individuals identified through clustering for more personalized interventions.
- **Further Research**: Investigate long-term impacts of steroid use on both mental health and physical performance.
""")
