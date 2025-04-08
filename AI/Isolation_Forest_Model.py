import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

#Generate synthetic normal and anomaly data
X_normal = np.random.normal(0, 1, (1000, 2))
X_anomalous = np.random.uniform(6, 8, (50, 2))
X = np.vstack((X_normal, X_anomalous))

#Labels: 0 = normal, 1 = anomaly
y = np.hstack((np.zeros(1000), np.ones(50)))

df = pd.DataFrame(X, columns=['Feature_1', 'Feature_2'])
df['Label'] = y

#Fit the Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df[['Feature_1', 'Feature_2']])
