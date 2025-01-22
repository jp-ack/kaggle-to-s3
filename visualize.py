from transform import pull_from_s3
import matplotlib.pyplot as plt
import seaborn as sns

#pulls data from s3 bucket and prints first few rows (file must exist in bucket)
data = pull_from_s3()
#print(data.head(20))

# Scatter plot between Age and Daily Water Intake
# Line plot between Age and Daily Water Intake
plt.figure(figsize=(10,6))
sns.lineplot(x='Age', y='Daily_Water_Intake', data=data, marker='o')
plt.title('Age vs. Daily Water Intake (Line Plot)')
plt.xlabel('Age')
plt.ylabel('Daily Water Intake (L)')
plt.show()



