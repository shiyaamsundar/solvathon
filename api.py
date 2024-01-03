from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import Body
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import schedule
import time  # Import time module to run the schedule

import schedule
import time
import re
from datetime import datetime
import locale
import dateutil.parser as parser
from transformers import pipeline
import requests
from bs4 import BeautifulSoup
import pandas as pd
import spacy
from spacy import displacy
NER = spacy.load("en_core_web_sm")

from datetime import datetime
import lxml

import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords

#for Named entity Recognition

nltk.download('universal_tagset')

from nltk import word_tokenize

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from keras.models import Sequential
# from keras.layers import Flatten, Dense, Dropout, GlobalMaxPooling1D, Embedding, Bidirectional, Conv1D, LSTM

import tensorflow as tf

from tensorflow import keras

from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences

from keras.models import Sequential

from keras.layers import Flatten, Dense, Dropout, GlobalMaxPooling1D, Embedding, Bidirectional, Conv1D, LSTM

 

#for model optimization

#I will be using Stochastic Gradient Descent

from keras.optimizers import SGD

#for wordCloud
from wordcloud import WordCloud

#gives most repetitive element in list
from collections import Counter


import numpy as np





app = FastAPI()

upload_dir = "uploads"
# Create the directory if it doesn't exist.
os.makedirs(upload_dir, exist_ok=True)

origins = [
    "http://localhost:3000",  # Add your React frontend URL here.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/dropdownData")
def getDataForDropDown():
  # Define the scope and credentials
  scope = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name('service.json', scope)

  # Authenticate and open the Google Sheets document
  gc = gspread.authorize(credentials)
  worksheet = gc.open('RSSFeedData').worksheet('Sheet1') # Replace with your sheet and worksheet names

  all_values = worksheet.get_all_values()
  main_csv=pd.DataFrame(all_values,columns=all_values[0])
  main_csv.drop(0,axis=0,inplace=True)

  companies_list = main_csv['CompanyName'].to_list()
  print("print number of unique company names : ",len(set(companies_list)))
  companyNames = list(set(companies_list))
  whitelist=[""]
  out_list=[]
  for i in companyNames:
    if i in whitelist:
      continue
    #removing The/the in beginning
    temp_list = i.split()
    for item in temp_list:

      if item == 'The':
        temp_list.remove("The")
      if item == 'the':
        temp_list.remove("the")

    i = " ".join(i for i in temp_list)
    out_list.append(i)

  unique_companies = list(set(out_list))
  output={
      "CompanyName":unique_companies,
      "ArticleName":["Times Of India","Economic Times","Mint Companies","Mint Technology","Mint AI"]
  }
  return output




class Article(BaseModel):
    articleurl: str
    ticker: str
class News(BaseModel):
    newstext: str
    ticker: str

class CsvUpload(BaseModel):
  file: UploadFile
  ticker:str



def remove_stopwords(input_text):

    stopwords_list = stopwords.words('english')
    # Some words which might indicate a certain sentiment are kept via a whitelist
    whitelist = ["n't", "not", "no"]
    words = input_text.split()
    clean_words = [word for word in words if (word not in stopwords_list or word in whitelist) and len(word) > 1]
    return " ".join(clean_words)

def tokenizingSequencingPadding(myList):
  oov_token  = '#OOV'
  max_length = 100
  trunc_type = 'post'
  pad_type   = 'pre'
  vocab_size = 10000
  embedding_dim = 100
  tokenizer = Tokenizer(num_words = vocab_size, oov_token = oov_token)
  tokenizer.fit_on_texts(myList)
  testing_sequence = tokenizer.texts_to_sequences(myList)
  padded_testing_seq = pad_sequences(testing_sequence, maxlen = max_length, padding = pad_type, truncating = trunc_type) # type numpy.ndarray
  return padded_testing_seq

def preprocess(paragraph):
  noStopwordsPara = remove_stopwords(paragraph)
  preprocessedText=tokenizingSequencingPadding(noStopwordsPara)
  return preprocessedText

def wordCloudGeneration(data):
  wordForCloud = " ".join(title for title in data.Title)
  word_cloud = WordCloud(collocations = False, background_color = 'white').generate(wordForCloud)
  word_cloud.to_file("ReferenceDocs\\wordCloud.png")

def getSentiment(text):
  out=pipe(text,
  candidate_labels=["positive","negative","neutral"],
  )
  labelIndex=out['scores'].index(max(out['scores']))
  return(out['labels'][labelIndex])

def userUpload(stockTicker,isUrl,isText,isFile,url,text,file):
  print("IN")
  if isUrl=="True":
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("title").text
    title_sentiment = getSentiment(title)
    return title_sentiment

  elif isText=="True":
    #NER
    organization_list=[]
    outputNER= NER(text)
    for word in outputNER.ents:
      if word.label_ == 'ORG':
        organization_list.append(word.text)
    counter = Counter(organization_list)
    most_common = counter.most_common(1)[0][0]

    # removing stop words
    sw_removed = remove_stopwords(text)

    # generating word cloud
    wordForCloud = " ".join(word for word in text.split())
    word_cloud = WordCloud(collocations = False, background_color = 'white').generate(wordForCloud)
    word_cloud.to_file("ReferenceDocs\\textWordCloud.png")

    # making a list for tokanization
    tempList=[]
    tempList.append(sw_removed)
    inputY = tokenizingSequencingPadding(tempList)

    # loading the LSTM model
    lstm_model=tf.keras.models.load_model('lstmModel.h5')

    # prediction
    lstm_output = lstm_model.predict(inputY)
    print(lstm_output)
    #[negative,neutral,positive]
    result={
        "negative":lstm_output[0][0],
        "neutral":lstm_output[0][1],
        "positive":lstm_output[0][2],
        "company":most_common
    }

    return result
  else:
    
    if isFile == "True":

      #get the file uploaded by user and remove stopwords
      data=pd.read_csv(file)

      print("Entered")

      data['reviews.text']=data['reviews.text'].apply(remove_stopwords)

      print("stopwords removal complete")

      # Generate a word cloud image
      wordForCloud = " ".join(record for record in data['reviews.text'])
      word_cloud = WordCloud(collocations = False, background_color = 'white').generate(wordForCloud)
      word_cloud.to_file("ReferenceDocs\\reviewWordCloud.png")

      print("wordcloud save complete")

      lstmModel = load_model('lstmModel.h5')
      print("loding model complete")

      #text preprocessing of uploaded file
      #tokenization, sequencing, padding
      sentancesForPrediction = data['reviews.text'].to_list()
      padded_sentancesForPrediction = tokenizingSequencingPadding(sentancesForPrediction)
      print("padding done")

      #prediction
      lstm_model_output = lstmModel.predict(padded_sentancesForPrediction[:])
      print("prediction complete")

      # [negative,neutral,positive]
      prediction_list=[]
      positive=0
      negative=0
      neutral=0
      for i in lstm_model_output:
        # print(i)
        maximum=(max(i))
        # print(maximum)
        index = np.where( i == maximum)[0][0]
        # print(index)
        if index==0:
          prediction_list.append("negative")
          negative = negative+1
        elif index==1:
          prediction_list.append("neutral")
          neutral = neutral+1
        else:
          prediction_list.append("positive")
          positive = positive+1

      print("POSITIVE : ",positive,"NEGATIVE",negative,"NEUTRAL",neutral)
      print(len(sentancesForPrediction))
      percentagePositive = (positive/len(sentancesForPrediction))*100
      percentageNegative = (negative/len(sentancesForPrediction))*100
      percentageNeutral = (neutral/len(sentancesForPrediction))*100

      result={
          "negative" : percentageNegative,
          "neutral":percentageNeutral,
          "positive":percentagePositive,
          "company":""
          }
      return result


 


@app.post('/api/url')
def findArticleSentiment(data:Article):
    print(data)
    page = requests.get(data.articleurl)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("title").text
    title_sentiment = getSentiment(title)
    return title_sentiment
    return 'success url'


@app.post("/api/text")
def findTextSentiment(data:News):
    print(data)
    organization_list=[]
    outputNER= NER(data.newstext)
    for word in outputNER.ents:
      if word.label_ == 'ORG':
        organization_list.append(word.text)
    counter = Counter(organization_list)
    most_common = counter.most_common(1)[0][0]

    # removing stop words
    sw_removed = remove_stopwords(data.newstext)

    # generating word cloud
    wordForCloud = " ".join(word for word in data.newstext.split())
    word_cloud = WordCloud(collocations = False, background_color = 'white').generate(wordForCloud)
    word_cloud.to_file("ReferenceDocs\\textWordCloud.png")

    # making a list for tokanization
    tempList=[]
    tempList.append(sw_removed)
    inputY = tokenizingSequencingPadding(tempList)

    # loading the LSTM model
    lstm_model=tf.keras.models.load_model('lstmModel.h5')

    # prediction
    lstm_output = lstm_model.predict(inputY)
    print(lstm_output)
    #[negative,neutral,positive]
    result={
        "negative":lstm_output[0][0],
        "neutral":lstm_output[0][1],
        "positive":lstm_output[0][2],
        "company":most_common
    }
    return {"result": result}
    




@app.post("/upload/csv/{ticker}/{filename}")
async def upload_csv(file:UploadFile,ticker,filename):
    print(file,filename,file.file)
    try:
        # Save the uploaded CSV file to the upload directory.
        with open(os.path.join(upload_dir, file), "wb") as f:
            shutil.copyfileobj(file, f)
            
        data=pd.read_csv(filename)

        print("Entered")

        data['reviews.text']=data['reviews.text'].apply(remove_stopwords)

        print("stopwords removal complete")

        # Generate a word cloud image
        wordForCloud = " ".join(record for record in data['reviews.text'])
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(wordForCloud)
        word_cloud.to_file("ReferenceDocs\\reviewWordCloud.png")

        print("wordcloud save complete")

        lstmModel = load_model('lstmModel.h5')
        print("loding model complete")

        #text preprocessing of uploaded file
        #tokenization, sequencing, padding
        sentancesForPrediction = data['reviews.text'].to_list()
        padded_sentancesForPrediction = tokenizingSequencingPadding(sentancesForPrediction)
        print("padding done")

        #prediction
        lstm_model_output = lstmModel.predict(padded_sentancesForPrediction[:])
        print("prediction complete")

        # [negative,neutral,positive]
        prediction_list=[]
        positive=0
        negative=0
        neutral=0
        for i in lstm_model_output:
          # print(i)
          maximum=(max(i))
          # print(maximum)
          index = np.where( i == maximum)[0][0]
          # print(index)
          if index==0:
            prediction_list.append("negative")
            negative = negative+1
          elif index==1:
            prediction_list.append("neutral")
            neutral = neutral+1
          else:
            prediction_list.append("positive")
            positive = positive+1

        print("POSITIVE : ",positive,"NEGATIVE",negative,"NEUTRAL",neutral)
        print(len(sentancesForPrediction))
        percentagePositive = (positive/len(sentancesForPrediction))*100
        percentageNegative = (negative/len(sentancesForPrediction))*100
        percentageNeutral = (neutral/len(sentancesForPrediction))*100

        result={
            "negative" : percentageNegative,
            "neutral":percentageNeutral,
            "positive":percentagePositive,
            "company":""
            }
        
        return {"result": result}


        return JSONResponse(content={"message": "File uploaded successfully"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.get('/api/recentnews/{hasFilter}/{isArticleFetch}/{givenArticleName}/{isCompanyFetch}/{givenCompanyName}')
def GetTop15(hasFilter,isArticleFetch, givenArticleName, isCompanyFetch, givenCompanyName):
  scope = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name('service.json', scope)
  gc = gspread.authorize(credentials)
  worksheet = gc.open('RSSFeedData').worksheet('Sheet1')

  all_values = worksheet.get_all_values()
  main_csv=pd.DataFrame(all_values,columns=all_values[0])
  main_csv.drop(0,axis=0,inplace=True)

  if hasFilter == "False":
    top15 = main_csv.tail(15)
    listOfNifty50 = []
    main_array=[]
    obj={
        "ArticleName":"",
        "LastBuildDate":"",
        "PublishedDate":"",
        "Title":"",
        "Description":"",
        "CompanyName":"",
        "Link":"",
        "Sentiment":"",
        }
    for i in range(0,15):
      currentObject = top15.iloc[i,:]

      obj={
        "ArticleName":currentObject.ArticleName,
        "LastBuildDate":currentObject.LastBuildDate,
        "PublishedDate":currentObject.PublishedDate,
        "Title":currentObject.Title,
        "Description":currentObject.Description,
        "CompanyName":currentObject.CompanyName,
        "Link":currentObject.Link,
        "Sentiment":currentObject.Sentiment,
      }
      main_array.append(obj)
    return main_array
  if hasFilter == "True":
    if isArticleFetch == "True":
      main_array=[]
      maskArticleName = main_csv["ArticleName"]==givenArticleName
      filteredData = main_csv[maskArticleName]
      print("Length of fetched data wrt news article",len(filteredData))
      for i in range(0,15):
        if i < len(filteredData):
          currentObject = filteredData.iloc[i,:]
          obj={
          "ArticleName":currentObject.ArticleName,
          "LastBuildDate":currentObject.LastBuildDate,
          "PublishedDate":currentObject.PublishedDate,
          "Title":currentObject.Title,
          "Description":currentObject.Description,
          "CompanyName":currentObject.CompanyName,
          "Link":currentObject.Link,
          "Sentiment":currentObject.Sentiment
          }
          main_array.append(obj)
        else:
          return main_array
      return main_array

    if isCompanyFetch == "True":
      # maskCompanyName = main_csv["CompanyName"]==givenCompanyName
      # # print(type(maskCompanyName))
      # filteredData = main_csv[maskCompanyName]
      maskCompanyName=[]
      temp_list=list(main_csv["CompanyName"])
      for i in temp_list:
        if givenCompanyName in i:
          maskCompanyName.append(True)  
        else:
          maskCompanyName.append(False)
  
      maskCompanyName_series=pd.Series(maskCompanyName)

      # print(main_csv["CompanyName"].shape)
      # print(maskCompanyName_series.shape)
      # print(maskCompanyName_series)
      # print(main_csv.head(5))
      
      main_csv = main_csv.reset_index(drop=True)
      filteredData = main_csv[maskCompanyName_series]
      main_array=[]
      for i in range(0,15):
        if i < len(filteredData):
          currentObject = filteredData.iloc[i,:]
          obj={
          "ArticleName":currentObject.ArticleName,
          "LastBuildDate":currentObject.LastBuildDate,
          "PublishedDate":currentObject.PublishedDate,
          "Title":currentObject.Title,
          "Description":currentObject.Description,
          "CompanyName":currentObject.CompanyName,
          "Link":currentObject.Link,
          "Sentiment":currentObject.Sentiment
          }
          main_array.append(obj)
        else:
          return main_array
      return main_array


  scope = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name('service.json', scope)
  gc = gspread.authorize(credentials)
  worksheet = gc.open('RSSFeedData').worksheet('Sheet1') 

  all_values = worksheet.get_all_values()
  main_csv=pd.DataFrame(all_values,columns=all_values[0])
  main_csv.drop(0,axis=0,inplace=True)

  top15 = main_csv.tail(15)
  listOfNifty50 = []
  main_array=[]
  obj={
      "ArticleName":"",
      "LastBuildDate":"",
      "PublishedDate":"",
      "Title":"",
      "Description":"",
      "CompanyName":"",
      "Link":"",
      "Sentiment":"",
      }
  for i in range(0,15):
    currentObject = top15.iloc[i,:] 

    obj={
      "ArticleName":currentObject.ArticleName,
      "LastBuildDate":currentObject.LastBuildDate,
      "PublishedDate":currentObject.PublishedDate,
      "Title":currentObject.Title,
      "Description":currentObject.Description,
      "CompanyName":currentObject.CompanyName,
      "Link":currentObject.Link,
      "Sentiment":currentObject.Sentiment,
    }
    main_array.append(obj)
  return main_array
