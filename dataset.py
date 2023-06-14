




import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white",color_codes=True)





iris=pd.read_csv("Iris.csv")
iris.head()





iris[0:150:15]





iris["Species"].value_counts()





iris.plot(kind="scatter",x="SepalLengthCm",y="SepalWidthCm")





sns.jointplot(x="SepalLengthCm",y="SepalWidthCm",data=iris,height=5)





sns.FacetGrid(iris,hue="Species",height=5).map(plt.scatter,"SepalLengthCm","SepalWidthCm").add_legend()





sns.boxplot(x="Species",y="PetalLengthCm",data=iris)





ax=sns.boxplot(x="Species",y="PetalLengthCm",data=iris)
ax=sns.stripplot(x="Species",y="PetalLengthCm",jitter=True,data=iris,edgecolor="gray")





sns.violinplot(x="Species",y="PetalLengthCm",data=iris,size=6)





sns.FacetGrid(iris,hue="Species",height=6).map(sns.kdeplot,"PetalLengthCm").add_legend()





sns.pairplot(iris.drop("Id",axis=1),hue="Species",height=3)