from generate_data.manage_file import *
import json

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from datetime import datetime, timedelta, date
import math
import traceback
import zipfile

class AccountData():  
  # if os.path.exists(r'backend\backtwitter\generate_data\twitter_data\data\account-creation-ip.js') == False:  
  #   print("Unziping the file")
  #   unzip_file()
  
  # f = print_file_info(r'generate_data\twitter_data\data\account.js').split("\n")
  fileProfile = ""
  fileAccount = ""
  fileDm = ""
  fileTweets = ""
  fileBlock = ""
  fileLike = ""
  fileFollower = ""
  fileFollowing = ""
  AccountId = ""
  AccountCreationDate = ""
  AccountAgeInDay = 0
  AccountUsername = ""
  ProfilePicture = ""
  Nb_of_dm_send = 0
  Nb_of_dm_received = 0
  Nb_of_tweet_total = 0
  Nb_of_rt = 0
  Nb_of_comment = 0
  Nb_of_tweet = 0
  
  Top5RepliedUser = []
  Top5RepliedUserNb = []
  Top5RepliedUserPercent = []
  UniqueRepliedUser = 0

  Top5DMedUser = []
  Top5DMedUserNb = []
  Top5DMedUserPercent = []
  UniqueDMedUser = 0
  
  Nb_of_account_blocked = 0
  Nb_of_tweet_liked = 0
  Nb_of_tweet_made_on_average = 0
  Nb_of_rt_made_on_average = 0
  Nb_of_comment_made_on_average = 0
  Nb_of_all_tweet_made_on_average = 0
  Nb_of_dm_send_on_average = 0
  Nb_of_dm_received_on_average = 0
  Nb_of_tweet_liked_on_average = 0
  Nb_of_word = 0
  Nb_of_char = 0
  Nb_of_unique_word = 0
  Nb_of_char_on_average = 0
  Nb_of_word_on_average = 0
  Nb_of_time_you_wrote_le_petit_prince_by_word = 0
  Nb_of_time_you_wrote_le_petit_prince_by_char = 0
  Nb_of_word_in_the_petit_prince = 14180
  Nb_of_char_in_the_petit_prince = 71595
  Nb_of_like = 0
  Nb_of_like_on_average = 0
  Nb_of_rts = 0
  Nb_of_rt_on_average = 0
  Top5MostLikedTweetNb = []
  Top5MostLikedTweetUrl = []
  Nb_of_follower = 0
  Nb_of_follower_on_average = 0
  Nb_of_following = 0
  Nb_of_following_on_average = 0
  
  Nb_of_tweet_made_on_average_time = "jour"
  Nb_of_rt_made_on_average_time = "jour"
  Nb_of_comment_made_on_average_time = "jour"
  Nb_of_all_tweet_made_on_average_time = "jour"
  Nb_of_dm_send_on_average_time = "jour"
  Nb_of_dm_received_on_average_time = "jour"
  Nb_of_tweet_liked_on_average_time = "jour"
  Nb_of_follower_on_average_time = "jour"
  Nb_of_following_on_average_time = "jour"
  
  Nb_of_action = 0
  Nb_of_action_on_average = 0
  Nb_of_action_time = "jour"

  WholeAccountData = {}
  dataJson = ""
  
  

class SeleniumData():
  options = webdriver.ChromeOptions()
  options.add_argument('--blink-settings=imagesEnabled=false')
  options.add_argument("--log-level=3")  # Suppress all logging levels
  options.add_argument("--window-size=1920,1080")
  # C:\Users\your_username\AppData\Local\Google\Chrome\User Data
  #Replace your_username with your username
  #and Profile 3 by your profile number
  # Everything is explained on the readme

  options.add_argument(r"--user-data-dir=C:\Users\sakin\AppData\Local\Google\Chrome\User Data\Profile 3")
  options.add_argument(r'--profile-directory=Profile 3')
  #options.add_argument('headless')
  driver = webdriver.Chrome(options=options)  # You can change this to whichever browser you prefer and have installed
  username_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'  
  button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
  password_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
  login_button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'


def get_zip_data(data):
  zip_path = "generate_data/"+current_zip_file()
  #f = str(print_file_info(r'generate_data\twitter_data\data\profile.js').replace('"',"").split("avatarMediaUrl")[1]).split("\n")[0].replace(":","").replace(",","").replace(" " ,"").strip('')
  with zipfile.ZipFile(zip_path, 'r') as zip_ref:
      # List all the contents of the zip file
      print("Files in the zip archive:")              
      file_name_list = ["data/profile.js","data/account.js","data/direct-messages.js","data/tweets.js","data/block.js","data/like.js","data/follower.js","data/following.js"]
      file_content_list = []
      # Read the content of the specified file
      for file_name in file_name_list:
        with zip_ref.open(file_name) as file:
            content = file.read()
            file_content_list.append(str(content.decode('utf-8')))
        
      data.fileProfile = file_content_list[0]
      data.fileAccount = file_content_list[1]
      data.fileDm = file_content_list[2]
      data.fileTweets = file_content_list[3]
      data.fileBlock = file_content_list[4]
      data.fileLike = file_content_list[5]
      data.fileFollower = file_content_list[6]
      data.fileFollowing = file_content_list[7]
      

def account_age(data):
    date_str = str(data.AccountCreationDate)
    today = datetime.now().date()
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    data.AccountAgeInDay = str(today - date).split(" ")[0].replace(" ","").strip()

def is_day_week_month_year_decadade_data(nb):
  r = 0
  info = "jour"
  if nb < 0.9:
    r = nb * 7
    info = "semaine"
    if r < 1:
      r = nb * 31
      info = "mois"
      if r < 1:
        r = nb * 365
        info = "année"
        if r < 1:
          r = nb * 3650
          info = "décenie"
        if r < 1:
          r = nb * 36500
          info = "siécle"
        if r < 1:
          r = nb * 365000
          info = "millénaire"
    return round_nb(r) , info
  else:
    return round(nb,1) , info

def round_nb(nb):
    nb_inf = int(nb)
    if nb - nb_inf >= 0.5:
        return  math.ceil(nb)
    else:
        return math.floor(nb)
    
def average_stat(data):
  
  age = int(data.AccountAgeInDay)
  data.Nb_of_tweet_made_on_average = round((data.Nb_of_tweet/age),10)
  data.Nb_of_rt_made_on_average = round((data.Nb_of_rt/age),10)
  data.Nb_of_comment_made_on_average = round((data.Nb_of_comment/age),10)
  data.Nb_of_all_tweet_made_on_average = round((data.Nb_of_tweet_total/age),10)
  data.Nb_of_dm_send_on_average = round((data.Nb_of_dm_send/age),10)
  data.Nb_of_dm_received_on_average = round((data.Nb_of_dm_received/age),10)
  data.Nb_of_tweet_liked_on_average = round((data.Nb_of_tweet_liked/age),10)
  data.Nb_of_follower_on_average = round((data.Nb_of_follower/age),10)
  data.Nb_of_following_on_average = round((data.Nb_of_following/age),10)
  
  data.Nb_of_action = int(data.Nb_of_tweet + data.Nb_of_rt + data.Nb_of_comment + data.Nb_of_dm_send + data.Nb_of_tweet_liked + data.Nb_of_following + data.Nb_of_account_blocked)
  data.Nb_of_action_on_average = round((data.Nb_of_action/age),1)
  data.Nb_of_tweet_made_on_average , data.Nb_of_tweet_made_on_average_time = is_day_week_month_year_decadade_data(data.Nb_of_tweet_made_on_average)
  data.Nb_of_rt_made_on_average , data.Nb_of_rt_made_on_average_time = is_day_week_month_year_decadade_data(data.Nb_of_rt_made_on_average)
  data.Nb_of_comment_made_on_average, data.Nb_of_comment_made_on_average_time = is_day_week_month_year_decadade_data(data.Nb_of_comment_made_on_average)
  data.Nb_of_all_tweet_made_on_average, data.Nb_of_all_tweet_made_on_average_time = is_day_week_month_year_decadade_data(data.Nb_of_all_tweet_made_on_average)
  data.Nb_of_dm_send_on_average, data.Nb_of_dm_send_on_average_time = is_day_week_month_year_decadade_data(data.Nb_of_dm_send_on_average)
  data.Nb_of_dm_received_on_average, data.Nb_of_dm_received_on_average_time = is_day_week_month_year_decadade_data(data.Nb_of_dm_received_on_average)
  data.Nb_of_tweet_liked_on_average, data.Nb_of_tweet_liked_on_average_time = is_day_week_month_year_decadade_data(data.Nb_of_tweet_liked_on_average)
  data.Nb_of_follower_on_average, data.Nb_of_follower_on_average_time = is_day_week_month_year_decadade_data(data.Nb_of_follower_on_average)  
  data.Nb_of_following_on_average, data.Nb_of_following_on_average_time = is_day_week_month_year_decadade_data(data.Nb_of_following_on_average)
  data.Nb_of_action_on_average , data.Nb_of_action_on_average_time = is_day_week_month_year_decadade_data(data.Nb_of_action_on_average)
  data.Nb_of_action_on_average = int(data.Nb_of_action_on_average)
  
def get_username_from_id(id,idx):
    S = SeleniumData()
    try:
        S.driver.get(f"https://twitter.com/intent/user?user_id={id}")
        time.sleep(1.2)
        current_url = str(S.driver.current_url)
        if idx == 5:
          S.driver.close()
        
        return (current_url.split("=")[1])
    except:
        return("error")

def convert_seconds_to_hms(seconds):
  hours = seconds // 3600
  minutes = (seconds % 3600) // 60
  remaining_seconds = seconds % 60

  return hours, minutes, remaining_seconds

def twitter_account_info():
  data = AccountData()
  print("Inside twitter_account_info function")
  #print("Start")
  get_zip_data(data)
  basic_account_data(data)
  get_profile_picture(data)
  number_of_dm(data)
  number_of_tweet(data)
  number_of_block(data)
  number_of_like(data)
  account_age(data)
  number_of_like_you_get(data)
  number_of_rt_you_get(data)
  number_of_follower(data)
  number_of_following(data)
  number_of_word(data)
  average_stat(data)
  write_data_to_json(data)
  #print("Json Data\n " , data.dataJson)
  #print("end")

def write_data_to_json(data):  
  data.WholeAccountData = {
    "AccountId": data.AccountId,
    "AccountCreationDate": data.AccountCreationDate,
    "AccountAgeInDay": data.AccountAgeInDay,
    "AccountUsername": data.AccountUsername,
    "ProfilePicture" : data.ProfilePicture,
    "Nb_of_dm_send": data.Nb_of_dm_send,
    "Nb_of_dm_received": data.Nb_of_dm_received,
    "Nb_of_tweet_total": data.Nb_of_tweet_total,
    "Nb_of_rt": data.Nb_of_rt,
    "Nb_of_comment": data.Nb_of_comment,
    "Nb_of_tweet": data.Nb_of_tweet, 
    "Top5RepliedUser": data.Top5RepliedUser,
    "Top5RepliedUserNb": data.Top5RepliedUserNb,
    "Top5RepliedUserPercent": data.Top5RepliedUserPercent,
    "UniqueRepliedUser":data.UniqueRepliedUser,
    "Top5DMedUser": data.Top5DMedUser,
    "Top5DMedUserNb": data.Top5DMedUserNb,
    "Top5DMedUserPercent":data.Top5DMedUserPercent, 
    "UniqueDMedUser":data.UniqueDMedUser,
    "Nb_of_account_blocked": data.Nb_of_account_blocked,
    "Nb_of_tweet_liked": data.Nb_of_tweet_liked,
    "Nb_of_tweet_made_on_average": data.Nb_of_tweet_made_on_average,
    "Nb_of_tweet_made_on_average_time" : data.Nb_of_tweet_made_on_average_time,
    "Nb_of_rt_made_on_average": data.Nb_of_rt_made_on_average,
    "Nb_of_rt_made_on_average_time" : data.Nb_of_rt_made_on_average_time,
    "Nb_of_comment_made_on_average": data.Nb_of_comment_made_on_average,
    "Nb_of_comment_made_on_average_time" : data.Nb_of_comment_made_on_average_time,
    "Nb_of_all_tweet_made_on_average": data.Nb_of_all_tweet_made_on_average,
    "Nb_of_all_tweet_made_on_average_time" : data.Nb_of_all_tweet_made_on_average_time,
    "Nb_of_dm_send_on_average": data.Nb_of_dm_send_on_average,
    "Nb_of_dm_send_on_average_time" : data.Nb_of_dm_send_on_average_time,
    "Nb_of_dm_received_on_average": data.Nb_of_dm_received_on_average,
    "Nb_of_dm_received_on_average_time" : data.Nb_of_dm_received_on_average_time,
    "Nb_of_tweet_liked_on_average": data.Nb_of_tweet_liked_on_average,
    "Nb_of_tweet_liked_on_average_time" : data.Nb_of_tweet_liked_on_average_time,
    "Nb_of_word": data.Nb_of_word,
    "Nb_of_char": data.Nb_of_char,
    "Nb_of_unique_word": data.Nb_of_unique_word,
    "Nb_of_char_on_average": data.Nb_of_char_on_average,
    "Nb_of_word_on_average": data.Nb_of_word_on_average,
    "Nb_of_time_you_wrote_le_petit_prince_by_word": data.Nb_of_time_you_wrote_le_petit_prince_by_word,
    "Nb_of_time_you_wrote_le_petit_prince_by_char": data.Nb_of_time_you_wrote_le_petit_prince_by_char,
    "Nb_of_word_in_the_petit_prince": data.Nb_of_word_in_the_petit_prince,
    "Nb_of_char_in_the_petit_prince": data.Nb_of_char_in_the_petit_prince,
    "Nb_of_like" : data.Nb_of_like,
    "Nb_of_like_on_average" : data.Nb_of_like_on_average,
    "Nb_of_rts" : data.Nb_of_rts,
    "Nb_of_rt_on_average" : data.Nb_of_rt_on_average,
    "Nb_of_follower" : data.Nb_of_follower,
    "Nb_of_follower_on_average" : data.Nb_of_follower_on_average,
    "Nb_of_follower_on_average_time" : data.Nb_of_follower_on_average_time,
    "Nb_of_following" : data.Nb_of_following,
    "Nb_of_following_on_average" : data.Nb_of_following_on_average,
    "Nb_of_following_on_average_time" : data.Nb_of_following_on_average_time,
    "Nb_of_action" : data.Nb_of_action,
    "Nb_of_action_on_average" : data.Nb_of_action_on_average,
    "Nb_of_action_time" : data.Nb_of_action_time,
    "Top5MostLikedTweetUrl" : data.Top5MostLikedTweetUrl,
    "Top5MostLikedTweetNb" : data.Top5MostLikedTweetNb

  }


      
  
  json_object = json.dumps(data.WholeAccountData, indent=4)
 
  data.dataJson = json_object
  # Writing to sample.json
  with open("generate_data/data.json", "w") as outfile:
      outfile.write(json_object)

def get_profile_picture(data):
  #f = str(print_file_info(r'generate_data\twitter_data\data\profile.js').replace('"',"").split("avatarMediaUrl")[1]).split("\n")[0].replace(":","").replace(",","").replace(" " ,"").strip('')
  f = data.fileProfile.replace('"',"").split("avatarMediaUrl")[1].split("\n")[0].replace(":","").replace(",","").replace(" " ,"").strip('')
  data.ProfilePicture = f

def basic_account_data(data):
  #f = print_file_info(r'generate_data\twitter_data\data\account.js').split("\n")
  f = data.fileAccount.split("\n")
  data.AccountId = get_account_data(data.fileAccount.split("\n"),"accountId").replace(",","")
  data.AccountCreationDate = get_account_creation_date(data.fileAccount.split("\n"))
  data.AccountUsername = str(get_account_data(data.fileAccount.split("\n"),"username").replace(",","").replace(" ",""))
  
def number_of_dm(data):
  #f = print_file_info(r'generate_data\twitter_data\data\direct-messages.js').replace('"',"")
  f = data.fileDm.replace('"',"")

  data.Nb_of_dm_send = f.count(f"senderId : {str(data.AccountId)}")
  data.Nb_of_dm_received = f.count(f"recipientId : {str(data.AccountId)}")
  fr = f.split("recipientId")
  fs = f.split("senderId")
  if data.Nb_of_dm_send == 0 and data.Nb_of_dm_received == 0:
    data.Top5DMedUser = []
    data.Top5DMedUserNb = []
    data.Top5DMedUserPercent = []
    return

  list_of_user = []
  list_of_user_ = []
  count_user = []
  #print("Account ID " , data.AccountId)
  for user, user2 in zip(fs, fr):
    userDm = str(user[0:100].split("\n")[0].replace(",","").replace(":","").replace(" ","")).replace(data.AccountId,"").replace("-","").replace(" ","")
    userDm2 = str(user2[0:100].split("\n")[0].replace(",","").replace(":","").replace(" ","")).replace(data.AccountId,"").replace("-","").replace(" ","")
    if "w" not in userDm and len(userDm) > 3 and data.AccountId not in userDm:
      list_of_user.append(userDm.replace("\n",""))
    if "w" not in userDm2 and len(userDm2) > 3 and data.AccountId not in userDm2:
      list_of_user.append(userDm.replace("\n",""))
        

  for user in list_of_user:
    if user not in list_of_user_ and len(user) > 5:
      list_of_user_.append(user)
      count_user.append(list_of_user.count(user))
      #print(user)
  #print("coco " , list_of_user)
  zipped_lists = zip(count_user, list_of_user_)
  sorted_zipped_lists = sorted(zipped_lists)
  sorted_list1, sorted_list2 = zip(*sorted_zipped_lists)
  
  data.UniqueDMedUser = len(list_of_user_)
  if len(sorted_list1) >= 6:
    for i in range(1,6):
      od = get_username_from_id(str(sorted_list2[-i]),i)
      data.Top5DMedUser.append(od)
      data.Top5DMedUserNb.append(sorted_list1[-i])
      data.Top5DMedUserPercent.append(round(float((sorted_list1[-i]/len(list_of_user)) * 100),1))
  else:
    for i in range(1,len(sorted_list1)):
      data.Top5DMedUser.append(sorted_list2[-i],i)
      data.Top5DMedUserNb.append(sorted_list1[-i])
      data.Top5DMedUserPercent.append(round(float((sorted_list1[-i]/len(list_of_user)) * 100),1))
  
def number_of_word(data):
  #f = print_file_info(r'generate_data\twitter_data\data\tweets.js').replace('"',"").split("full_text")
  f = data.fileTweets.replace('"',"").split("full_text")
  list_of_word = []
  unique_word = []
  for Wrd in f:
    if "RT" not in Wrd[0:5]:
      Tweetword = Wrd[0:400].split("\n")[0].replace(",","").replace(":","")
      words = Tweetword.split(" ")
      for word in words:
        if "@" not in word and "https//t.co/" not in word and "window.YTD.tweets.part0" not in word and len(word) > 0:
          list_of_word.append(word)
          data.Nb_of_char += len(word)
          if word not in unique_word:
            unique_word.append(word)
  

  data.Nb_of_word = len(list_of_word)
  data.Nb_of_word_on_average = int(round(data.Nb_of_word/(data.Nb_of_tweet + data.Nb_of_comment),0))
  data.Nb_of_char_on_average = int(round(data.Nb_of_char/(data.Nb_of_tweet + data.Nb_of_comment),0))
  
  data.Nb_of_unique_word = len(unique_word)
  
  
  data.Nb_of_time_you_wrote_le_petit_prince_by_word = round((data.Nb_of_word/data.Nb_of_word_in_the_petit_prince),1)
  data.Nb_of_time_you_wrote_le_petit_prince_by_char = round((data.Nb_of_char/data.Nb_of_char_in_the_petit_prince),1)
  
  
def number_of_tweet(data):
  #f = print_file_info(r'generate_data\twitter_data\data\tweets.js').replace('"',"")
  f = data.fileTweets.replace('"',"")
  data.Nb_of_rt = f.count("full_text : RT")
  data.Nb_of_comment = f.count("full_text : @")
  data.Nb_of_tweet_total = f.count("full_text : ")

  if data.Nb_of_comment == 0:
    data.Top5RepliedUser = []
    data.Top5RepliedUserNb = []
    data.Top5RepliedUserPercent = []
    return
  data.Nb_of_tweet = data.Nb_of_tweet_total - (data.Nb_of_rt + data.Nb_of_comment)
  list_of_user_replied = f.split("in_reply_to_screen_name")
  list_of_user = []
  list_of_user_ = []
  count_user = []
  for userT in list_of_user_replied:    
    userTweet = userT[0:30].split("\n")[0].replace(",","").replace(":","").replace(" ","")
    if len(userTweet) < 16 and userTweet.lower() != data.AccountUsername.lower():
      list_of_user.append(userTweet)
    

  for user in list_of_user:
    if user not in list_of_user_:
      list_of_user_.append(user)
      count_user.append(list_of_user.count(user))
  
  zipped_lists = zip(count_user, list_of_user_)
  sorted_zipped_lists = sorted(zipped_lists)
  sorted_list1, sorted_list2 = zip(*sorted_zipped_lists)
  
  data.UniqueRepliedUser = len(list_of_user_)
  
  if len(sorted_list1) >= 6:
    for i in range(1,6):
      data.Top5RepliedUser.append(sorted_list2[-i])
      data.Top5RepliedUserNb.append(sorted_list1[-i])
      data.Top5RepliedUserPercent.append(round(float((sorted_list1[-i]/data.Nb_of_comment) * 100),1))
      
  else:
    for i in range(1,len(sorted_list1)):
      data.Top5RepliedUser.append(sorted_list2[-i])
      data.Top5RepliedUserNb.append(sorted_list1[-i])
      data.Top5RepliedUserPercent.append(round(float((sorted_list1[-i]/data.Nb_of_comment) * 100),1))

def number_of_block(data):
  data.Nb_of_account_blocked = data.fileBlock.replace('"',"").count("blocking")

def number_of_like(data):
  data.Nb_of_tweet_liked = data.fileLike.replace('"',"").count("expandedUrl")

def number_of_follower(data):
  data.Nb_of_follower = data.fileFollower.replace('"',"").count("follower")

def number_of_following(data):
  data.Nb_of_following = data.fileFollowing.replace('"',"").count("following")

def number_of_like_you_get(data):
  f = data.fileTweets.replace('"',"").split("favorite_count")
  nb_like = 0
  index = 0
  list_of_tweet = []
  tweet_fav = []
  idx = 0
  for nbLike in f:
    idx +=1    
    userLike = nbLike[0:30].split("\n")[0].replace(",","").replace(":","").replace(" ","")
    try:
      tweetId = str(nbLike).split("in_reply_to_user_id")[0].replace(",","").replace(" ","").split(":")[3].replace("\n","")
    except:
      tweetId = ""
    
    if "window.YTD.tweets.part0=[" not in userLike:
      if userLike[0] == "0" and index < data.Nb_of_rt:
        index+=1
      else:
        try:
          nb_like+=int(userLike)
          list_of_tweet.append("https://twitter.com/i/web/status/"+tweetId)
          tweet_fav.append(int(userLike))
        except:
          pass
  
  zipped_lists = zip(tweet_fav, list_of_tweet)
  sorted_zipped_lists = sorted(zipped_lists)
  sorted_list1, sorted_list2 = zip(*sorted_zipped_lists)
  
  if len(sorted_list1) >= 6:
    for i in range(1,6):
      data.Top5MostLikedTweetUrl.append(sorted_list2[-i])
      data.Top5MostLikedTweetNb.append(sorted_list1[-i])
      
  else:
    for i in range(1,len(sorted_list1)):
      data.Top5MostLikedTweetUrl.append(sorted_list2[-i])
      data.Top5MostLikedTweetNb.append(sorted_list1[-i])
      
  data.Nb_of_like = nb_like
  if data.Nb_of_comment+data.Nb_of_tweet == 0:
    return
  data.Nb_of_like_on_average = round(nb_like/(data.Nb_of_comment+data.Nb_of_tweet),1)
  if data.Nb_of_like_on_average < 0.2:
    data.Nb_of_like_on_average = round(nb_like/(data.Nb_of_comment+data.Nb_of_tweet),3)

def number_of_rt_you_get(data):
  f = data.fileTweets.replace('"',"").split("retweet_count")
  nb_rt = 0
  index = 0
  for nbLike in f:    
    userRt = nbLike[0:30].split("\n")[0].replace(",","").replace(":","").replace(" ","")
    
    if "window.YTD.tweets.part0=[" not in userRt:
      if userRt[0] == "0" and index < data.Nb_of_rt:
        index+=1
      else:
        nb_rt+=int(userRt)

  data.Nb_of_rts = nb_rt
  if data.Nb_of_comment+data.Nb_of_tweet == 0:
    return
  data.Nb_of_rt_on_average = round(nb_rt/(data.Nb_of_comment+data.Nb_of_tweet),1)
  if data.Nb_of_rt_on_average < 0.2:
    data.Nb_of_rt_on_average = round(nb_rt/(data.Nb_of_comment+data.Nb_of_tweet),3)
  

def twitter_account_data():
  try:
    #start_time = time.time()
    print("Unziping the file")
    ca = 0
    if ca == 1:
      unzip_file()
      list_of_files = os.listdir(r"generate_data\twitter_data\data")
      #print("list of files " , list_of_files)
      if "account-creation-ip.js" not in list_of_files:  
        print("The file provided is not twitter archive")
        delete_data()
        return("")
    twitter_account_info()
    delete_data()
    #end_time = time.time()
    #elapsed_time = end_time - start_time
    #hours, minutes, remaining_seconds = convert_seconds_to_hms(int(elapsed_time))
    # with open("data.json", 'w') as f:
    #   json.dump({}, f)
    # #print(f"It tooks {hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")
    print("Everything went well good")
    return True
  except:
    traceback.print_exc()
    delete_data()
    print("Everything went bad")
    return (False)
