# Create the scatterplot
sns.scatterplot(data = divorce, x = "marriage_duration", y = "num_kids")
plt.show()

##########################################################

# Create a pairplot for income_woman and marriage_duration
sns.pairplot(data = divorce, vars = ["income_woman", "marriage_duration"])
plt.show()

##########################################################

# Create the scatter plot
sns.scatterplot(data = divorce, x = "woman_age_marriage", y = "income_woman", hue = "education_woman")
plt.show()

##########################################################

# Update the KDE plot to show a cumulative distribution function
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0, cumulative = True)
plt.show()