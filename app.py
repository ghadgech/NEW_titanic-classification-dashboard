import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
confusion_matrix,
accuracy_score,
precision_score,
recall_score,
f1_score,
roc_curve,
roc_auc_score
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
RandomForestClassifier,
GradientBoostingClassifier
)

from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier


# ----------------------
# TITLE
# ----------------------

st.title("Titanic Classification Dashboard")

# ----------------------
# LOAD DATA
# ----------------------

df=sns.load_dataset("titanic")

st.subheader("Raw Dataset")

st.dataframe(df)


# ----------------------
# PREPROCESS
# ----------------------

keep=[
"survived",
"pclass",
"sex",
"age",
"sibsp",
"parch",
"fare",
"embarked"
]

df=df[keep]

df["age"]=df["age"].fillna(df["age"].median())

df["embarked"]=df["embarked"].fillna(
df["embarked"].mode()[0]
)

df=pd.get_dummies(
df,
drop_first=True
)

target="survived"

X=df.drop(
target,
axis=1
)

y=df[target]



# ----------------------
# MODEL SELECT
# ----------------------

model_name=st.selectbox(
"Choose Model",
[
"Logistic",
"DecisionTree",
"RandomForest",
"GBM",
"XGBoost",
"CatBoost",
"LightGBM"
]
)


test=st.slider(
"Test Size",
0.1,
0.5,
0.2
)

X_train,X_test,y_train,y_test=(
train_test_split(
X,
y,
test_size=test,
random_state=42
)
)



# ----------------------
# MODEL
# ----------------------

if model_name=="Logistic":

 model=LogisticRegression(
 max_iter=500
 )

elif model_name=="DecisionTree":

 model=DecisionTreeClassifier()

elif model_name=="RandomForest":

 model=RandomForestClassifier()

elif model_name=="GBM":

 model=GradientBoostingClassifier()

elif model_name=="XGBoost":

 model=XGBClassifier()

elif model_name=="CatBoost":

 model=CatBoostClassifier(
 verbose=0
 )

else:

 model=LGBMClassifier()



# ----------------------
# TRAIN
# ----------------------

if st.button("Run"):

 model.fit(
 X_train,
 y_train
 )

 pred=model.predict(
 X_test
 )

 prob=model.predict_proba(
 X_test
 )[:,1]



 # -------------------
 # METRICS
 # -------------------

 acc=accuracy_score(
 y_test,
 pred
 )

 precision=precision_score(
 y_test,
 pred
 )

 recall=recall_score(
 y_test,
 pred
 )

 f1=f1_score(
 y_test,
 pred
 )

 auc=roc_auc_score(
 y_test,
 prob
 )

 cm=confusion_matrix(
 y_test,
 pred
 )

 tn,fp,fn,tp=cm.ravel()

 tpr=tp/(tp+fn)

 fprate=fp/(fp+tn)



 metric_df=pd.DataFrame({

 "Metric":[

 "Accuracy",
 "Precision",
 "Recall",
 "F1",
 "TPR",
 "FPR",
 "AUC"

 ],

 "Value":[

 acc,
 precision,
 recall,
 f1,
 tpr,
 fprate,
 auc

 ]

 })


 st.subheader(
 "Metrics"
 )

 st.dataframe(
 metric_df
 )



 cm_df=pd.DataFrame(
 cm,
 columns=[
 "Pred0",
 "Pred1"
 ],
 index=[
 "Actual0",
 "Actual1"
 ]
 )

 st.subheader(
 "Confusion Matrix"
 )

 st.dataframe(
 cm_df
 )



 # -------------------
 # ROC
 # -------------------

 roc_fpr,roc_tpr,_=roc_curve(
 y_test,
 prob
 )

 fig,ax=plt.subplots()

 ax.plot(
 roc_fpr,
 roc_tpr
 )

 ax.set_title(
 f"ROC AUC={auc:.3f}"
 )

 st.pyplot(
 fig
 )



 # -------------------
 # TEST OUTPUT
 # -------------------

 test_df=X_test.copy()

 test_df["Actual"]=(
 y_test.values
 )

 test_df["Prediction"]=(
 pred
 )

 test_df["Probability"]=(
 prob
 )



 # -------------------
 # EXCEL
 # -------------------

 output=BytesIO()

 with pd.ExcelWriter(
 output,
 engine="xlsxwriter"
 ) as writer:



  sns.load_dataset(
  "titanic"
  ).to_excel(

  writer,

  sheet_name=
  "rawdata",

  index=False
  )



  X_train.assign(
  survived=y_train
  ).to_excel(

  writer,

  sheet_name=
  "train",

  index=False
  )



  test_df.to_excel(

  writer,

  sheet_name=
  "test",

  index=False
  )



  cm_df.to_excel(

  writer,

  sheet_name=
  "confusion"

  )



  metric_df.to_excel(

  writer,

  sheet_name=
  "metrics",

  index=False
  )



  pd.DataFrame({

  "FPR":
  roc_fpr,

  "TPR":
  roc_tpr,

  "AUC":
  [auc]+[None]*(len(roc_fpr)-1)

  }).to_excel(

  writer,

  sheet_name=
  "roc_auc",

  index=False
  )



 st.download_button(

 "Download Excel",

 output.getvalue(),

 f"{model_name}.xlsx"

 )
