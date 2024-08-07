import pandas as pd
import matplotlib.pyplot as plt

rates = pd.read_csv('data/logan_webb_metrics.csv', index_col=0)

plt.figure(figsize=(12, 8))
for col in rates.columns:
    plt.plot(rates.index, rates[col], label=col.replace('_', ' ').title())

plt.title('Pitching Metrics Over Time for Logan Webb (2019-2024)')
plt.xlabel('Year')
plt.ylabel('Rate')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.tight_layout()
plt.show()
