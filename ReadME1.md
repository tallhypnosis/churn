The flask app takes input in the following json format:

    {
  "feature1": 1.0,
  "feature2": 2.0,
  "feature3": 3.0
}

About Model design:

    I've used neural network to train the model, even after trying learning rate decay method i couldn't get the desired results.
    I used boxplot and histograms for data analysis.
    I tried to details from training a single perceptron model inorder to see it's performance but even then the accuracy was quiet the same, which gave me the conclusion that the model was linearly inseperable.
    I've tried to analyse the model through various plots,it was very difficult to find the most weighted neuron for my neural network,
    since i've only had a window of one day i could not optimize my model more than 52% accuracy but i did try that by using weight matrix.
    If given enough time I might be able to increase the accuracy well beyond that which i will do after submission.


There is some issue with my docker daemon, that is why i could not deploy it, but i you can see my dockerfile attached in it.
I hope you like the project.

Link to my github: https://github.com/tallhypnosis