# import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('service.json', scope)
gc = gspread.authorize(credentials)
worksheet = gc.open('RSSFeedData').worksheet('Sheet1') 

all_values = worksheet.get_all_values()

print(all_values)


def GetTop15():
  scope = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name('service.json', scope)
  gc = gspread.authorize(credentials)
  worksheet = gc.open('RSSFeedData').worksheet('Sheet1') 

  all_values = worksheet.get_all_values()

  print(all_values)
#   main_csv=pd.DataFrame(all_values,columns=all_values[0])
#   main_csv.drop(0,axis=0,inplace=True)

#   top15 = main_csv.tail(15)
#   listOfNifty50 = []
#   main_array=[]
#   obj={
#       "ArticleName":"",
#       "LastBuildDate":"",
#       "PublishedDate":"",
#       "Title":"",
#       "Description":"",
#       "CompanyName":"",
#       "Link":"",
#       "Sentiment":"",
#       }
#   for i in range(0,15):
#     currentObject = top15.iloc[i,:] 

#     obj={
#       "ArticleName":currentObject.ArticleName,
#       "LastBuildDate":currentObject.LastBuildDate,
#       "PublishedDate":currentObject.PublishedDate,
#       "Title":currentObject.Title,
#       "Description":currentObject.Description,
#       "CompanyName":currentObject.CompanyName,
#       "Link":currentObject.Link,
#       "Sentiment":currentObject.Sentiment,
#     }
#     main_array.append(obj)
#   return main_array

