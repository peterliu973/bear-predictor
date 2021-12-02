**Project Overview**

People in finance have always been interested in making market prediction. In 1910, a polish economist Pawel Ciompa published the first paper that describe using statistic methods on economic data to model future trends. Given enough data and analysis, models can be built to predict near future events with certain degree of accuracy. For many reasons financial modelling remains inaccessible to most people. Analyzing large amount of data requires fast and costly computing power. The algorithms tend to be complex and difficult to understand. But most of all, since the knowledge is so valuable monetary, it is not easily shared. Financial computer modelling remains one of the best kept secret in finance. With the continuing advances of computer resources both hardware and software, and financial data readily available online, building a financial computer model is more accessible than before. In this project I will apply machine learning technique to make market prediction.

The US stock market has been on a steady rise since early 2009. Many investors believe the market cannot sustain this trend forever. They believe the market should fall slightly from time to time to maintain the long term health. The slight bumps of market corrections are more desirable than a large market crash event. In this project, I will build a model to predict when a correction is going to occur. With this knowledge, an investor can choose to sell their investments before a correction, and buy it back during the correction at a lower price.

**Problem Statement**

The goal of this project is to create a model to predict when the rising US stock market will sustain market correction. A correction is defined as a 10% drop from the 52 week high. In this model, the Dow Jones Industry Average (DJA) will be an alias for the US stock market.

The following tasks is to be considered:

- Download and preprocess publicly available financial data from sources such as Yahoo Finance, Bureau of Labor and Statistics, and the US Treasury Department.
- Perform data analysis to determine periods of market corrections.
- Create a neural network model using Python and Keras on top of Tensorflow to train and learn to predict market corrections.
- Test the model

The model will output three variables corresponding to short term correction, medium term correction, and longer term correction. The variable ranges from 0 to 1 with 0 meaning low probability of correction, and 1 meaning high probability of correction.
