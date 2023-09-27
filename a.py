@app.post("/upload2")
def upload(file: UploadFile = File(...)):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    print('yesss')
    data = {}
    for rows in csvReader:             
        key = rows['Id']  # Assuming a column named 'Id' to be the primary key
        data[key] = rows  
    
    file.file.close()
    return data



@app.post("/upload11")
def upload(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    background_tasks.add_task(file.file.close)
    return list(csvReader)


@app.post("/upload111")
async def upload_csv_file(csv_file: UploadFile = File(...)):
    # Check if the file is of the expected type
    # if not csv_file.filename.endswith(".csv"):
    #     return {"error": "Invalid file type. Please upload a CSV file."}

    # # Process the uploaded CSV file here
    # # You can access the file contents via csv_file.file

    # # For example, you can read and print the file content
    # content = await csv_file.read()
    # print(content.decode())

    # You can also save the file or perform any other processing as needed

    return {"message": "File uploaded and processed successfully"}


# @app.post("/files")
# async def create_file(file: Any[bytes, File()]):
#     return {"file_size": len(file)}


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}