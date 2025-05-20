!pip install seaborn --quiet
     

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
     

data = {
    'Year': [2016, 2017, 2018, 2019, 2020],
    'Sales': [102, 104, 106, 107, 108]
}
     

df = pd.DataFrame(data)
     

#BAD VISUALIZATION (Misleading and Ugly)

plt.figure(figsize=(6, 4))
plt.bar(df['Year'], df['Sales'], color='red')
plt.ylim(100, 110)  # Truncated Y-axis misleads viewer into thinking big change
plt.title("Company Sales (Misleading)")
plt.xlabel("Year")
plt.ylabel("Sales (in Crores)")
plt.grid(False)
plt.tight_layout()
plt.show()
     


#REDESIGNED VISUALIZATION (Clean and Accurate)

plt.figure(figsize=(8, 5))
sns.lineplot(data=df, x='Year', y='Sales', marker='o', color='green')
plt.title("Company Sales (Accurate Representation)")
plt.xlabel("Year")
plt.ylabel("Sales (in Crores)")
plt.ylim(100, 110)  # Still shows the full range for reference
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
