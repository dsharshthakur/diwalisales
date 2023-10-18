import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sys
import numpy as np
# data=pd.read_csv("Diwali Sales Data.csv",encoding="unicode_escape")
data=pd.read_csv("Diwali Sales Data.csv",sep=",",encoding="unicode_escape")
print(data.columns)
print("*"*55)
                                                 #cleaning
#

print()
#removing null value from amount  column
data["Amount"].fillna(data["Amount"].mean(),inplace=True)
data.drop(labels=["Status","unnamed1"],axis=1,inplace=True)

#making age group on the basis of age
data.drop(labels="Age Group",axis=1,inplace=True)       #drop already existing age group column
data["Age_Group"]=pd.cut(data["Age"],bins=[15,25,35,45,55,65],labels=["15-25","25-35","35-45","45-55","55-65"])

#removing duplicates
data.drop_duplicates(inplace=True)
print(data.duplicated().any())

#convert dtype of amount column to integer.
data["Amount"]=data["Amount"].astype(int)

                                            #show gender distribution
fig=plt.figure()
fig.add_subplot(2,2,1)
plot1=sys.countplot(data=data,x="Gender")
for bar in plot1.containers: #container that store the bar
    plt.bar_label(bar) #creating label to place at the top of each bar.
plt.xlabel("")
plt.title("Gender distribution")

                                    #show total amount spend by each gender
fig.add_subplot(2,2,2)
gender_grp=data.groupby("Gender")
amt_spend=gender_grp["Amount"].sum()
print(amt_spend)
plot2=sys.barplot(x=amt_spend.index,y=amt_spend)
plt.title("Spending on the basis of gender")


                                                        #show age distribution
fig.add_subplot(2,2,3)
plot3=sys.countplot(data=data,x="Age_Group",hue="Gender")
for bar in plot3.containers:                 #container that store the bar
    plt.bar_label(bar,padding=0)                       #creating label to place at the top of each bar.
plt.yticks([0,1000,2000,3000,4000])
plt.title("Age distribution")


                                                        #show total order from different states
fig2=plt.figure()
fig2.add_subplot(1,3,1)
state_grp=data.groupby("State")
state_orders=state_grp["Orders"].sum().sort_values(ascending=False)
plot4=sys.barplot(y=state_orders.index,x=state_orders)
plt.xlim([0,6000])
for bar in plot4.containers:
    plt.bar_label(bar)
plt.title("Orders from different  states")

                                                 #show sale amount from different states

fig2.add_subplot(1,3,3)
state_amt=state_grp["Amount"].sum().sort_values(ascending=False)
plot5=sys.barplot(y=state_amt.index,x=state_amt)
plt.title("Spendings from different states")



                                                #show maritial status
fig3=plt.figure()
plot6=sys.countplot(data=data,x="Marital_Status")
plt.title("Marital Status (0=>'married' and 1=>'single']")


                                            #show occupation distribution
fig4=plt.figure()
plot7=sys.countplot(data,x="Occupation",order=data["Occupation"].value_counts(ascending=False).index)
for bar in plot7.containers:
    plt.bar_label(bar)
plt.xticks(rotation=20)
plt.title("Distribution of occupation ")

                                        #Most frequent product categories
fig5=plt.figure()
fig5.add_subplot(1,3,1)
pcategory_count=data["Product_Category"].value_counts(ascending=False).index
sys.countplot(data=data,y="Product_Category",order=pcategory_count)
plt.title("Most frequent product category")


                                        #Total sales amount from product categories
product_grp=data.groupby("Product_Category")
category_amt=product_grp["Amount"].sum().sort_values(ascending=False)
fig5.add_subplot(1,3,3)
sys.barplot(y=category_amt.index,x=category_amt)
plt.title("Sales amount in different product category")
plt.show()
print()