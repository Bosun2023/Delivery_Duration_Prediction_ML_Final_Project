# Delivery Duration Prediction - DoorDash 

## Project Overview

In this completed project, I focused on predicting delivery times for DoorDash orders. My primary goal was to develop a predictive model capable of accurately estimating the time it takes for an order to be delivered. This prediction is crucial for optimizing delivery operations and enhancing customer satisfaction.

## Dataset

The dataset utilized in this project originates from doordash historical_data.csv, which comprises a curated subset of DoorDash deliveries recorded in the early months of 2015 across specific cities. Each row in this dataset represents a distinct delivery, and to preserve the confidentiality of sensitive business details, certain information has been intentionally obfuscated.

In this dataset, each column corresponds to a distinct feature. Notably, all monetary values are presented in cents, while time durations are consistently measured in seconds.

It's worth noting that this data project has been employed as a take-home assignment in the recruitment process for data science positions at DoorDash. The primary objective of this dataset is to predict the total time duration, measured in seconds, between the "created_at" timestamp, indicating the order submission time, and the "actual_delivery_time," which signifies the successful delivery of the order. This predictive task serves as a fundamental component of optimizing DoorDash's delivery operations and enhancing the overall customer experience.

## Project Workflow

### Part I: Data Preparation and Exploration

1. **Data Loading and Exploration:** I imported and thoroughly explored the delivery dataset, gaining insights into its structure and content.

2. **Data Cleaning:** I handled missing values, outliers, and formatting issues to ensure the data's quality and consistency.

3. **Data Visualization:** Key statistics and relationships within the data were visualized to identify patterns and potential insights.

### Part II: Feature Engineering

1. **Feature Selection:** I identified the most relevant features for predicting delivery time, considering factors such as customer location, restaurant information, and historical delivery times.

2. **Feature Transformation:** I performed necessary data transformations and preprocessing steps to prepare the features for modeling.

### Part III: Model Development

1. **Model Selection:** I carefully chose appropriate machine learning models for regression, including Random Forest, XGBoost, and Gradient Boosting, considering their suitability for the prediction task.

2. **Model Training:** The selected models were trained on the training data, and I fine-tuned their hyperparameters to optimize predictive performance.

### Part IV: Model Evaluation

1. **Model Performance:** I evaluated the models' performance using various metrics, including Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared (R^2).

2. **Hyperparameter Tuning:** To achieve better performance, I optimized the models' hyperparameters through systematic tuning.

### Part V: Model Deployment

1. **Flask Application:** The best-performing model, XGBoost Regressor, was deployed as a Flask API, enabling real-time predictions of delivery times.

## Models Used

I employed three machine learning models for regression:

1. **Random Forest Regressor:** A robust ensemble learning method.

2. **XGBoost Regressor:** An optimized gradient boosting algorithm.

3. **Gradient Boosting Regressor:** A boosting technique for improved prediction.

## Results and Insights

1. **Accurate Delivery Time Prediction:** The project successfully delivered a model capable of accurately predicting delivery times. The XGBoost Regressor outperformed other models, with an MAE of 552.43 seconds, an RMSE of 704.67 seconds, and an R-squared value of 0.34 on the test set.

2. **Feature Insights:** Feature engineering and selection processes identified the most influential factors affecting delivery times. Key features included customer location, restaurant preparation time, and historical delivery data.

3. **Model Optimization:** Through rigorous model training and hyperparameter tuning, I optimized predictive accuracy, ensuring robust performance.

4. **Real-time Predictions:** The final model was deployed as a Flask API, facilitating real-time delivery time predictions and integration with the DoorDash platform.

## Future Enhancements

1. **Refined Stage-Based Predictions:** Implementing a stage-based approach to predict delivery times by breaking down the process into distinct phases, such as pick-up time, driving time, and drop-off time, holds promise for enhancing forecasting accuracy. For instance, addressing factors like parking availability or building access issues could involve building dedicated models to predict pick-up times, allowing for a more precise estimation.

2. **Incorporation of Geospatial Data:** Expanding the dataset to include zip codes and specific delivery addresses would provide a clearer and more granular location perspective. Integration with mapping services like Google Maps or Apple Maps could offer real-time traffic updates, enabling us to capture accurate driving times, especially in varying traffic conditions.

3. **Weather and Environmental Factors:** Recognizing the impact of weather and temperature on delivery times, integrating weather data into the model could enhance predictions. Accounting for adverse weather conditions and their influence on delivery speed would lead to more reliable estimates.

4. **Enhanced User Experience:** Prioritizing user-friendly interfaces for both customers and delivery drivers remains a key focus. Implementing intuitive tools for accessing real-time delivery predictions would contribute to a smoother and more satisfactory experience.

5. **Scalability:** Preparing the model and API infrastructure to handle increased demand is crucial as DoorDash continues to grow. Ensuring scalability will guarantee consistent and efficient service even during periods of high activity.

6. **Security and Privacy:** Robust security measures will be paramount to safeguard customer data and maintain strict privacy standards. Maintaining the confidentiality and integrity of sensitive information remains a top priority.

7. **Customer Feedback Integration:** Leveraging customer feedback can be a valuable resource for model improvement. Utilizing feedback to fine-tune the model will ultimately lead to more accurate predictions and an enhanced customer experience.

These enhancements represent a strategic roadmap for further improving DoorDash's delivery time predictions and overall service quality. By addressing specific stages, geospatial data, environmental factors, and user experience, DoorDash can continue to lead in the competitive delivery industry.

## Tableau Visualizations

In addition to the predictive model, I leveraged Tableau to create insightful visualizations and a dashboard that provide a comprehensive view of DoorDash's delivery duration and related insights. Here's an overview of the Tableau work:

### Tableau Dashboard

#### Store Performance Analysis

- **Bar Chart of Store Primary Category by Subtotal**
  - Visualizes how different store primary categories contribute to the total order value (subtotal).
  - Provides insights into popular store categories, revenue distribution, and market trends.

#### Delivery Insights

- **Line Chart of Daily Average Delivery Duration**
  - Displays trends in daily delivery durations over time.
  - Offers insights into delivery time trends, seasonal variations, and operational efficiency.

- **Pie Chart of Timeslot by Subtotal**
  - Compares the distribution of deliveries across various time slots (Morning, Afternoon, Evening, Night).
  - Provides insights into time slot popularity, peak hours, and trends.

- **Stacked Bar Chart of Average Onshift Doordasher, Average Busy Doordasher, and Line Chart of Average Delivery Duration**
  - Visualizes dasher availability, busyness, and their impact on delivery duration.
  - Offers insights into dasher operations and their correlation with delivery times.

These Tableau visualizations will play a crucial role in providing actionable insights and enhancing decision-making processes for DoorDash. They will enable stakeholders to explore data interactively. 
