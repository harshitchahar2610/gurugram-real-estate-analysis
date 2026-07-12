import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data.csv")


# Data Cleaning
df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
df=df.drop_duplicates()


# Numerical column cleaning
df['price']=df['price'].astype(str).str.replace(",", "").astype(float)
df['area']=df['area'].astype(str).str.replace(",", "").astype(int)
df['rate_per_sqft']=df['rate_per_sqft'].astype(str).str.replace(",", "").astype(int)


#  Categorical data cleaning
df['status']=df['status'].str.strip().str.lower()
df['rera_approval']=df['rera_approval'].str.strip().str.lower().map({'approved by rera':True, 'not approved by rera':False})
df['flat_type']=df['flat_type'].str.lower().str.strip()
# print(df.info())


#Visualization

# Question 1: Which is the costliest flat in dataset ?
costliest_flat=df.loc[df['price'].idxmax()]
print(f"The costliest flat is a {costliest_flat['bhk_count']} Bhk flat located in {costliest_flat['locality']} priced at {costliest_flat['price']/10000000} crores in {costliest_flat['socity'] }  socity. ")


# Question 2: Which locality has the highest average price ?
highest_average_price=df.groupby('locality')['price'].mean().idxmax()
print(f"locality with the highest average price is {highest_average_price}.  ")


# Question 3: Which locality with has the highest average rate per sqft foot ?
highest_rate_per_sqrt = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"locality with the highest rate per sqrt foot is {highest_rate_per_sqrt}. ")


# Question 4:  Do ready to move properties cost more than under-construction properties?
ready_to_move_avg_price = df[df['status']=='ready to move']['price'].mean()
under_construction_avg_price = df[df['status']=='under construction']['price'].mean()
if (ready_to_move_avg_price > under_construction_avg_price):
    print("Ready to move properties cost more on average than under-construction properties.")
else:
    print("under-construction properties cost more on average than ready-to-move properties.")


#Question 5:  Do RERA-approved properties command a price premium?

rera_approved_avg_price = df[df['rera_approval']==True]['price'].mean()
rera_not_approved_avg_price = df[df['rera_approval']==False]['price'].mean()

if(rera_approved_avg_price > rera_not_approved_avg_price):
    print("RERA-approved properties command a price premium")
else:
    print("RERA-approved properties do not command a price premium")


#Question 6: How does area impact price?
sns.scatterplot(data = df, x= 'area', y= 'price')
plt.title("Area vs Price")
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.savefig("Area_vs_price.png", dpi=300, bbox_inches="tight")
plt.show()


#Question 7: Which BHK configuration is most expensive based on per sqft rate?
most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive BHK configuration on average is {most_expensive_bhk} BHK.")


#Question 8:Which property type is the costliest?
most_expensive_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive property type is {most_expensive_property_type}.")


#Question 9: Do certain builders price higher?
print("The top 5 builders that price higher are:", end=" ")
top_5_builders = df.groupby("company_name")['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
for builder in top_5_builders.index:
    print(builder, end=", ")

plt.title("Top 5 Builders by Average Rate per Sq Ft")

plt.xlabel("Average Rate per Sq Ft")

plt.ylabel("Builder")
sns.barplot(x=top_5_builders.values,y=top_5_builders.index)
plt.savefig("top_5_builders.png", dpi=300, bbox_inches="tight")
plt.show()


#Question 10: Are larger homes more expensive per sqft?
sns.scatterplot(data=df, x= 'area', y= 'rate_per_sqft')
plt.title("Area vs Price Per Sq Ft")
plt.xlabel("Area ")
plt.ylabel("Rate Per Sq Ft")
plt.savefig("Area_vs_rate.png", dpi=300)
plt.show()








