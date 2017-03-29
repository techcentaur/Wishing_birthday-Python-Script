#Description: A simple python application to wish your friends a happy birthday on facebook


from facepy import GraphAPI
import datetime
import random
import facebook

oauth_token = ''#Put your User access token here.!!
graph = GraphAPI(oauth_token)
friend_list = graph.get("me/friends?fields=birthday,name")
#birthday wishes are as follows
birthday_wishes = ["Life wouldn't be the same without a friend like you. Happy Birthday!",
"My best wishes for a furious and voracious day filled with plenty of smile and laughter. Happy Birthday to you!",
"May the special day of yours be filled with loving memories full of fun and the company of good friends. Happy Birthday!",
"Look for the best and leave behind all the rest. Happy Birthday my friend!",
"One year older means one year wiser. The truth is that our company needed an old wise person like you. Happy Birthday my friend"
]

#Get today's day and month
now = datetime.datetime.now().strftime("%m-%d")
month_day = now.split('-')

#Iterate through friend list birthday's and wish a random message
for friend in friend_list['data']:
    if 'birthday' in friend:
        bday_array = friend['birthday'].split('/')
        if bday_array[0] == month_day[0] and bday_array[1] == month_day[1]:
            bday_wish  = birthday_wishes[random.randint(0, len(birthday_wishes) -1) ]
            graph.post(friend['id']+ '/feed', 0, message = bday_wish)
            print ("Wished " + friend['name'])
