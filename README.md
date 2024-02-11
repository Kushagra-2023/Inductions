# Inductions
NLP; Sentiment analysis attempt using Doc2Vec model

The given task expected us to design a pipeline using our own model to detct the sentiment in a sentence.

The components of the code include :-
1. NLTK tokenizer and lemmetizer.
2. Doc2Vec model for vectorization of text. (Earlier I tried using Word2Vec but Doc2Vec was more suited for working with sentences)
3. LSTM for predicting the sentiment.

Approach:
1. Cleaning the text data.
2. Training Doc2Vec.
3. Extracting sentence vectors.
4. Training my neural network.
5. Making predictions.

I faced difficulty in training my Doc2Vec model as it required large (and good data). I did find some good datasets but they were too large to be loaded in colab notebook, and train time was even larger. In the end I had to balance resources and quality. Having reached limitations due to computational, my predictions were as good as random, but I believe there's still scope for improvement if I find a relevant dataset and somehow train for 'even longer'.
The good thing about my model is that it gives output in almost a second.

Steps to run the project :
  Just run all at once!

URL: https://827efa31e0772b5341.gradio.live
![image](https://github.com/Kushagra-2023/Inductions/assets/142250675/9bcad662-9e9d-4242-8d99-d759ee63855a)


