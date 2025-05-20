import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data representing categories and their corresponding values
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [40, 30, 20, 10]
}

df = pd.DataFrame(data)

# Set the style
sns.set(style="whitegrid")

# Create a horizontal bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x='Value', y='Category', data=df, palette='muted')

# Add labels and title
plt.title('Redesigned Chart: Category Distribution')
plt.xlabel('Percentage')
plt.ylabel('Category')

# Show the plot
plt.tight_layout()
plt.show()
