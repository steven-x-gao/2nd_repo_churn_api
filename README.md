# 2nd_repo_churn_api
1.This is a ecom_chur API for predicting online user loss for an e-Commerce business;
2. Final data were cleaned out from 2.7 million rows of timestamps raw_data of 4 month user browsing records;
3. Users who has no record in the last month but were actively buying or adding to cart were difined churn customers(class 1);
4. Users who has at least one record in the last month and were actively buying or adding to cart were difined non-churn customers(class 0);
5. Total 35 features were generated through feature engineering(user shopping behavior aggregation);
6. Top features were selected based on the rank of importance in LightGBoost model;
7. Final features in Web API may be reduced further in the next version to avoid the redundant requests of value input;
8. Web page implementation of SHAP force plot visulization is under processing...
