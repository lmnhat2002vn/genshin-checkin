import requests, json

act_id = "e....." # i think is is the update patch code?

# this header is to mask the bot as a normal mozilla user
header = {"Cookie": your cookie",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
  "Origin": "https://act.hoyolab.com",
  "Referer" : "https://act.hoyolab.com/"
} 


# get the account info and log in streak/date
info_url = "https://sg-hk4e-api.hoyolab.com/event/sol/info?lang=en-us&act_id=" + act_id
info_response = requests.get(info_url, headers=header)
info_response_json = info_response.json()
total_sign_day = info_response_json['data']['total_sign_day'] - 1

# get the rewards list
reward_url = "https://sg-hk4e-api.hoyolab.com/event/sol/home?lang=en-us&act_id=" + act_id
reward_response = requests.get(reward_url, headers=header)
reward_response_json = reward_response.json()
reward = reward_response_json['data']['awards']
# combine with the total_sign_day from info to get today reward
reward_name = reward[total_sign_day]['name']
reward_cnt = str(reward[total_sign_day]['cnt'])
reward_value = reward_name + ' x ' + reward_cnt
reward_icon = reward[total_sign_day]['icon']

# this is the actual sign-in for the day
sign_url = "https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=en-us" 

payload = '{"act_id": "' + act_id + '"}'

sign_response = requests.post(sign_url, data=payload, headers=header)
sign_response_json = sign_response.json()

# debug
sign_message = str(sign_response_json["message"])
reward_message = str(reward_name)
info_message = str(info_response_json)
sign_date = str(total_sign_day)
# print(reward_message)

# dicord webhook
log_message_json = {"embeds": [{
    "author" : {"name": "Paimon",
                "url": "https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e.....&lang=en-us",
                "icon_url" : "https://fastcdn.hoyoverse.com/static-resource-v2/2024/04/12/b700cce2ac4c68a520b15cafa86a03f0_2812765778371293568.png"},
    "thumbnail" : {"url": reward_icon},
    "fields": [
               {"name": "Today's rewards", "value": reward_value, "inline": "True"},
               {"name": "Check-In Streak", "value": total_sign_day + 1, "inline": "True"},
               {"name": "Check-in result:", "value": sign_message, "inline": "False"}
              ]
    }]}
webhook_url = 'your discord webhook'
requests.post(webhook_url, json=log_message_json)








# on device logs
# f = open("genshin_checkin_logs.txt","a")
# f.write(reward_value + "/n" + sign_message+ "/n")
# f.close()                  + "/n" + sign_message