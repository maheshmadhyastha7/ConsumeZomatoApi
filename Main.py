import VehicleModule as vehi
import os
import ZomatoModule
import json

'''make =input("Enter make: ")
model=input("Enter model:")
year=input("Year of manufacture:")
vehicletype =input("Vehicle type:")
vehicleDet = vehi.Car(make.strip(),model.strip(),
                      year.strip(),vehicletype.strip())
vehi.welcomeMessage()
vehicleDet.printCarDetails()'''

apiKey = "8d2c527f069d1765b7b9d46066060e88"

zom = ZomatoModule.Zomato(apiKey)


def getCategories():
    response = zom.getCategory()
    print("Categories:\n")
    for num, category in enumerate(response['categories']):
        print("{number}. {name}".format(
            number=category['categories']['id'],
            name=category['categories']['name']
        ))


def getGeoCode(lat,lon):
    lati = lat
    longi = lon
    cordinate = "{lat}-{lon}".format(lat=lati, lon=longi)
    return zom.getGeoCode(cordinate)

def processAndPrintRestaurantDetails(geoCodeResponse):
    for num, restaurant in enumerate(geoCodeResponse['nearby_restaurants']):
        dicResturant = dict(restaurant)
        restName = dicResturant['restaurant']['name']
        address = dicResturant['restaurant']['location']['address']
        city = dicResturant['restaurant']['location']['city']
        locality = dicResturant['restaurant']['location']['locality']
        name = dicResturant['restaurant']['name']
        restaurantDetails = "Restaurant Details:\n Name:{3}\n Address:{0} \n City:{1} \n Locality:{2}"
        print(restaurantDetails.format(address, city, locality,name))
        print("--------------------------------------------------------------------")

def listUserReviews(userReviews):
    print("User reviews:")
    for num,review in enumerate(userReviews['user_reviews']):
        dicReview = dict(review)
        userRating = dicReview['review']['rating_text']
        userReview = dicReview['review']['review_text']
        userName = dicReview['review']['user']['name']
        print("User:{0} \n Review rating:{1} \n Review:{2}".format(userName,userRating,userReview))
        print("------------------------------------------------------------------------------")

def searchRestaurants(searchText,lat,lon):
    searchResult=zom.searchRestaurants(searchText,lat,lon)   


def getUserReviews(restaurantId):
    userReviews = zom.getUserReviews(restaurantId)
    listUserReviews(userReviews)

def getRestaurantsByGeoCode(lat,lon):
    geoCodeResponse = getGeoCode(lat,lon)
    processAndPrintRestaurantDetails(geoCodeResponse)




#restaurantId=16782899

print("Welcome to Zomato app!!!")
print("Please choose one of the selection to proceed:")
print("1.User reviews of restaurant\n2.Get restaurants by Geo code\n3.Get the categories of restaurants\n4.Search restaurants")
userInput = input("Enter your choice:")

if(userInput=="1"):
    rest_id=input("Enter Restaurant Id:")
    getUserReviews(rest_id)
elif (userInput=="2"):
    lat= input("Enter latitude:")
    lon=input("Enter Longitude:")
    getRestaurantsByGeoCode(lat,lon)
elif (userInput=="3"):
    getCategories()
elif (userInput=="4"):
    searchText=input("Enter search text:")
    lat=input("Enter lattitude:")
    lon=input("Enter the longitude:")
    searchRestaurants(searchText,lat,lon)      
else:
    print("Invalid choice")
        


path = "C:\\Users\\z003er8w\\Desktop\\Python\\NewItinenary.txt"


def readFile():
    try:
        if os.path.exists(path):
            file = open(
                path, "r")
            fileContents = file.read()
            print("The contents of file are:\n")
            print(fileContents)
        else:
            print("File does not exists!!!Please create one")
    except Exception as e:
        print(e)


def writeToFile():
    try:
        if not os.path.exists(path):
            file = open(
                path, "x")
        else:
            file = open(
                path, "a")
            file.write("Waiting...\n")
        file.close()
        file = open(
            path, "r")
        fileContents = file.read()
        print(fileContents)
    except Exception as e:
        print("Error occured while writing and reading file: %s" % (e))


def deleteFile():
    try:
        if os.path.exists(path):
            os.remove(path)
            print("File Deleted!!!")
        else:
            print("File doesnt exists!!!")
    except Exception as e:
        print("Error while deleting the file:%s" % (e))


# Accept user input to read/write/delete file
'''userInput = int(input(
    "Please enter the choice of your operation\n\"Read:0\",\"Create:1\",\"Write:2\" and \"Delete:3\"\n"))


if userInput == 0:
    readFile()
elif userInput == 1 or userInput == 2:
    writeToFile()
elif userInput == 3:
    deleteFile()
else:
    raise Exception("Invalid Entry")'''

exit
