# house_prediction
The objective of our project is to position ourselves as a real estate agency that offers several services, including home price estimation. To do so, we used a database of house prices in the United States from Kaggle:https://www.kaggle.com/datasets/shree1992/housedata. Our home price prediction method was based on a machine learning model: the gradient boosting regressor.

Thus, a user wishing to estimate the price of his potential future house just entered the characteristics of the said house and an estimate of the price will be given. 

## Run the app
To run the app, go to the proper directory on your terminal and do: `export FLASK_APP = app.py`, then do: `flask run`. 
For a better user experience, it is best to use google chrome or microsoft edge browser to open the application.

## In your terminal
### To build the image : 
`docker build -t house_prediction .`

### To run the app :
`docker run -d -p 5000:5000`

## Difficulties encountered during the implementation of the application

We had saved our machine learning model with pickle. However, we could not get any predictions. After a lot of research, we got around the problem by putting the model (training and test) directly into the application. 

Also, we started with a dynamic form using javascript. However, we were not able to retrieve the data from each question in order to use it in the model. After several tries, we decided to stay on a static form which gives good predictions.



