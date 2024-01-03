def GetTop15(hasFilter,isArticleFetch, givenArticleName, isCompanyFetch, givenCompanyName):
  scope = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name('ReferenceDocs\service.json', scope)
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
    
out = GetTop15("True","False", "", "True", "Tata")
print(len(out))