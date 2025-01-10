import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load your datasets
# Replace 'coffee_data.txt' and 'academic_data.txt' with your actual file paths

# Load the coffee consumption data
coffee_data = pd.read_csv("coffee_data.txt", sep=",", names=["DATE", "COMPANY"], usecols=[0, 1])
coffee_data['DATE'] = pd.to_datetime(coffee_data['DATE'], format="%d/%m/%Y")

# Load academic calendar data
academic_data = pd.read_csv("academic_data.txt", sep=",", names=["DATE", "DEADLINE"], usecols=[0, 1])
academic_data['DATE'] = pd.to_datetime(academic_data['DATE'], format="%d/%m/%Y")

# Aggregate coffee consumption by date and company
coffee_counts = coffee_data.groupby(['DATE', 'COMPANY']).size().reset_index(name='COUNT')
coffee_pivot = coffee_counts.pivot(index='DATE', columns='COMPANY', values='COUNT').fillna(0)

# Aggregate academic deadlines by date
academic_counts = academic_data.groupby('DATE').size().reset_index(name='DEADLINE_COUNT')
academic_counts.set_index('DATE', inplace=True)

# Merge both datasets
merged_data = coffee_pivot.join(academic_counts, how='outer').fillna(0)

# Ensure the DATE column is the index and convert to DatetimeIndex
merged_data.index = pd.to_datetime(merged_data.index)

# Extract the month as a period
merged_data['MONTH'] = merged_data.index.to_period('M')

# Plot stacked bar chart for each month
unique_months = merged_data['MONTH'].unique()
colors = ['skyblue', 'limegreen', 'gold', 'coral', 'violet']
academic_color = 'darkblue'

for month in unique_months:
    month_data = merged_data[merged_data['MONTH'] == month]

    # Separate coffee data and deadlines
    coffee_data_only = month_data.drop(columns=['MONTH', 'DEADLINE_COUNT'])
    deadline_counts = month_data['DEADLINE_COUNT']

    # Plot the coffee data
    fig, ax = plt.subplots(figsize=(14, 7))
    coffee_data_only.plot(kind='bar', stacked=True, ax=ax, color=colors, edgecolor='black', width=0.8)

    # Add the academic deadlines as a separate bar
    ax.bar(
        range(len(deadline_counts)),
        deadline_counts,
        bottom=coffee_data_only.sum(axis=1),
        color=academic_color,
        label='Deadlines',
        edgecolor='black',
        width=0.8
    )

    # Format the x-axis to show all dates
    ax.set_xticks(range(len(month_data.index)))
    ax.set_xticklabels(month_data.index.strftime('%d %b %Y'), rotation=45, ha='right')

    plt.title(f'Daily Coffee Consumption and Deadlines - {month}')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.legend(title='Category')
    plt.gca().set_facecolor('whitesmoke')  # Set a light background to avoid pure white

    # Annotate bars with counts and dates
    for i, (coffee_total, deadline_count) in enumerate(zip(coffee_data_only.sum(axis=1), deadline_counts)):
        if coffee_total > 0:
            plt.text(i, coffee_total / 2, int(coffee_total), ha='center', va='center', fontsize=8, color='black')
        if deadline_count > 0:
            plt.text(i, coffee_total + deadline_count / 2, int(deadline_count), ha='center', va='center', fontsize=8, color='black')

    plt.tight_layout()
    plt.savefig(f"coffee_and_deadlines_{month}.png")
    plt.show()

#Statistics
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from scipy.stats import chi2_contingency
import numpy as np

# Load your datasets
# Replace 'coffee_data.txt' and 'academic_data.txt' with your actual file paths

# Load the coffee consumption data
coffee_data = pd.read_csv("coffee_data.txt", sep=",", names=["DATE", "COMPANY"], usecols=[0, 1])
coffee_data['DATE'] = pd.to_datetime(coffee_data['DATE'], format="%d/%m/%Y")

# Load academic calendar data
academic_data = pd.read_csv("academic_data.txt", sep=",", names=["DATE", "DEADLINE"], usecols=[0, 1])
academic_data['DATE'] = pd.to_datetime(academic_data['DATE'], format="%d/%m/%Y")

# Aggregate coffee consumption by date and company
coffee_counts = coffee_data.groupby(['DATE', 'COMPANY']).size().reset_index(name='COUNT')
coffee_pivot = coffee_counts.pivot(index='DATE', columns='COMPANY', values='COUNT').fillna(0)

# Aggregate academic deadlines by date
academic_counts = academic_data.groupby('DATE').size().reset_index(name='DEADLINE_COUNT')
academic_counts.set_index('DATE', inplace=True)

# Merge both datasets
merged_data = coffee_pivot.join(academic_counts, how='outer').fillna(0)

# Ensure the DATE column is the index and convert to DatetimeIndex
merged_data.index = pd.to_datetime(merged_data.index)

# Extract the month as a period
merged_data['MONTH'] = merged_data.index.to_period('M')

# Aggregate total coffee consumption per day
merged_data['TOTAL_COFFEE'] = coffee_pivot.sum(axis=1)

# Handle missing values
merged_data['TOTAL_COFFEE'] = merged_data['TOTAL_COFFEE'].fillna(0)
merged_data['DEADLINE_COUNT'] = merged_data['DEADLINE_COUNT'].fillna(0)

# --- Linear Regression ---
X = merged_data['DEADLINE_COUNT'].values.reshape(-1, 1)  # Independent variable
y = merged_data['TOTAL_COFFEE'].values  # Dependent variable

# Ensure no NaN values
if np.isnan(y).any() or np.isnan(X).any():
    print("NaN values detected in input data. Ensure all missing values are handled.")
else:
    reg_model = LinearRegression()
    reg_model.fit(X, y)
    slope = reg_model.coef_[0]
    intercept = reg_model.intercept_
    r_squared = reg_model.score(X, y)
    print(f"Linear Regression Results:")
    print(f"Slope: {slope:.2f}, Intercept: {intercept:.2f}, R-squared: {r_squared:.2f}")

# --- Chi-Square Test ---
bins = [0, 1, 2, 3, 4, 5]
merged_data['Coffee_Bins'] = pd.cut(merged_data['TOTAL_COFFEE'], bins=bins, labels=False, include_lowest=True)
merged_data['Deadline_Bins'] = pd.cut(merged_data['DEADLINE_COUNT'], bins=bins, labels=False, include_lowest=True)
contingency_table = pd.crosstab(merged_data['Coffee_Bins'], merged_data['Deadline_Bins'])
chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"Chi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2:.2f}, p-value: {p:.2e}, Degrees of Freedom: {dof}")

# --- Classification Using Logistic Regression ---
merged_data['High_Coffee'] = (merged_data['TOTAL_COFFEE'] > merged_data['TOTAL_COFFEE'].median()).astype(int)
merged_data['High_Deadlines'] = (merged_data['DEADLINE_COUNT'] > merged_data['DEADLINE_COUNT'].median()).astype(int)
X_class = merged_data['High_Deadlines'].values.reshape(-1, 1)
y_class = merged_data['High_Coffee'].values
X_train, X_test, y_train, y_test = train_test_split(X_class, y_class, test_size=0.2, random_state=42)
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))

# --- Correlation Analysis ---
pearson_corr = merged_data[['TOTAL_COFFEE', 'DEADLINE_COUNT']].corr(method='pearson').iloc[0, 1]
spearman_corr = merged_data[['TOTAL_COFFEE', 'DEADLINE_COUNT']].corr(method='spearman').iloc[0, 1]
print(f"Pearson Correlation: {pearson_corr:.2f}")
print(f"Spearman Correlation: {spearman_corr:.2f}")

# --- Scatter Plot with Regression Line ---
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='darkblue', alpha=0.6, edgecolor='black', label='Data points')
plt.plot(X, reg_model.predict(X), color='red', label='Regression Line')
plt.title('Coffee Consumption vs. Deadlines')
plt.xlabel('Deadlines')
plt.ylabel('Coffee Consumption')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("coffee_deadline_correlation_fixed.png")
plt.show()


#to figure out the relationship between coffy and others
# Calculate the visit counts for each coffee shop
coffee_counts = coffee_data["COMPANY"].value_counts()

# Display the counts as a DataFrame
coffee_counts_df = coffee_counts.reset_index()
coffee_counts_df.columns = ["COMPANY", "Visit Count"]
print(coffee_counts_df)

# Plot the bar chart
plt.figure(figsize=(10, 6))
coffee_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Coffee Shop Visit Counts", fontsize=14)
plt.xlabel("Coffee Shop", fontsize=12)
plt.ylabel("Visit Count", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("coffy.png")
plt.show()


