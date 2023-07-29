from PIL import Image
from pymongo import MongoClient

# Open the image file
def connectToDb(filename,category):
    uploaded_file = "C:/Users/91810/Desktop/Automated-document-processeing/images/"+category+"/"+filename
    image = Image.open(uploaded_file)

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017")
    database = client["documents"]
    collection = database[category]

    # Convert the image to binary data
    image_data = image.tobytes()

    # Create a document and insert the image data
    document = {"image": image_data}
    collection.insert_one(document)

    # Close the MongoDB connection
    client.close()
