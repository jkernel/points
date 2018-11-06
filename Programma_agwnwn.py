import sys
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


###############################😎 Split LINES IN .TXT FILE & opening WEBDRIVER at the 1st Url #####################################################


with open('links.txt','r') as fo:
   count=0
   for line in fo:
      count+=1
      
      url=line
      from selenium import webdriver
      driver=webdriver.PhantomJS('/home/jkernel/Desktop/phantom/phantomjs/bin/phantomjs',service_args=['--load-images=no','--disk-cache=true'])
      driver.get(url)
      time.sleep(7)
      
 ##################################😎 HOME TEAM CONFIG ###################################################
      try:
            search_team1_name = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div#teamname.value')
            search_team1_country = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) span.name')
            
            
            
            search_apotelesma= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.starttime')
            search_game_datetime= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.starttime')


            
            
            
      except NoSuchElementException:
            print("Element of Home Team not found")
            
      
      team1_name = search_team1_name.text
      team1_country = search_team1_country.text          
      game_datetime=search_game_datetime.text
            
            
    
         

         
      ##################################😎 AWAY TEAM CONFIG ###################################################
      try:
            search_team2_name = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div#teamname.value')
            search_team2_country = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) span.name')
            
            
      except NoSuchElementException:
         print("Element of Away Team not found")   
      team2_name = search_team2_name.text
      team2_country = search_team2_country.text     
      
      #print("Χώρα: ",team2_country)
      #print("Away Team: ",team2_name)
      
    
          
      
      
      

      driver.quit()
     
      
      
     
    
      print("Χώρα: ",team2_country)
      print(team1_name,"**VS**",team2_name)
      print("Έναρξη: ",game_datetime)
      
      
     
      
      print("###########*###################################*#######################################*##############################*##########################*############")    


