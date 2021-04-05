# Bank Note Classification

### Summary:

We use the randomeforest machine learning algorithm to predict whether a currency note from banks is authentic or otherwise. To do this, we take in 4 parameters namely variance, skewness, curtosis and entropy and train our ML model on this. Finally, we create a Flask API using Flassger of the same and dockerize the application. 

### Data:

The dataset in this problem is pbtained from [Kaggle](https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data). The images of real and forged bank-notes were processed according to the author:
> Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.
