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
            search_team1_form = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.formastext')
            search_team1_avg_goals_scored = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(5) div.value')
            search_team1_avg_goals_conceded = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(6) div.value')
            search_team1_world_rank= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.datarow:nth-of-type(5) div.value')
            search_team1_chance_score= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(7) div.value')
            search_team1_chance_concede= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(8) div.value')
            search_team1_over_1_5_mats= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.barchart:nth-of-type(8) div.barrow:nth-of-type(1) div.bar')
            search_team1_over_2_5_mats= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.barchart:nth-of-type(10) div.barrow:nth-of-type(1) div.bar')
            search_team1_btts= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.barchart:nth-of-type(17) div.barrow:nth-of-type(1) div.bar')
            search_team1_last10_cleansheet= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(9) div.value')
            search_team1_last10_failtoscore= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(10) div.value')
            search_team1_goal_difference= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.barchart:nth-of-type(38) div.barrow:nth-of-type(1) div.bar')
            search_team1_last10_draws=driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.barchart:nth-of-type(3) div.barrow:nth-of-type(2) div.bar').text
            search_team1_table= driver.find_element_by_class_name('pos').text


            search_apotelesma= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.starttime')
            search_game_datetime= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.starttime')


            
            
            
      except NoSuchElementException:
            print("Element of Home Team not found")
            
      #team1_table_int= int(search_team1_table)
      team1_name = search_team1_name.text
      team1_country = search_team1_country.text          
      team1_last10 = search_team1_form.text   #😀 Kanei text ta last 10 formas
      team1_avg_goals_scored = search_team1_avg_goals_scored.text
      team1_avg_goals_conceded = search_team1_avg_goals_conceded.text
      team1_int_avg_scored= float(team1_avg_goals_scored)
      team1_int_avg_conceded= float(team1_avg_goals_conceded)
      team1_world_rank= search_team1_world_rank.text
      team1_chance_to_score= search_team1_chance_score.text
      team1_nosymbol_chance_to_score= team1_chance_to_score.strip('%')  #afairesh symbolou %
      team1_int_chance_to_score=int(team1_nosymbol_chance_to_score)
      team1_chance_to_concede= search_team1_chance_concede.text
      team1_nosymbol_chance_to_concede=team1_chance_to_concede.strip('%')
      team1_int_chance_to_concede=int(team1_nosymbol_chance_to_concede)
      team1_over_1_5_mats= search_team1_over_1_5_mats.text
      team1_over_1_5_mats_nosymbol= team1_over_1_5_mats.strip('%')  #afairesh symbolou %
      team1_over_1_5_int= int(team1_over_1_5_mats_nosymbol)
      team1_over_2_5_mats= search_team1_over_2_5_mats.text
      team1_over_2_5_mats_nosymbol= team1_over_2_5_mats.strip('%')
      team1_over_2_5_int= int(team1_over_2_5_mats_nosymbol)
      team1_btts= search_team1_btts.text
      team1_btts_nosymbol= team1_btts.strip('%')
      team1_btts_int= int(team1_btts_nosymbol)
      team1_last10_cleansheet= search_team1_last10_cleansheet.text
      team1_last10_cleansheet_int= int(team1_last10_cleansheet)
      team1_last10_failtoscore= search_team1_last10_failtoscore.text
      team1_last10_failtoscore_int= int(team1_last10_failtoscore)
      
      team1_goal_difference= search_team1_goal_difference.text
      team1_nosymbol_goal_difference= team1_goal_difference.strip('%')  #afairesh symbolou %
      team1_goal_difference_int=int(team1_nosymbol_goal_difference)      
      team1_last10_draws_nosymbol=search_team1_last10_draws.strip('%')
      team1_last10_draws_int=int(team1_last10_draws_nosymbol)

      
      try:
            game_datetime=search_game_datetime.text
            search_history_team1_wins= driver.find_element_by_css_selector('div.facts div.datarow:nth-of-type(3) div.value')
            search_history_draws= driver.find_element_by_css_selector('div.facts div.datarow:nth-of-type(4) div.value')
            search_history_team2_wins= driver.find_element_by_css_selector('div.facts div.datarow:nth-of-type(5) div.value')
            history_team1_wins= search_history_team1_wins.text
            history_team1_wins_int= int(history_team1_wins)
            history_draws= search_history_draws.text
            history_draws_int=int(history_draws)
            history_team2_wins= search_history_team2_wins.text
            history_team2_wins_int= int(history_team2_wins)
            
      except NoSuchElementException:
            print("History not found")  
      
      
      
      try:
            team1_int_world_rank= int(team1_world_rank)
            #print("World Rank: ",team1_int_world_rank)           
      except ValueError:
            #print("Δεν έχουν World Rank")
            norank=True

     
      
      try:
            list(team1_last10)
            team1_last7=team1_last10[3:10]
            team1_last6=team1_last10[4:10]
            team1_last5=team1_last10[5:10]
            team1_7th=team1_last7[0]
            team1_6th=team1_last7[1]
            team1_5th=team1_last7[2]
            team1_4th=team1_last7[3]
            team1_3rd=team1_last7[4]
            team1_2nd=team1_last7[5]
            team1_1st=team1_last7[6]

      except:
            pass
    
      team1_wins_draws_losses=team1_last6.count('W'),"-",team1_last6.count('D'),"-",team1_last6.count('L')
      team1_sum6_wins=team1_last6.count('W')
      team1_sum6_draws=team1_last6.count('D')
      team1_sum6_losses=team1_last6.count('L')
      team1_sum5_wins=team1_last5.count('W')
      team1_sum5_draws=team1_last5.count('D')
      team1_sum5_losses=team1_last5.count('L')
 
      team1_sum7_wins=team1_last7.count('W')
      team1_sum7_draws=team1_last7.count('D')      
      team1_sum7_losses=team1_last7.count('L')    


      ##################################😎 AWAY TEAM CONFIG ###################################################
      try:
            search_team2_name = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div#teamname.value')
            search_team2_country = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) span.name')
            search_team2_form = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.formastext')
            search_team2_avg_goals_scored = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.factitem:nth-of-type(5) div.value')
            search_team2_avg_goals_conceded = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.factitem:nth-of-type(6) div.value')
            search_team2_world_rank= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.datarow:nth-of-type(5) div.value')
            search_team2_chance_score= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.factitem:nth-of-type(7) div.value')
            search_team2_chance_concede= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.factitem:nth-of-type(8) div.value')
            search_team2_over_1_5_mats= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.barchart:nth-of-type(8) div.barrow:nth-of-type(1) div.bar')
            search_team2_over_2_5_mats= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.barchart:nth-of-type(10) div.barrow:nth-of-type(1) div.bar')
            search_team2_btts= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.barchart:nth-of-type(17) div.barrow:nth-of-type(1) div.bar')
            search_team2_btts= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.barchart:nth-of-type(17) div.barrow:nth-of-type(1) div.bar')
            search_team2_last10_cleansheet= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.factitem:nth-of-type(9) div.value')
            search_team2_last10_failtoscore= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.factitem:nth-of-type(10) div.value')
            search_team2_goal_difference= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.barchart:nth-of-type(38) div.barrow:nth-of-type(1) div.bar')
            
            search_team2_last10_draws=driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.barchart:nth-of-type(3) div.barrow:nth-of-type(2) div.bar').text
            search_team2_table= driver.find_element_by_css_selector('div.standingrow.highlite.mark div.pos').text


      except NoSuchElementException:
         print("Element of Away Team not found")   
      
      team2_name = search_team2_name.text
      team2_country = search_team2_country.text     
      team2_last10 = search_team2_form.text   #😀 Kanei text ta last 10 formas
      team2_avg_goals_scored = search_team2_avg_goals_scored.text
      team2_avg_goals_conceded = search_team2_avg_goals_conceded.text
      team2_int_avg_scored= float(team2_avg_goals_scored)
      team2_int_avg_conceded= float(team2_avg_goals_conceded)
      team2_world_rank= search_team2_world_rank.text      
      team2_chance_to_score= search_team2_chance_score.text
      team2_nosymbol_chance_to_score= team2_chance_to_score.strip('%')
      team2_int_chance_to_score=int(team2_nosymbol_chance_to_score)
      team2_chance_to_concede= search_team2_chance_concede.text
      team2_nosymbol_chance_to_concede=team2_chance_to_concede.strip('%')
      team2_int_chance_to_concede=int(team2_nosymbol_chance_to_concede)
      team2_over_1_5_mats= search_team2_over_1_5_mats.text
      team2_over_1_5_mats_nosymbol= team2_over_1_5_mats.strip('%')  #afairesh symbolou %
      team2_over_1_5_int= int(team2_over_1_5_mats_nosymbol)
      team2_over_2_5_mats= search_team2_over_2_5_mats.text
      team2_over_2_5_mats_nosymbol= team2_over_2_5_mats.strip('%')
      team2_over_2_5_int= int(team2_over_2_5_mats_nosymbol)
      team2_btts= search_team2_btts.text
      team2_btts_nosymbol= team2_btts.strip('%')
      team2_btts_int= int(team2_btts_nosymbol)
      team2_last10_cleansheet= search_team2_last10_cleansheet.text
      team2_last10_cleansheet_int= int(team2_last10_cleansheet)
      team2_last10_failtoscore= search_team2_last10_failtoscore.text
      team2_last10_failtoscore_int= int(team2_last10_failtoscore)
      team2_last10_draws_nosymbol=search_team2_last10_draws.strip('%')
      team2_last10_draws_int=int(team2_last10_draws_nosymbol)

      team2_goal_difference= search_team2_goal_difference.text      
      team2_nosymbol_goal_difference= team2_goal_difference.strip('%')  #afairesh symbolou %
      team2_goal_difference_int=int(team2_nosymbol_goal_difference)  
      

      ##print(team2_last10)
      driver.quit()
      try:
            list(team2_last10)
            team2_last7=team2_last10[3:10]
            team2_last6=team2_last10[4:10]
            team2_last5=team2_last10[5:10]
            team2_7th=team2_last7[0]
            team2_6th=team2_last7[1]
            team2_5th=team2_last7[2]
            team2_4th=team2_last7[3]
            team2_3rd=team2_last7[4]
            team2_2nd=team2_last7[5]
            team2_1st=team2_last7[6]
      except:
            pass

      
    
      team2_wins_draws_losses=team2_last6.count('W'),"-",team2_last6.count('D'),"-",team2_last6.count('L')
      team2_sum6_wins=team2_last6.count('W')
      team2_sum6_draws=team2_last6.count('D')
      team2_sum6_losses=team2_last6.count('L')
      team2_sum5_wins=team2_last5.count('W')
      team2_sum5_draws=team2_last5.count('D')
      team2_sum5_losses=team2_last5.count('L')
 
      team2_sum7_wins=team2_last7.count('W')
      team2_sum7_draws=team2_last7.count('D')
      team2_sum7_losses=team2_last7.count('L')    
      try:
            print("Χώρα: ",team2_country)
            print(team1_name,"**VS**",team2_name)
            print("Έναρξη: ",game_datetime)
            
            print("Γηπ. Θέση:",search_team1_table,"Φιλ.Θέση:",search_team2_table)
      except NameError:
            pass

      points_assos=0
      points_draw=0
      points_diplo=0
      try:
            print("Φόρμες6:  {}{}{} | {}{}{}".format(team1_sum6_wins,team1_sum6_draws,team1_sum6_losses,team2_sum6_wins,team2_sum6_draws,team2_sum6_losses))

            
            print("---> Προϊστορία: {}-{}-{}.".format(history_team1_wins_int,history_draws_int,history_team2_wins_int))

            if (history_team1_wins_int>history_team2_wins_int+5 and history_team1_wins_int>history_draws_int+5):
                  print("H Προϊστορία δείχνει ΑΣΣΟ.")
                  points_assos+=10
                  #points_diplo-=5
                  #points_draw-=3
            
            elif (history_team1_wins_int+5<history_team2_wins_int and history_team2_wins_int> history_draws_int+5):
                  print("Η Προϊστορία δείχνει ΔΙΠΛΟ")
                  points_diplo+=7
                  #points_assos-=5
                  #points_draw-=3
            elif ((history_draws_int> history_team1_wins_int+5) and (history_draws_int> history_team2_wins_int+5) ):
                  print("Η Προϊστορία δείχνει Ισοπαλία")
                  points_draw+=7
                  #points_assos-=3
                  #points_diplo-=3
            elif (history_draws_int-7>= history_team1_wins_int and history_draws_int-7>= history_team2_wins_int):
                  print("Η Προϊστορία δείχνει καθαρή ΙΣΟΠΑΛΙΑ!!!")
                  points_draw+=10
                  #points_assos-=5
                  #points_diplo-=5
            elif (history_team1_wins_int>history_team2_wins_int+8 and history_team1_wins_int>history_draws_int+8):
                  print("H Προϊστορία δείχνει καρφωτό ΑΣΣΟ !!!")
                  points_assos+=15
                  points_diplo-=5
            elif (history_team1_wins_int+7<history_team2_wins_int and history_team2_wins_int> history_draws_int+7):
                  print("Η Προϊστορία δείχνει καθαρό ΔΙΠΛΟ")
                  points_diplo+=10
            

            if (history_team1_wins_int in range(0,1) and history_draws_int>4 and history_team2_wins in range(0,1)):
                  print("Τα Χ υπερτερούν στην Προϊστορία!!")
                  #points_assos-=3
                  #points_diplo-=3
                  points_draw+=8
            elif (history_draws_int in range(0,1) and history_team2_wins_int in range (0,1) and history_team1_wins_int>4):
                  print("Ο άσσος επικρατεί στην Προϊστορία!!")
                  points_assos+=7
                  #points_diplo-=3
                  #points_draw-=3
            
            elif(history_team1_wins_int==0 and history_team2_wins_int==0 and history_draws_int>3):
                  print("Κανένας Άσσος και κανένα διπλό στην Προϊστορία..Περισσότερες απο 3 ΙΣΟΠΑΛΙΕΣ!!!")
                  points_draw+=5
                  #points_assos-=3
                  #points_diplo-=5
            elif(history_team1_wins_int>10 and history_draws_int<4 and history_team2_wins_int<4):
                  print("Μεγάλο Προβάδισμα στον ΑΣΣΟ λόγω Προϊστορίας.")
                  points_assos+=10
                  #points_diplo-=5
                  #points_draw-=5
            elif(history_team1_wins_int<4 and history_draws_int>9 and history_team2_wins_int<4):
                  print("Μεγάλο Προβάδισμα στην ΙΣΟΠΑΛΙΑ λόγω Προϊστορίας.")
                  #points_assos-=5
                  #points_diplo-=5
                  points_draw+=8
            elif(history_team1_wins_int<4 and history_draws_int<4 and history_team2_wins_int>9):
                  print("Η Προϊστορία δείχνει ξεκάθαρο ΔΙΠΛΟ")
                  points_diplo+=7
                  points_assos-=3
                  points_draw-=3
      except NameError:
            print ("Δεν έχουν Προϊστορία")
            
            
      try:  
            if (team1_int_world_rank+400 < team2_int_world_rank):
                  print("---> Οι γηπεδούχοι {} έχουν βαρύτερη φανέλα λόγω World Rank !".format(team1_name))
            elif (team2_int_world_rank+400 < team1_int_world_rank):
                  print("---> Οι φιλοξενούμενοι {} έχουν βαρύτερη φανέλα λόγω World Rank !".format(team2_name))
            elif (norank==True):
                  print("Δεν έχουν Rank.")
                  
                  
            
              
      except NameError:

            pass

      
      if ('W' in team1_1st and 'W' in team2_1st):
            print("Οι ομάδες προέρχονται από Νίκες")
            points_draw+=4     
      elif ('L' in team1_1st and 'L' in team2_1st):
            print("Οι ομάδες προέρχονται από Ήττες")
            points_draw+=4          
      elif ('L' in team1_1st and 'W' in team2_1st):
            print("Οι γηπεδούχοι προέρχονται από Ήττα ενώ οι φιλοξενούμενοι από Νίκη ")
            points_diplo+=5
            points_assos-=3
      elif ('W' in team1_1st and 'L' in team2_1st):
            print("Οι γηπεδούχοι προέρχονται από Νίκη και οι φιλοξενούμενοι από Ήττα")
            points_assos+=8
            points_diplo-=3
      elif('D' in team1_1st and 'D' in team2_1st):
            print("Οι ομάδες προέρχονται από ισοπαλίες.")
            points_draw+=7
      
      if (team1_goal_difference_int>69 and team2_goal_difference_int>69):
            print("Τα παιχνίδια των 2 ομάδων κρίνονται στο γκολ! Τείνουν προς ισοπαλίες.")
            points_draw+=8

      
      if 'L' in team1_7th and 'L' in team2_7th:
            print("7ο: ΉΤΤΑ ΚΑΙ οι δύο στο 7ο!!! Η ισοπαλία παραμονεύει.")
            points_draw+=6
      elif 'L' in team1_7th and 'W' in    team2_7th:
            print("7ο: ΉΤΤΑ ΜΟΝΟ οι γηπεδούχοι! Πάνε για θετικό αποτέλεσμα.")
            points_assos+=10
            points_draw+=8
            points_diplo-=5
      elif 'W' in team1_7th and 'L' in team2_7th:
            print("7ο: ΉΤΤΑ ΜΟΝΟ οι φιλοξενούμενοι! Μπορούν να πάρουν κάτι θετικό")
            points_diplo+=7
            points_draw+=7
            points_assos-=3
      elif 'D' in team1_7th and 'D' in team2_7th:
            print("7ο: ΙΣΟΠΑΛΙΑ ΚΑΙ οι δύο.  ")
            points_draw+=10
      elif 'D' in team1_7th and 'W' in team2_7th:
            print("7ο: D-W. Υπό συνθήκες ισοπαλία.")
            points_draw+=5
      elif 'W' in team1_7th and 'D' in team2_7th:
            print("7ο: W-D. Υπό συνθήκες ισοπαλία")
            points_draw+=5
      elif 'W' in team1_7th and 'W' in team2_7th:
            print("7ο: W-W. Ευνοείται η Ισοπαλία")
            points_draw+=7
      elif 'D' in team1_7th and 'D' in team2_7th:
            print("7ο: D-D. Ευνοείται η Ισοπαλία")
            points_draw+=10
      elif 'D' in team1_7th and 'L' in team2_7th:
            print("7ο: ΉΤΤΑ ΜΟΝΟ οι φιλοξενούμενοι! Οι φιλοξενούμενοι μπορούν να πάρουν κάτι θετικό")
            points_diplo+=6
            points_draw+=6
            points_assos-=2

      elif 'L' in team1_7th and 'D' in team2_7th:
            print("7ο: ΉΤΤΑ ΜΟΝΟ οι γηπεδούχοι! Πάνε για θετικό αποτέλεσμα.")
            points_assos+=9
            points_draw+=8
            #points_diplo-=2
      
      if (team1_sum6_wins==0 and team1_sum6_draws==2 and team1_sum6_losses==4 and team2_sum6_wins==1 and team2_sum6_draws==2 and team2_sum6_losses==3):
         print("Κριτήριο 024+123!!!: Νίκη της γηπεδούχου ομάδας {}.".format(team1_name))
         points_assos+=10
         
      if (team1_sum6_wins==3 and team1_sum6_draws==2 and team1_sum6_losses==1 and team2_sum6_wins==4 and team2_sum6_draws==2 and team2_sum6_losses==0):
         print("Κριτήριο 321+420!!!: Νίκη της γηπεδούχου ομάδας {}.".format(team1_name))
         points_assos+=10
         
      if (team1_sum6_wins==2 and team1_sum6_draws==1 and team1_sum6_losses==3 and 'L' in team1_1st and 'L' in team1_2nd and 'L' in team1_3rd):
            print("Οι γηπεδούχοι έχουν 213 με 3 συνεχόμενες ήττες. Πάνε για θετικό αποτέλεσμα.")
            points_assos+=8
            points_draw+=8
            #points_diplo-=2
      
      if (team1_sum6_wins==1 and team1_sum6_draws==2 and team1_sum6_losses==3 and 'L' in team1_1st and 'L' in team1_2nd and 'L' in team1_3rd):
         highlight3_match= "Οι γηπεδούχοι έχουν 123 με 3 συνεχόμενες ήττες. Πάνε για θετικό αποτέλεσμα."
         points_assos+=8
         points_draw+=8
         #points_diplo-=2
      
      if (team1_sum6_wins==team2_sum6_wins-1 and team1_sum6_draws==team2_sum6_draws and team1_sum6_losses== team2_sum6_losses+1 and 'L' in team1_7th):
         print("Οι γηπεδούχοι έχουν ΗΤΤΑ στο 7ο και με νίκη ισορροπούν τη φόρμα πλήρως{}.")
         points_assos+=10
         points_draw+=5
         points_diplo-=5
      
      if (team2_sum6_wins==team1_sum6_wins-1 and team2_sum6_draws==team1_sum6_draws and team2_sum6_losses== team1_sum6_losses+1 and 'L' in team2_7th):
         print("Οι φιλοξενούμενοι έχουν ΗΤΤΑ στο 7ο και με νίκη ισορροπούν τη φόρμα πλήρως{}.")
         points_diplo+=7
         points_draw+=5
         points_assos-=3
      
      
      if (team1_sum6_wins==1 and team1_sum6_draws==1 and team1_sum6_losses==4 and team2_sum6_wins==1 and team2_sum6_draws==2 and team2_sum6_losses==3):
         print("Κριτήριο 114+123!!!: Νίκη της γηπεδούχου ομάδας {}.".format(team1_name))
         points_assos+=10
         points_draw+=3
         points_diplo-=5
         
      if (team1_sum7_losses == team2_sum7_losses+1 and 'L' in team1_7th and 'D' in team2_7th and team1_sum6_wins==3 and team1_sum6_draws==2 and team1_sum6_losses==1 and team2_sum6_wins==4 and team2_sum6_draws==2 and team2_sum6_losses==0):
         print("Δεδομένη η νίκη της γηπεδούχου ομάδας {}.".format(team1_name))
         points_assos+=10
         points_draw+=6
         points_diplo-=3        
      
      if (team1_sum7_losses == team2_sum7_losses+1):
        print("---> Οι γηπεδούχοι {} έχουν μια ήττα παραπάνω! Πάει για νίκη!".format(team1_name))
        points_assos+=8
        points_draw+=6
        points_diplo-=3
        
        
    
      if (team1_sum7_losses == team2_sum7_losses):
        print("---> Ισάριθμες ήττες ({})! Μυρίζει Ισοπαλία!".format(team1_sum7_losses))
        points_draw+=10
        #points_assos-=2
        #points_diplo-=3  
    
      if (team2_sum7_losses == (team1_sum7_losses+1)):
        print("---> Οι φιλοξενούμενοι {} έχουν μια ήττα παραπάνω! Πάνε για θετικό αποτέλεσμα!".format(team2_name))
        points_diplo+=7
        points_draw+=4
        points_assos-=3    
   
      if (team1_sum6_losses == team2_sum6_losses+1 and 'L' in team1_7th):
        print("---> Οι γηπεδούχοι έχουν έχουν μια ήττα παραπάνω στα 6 & ΉΤΤΑ στο 7ο!!! Νίκη για {}.".format(team1_name))
        points_assos+=10
        points_draw+=5
        #points_diplo-=5
    
      if (team2_sum7_losses ==0 and team1_sum7_losses==1):
        print("---> Οι γηπεδούχοι έχουν έχουν μία ήττα μόνο. Οι φιλοξενούμενοι 0 ήττες! Η ομάδα {} πρέπει να κερδίσει!".format(team1_name))
        points_assos+=10
        points_draw+=5
        points_diplo-=5
    
      
      
      if (team1_sum7_losses ==0 and team2_sum7_losses==1):
        print("---> Οι γηπεδούχοι έχουν 0 ήττες. Οι φιλοξενούμενοι 1 ήττα! Δύσκολο ματς για τους γηπεδούχους.".format(team2_name))
        points_diplo+=7
        #points_draw+=4
        points_assos-=5      
   
      if (team1_sum6_wins==1 and team1_sum6_draws==1 and team1_sum6_losses==4 and team2_sum6_wins==1 and team2_sum6_draws==2 and team2_sum6_losses==3):
        print("---> Οι γηπεδούχοι έχουν 1-1-4 και οι φιλοξενούμενοι 1-2-3!!! Φουλ του άσσου για {}!!!".format(team1_name))
        points_assos+=10
        #points_draw+=3
        points_diplo-=5 
       

      if (team1_sum6_wins==1 and team1_sum6_draws==1 and team1_sum6_losses==4 and 'L' in team1_7th and team2_sum6_wins==1 and team2_sum6_draws==2 and team2_sum6_losses==3 and 'D' in team2_7th ):
        print("---> Οι γηπεδούχοι έχουν 1-1-4,ήττα στο 7ο, και οι φιλοξενούμενοι 123. Η ομάδα {} πάει για νίκη!!!".format(team1_name))
        points_assos+=10
        points_draw+=2
        #points_diplo-=3      
      elif (team1_sum6_wins==1 and team1_sum6_draws==1 and team1_sum6_losses==4 and 'L' in team1_7th):
        print("---> Οι γηπεδούχοι έχουν 1-1-4 & ήττα στο 7ο!!!!! Η ομάδα {} πάει για νίκη!!!".format(team1_name))
        points_assos+=6
        points_draw+=3
        points_diplo-=2
      
      if (team1_sum6_wins==3 and team1_sum6_draws==2 and team1_sum6_losses==1):
        print("---> Οι γηπεδούχοι έχουν 3-2-1 !!!  Αυξημένες πιθανότητες νίκης για την ομάδα {}." .format(team1_name))
        points_assos+=6
        points_draw+=3 
      if (team1_sum6_wins==3 and team1_sum6_draws==1 and team1_sum6_losses==2 and team2_sum6_wins==4 and team2_sum6_draws==1 and team2_sum6_losses==1 ):
        print("---> Οι γηπεδούχοι έχουν 3-1-2 και οι φιλοξενούμενοι 4-1-1 !!!  Άσσος αν δεν σπινιάρει ανάποδα!!!." )
        points_assos+=8
        points_draw+=3
        points_diplo-=2
      
      if (team1_sum6_wins==3 and team1_sum6_draws==1 and team1_sum6_losses==2):
        print("---> Οι γηπεδούχοι έχουν 3-1-2 !!!  Αυξημένες πιθανότητες νίκης για τους γηπεδούχους." )
        points_assos+=7
        points_draw+=4
        #points_diplo-=2             
       
      if (team2_sum6_wins==1 and team2_sum6_draws==1 and team2_sum6_losses==4):
        print("---> Οι φιλοξενούμενοι έχουν 1-1-4 !!! Προσοχή." )
        points_diplo+=2
        points_draw+=5
      
      if (team2_sum6_wins==4 and team2_sum6_draws==1 and team2_sum6_losses==1):
        print("---> Οι φιλοξενούμενοι έχουν 4-1-1 !!! " )
        points_assos+=1
        points_draw+=1
      
      if (team2_sum6_wins==1 and team2_sum6_draws==2 and team2_sum6_losses==3):
        print("---> Οι φιλοξενούμενοι έχουν 1-2-3!!! Θα τα βρούν σκούρα." )
        points_diplo-=8
        points_assos+=3
        #points_draw-=3

      
      
      if (team1_sum6_wins==0 ):
        print("---> Οι γηπεδούχοι έχουν 0 στις Νίκες!  Ίσως άσσος." )      
      if (team1_sum6_draws==0 ):
        print("---> Οι γηπεδούχοι έχουν 0 στις Ισοπαλίες!  Ίσως Χ." )
        points_draw+=3
      if (team1_sum6_losses==0 ):
        print("---> Οι γηπεδούχοι έχουν 0 στις Ήττες!  Ίσως 2πλό." )    
      if (team2_sum6_wins==0 ):
        print("---> Οι φιλοξενούμενοι έχουν 0 στις Νίκες!  Ίσως διπλό." )      
      if (team2_sum6_draws==0 ):
        print("---> Οι φιλοξενούμενοι έχουν 0 στις Ισοπαλίες!  Ίσως Χ." )
        points_draw+=3
      if (team2_sum6_losses==0 ):
        print("---> Οι φιλοξενούμενοι έχουν 0 στις Ήττες!  Ίσως άσσος." )
      
      
      
      
      if (team1_sum6_wins==0 and team1_sum6_draws==2 and team1_sum6_losses==4 and team2_sum6_wins==1 and team2_sum6_draws==2 and team2_sum6_losses==3 ):
        print("---> Κριτήριο βιβλίου!!!: Οι γηπεδούχοι έχουν  0-2-4 & οι φιλοξενούμενοι 1-2-3!!! Νίκη για {}.".format(team1_name))
        points_assos+=8
       
      
      if (team1_sum6_wins==3 and team1_sum6_draws==2 and team1_sum6_losses==1 and team2_sum6_wins==4 and team2_sum6_draws==2 and team2_sum6_losses==0 ):
        print("---> Κριτήριο βιβλίου!!!: Οι γηπεδούχοι έχουν 3-2-1 & οι φιλοξενούμενοι 4-2-0 ήττες!!!  {} will win." .format(team1_name))
        points_assos+=10
      
      if (team1_sum6_wins==4 and team1_sum6_draws==0 and team1_sum6_losses==2 and team2_sum6_wins==4 and team2_sum6_draws==0 and team2_sum6_losses==2 ):
        print("---> Κριτήριο βιβλίου!!!: Οι γηπεδούχοι έχουν 4-0-2 & οι φιλοξενούμενοι 4-0-2!!! ΙΣΟΠΑΛΙΑ.")
        points_draw+=8
        
          
      
      if (team1_sum5_wins==2 and team1_sum5_draws==2 and team1_sum5_losses==1):
            print("---> Φόρμα5 γηπεδούχων: 1X.")
            points_assos+=5
            points_draw+=5
      
      if (team2_sum5_wins==2 and team2_sum5_draws==2 and team2_sum5_losses==1):
            print("---> Φόρμα5 φιλοξενούμενων: 2Χ.")
            points_diplo+=4
            points_draw+=4
            #points_assos-=2        
      if (team1_sum5_wins==1 and team1_sum5_draws==2 and team1_sum5_losses==2):
            print("---> Φόρμα5 γηπεδούχων: Χ2.")
            points_diplo+=4
            points_draw+=4
            #points_assos-=2
      
      if (team2_sum5_wins==1 and team2_sum5_draws==2 and team2_sum5_losses==2):
            print("---> Φόρμα5 φιλοξενούμενων: 1X.")
            points_assos+=4
            points_draw+=4
            points_diplo-=2
          
      if (team1_sum5_wins==2 and team1_sum5_draws==1 and team1_sum5_losses==2):
            print("---> Η φόρμα5 γηπεδούχων: 12.")
            points_assos+=3
            points_diplo+=3
            points_draw-=2
      if (team2_sum5_wins==2 and team2_sum5_draws==1 and team2_sum5_losses==2):
            print("---> Η φόρμα5 φιλοξενούμενων: 12.")
            points_assos+=3
            points_diplo+=3
            points_draw-=2
        
        
      if (team2_sum6_wins==3 and team2_sum6_draws==1 and team2_sum6_losses==2):
            print("---> 3-1-2 για την ομάδα {}. Επικίνδυνο ματς, καλύτερα να το αποφύγουμε.".format(team2_name))
            points_diplo+=6
            points_draw+=3
                  
    
      if (team1_int_avg_scored>2 and team2_int_avg_scored<0.5 and team1_int_avg_conceded<0.5 and team2_int_avg_conceded>2):
            points_diplo-=7
            points_assos+=20
            points_draw-=4
            print("{}-{}. Οι γηπεδούχοι σκοράρουν κατα ριππάς και δέχoνται γκολ με το σταγονόμετρο!!! Οι φιλοξενούμενοι δεν σκοράρουν και δέχονται πάνω απο 2 σε κάθε ματς!!!!!".format(team1_name,team2_name)) 
        
      if (team1_int_avg_scored>2 and team2_int_avg_scored<0.6 and team1_int_avg_conceded<0.7 and team2_int_avg_conceded>1.7):
            print("{}-{}. Οι γηπεδούχοι σκοράρουν πάνω απο 2 γκολ σε κάθε ματς και δέχονται γκολ κάτω από 0.7. Οι φιλοξενούμενοι βάζουν γκολ <0.7 και δέχονται πάνω απο 2 σε κάθε ματς".format(team1_name,team2_name))
            points_diplo-=7
            points_assos+=15
            points_draw-=5
      
      
      if (team1_int_chance_to_score>69 and team2_int_chance_to_score<45 and team1_int_chance_to_concede<45 and team2_int_chance_to_concede>69):
            print("{}-{}. Οι γηπεδούχοι έχουν πάνω απο 69% να σκοράρουν στο προσεχές ματς και λιγότερο απο 45% να δεχτούν. Οι φιλοξενούμενοι δε σκοράρουν και δέχεται με ευκολία γκολ. Η γηπεδούχοι θα κερδίσουν!!!".format(team1_name,team2_name))
            points_diplo-=2
            points_assos+=7
            #points_draw-=2
      
      if (team1_int_chance_to_score<40 and team2_int_chance_to_score<40 and team1_int_chance_to_concede<40 and team2_int_chance_to_concede<40 and team1_last10_failtoscore_int>6 and team2_last10_failtoscore_int>6 and team1_last10_cleansheet_int>4 and team2_last10_cleansheet_int>4 and team1_int_avg_scored<1 and team2_int_avg_scored<1):
            print("{}-{}. ΔΕ ΘΑ ΜΠΕΙ ΓΚΟΛ !!!!!!".format(team1_name,team2_name))
            points_draw+=5
      if (team1_int_chance_to_score<50 and team2_int_chance_to_score<50 and team1_int_chance_to_concede<50 and team2_int_chance_to_concede<50 and team1_last10_failtoscore_int>5 and team2_last10_failtoscore_int>5 and team1_last10_cleansheet_int>5 and team2_last10_cleansheet_int>5 and team1_int_avg_scored<1 and team2_int_avg_scored<1):
            print("{}-{}. UNDERάκι !!!!!!".format(team1_name,team2_name))
            points_draw+=5
      
      
      if (team2_last10_failtoscore_int>5 and team1_last10_failtoscore_int<2 and team2_last10_cleansheet_int<3 and team2_last10_cleansheet_int>5 and team1_int_avg_scored>1.5 and team2_int_avg_scored<1):
            print("Γκολ: Οι γηπεδούχοι σκοράρουν ανελλειπώς, οι φιλοξενούμενοι έχουν δυστοκία! Άσσος!!!" )
            points_diplo-=6
            points_assos+=6
            points_draw-=2
      
      if (team1_last10_failtoscore_int>5 and team1_last10_cleansheet_int<2):
            print("Οι γηπεδούχοι έχουν σοβαρό πρόβλημα στο σκοράρισμα και τρώνε τουλάχιστον 1 γκολ σε κάθε ματς !!!")
            #points_diplo+=6
            points_assos-=7
            #points_draw+=2
      
      if (team2_last10_failtoscore_int>5 and team2_last10_cleansheet_int<2):
            print("Οι φιλοξενούμενοι έχουν σοβαρό πρόβλημα στο σκοράρισμα και τρώνε τουλάχιστον 1 γκολ σε κάθε ματς !!!")
            points_diplo-=7
            #points_assos+=4
                        
      
      if (team1_last10_failtoscore_int>5 and team1_last10_cleansheet_int<2 and team1_int_avg_scored<0.8  ):
            print("Οι γηπεδούχοι έχουν σοβαρό πρόβλημα στο σκοράρισμα και τρώνε τουλάχιστον γκολ !!!")
            #points_diplo+=6
            points_assos-=7
      
      
      #μ.ο γκολ στα τελευταια 10. συνθήκη πόσα βαζει η μια και ποσα τρώει η αλλη
      if (team1_int_avg_scored>1.9 and team2_int_avg_conceded>1.9 and team2_int_avg_scored<0.8 and team1_int_avg_conceded<0.9 and team1_last10_failtoscore_int<3 and team2_last10_cleansheet_int<3):
            points_diplo-=7
            points_assos+=10
            points_draw-=7
            print("Οι γηπεδούχοι ΣΚΟΡΑΡΟΥΝ ΠΑΝΩ απο 2 ΓΚΟΛ σε κάθε ματς ενώ οι φιλοξενούμενοι δέχονται τουλάχιστον 2 γκολ σε κάθε ματς. ΑΣΣΟΣ!!!")
      
      elif(team2_int_avg_scored>2.0 and team1_int_avg_conceded>2.0 and team1_int_avg_scored<0.8 and team2_int_avg_conceded<0.9 and team2_last10_failtoscore_int<3 and team1_last10_cleansheet_int<3):
            points_diplo+=8
            points_assos-=7
            points_draw-=2
            print("Οι γηπεδούχοι ΤΡΩΝΕ ΠΑΝΩ απο 2 ΓΚΟΛ σε κάθε ματς ενώ οι φιλοξενούμενοι ΣΚΟΡΑΡΟΥΝ τουλάχιστον 2 γκολ σε κάθε ματς. ΔΙΠΛΟ!!!")
      if (team1_int_avg_scored>1.5 and team2_int_avg_conceded >1.6 and team2_int_avg_scored<0.9 and team1_int_avg_conceded<0.8 and team1_last10_failtoscore_int<4 and team2_last10_cleansheet_int<4):
            points_diplo-=7
            points_assos+=10
            points_draw-=4
            print("Οι γηπεδούχοι σκοράρουν αρκετά (>1.5) και αμύνονται καλά (<0.8). Οι φιλοξενούμενοι μπορούν να δεχτούν τα γκολ αυτά ενώ δύσκολα θα βρουν κενά στην άμυνα των γηπεδούχων. Άσσος.")
      elif (team2_int_avg_scored>1.5 and team1_int_avg_conceded >1.6 and team1_int_avg_scored<0.9 and team2_int_avg_conceded<0.8 and team2_last10_failtoscore_int<4 and team1_last10_cleansheet_int<4):
            points_diplo+=10
            points_assos-=7
            points_draw+=2
            print("Οι φιλοξενούμενοι σκοράρουν αρκετά (>1.5) και αμύνονται καλά (<0.8). Οι γηπεδούχοι μπορούν να δεχτούν τα γκολ αυτά ενώ δύσκολα θα βρουν κενά στην άμυνα των φιλοξενούμενων. Γέρνει στο Διπλό.")
      
      #Συνθήκη για το αν οι ομάδες σκοράρουν με τον ίδιο ρυθμό.
      if (team1_int_avg_scored== team2_int_avg_scored + 0.1 or team1_int_avg_scored== team2_int_avg_scored - 0.2 or team1_int_avg_scored== team2_int_avg_scored - 0.1 or team1_int_avg_scored== team2_int_avg_scored - 0.2):
            print("Οι 2 ομάδες σκοράρουν σχεδόν με τον ίδιο ρυθμό.")
            points_draw+=5
            same_scoring_avg=True
            if (team1_int_avg_conceded== team2_int_avg_conceded + 0.1 or team1_int_avg_conceded== team2_int_avg_conceded - 0.2 or team1_int_avg_conceded== team2_int_avg_conceded - 0.1 or team1_int_avg_conceded== team2_int_avg_conceded - 0.2):
                  print("Οι 2 ομάδες δέχονται γκολ σχεδόν με τον ίδιο ρυθμό.")
                  points_draw+=5
                  same_conceding_avg=True
                  if (same_scoring_avg==True and same_conceding_avg==True):
                        print("Οι ομάδες τρώνε και βάζουν τα ίδια γκολ. ΙΣΟΠΑΛΙΑ εν όψει.")
                        points_draw+=6
      if(team1_int_avg_scored== team2_int_avg_scored + 0.1 or team1_int_avg_scored== team2_int_avg_scored - 0.2 or team1_int_avg_scored== team2_int_avg_scored - 0.1 or team1_int_avg_scored== team2_int_avg_scored - 0.2 and team1_int_avg_conceded== team2_int_avg_conceded + 0.1 or team1_int_avg_conceded== team2_int_avg_conceded - 0.2 or team1_int_avg_conceded== team2_int_avg_conceded - 0.1 or team1_int_avg_conceded== team2_int_avg_conceded - 0.2):
            print("Οι ομάδες ΣΚΟΡΑΡΟΥΝ και δέχονται με τον ίδιο ρυθμό")
            points_draw+=10
      if (team1_int_avg_scored>team2_int_avg_scored+0.8):
            print("Προσοχή οι γηπεδούχοι σκοράρουν σχεδόν 1 γκολ ΠΑΡΑΠΑΝΩ από τους φιλοξενούμενος. Προβάδισμα στον Άσσο.")
            points_assos+=8
            points_diplo-=3
            
      elif (team2_int_avg_scored>team1_int_avg_scored+0.8):
            print("Προσοχή οι φιλοξενούμενοι σκοράρουν σχεδόν 1 γκολ ΠΑΡΑΠΑΝΩ από τους γηπεδούχους. Προβάδισμα στο Χ2")
            points_diplo+=8
            points_draw+=3
            points_assos-=4
      
      if (team1_int_avg_conceded>team2_int_avg_conceded+0.7):
            print("Προσοχή οι γηπεδούχοι ΤΡΩΝΕ σχεδόν 1 γκολ ΠΑΡΑΠΑΝΩ από τους φιλοξενούμενους.Προβάδισμα στον Χ2.")
            points_diplo+=5
            points_assos-=5
      elif (team2_int_avg_conceded>team1_int_avg_conceded+0.7):
            print("Προσοχή οι φιλοξενούμενοι ΤΡΩΝΕ σχεδόν 1 γκολ ΠΑΡΑΠΑΝΩ από τους γηπεδούχους. Προβάδισμα στο ΑΣΣΟ.")
            points_diplo-=5
            points_assos+=10
            #points_draw+=2
      
      if(team1_last10_cleansheet_int>5):
            print("--> Οι γηπεδούχοι ΑΜΥΝΟΝΤΑΙ καλά. Πάνω από 5 Clean Sheets στα 10 τελευταία ματς.")
            points_assos+=7
            points_draw+=7
            points_diplo-=2
      if(team2_last10_cleansheet_int>5):
            print("--> Οι φιλοξενούμενοι ΑΜΥΝΟΝΤΑΙ καλά. Πάνω από 5 Clean Sheets στα 10 τελευταία ματς.")
            points_assos-=5
            points_draw+=5
            points_diplo+=5
      if(team1_last10_failtoscore_int>5):
            print("--> Προσοχή: Fail2Sore, οι γηπεδούχοι ΑΠΕΤΥΧΑΝ να σκοράρουν σε πάνω από 5/10 ματς!!! ΔΕΝ ΒΑΖΟΥΝ ΓΚΟΛ..")
            points_assos-=8
            points_diplo+=5
            #points_draw+=2
                        
      if(team2_last10_failtoscore_int>5):
            points_diplo-=5
            points_assos+=5

            print("--> Προσοχή: Fail2Sore, οι φιλοξενούμενοι ΑΠΕΤΥΧΑΝ να σκοράρουν σε πάνω από 5/10 ματς!!! ΔΕΝ ΒΑΖΟΥΝ ΓΚΟΛ..")
      if (team1_int_chance_to_score>69 and team2_int_chance_to_score>69 and team1_int_chance_to_concede>65 and team2_int_chance_to_concede>65 and team1_last10_failtoscore_int<3 and team2_last10_failtoscore_int<3 and team1_last10_cleansheet_int<3 and team2_last10_cleansheet_int<3 and team1_int_avg_scored>2 and team2_int_avg_scored>1.5):
            print("{}-{}. Το παιχνίδι είναι BTTS και OVER !!!!!!".format(team1_name,team2_name))
            points_draw-=10
            #points_assos+=5
            #points_diplo+=5      
      
      if(team1_last10_failtoscore_int<3 and team1_last10_cleansheet_int>5 and team1_int_avg_scored>1.6 and team1_int_avg_scored<0.8):
            print("Οι γηπεδούχοι βρίσκονται σε άριστη κατάσταση!!! Αξίζουν εμπιστοσύνη. Άσσος.")
            points_assos+=12
            points_diplo-=3
            points_draw+=3
      if(team2_last10_failtoscore_int<3 and team2_last10_cleansheet_int>5 and team2_int_avg_scored>1.6 and team2_int_avg_scored<0.8):
            print("Οι Φιλοξενούμενοι βρίσκονται σε άριστη κατάσταση!!! Αξίζουν εμπιστοσύνη. Διπλό.")
            points_diplo+=10
            points_assos-=4
            points_draw+=3
      
      if(team1_last10_cleansheet_int>5 and team2_last10_cleansheet_int<3 and team1_last10_failtoscore_int<3 and team2_last10_failtoscore_int>4):
            print("CleanSheet & Fail2Sore, μεγάλες διαφορές ΥΠΕΡ των Γηπεδούχων. ΆΣΣΟΣ")
            points_diplo-=10
            points_diplo+=13
      if(team1_last10_draws_int>50 and team2_last10_draws_int>50):
            points_draw+=8
            print("Οι ομάδες έχουν περισσότερες από 5 ΙΣΟΠΑΛΙΕΣ στα τελευταία 10 παιχνίδια.ΙΣΟΠΑΛΙΟΛΑΓΝΕΣ!!!!")


      print("")
      print("ΑΣΣΟΣ:{}p,          ΙΣΟΠΑΛΙΑ:{}p,          ΔΙΠΛΟ:{}p".format(points_assos,points_draw,points_diplo))
      print("")
      if(points_assos>19 and points_draw<6 and points_diplo<0):
            print("Πρόβλεψη: ΑΣΣΟΣ")
      elif(points_assos<=0 and points_draw>15 and points_diplo>10):
              print("Πρόβλεψη: Χ2")
      elif(points_assos<=0 and points_draw>19 and points_diplo<=0):
              print("Πρόβλεψη: ΙΣΟΠΑΛΙΑ !!!!!!")
      elif(points_assos>23 and points_draw>20 and points_diplo<0):
              print("Πρόβλεψη: 1X για στάνταρ!!!!")
      elif(points_assos<0 and points_draw<8 and points_diplo>18):
              print("Πρόβλεψη: ΔΙΠΛΟοοοοοο")
      elif(points_assos<9 and points_draw>29 and points_diplo<=0):
              print("Πρόβλεψη: ΙΣΟΠΑΛΙΑ κατά μεγάλο Ποσοστό")
      elif(points_assos>29 and points_draw<5 and points_diplo<=0):
              print("Πρόβλεψη: ΑΣΣΟΣ καρφωτός!!! Μπορεί και στάνταρ 1Χ")
      elif(points_assos>15 and points_draw>15 and points_diplo<=0):
              print("Πρόβλεψη: 1Χ καλό.")
      elif(points_assos<=0 and points_draw>20 and points_diplo>20):
              print("X2 καρφωτό!!!")
      print("")
      
      print("###########*###################################*#######################################*##############################*##########################*############")    


