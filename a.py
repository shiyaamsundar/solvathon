from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
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

from datetime import datetime
import lxml

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Flatten, Dense, Dropout, GlobalMaxPooling1D, Embedding, Bidirectional, Conv1D, LSTM

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




pipe = pipeline(model="facebook/bart-large-mnli")
NER = spacy.load("en_core_web_sm")

requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning)


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
  word_cloud.to_file("wordCloud.png")
  plt.imshow(word_cloud, interpolation='bilinear')
  plt.axis("off")
  plt.show()

def userUpload(stockTicker,isUrl,isText,isFile,url,text,file):
  if isUrl==True:
    sentiment = userUploadUrl(url)

  elif isText==True:
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
    word_cloud.to_file("textWordCloud.png")

    # making a list for tokanization
    tempList=[]
    tempList.append(sw_removed)
    inputY = tokenizingSequencingPadding(tempList)

    # loading the LSTM model
    lstm_model=tf.keras.models.load_model('lstmModel.keras')

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

    if isFile == True:

      #get the file uploaded by user and remove stopwords
      data=pd.read_csv(file)

      data['reviews.text']=data['reviews.text'].apply(remove_stopwords)

      print("stopwords removal complete")

      # Generate a word cloud image
      wordForCloud = " ".join(record for record in data['reviews.text'])
      print(wordForCloud)
      word_cloud = WordCloud(collocations = False, background_color = 'white').generate(wordForCloud)
      word_cloud.to_file("reviewWordCloud.png")

      print("wordcloud save complete")

      lstmModel = tf.keras.models.load_model('lstmModel.keras')
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






def getLastBuildDate(articleName,main_csv_df):
  last_index = main_csv_df.where(main_csv['ArticleName'] == articleName).last_valid_index()
  if last_index == None:
    return "None"
  else:
    lastBuildDate = main_csv_df.loc[last_index,"LastBuildDate"]
    return(lastBuildDate)

def getISOformattedDate(date=""):
  myDate = parser.parse(date)
  return (myDate.isoformat())

def getSentiment(title=""):
  out=pipe(title,
  candidate_labels=["positive","negative","neutral"],
  )
  labelIndex=out['scores'].index(max(out['scores']))
  return(out['labels'][labelIndex])

def find_articleName(url):
  if url == "https://timesofindia.indiatimes.com/rssfeeds/1898055.cms":
      articleName="Times Of India"
  elif url == "https://cfo.economictimes.indiatimes.com/rss/corporate-finance":
    articleName="Economic Times"
  elif (url=="https://www.livemint.com/rss/companies"):
    articleName = "Mint Companies"
  elif (url == "https://www.livemint.com/rss/technology"):
    articleName = "Mint Technology"
  elif (url == "https://www.livemint.com/rss/AI"):
    articleName = "Mint AI"
  elif (url=="https://www.business-standard.com/rss/companies/results-10103.rss"):
    articleName = "Business Standard"
  else:
    articleName=""
  return articleName

# scraping function for getting live news

def news_rss(url,main_csv):
    print('rss calling')

    publishedDate_list=[]
    title_list=[]
    description_list=[]
    company_list=[]
    lastBuildDate_list=[]
    link_list=[]
    sentiment_list=[]

    articleName = find_articleName(url)

    try:
        r = requests.get(url,verify=False)
        print(r.status_code," ",articleName)
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')

        if (articleName != "Mint Companies" and articleName != "Mint Technology" and articleName != "Mint AI"):
          lastBuildDate = soup.find('lastBuildDate').text

        # for articles that does not have lastBuildDate (mint)
        if soup.find('lastBuildDate') == None:
          for count,ele in enumerate(articles,1):
            if count == 1:
              lastBuildDate = ele.find('pubDate').text
              break

        # call function to get the DB's LastBuildDate for this article
        thisArticles_LastBuildDate_inDB = getLastBuildDate(articleName,main_csv)


        # ------------------------ for loop each article in RSS of one get call --------------------------------#
        allRows=[]

        for count,a in enumerate(articles,1): #for each ITEM tag
          organization_list=""

          temp_publishedDate = a.find('pubDate').text

          if getISOformattedDate(temp_publishedDate) > getISOformattedDate(thisArticles_LastBuildDate_inDB):
            
            #get title,description,link,published date for each ITEM tag
            title = a.find('title').text
            description = a.find('description').text
            link = a.find('link').text
            publishedDate = a.find('pubDate').text

            #remove image tag in description
            if articleName == "Times Of India":
              image_tag = re.compile(r'<img.*?/>').search(description).group()
              description=description.replace(image_tag, '')
            

            #field COMPANY -> Named Entity recognition to fetch company name
            raw_text=description
            if len(raw_text)==0:
              raw_text=title
            outputNER= NER(raw_text)
            for word in outputNER.ents:
              if word.label_ == 'ORG':
                organization_list=organization_list+" "+(word.text)

            #field SENTIMENT -> Finding sentiment using Zero shot Model
            if len(description)==0:
              sentiment_article = getSentiment(title)
            else:
              sentiment_article = getSentiment(description)

            row=[]

            #append data to list
            row.append(articleName)
            row.append(lastBuildDate)
            row.append(publishedDate)
            row.append(title)
            row.append(description)
            row.append(organization_list)
            row.append(link)
            row.append(sentiment_article)

            allRows.append(row)

          else:
            
            break

          # end of for loop

        return allRows

    except Exception as e:
        print("The scraping job failed in "+articleName+". See exception: ")
        print(e)

    #links to live news
# timesOfIndiaURL='https://timesofindia.indiatimes.com/rssfeeds/1898055.cms'
# economicTimesURL='https://cfo.economictimes.indiatimes.com/rss/corporate-finance'
# liveMintURL="https://www.livemint.com/rss/companies"
# liveMintTechURL = "https://www.livemint.com/rss/technology"
# liveMintAIURL = "https://www.livemint.com/rss/AI"
# # BusinessTodayCompaniesResultsURL = "https://www.business-standard.com/rss/companies/results-10103.rss"
# # BusinessTodayMarketsURL = "https://www.business-standard.com/rss/markets-106.rss"
# # hindustanTimeBusiness = "https://www.hindustantimes.com/feeds/rss/business/rssfeed.xml"

# # #function call to get xml rss live feed in dataframe format
# timesOfIndia_data = news_rss(timesOfIndiaURL,main_csv)
# economicTimes_data = news_rss(economicTimesURL,main_csv)
# liveMint_data = news_rss(liveMintURL,main_csv)
# liveMint_tech_data = news_rss(liveMintTechURL,main_csv)
# liveMintAI_data = news_rss(liveMintAIURL,main_csv)
#     # bTCompanyResults_data = news_rss(BusinessTodayCompaniesResultsURL)
#     # bTMarket_data = news_rss(BusinessTodayMarketsURL)
#     # hindustanTimes_data=news_rss(hindustanTimeBusiness)

# master_list=[]
# for i in timesOfIndia_data:
#     master_list.append(i)
# for i in economicTimes_data:
#     master_list.append(i)
# for i in liveMint_data:
#     master_list.append(i)
# for i in liveMint_tech_data:
#     master_list.append(i)
# for i in liveMintAI_data:
#     master_list.append(i)

# data_to_append=master_list
# worksheet.append_rows(data_to_append)







def my_function():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time}: Running my_function every minute")


# Schedule my_function to run every minute
schedule.every(1).minutes.do(my_function)



def sakura():
    print('sakuraaaaa')
    timesOfIndiaURL='https://timesofindia.indiatimes.com/rssfeeds/1898055.cms'
    economicTimesURL='https://cfo.economictimes.indiatimes.com/rss/corporate-finance'
    liveMintURL="https://www.livemint.com/rss/companies"
    liveMintTechURL = "https://www.livemint.com/rss/technology"
    liveMintAIURL = "https://www.livemint.com/rss/AI"
    # BusinessTodayCompaniesResultsURL = "https://www.business-standard.com/rss/companies/results-10103.rss"
    # BusinessTodayMarketsURL = "https://www.business-standard.com/rss/markets-106.rss"
    # hindustanTimeBusiness = "https://www.hindustantimes.com/feeds/rss/business/rssfeed.xml"

    # #function call to get xml rss live feed in dataframe format
    timesOfIndia_data = news_rss(timesOfIndiaURL,main_csv)
    economicTimes_data = news_rss(economicTimesURL,main_csv)
    liveMint_data = news_rss(liveMintURL,main_csv)
    liveMint_tech_data = news_rss(liveMintTechURL,main_csv)
    liveMintAI_data = news_rss(liveMintAIURL,main_csv)
        # bTCompanyResults_data = news_rss(BusinessTodayCompaniesResultsURL)
        # bTMarket_data = news_rss(BusinessTodayMarketsURL)
        # hindustanTimes_data=news_rss(hindustanTimeBusiness)

    master_list=[]
    for i in timesOfIndia_data:
        master_list.append(i)
    for i in economicTimes_data:
        master_list.append(i)
    for i in liveMint_data:
        master_list.append(i)
    for i in liveMint_tech_data:
        master_list.append(i)
    for i in liveMintAI_data:
        master_list.append(i)

    data_to_append=master_list
    worksheet.append_rows(data_to_append)


@app.get("/")
def read_root():
    sakura()
    return {"Hello": "World"}

@app.post("/post")
def post(data: Dict[str, Any]):
    return {"message": "Success"}

@app.post("/upload")
async def upload_csv(file: UploadFile):
    print(file)
    try:
        # Save the uploaded CSV file to the upload directory.
        print(file.filename)
        with open(os.path.join(upload_dir, file.filename), "wb") as f:
            shutil.copyfileobj(file.file, f)
            

        return JSONResponse(content={"message": "File uploaded successfully"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post('/api/upload')
def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file).head()

    print(df,'hello')

    return df

# Run the schedule loop in the background
# while True:
#     schedule.run_pending()
#     time.sleep(1)


@app.get('/api/recentnews')
def GetTop15(hasFilter,isArticleFetch, givenArticleName, isCompanyFetch, givenCompanyName):
  scope = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name('service.json', scope)
  gc = gspread.authorize(credentials)
  worksheet = gc.open('RSSFeedData').worksheet('Sheet1')

  all_values = worksheet.get_all_values()
  main_csv=pd.DataFrame(all_values,columns=all_values[0])
  main_csv.drop(0,axis=0,inplace=True)

  if hasFilter == False:
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
  if hasFilter == True:
    if isArticleFetch == True:
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

    if isCompanyFetch == True:
      maskCompanyName = main_csv["CompanyName"]==givenCompanyName
      filteredData = main_csv[maskCompanyName]
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

scope = ['https://spreadsheets.google.com/feeds',
      'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('service.json', scope)
gc = gspread.authorize(credentials)
worksheet = gc.open('RSSFeedData').worksheet('Sheet1') 

all_values = worksheet.get_all_values()
a=[]
for i in all_values:
  if i[-3] not in a:
    a.append(i[-3])
#   if i.CompanyName not in a:
#     a.append(i.CompanyName)

@app.get('/api/recentnews/{option}')
def recentfilter(option):

  scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name('service.json', scope)
  gc = gspread.authorize(credentials)
  worksheet = gc.open('RSSFeedData').worksheet('Sheet1') 

  all_values = worksheet.get_all_values()
  a=[]
  for i in all_values:
    if i.CompanyName not in a:
      a.append(i.CompanyName)
  print(a)

  if option=='1':
    return 'text'
  elif option=='2':
    return 'url'
  elif option=='3':
    return 'pdf'
  return 'hello'
