import requests

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


# User fields are adjustable, options include:
# created_at, description, entities, id, location, name,
# pinned_tweet_id, profile_image_url, protected,
# public_metrics, url, username, verified, and withheld


class User():
    def __init__(self, BEARER_TOKEN, fields=['id','created_at', 'description']):
        self.headers = {"Authorization": "Bearer {bearer_token}".format(bearer_token=BEARER_TOKEN)}
        self.user_fields = "user.fields="+','.join(fields)
        self.url = "https://api.twitter.com/2/users/by?{usernames}&"+self.user_fields

    def target(self, username):
        self.username = username


    def getUserInfo(self):
        response = requests.request("GET", self.url.format(usernames=self.username), headers=self.headers)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

    def getFollowers(self):
        pass
