import requests

class Zomato(object):
    def __init__(self,key,headers=None):
        self.key = key
        self.baseurl = 'https://developers.zomato.com/api/v2.1/'
        if (headers != None):
            self.headers = headers
        else :
            self.headers = {
                "User-agent": "curl/7.43.0",
                "Content-type": "application/json",
                "X-Zomato-API-Key": self.key
            }

    def getCategory(self):
        categories_url=self.baseurl+'categories'
        try:
            response= requests.get(url=categories_url,headers=self.headers).json()
            return response
        except Exception as ex:
            return "Unexpected error occured"

    def getGeoCode(self,cordinate):
        geoCode_url=self.baseurl+'geocode'
        if type(cordinate) is str:
            lat,lon=cordinate.split('-')
            option={
                'lat':lat,
                'lon':lon
            }
        response=requests.get(url=geoCode_url,params=option,headers=self.headers).json()   
        return response    


    def getRestaurant(self,restaurantId):
        dailyMenu_url=self.baseurl+'restaurant'
        option={
            'res_id':restaurantId
        }
        response=requests.get(url=dailyMenu_url,params=option,headers=self.headers).json()
        return response     

    def getUserReviews(self,restaurantId):
        userReview_url=self.baseurl+'reviews'
        option={
            'res_id':restaurantId,
            'start':0,
            'count':10
        }
        response=requests.get(url=userReview_url,params=option,headers=self.headers).json()
        return response

    def searchRestaurants(self,searchText,lat,lon):
        search_url=self.baseurl+'search'
        option={
            'q':searchText,
            'lat':lat,
            'lon':lon
        }
        response=requests.get(url=search_url,params=option,headers=self.headers).json()
        return response
