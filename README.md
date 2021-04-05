# Bank Note Classification

### Summary:

We use the randomeforest machine learning algorithm to predict whether a currency note from banks is authentic or otherwise. To do this, we take in 4 parameters namely variance, skewness, curtosis and entropy and train our ML model on this. Finally, we create a Flask API using Flassger of the same and dockerize the application. 

### Data:

The dataset in this problem is pbtained from [Kaggle](https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data). The images of real and forged bank-notes were processed according to the author:
> Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

### Libraries:

flasgger==0.9.5

Flask==1.1.2

numpy==1.18.4

pandas==1.0.3

scikit-learn==0.22.1

See other packages [here](https://github.com/Sarthak2597/Bank_Note_Classification/blob/main/requirement.txt)

### Machine Learning:

RandomForest Classifier from Sci-kit Learn.

### API:

Using Flask and Flassger

### Creating image, building containers and Running docker container:

We first create a [Dockerfile](https://github.com/Sarthak2597/Bank_Note_Classification/blob/main/Dockerfile) in our working directory, with Debian base image. We then navigate to our working directory and use the following command in Command Prompt (in Docker for Desktop) or Docker Quickstart terminal (Docker toolkit) to build a container.

```
docker build --tag money_api_2 .
```

Finally we run the application from our container using the command 

```
docker run-it --name money_api_2 --rm -p 5000:5000 money_api_2
```
