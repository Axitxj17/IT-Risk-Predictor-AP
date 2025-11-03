import pandas as pd
import numpy as np

#reproductibility seed
np.random.seed(42)
n = 1000

#Generate audit features
data = pd.DataFrame({
    'audit_id': np.arange(1, n + 1),
    'audit_score': np.random.randint(50, 101, size=n),
    'num_issues_found': np.random.poisson(lam=5, size=n),
    'audit_duration_days': np.random.randint(1, 31, size=n)
})

#creat target variable 'is_compliant'
data['is_compliant'] = np.where(
    (data['audit_score'] >= 75) & (data['num_issues_found'] <= 3),
    1,
    0
)

#save dataset to CSV
data.to_csv('audit_data.csv', index=False)
print("Dataset 'audit_data.csv' generated successfully.")