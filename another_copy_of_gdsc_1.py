# -*- coding: utf-8 -*-
"""Another copy of GDSC 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bhO_5tZ5h5SwNCZawY8lptX2kyJOO405
"""

import pandas as pd
import numpy as np
import torch

df = pd.read_csv("/content/sentiment_analysis_dataset.csv")

df.columns

df.nunique(), df.shape

df.head()

df[df['sentiment'].isnull()]
df.dropna(inplace = True)
df.isnull().sum()

import matplotlib.pyplot as plt

sl = df['sentiment'].unique()
sl

y = [df['sentiment'].value_counts()[emo] for emo in sl]
y

plt.bar(sl, y)
plt.show()

lnths = [len(str(t)) for t in df['text']]

lnths = np.array(lnths)

print(lnths.max())
print(lnths.min())
print(lnths.std())
print(lnths.mean())

df.isnull().sum()

df[df['text'].isnull() == True]

df = df.dropna()

df[df['text'].isnull() == True]

one_hot_encoded_data = pd.get_dummies(df, columns = ['sentiment'])
one_hot_encoded_data

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

df.dropna()

"""Word2Vec"""

df.dropna(inplace=True)

"""Word2Vec"""

nltk.download('stopwords')

nltk.download('wordnet')

nltk.download('punkt')

stop_words = set(stopwords.words('english'))



!pip install -q transformers

import numpy as np
import pandas as pd
from sklearn import metrics
import transformers
import torch
from torch.utils.data import Dataset, DataLoader, RandomSampler, SequentialSampler
from transformers import BertTokenizer, BertModel, BertConfig

from torch import cuda
device = 'cuda' if cuda.is_available() else 'cpu'

df = pd.read_csv("/content/sentiment_analysis_dataset.csv")
df['list'] = df[df.columns[2:]].values.tolist()
new_df = df[['text', 'list']].copy()
new_df.head()

"""tokenize, remove stop words, embed, predict"""

from sklearn.model_selection import train_test_split

one_hot_encoded_data['sentiment_negative'][0]

arr = []

for i in range(0,27481):

  if(i==314):
    continue

  a = one_hot_encoded_data['sentiment_negative'][i]
  b = one_hot_encoded_data['sentiment_neutral'][i]
  c = one_hot_encoded_data['sentiment_positive'][i]

  temp = np.array([a,b,c])
  arr.append(temp)

arr[0] #to store classes



# x_train, x_test, y_train, y_test = train_test_split(df['text'], arr, train_size=0.8, stratify=df['sentiment'])
x_train, x_test, y_train, y_test = train_test_split(df['text'], df['sentiment'], train_size=0.8, stratify=df['sentiment'])

# # #remove stop words
# x_train = np.array(x_train)
# x_test = np.array(x_test)

# x_train[:3], x_test[:3]

test = "Hi, mom, @"
import string

# Remove punctuation from the string
test = test.translate(str.maketrans('', '', string.punctuation))

# Now 'test' contains the modified string
print(test)

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

t = word_tokenize("I was run and running")
t = [lemmatizer.lemmatize(w) for w in t]
t = np.array(t)
t

"""Used to make the text fit for Doc2Vec model"""

def clean(s):#return in tokenized form
  s = s.translate(str.maketrans('', '', string.punctuation))
  s = word_tokenize(s)
  s = [lemmatizer.lemmatize(t) for t in s]
  #s = np.array(s)
  s = (" ".join(s))
  #s = word_tokenize(s)
  return s

"""Doc2Vec takens in tokenized data"""

x_train = np.array(x_train)
x_train[1]

# def text_prepro(s) -> str:#used to preprocess a piece of string
#   s = s.translate(str.maketrans('', '', string.punctuation))
#   s = word_tokenize(s)
#   s = [lemmatizer.lemmatize(s) for s in t]
#   s = np.array(s)
#   vectors = vectorizer.transform(s)
#   return vectors

x_train.shape

"""Preparing train data"""

temp = []

for i in range(21984):
  temp.append(clean(str(x_train[i])))

x_train = np.array(temp)
x_train

x_test.shape

x_test = np.array(x_test)

"""Preparing test data"""

temp = []

for sen in x_test:
  temp.append(clean(str(sen)))

x_test = np.array(temp)
x_test

# cleaned = [] #for training

# for sen in x_train:
#   cleaned.append(np.array(clean(sen)))

# cleaned[:3]

"""Doc2Vec"""

# cleaned = np.array(cleaned)
# cleaned

# cleaned.shape

# cleaned_test = [] #for testing

# for sen in x_test:
#   cleaned_test.append(np.array(clean(sen)))

import gensim
from gensim import models

# import gensim.downloader as api
# wv = api.load('word2vec-google-news-300')

from gensim.test.utils import common_texts
from gensim.models import Word2Vec

# model = Word2Vec(sentences=common_texts, vector_size=100, window=10, min_count=1, workers=4)
# model.save("word2vec.model")

# t = np.array([[1., 2.], [1., 2.]])
# print(np.mean(t, axis=0))

# s = 'happy'
# model.wv[s].shape

from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]
#model = Doc2Vec(documents, vector_size=500, window=15, min_count=1, workers=4)

def build_model(max_epochs, vec_size, alpha, tagged_data):

    model = Doc2Vec(vector_size=vec_size,
               alpha=alpha,
               min_alpha=0.00025,
               min_count=1,
               dm=1)

    model.build_vocab(tag_data)

    # With the model built we simply train on the data.

    for epoch in range(max_epochs):
        print(f"Iteration {epoch}")
        model.train(tag_data,
                   total_examples=model.corpus_count,
                   epochs=model.epochs)

        # Here I decrease the learning rate.

        model.alpha -= 0.0002

        model.min_alpha = model.alpha

    # Now simply save the model to avoid training again.

    model.save("COVID_MEDICAL_DOCS_w2v_MODEL.model")
    print("Model Saved")
    return model

dfv = pd.read_csv("/content/file.csv")
dfv.dropna()
dfv.head()

dfv['tweets'] = [clean(sen) for sen in dfv['tweets']]
dfv.head()

w2v_body = list(dfv['tweets'])
w2v_title = list(dfv['labels'])

w2v_total_data = w2v_body + w2v_title

tag_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(w2v_total_data)]

model = build_model(max_epochs=5, vec_size=10, alpha=0.025, tagged_data=tag_data)

model.wv.similar_by_word("happy")



# a = np.array(wv['sad'])
# b = np.array(wv['joke'])
# t = np.array((a, b))

# avg = np.mean(t, axis=0)
# avg.shape

# vocab = []
# for index, word in enumerate(wv.index_to_key):
#   vocab.append(word)

# vocab[:2]

import torch

# Assuming cleaned is a list of sentences
train_vectors = []

for sen in x_train:
    vec = model.infer_vector(list([w for w in sen]))
    vec = torch.tensor(vec)
    train_vectors.append(vec)

# Convert the list to a tensor of tensors (samples x features)
train_tensor = torch.stack(train_vectors, dim=0)

# Access the first two sentences' vectors:
print(train_tensor.shape)

train_tensor.shape

train_tensor.shape

import numpy as np

test_vectors = []

for sen in x_test:
  vec = model.infer_vector(list([w for w in sen]))
  vec = torch.tensor(vec)
  test_vectors.append(vec)

test_tensor = torch.stack(test_vectors, dim=0)

test_tensor.shape

train_tensor[0].shape

train_tensor

from torch import nn

device = "cuda" if torch.cuda.is_available() else "cpu"



class Analyze(nn.Module):
  def __init__(self, input_size, hidden_size):
    super().__init__()

    self.hidden_size = hidden_size

    self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size,
                          num_layers=2, batch_first=True)
    self.layer = nn.Linear(input_size, hidden_size)
    self.l1 = nn.Linear(hidden_size, 128)
    self.l2 = nn.Linear(128, 3)
    self.relu = nn.ReLU()
    self.sftmx = nn.Softmax(dim=1)

  def forward(self, x):
    x, _ = self.lstm(x)
    #x = self.layer(x)
    x = self.relu(x)
    x = self.l1(x)
    #x = self.relu(x)
    x = self.l2(x)
    #x = self.sftmx(x)
    return x

model1 = Analyze(10, 128)
model1.to(device)

"""t1, t2 is the tensor format which lstm expects"""

t1 = train_tensor.unsqueeze(dim=1)
t2 = test_tensor.unsqueeze(dim=1)

t1.shape

train_tensor.shape

untrained_preds = model1(t1.to(device))
untrained_preds = untrained_preds.squeeze()
untrained_preds

untrained_preds

loss_fn = nn.CrossEntropyLoss()
opt = torch.optim.SGD(params = model1.parameters(), lr=0.01)

y_train = pd.DataFrame(y_train)

from sklearn import preprocessing

# label_encoder object knows
# how to understand word labels.
label_encoder = preprocessing.LabelEncoder()

# Encode labels in column 'species'.
y_train = label_encoder.fit_transform(np.array(y_train))


y_test = label_encoder.transform(np.array(y_test))





y_train = torch.tensor(y_train)
y_test = torch.tensor(y_test)

y_train = y_train.to(dtype=torch.float)
y_test = y_test.to(dtype=torch.float)



untrained_preds, untrained_preds.argmax(dim=1)

import torch

# Assuming y_train is a NumPy array or a pandas Series
y_train = torch.tensor(y_train, dtype=torch.long)

# Now you can use the loss function
loss_fn(untrained_preds, y_train)

!pip install torchmetrics
import torchmetrics

from torchmetrics import Accuracy
accuracy = Accuracy(task="multiclass", num_classes=3)

model1.to(device)
accuracy.to(device)

y_classes = torch.tensor([int(arr.argmax()) for arr in y_test])

y_train.max(dim=0)

# _, try1 = y_train.max(dim=1)
# try1.shape

# _, try2 = y_test.max(dim=1)

epoch = 50

for epochs in range(epoch):

  model1.train()
  logits = model1(t1.to(device))
  pred_prob = torch.nn.functional.softmax(logits, dim=0)
  loss = loss_fn(logits.squeeze(), y_train.to(dtype=torch.long))


  opt.zero_grad()
  loss.backward()
  opt.step()

  if(epochs%5==0):
    print(f"{epochs}/{epoch}: train loss is {loss}")

  with torch.no_grad():
    model1.eval()
    test_logits = model1(t2.to(device))
    test_prob = torch.nn.functional.softmax(test_logits, dim=0)
    test_res = [int(arr.argmax()) for arr in test_prob]
    test_res = torch.tensor(test_res)
    test_loss = loss_fn(test_logits.squeeze().to(device), y_test.to(dtype=torch.long))
    acc = accuracy(test_res.to(device), y_test.to(device))

    if(epochs%5==0):
      print(f"{epochs}/{epoch}: test loss is {test_loss}")
      print(f"{epochs}/{epoch}: test accuracy is {acc}")



logits.shape, y_train.shape

label_encoder.inverse_transform([0,1,2])

s = "Today I am very happy"
s = clean(s)
s = model.infer_vector(list(s))
s = torch.tensor(s)
s = torch.tensor(s.unsqueeze(dim=0))

model1(s)

model1(s).argmax(dim=1)

def pred(Input_Sentence):
  s = Input_Sentence
  s = clean(s)
  s = model.infer_vector(list(s))
  s = torch.tensor(s)
  s = torch.tensor(s.unsqueeze(dim=0))
  pred = model1(s).argmax(dim=1)

  ans = ""

  if pred==0:
    ans = "negative"
  elif pred==1:
    ans = "neutral"
  else:
    ans = "positive"


  return ans

pip install gradio

import gradio as gr

"""The Gradio app"""

app = gr.Interface(
    fn=pred,
    inputs="text",
    outputs="text",
    title="Text Prediction",
    description="This app allows you to predict sentiment of sentence.",
)
app.launch()

