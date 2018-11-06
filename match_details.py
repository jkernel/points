import sys
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


###############################😎 Split LINES IN .TXT FILE & opening WEBDRIVER at the 1st Url #####################################################


with open('links-penalty.txt','r') as fo:
   count=0
   for line in fo:
      count+=1
      
      url=line
      from selenium import webdriver
      driver=webdriver.PhantomJS('/home/jkernel/Desktop/python books/phantomjs/bin/phantomjs',service_args=['--load-images=no','--disk-cache=true'])
      driver.get(url)
      time.sleep(3)
      
 ##################################😎 HOME TEAM CONFIG ###################################################
      search_team1_name= driver.find_element_by_css_selector('div.hostteam div.name')
      search_team2_name= driver.find_element_by_css_selector('div.guestteam div.name')
      team1_name= search_team1_name.text
      team2_name= search_team2_name.text
      
      
      
      #Typwnei ta onomata omadwn
      print(team1_name,"-",team2_name)
      
      #typwnei tis red cards
      try:
      	search_team1_red_card= driver.find_element_by_css_selector('div.statrow:nth-of-type(2) div.value:nth-of-type(1)')
      	team1_red_card=search_team1_red_card.text
      	
      	print("Home Team Red Cards: ",team1_red_card)
      	search_team2_red_card= driver.find_element_by_css_selector('div.statrow:nth-of-type(2) div.value:nth-of-type(3)')
      	team2_red_card=search_team2_red_card.text
      	print("Away Team Red Cards: ",team2_red_card)      	

      except NoSuchElementException:
      	print("No red card")
      
      
      #dokimazei ean yparxei penalty
      try:	            
	      search_team1_penalty= driver.find_element_by_css_selector('div.penalty')
	      if(search_team1_penalty.is_displayed()==True):
	      	print(team1_penalty_scored)
      except NoSuchElementException:
      	print("No penalty found")
      
    
      	
      try:
	      search_penalty_missed= driver.find_element_by_css_selector('div.miss')
      except NoSuchElementException:
      	print("No missed penalty")
      try:
	      search_team1_own_goal= driver.find_element_by_css_selector('div.own')
	      owngoal=search_team1_own_goal.text
	      print(owngoal)
      except NoSuchElementException:
      	print("No own goal")
      	

      driver.quit()
      print("#######################################################")      



