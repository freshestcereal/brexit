#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:50:01 2018

@author: ianwmcdaniel
"""

import re
import pandas as pd
brexit = pd.read_csv('brex_sample_fixed.csv', keep_default_na=False)
pd.set_option('display.max_colwidth', -1)
date = pd.to_datetime(brexit['tweet_created_at']).astype(str) #changing date format
date = date.str[:10] #limiting date to essential characters
brexit = brexit.assign(date = date) #adding date column to datasheet
tweets = brexit['tweet_text'].str.lower() 
#collecting the top 10 hashtags
ht = tweets.str.findall('\#[a-z0-9\_]+', re.IGNORECASE) 
ht_NB = ht[ht.str.len() > 0]
ht_NB_list = [i for j in ht_NB.tolist() for i in j]
ht_NB_pd = pd.Series(ht_NB_list)
ht_NB_pd.value_counts()[:10].to_csv('top_10_ht.csv',header=['Top 10 Hashtags'])
#collecting the top 10 mentions
men = tweets.str.findall('\@[a-z0-9\_]+', re.IGNORECASE)
men_NB = men[men.str.len() > 0]
men_NB_list = [i for j in men_NB.tolist() for i in j]
men_NB_pd = pd.Series(men_NB_list)
men_NB_pd.value_counts()[:10].to_csv('top_10_men.csv',header=['Top 10 Mentions'])
#top 10 hashtags and their dates begin below
brx = brexit[brexit['tweet_text'].str.contains('#brexit\\b',case=False)]
brx['date'].value_counts().to_csv('brexit_ht_dates.csv',header=['#brexit Dates'])
euref = brexit[brexit['tweet_text'].str.contains('#euref\\b',case=False)]
euref['date'].value_counts().to_csv('euref_ht_dates.csv',header=['#euref Dates'])     
voteleave = brexit[brexit['tweet_text'].str.contains('#voteleave\\b',case=False)]
voteleave['date'].value_counts().to_csv('voteleave_ht_dates.csv',header=['#voteleave Dates'])   
eu = brexit[brexit['tweet_text'].str.contains('#eu\\b',case=False)]
eu['date'].value_counts().to_csv('eu_ht_dates.csv',header=['#eu Dates'])   
remain = brexit[brexit['tweet_text'].str.contains('#remain\\b',case=False)]
remain['date'].value_counts().to_csv('remain_ht_dates.csv',header=['#remain Dates'])   
uk = brexit[brexit['tweet_text'].str.contains('#uk\\b',case=False)]
uk['date'].value_counts().to_csv('uk_ht_dates.csv',header=['#uk Dates'])   
strongerin = brexit[brexit['tweet_text'].str.contains('#strongerin\\b',case=False)]
strongerin['date'].value_counts().to_csv('strongerin_ht_dates.csv',header=['#strongerin Dates'])  
leaveeu = brexit[brexit['tweet_text'].str.contains('#leaveeu\\b',case=False)]
leaveeu['date'].value_counts().to_csv('leaveeu_ht_dates.csv',header=['#leaveeu Dates'])   
leave = brexit[brexit['tweet_text'].str.contains('#leave\\b',case=False)]
leave['date'].value_counts().to_csv('leave_ht_dates.csv',header=['#leave Dates'])   
eureferendum = brexit[brexit['tweet_text'].str.contains('#eureferendum\\b',case=False)]
eureferendum['date'].value_counts().to_csv('eureferendum_ht_dates.csv',header=['#eureferendum Dates'])
#top 5 mentions and their dates         
trump = brexit[brexit['tweet_text'].str.contains('@realdonaldtrump\\b',case=False)]
trump['date'].value_counts().to_csv('trump_men_dates.csv',header=['@realdonaldtrump Mentions'])
independent = brexit[brexit['tweet_text'].str.contains('@independent\\b',case=False)]
independent['date'].value_counts().to_csv('independent_men_dates.csv',header=['@independent Mentions'])
guardian = brexit[brexit['tweet_text'].str.contains('@guardian\\b',case=False)]
guardian['date'].value_counts().to_csv('guardian_men_dates.csv',header=['@guardian Mentions'])
business = brexit[brexit['tweet_text'].str.contains('@business\\b',case=False)]
business['date'].value_counts().to_csv('business_men_dates.csv',header=['@business Mentions'])
farage = brexit[brexit['tweet_text'].str.contains('@nigel_farage\\b',case=False)]
farage['date'].value_counts().to_csv('farage_men_dates.csv',header=['@nigel_farage Mentions'])
#setting up locations
uk = ['london','london, england','england, united kingdom','\\buk\\b', 'united kingdom','england','london, uk','scotland','edinburgh','sheffield','liverpool','leeds','glasgow','scotland, united kingdom','south west, england','west yorkshire','sheffield, england','essex','north yorkshire','south east, england','wales','cardiff, wales','city of london, london','\\bu\.k\.\\b','cambridge, england','hackney, london','newcastle upon tyne','cardiff','newcastle upon tyne, england','edinburgh, scotland','manchester, uk','hampshire','manchester','nottingham','oxford, uk','glasgow, scotland','manchester, england','north west, england','salford, uk','cornwall','bristol','nottingham, uk','westminster, london','hull, england','engand','thornton in bradforddale, uk','high wycombe','nottingham, england','london, united kingdom','yorkshire','bristol, england','belfast, northern ireland','birmingham, england','birmingham','wales, united kingdom','great britain','belfast','west midlands, england','oxford','leeds, england','liverpool, england','kent','cambridge','oxford, england','bristol, uk','brighton','east midlands, england','north east, england','northern ireland','surrey','birmingham, uk','cheshire','north east england','staffordshire','norwich, england','cambridge, uk','southampton, england','leicester, england','east, england','blackpool','uk.','oxfordshire','gibraltar','york, england','buckinghamshire','coningsby, lincs','leicester','sussex','isle of man','aberdeen, scotland','england, great britain.','england, uk','derbyshire','plymouth','west yorkshire','hertfordshire']
uk = "|".join(uk)
eu = ['europe','paris','paris, france','france','italia','españa','madrid','ireland','roma','dublin','the netherlands','madrid, comunidad de madrid','brussels, belgium','deutschland','dublin, ireland','warszawa, polska','berlin','paris, ile-de-france','italy','dublin city, ireland','greece','madrid, spain','germany','brussels','barcelona','nederland','amsterdam','berlin, germany','european union','spain','sweden','milano','geneva, switzerland','athens, greece','berlin, deutschland','madrid, españa','netherlands','stockholm, sweden','milano, lombardia','portugal','athens','stockholm','\\beu\\b','rome, lazio','belgium','finland','helsinki, finland','hamburg','switzerland','luxembourg','cyprus','bruxelles','catalunya','polska','norway','europa','amsterdam, the netherlands','barcelona, españa','rome, italy','stockholm, sverige','ile-de-france, france','barcelona, spain','rotterdam','oslo, norway','milan, italy','zurich, switzerland','lyon, france','vienna, austria','sverige']
eu = "|".join(eu)
ru = ['россия','москва, россия','москва']
ru = "|".join(ru)
na = ['united states', '\\busa\\b','new york, ny','new york','canada','new york city','toronto','denver, co','washington, dc','chicago, il','houston, tx','méxico','los angeles, ca','new york, usa','california, usa','toronto, ontario','mexico','san francisco, ca','florida, usa','nyc','california','boston, ma','texas, usa','los angeles','texas','atlanta, ga','washington, d.c.','seattle, wa','chicago','miami, fl','brooklyn, ny','washington dc','austin, tx','san francisco','philadelphia, pa','manhattan, ny','san diego, ca','mexico city','dallas, tx','arizona, usa','toronto, canada','new jersey, usa','florida','ontario, canada','ciudad de méxico','north carolina, usa','alabama, usa','portland, or','seattle','miami','pennsylvania, usa','tampa, fl','denver, co','boston','united states of america','michigan, usa','colorado, usa','phoenix, az','massachusetts, usa','las vegas, nv','nashville, tn','vancouver, british columbia','georgia, usa','arlington, tx','maryland, usa','dominican republic']
na = "|".join(na)
world = ['worldwide','global','earth','world','planet earth','everywhere','the world','here','international']
world = "|".join(world)
asia = ['new delhi, india','hong kong','singapore','japan','indonesia','tokyo','mumbai, india','jakarta','mumbai','pakistan','malaysia','new delhi','bangladesh','bangkok, thailand','thailand','istanbul','bengaluru, india','dhaka, bangladesh','philippines','tokyo','jakarta, indonesia','bangalore','i̇stanbul, türkiye','lahore, pakistan','dubai, united arab emirates','dubai']
asia = "|".join(asia)
oceania = ['sydney, new south wales','melbourne','australia','sydney','sydney, australia','melbourne, australia','melbourne, victoria','new zealand','auckland, new zealand','perth, western australia']
oceania = "|".join(oceania)
africa = ['nigeria','lagos, nigeria','nairobi, kenya','south africa','lagos','johannesburg, south africa','cape town, south africa','egypt','nairobi','africa']
africa = "|".join(africa)
sa = ['venezuela','argentina','chile','brasil','caracas, venezuela','santiago, chile','buenos aires, argentina','colombia','buenos aires','ecuador','são paulo, brasil','bogotá, d.c., colombia','santiago de chile']
sa = "|".join(sa)
#as you suggested, determining the RT rate of the regions
retweets = brexit[brexit['tweet_text'].str.contains('rt @',case=False)]
uk_rt_num = len(retweets[retweets['location'].str.contains(uk,case=False)])
eu_rt_num = len(retweets[retweets['location'].str.contains(eu,case=False)])
ru_rt_num = len(retweets[retweets['location'].str.contains(ru,case=False)])
na_rt_num = len(retweets[retweets['location'].str.contains(na,case=False)])
world_rt_num = len(retweets[retweets['location'].str.contains(world,case=False)])
asia_rt_num = len(retweets[retweets['location'].str.contains(asia,case=False)])
oceania_rt_num = len(retweets[retweets['location'].str.contains(oceania,case=False)])
africa_rt_num = len(retweets[retweets['location'].str.contains(africa,case=False)])
sa_rt_num = len(retweets[retweets['location'].str.contains(sa,case=False)])
retweets_denom = (uk_rt_num + eu_rt_num + ru_rt_num + na_rt_num + world_rt_num + asia_rt_num + oceania_rt_num + africa_rt_num + sa_rt_num)
uk_rt_pct = uk_rt_num / retweets_denom
eu_rt_pct = eu_rt_num / retweets_denom
ru_rt_pct = ru_rt_num / retweets_denom
na_rt_pct = na_rt_num / retweets_denom
world_rt_pct = world_rt_num / retweets_denom
asia_rt_pct = asia_rt_num / retweets_denom
oceania_rt_pct = oceania_rt_num / retweets_denom
africa_rt_pct = africa_rt_num / retweets_denom
sa_rt_pct = sa_rt_num / retweets_denom


#breaking the United Kingdom down into its 4 constituent countries + London
england = ['london','london, england','england, united kingdom','england','london, uk','sheffield','liverpool','leeds','south west, england','west yorkshire','sheffield, england','essex','north yorkshire','south east, england','city of london, london','cambridge, england','hackney, london','newcastle upon tyne','newcastle upon tyne, england','manchester, uk','hampshire','manchester','nottingham','oxford, uk','manchester, england','north west, england','salford, uk','cornwall','bristol','nottingham, uk','westminster, london','hull, england','engand','thornton in bradforddale, uk','high wycombe','nottingham, england','london, united kingdom','yorkshire','bristol, england','birmingham, england','birmingham','west midlands, england','oxford','leeds, england','liverpool, england','kent','cambridge','oxford, england','bristol, uk','brighton','east midlands, england','north east, england','surrey','birmingham, uk','cheshire','north east england','staffordshire','norwich, england','cambridge, uk','southampton, england','leicester, england','east, england','blackpool','oxfordshire','york, england','buckinghamshire','coningsby, lincs','leicester','sussex','england, great britain.','england, uk','derbyshire','plymouth','west yorkshire','hertfordshire']
england = '|'.join(england)
scotland = ['scotland','edinburgh','glasgow','scotland, united kingdom','glasgow, scotland','edinburgh, scotland','aberdeen, scotland','scotland, uk']
scotland = '|'.join(scotland)
wales = ['wales','cardiff, wales','cardiff','wales, united kingdom','swansea','swansea, wales','wales, uk']
wales = '|'.join(wales)
nireland = ['belfast, northern ireland','belfast','northern ireland','northern ireland, united kingdom','northern ireland, uk']
nireland = '|'.join(nireland)
london = ['london','london, england','london, uk','city of london, london','hackney, london','westminster, london','london, united kingdom']
london = '|'.join(london)

#As you suggested, since I decided to break the UK down, looking at the screen name uniqueness of hashtags tweeted
eng_vl_total = len(voteleave[voteleave['location'].str.contains(england,case=False)])
eng_vl_unique = len(set(voteleave[voteleave['location'].str.contains(england,case=False)]['screen_name']))
scot_vl_total = len(voteleave[voteleave['location'].str.contains(scotland,case=False)])
scot_vl_unique = len(set(voteleave[voteleave['location'].str.contains(scotland,case=False)]['screen_name']))
wales_vl_total = len(voteleave[voteleave['location'].str.contains(wales,case=False)])
wales_vl_unique = len(set(voteleave[voteleave['location'].str.contains(wales,case=False)]['screen_name']))
ni_vl_total = len(voteleave[voteleave['location'].str.contains(nireland,case=False)])
ni_vl_unique = len(set(voteleave[voteleave['location'].str.contains(nireland,case=False)]['screen_name']))
london_vl_total = len(voteleave[voteleave['location'].str.contains(london,case=False)])
london_vl_unique = len(set(voteleave[voteleave['location'].str.contains(london,case=False)]['screen_name']))

eng_r_total = len(remain[remain['location'].str.contains(england,case=False)])
eng_r_unique = len(set(remain[remain['location'].str.contains(england,case=False)]['screen_name']))
scot_r_total = len(remain[remain['location'].str.contains(scotland,case=False)])
scot_r_unique = len(set(remain[remain['location'].str.contains(scotland,case=False)]['screen_name']))
wales_r_total = len(remain[remain['location'].str.contains(wales,case=False)])
wales_r_unique = len(set(remain[remain['location'].str.contains(wales,case=False)]['screen_name']))
ni_r_total = len(remain[remain['location'].str.contains(nireland,case=False)])
ni_r_unique = len(set(remain[remain['location'].str.contains(nireland,case=False)]['screen_name']))
london_r_total = len(remain[remain['location'].str.contains(london,case=False)])
london_r_unique = len(set(remain[remain['location'].str.contains(london,case=False)]['screen_name']))

eng_si_total = len(strongerin[strongerin['location'].str.contains(england,case=False)])
eng_si_unique = len(set(strongerin[strongerin['location'].str.contains(england,case=False)]['screen_name']))
scot_si_total = len(strongerin[strongerin['location'].str.contains(scotland,case=False)])
scot_si_unique = len(set(strongerin[strongerin['location'].str.contains(scotland,case=False)]['screen_name']))
wales_si_total = len(strongerin[strongerin['location'].str.contains(wales,case=False)])
wales_si_unique = len(set(strongerin[strongerin['location'].str.contains(wales,case=False)]['screen_name']))
ni_si_total = len(strongerin[strongerin['location'].str.contains(nireland,case=False)])
ni_si_unique = len(set(strongerin[strongerin['location'].str.contains(nireland,case=False)]['screen_name']))
london_si_total = len(strongerin[strongerin['location'].str.contains(london,case=False)])
london_si_unique = len(set(strongerin[strongerin['location'].str.contains(london,case=False)]['screen_name']))

eng_le_total = len(leaveeu[leaveeu['location'].str.contains(england,case=False)])
eng_le_unique = len(set(leaveeu[leaveeu['location'].str.contains(england,case=False)]['screen_name']))
scot_le_total = len(leaveeu[leaveeu['location'].str.contains(scotland,case=False)])
scot_le_unique = len(set(leaveeu[leaveeu['location'].str.contains(scotland,case=False)]['screen_name']))
wales_le_total = len(leaveeu[leaveeu['location'].str.contains(wales,case=False)])
wales_le_unique = len(set(leaveeu[leaveeu['location'].str.contains(wales,case=False)]['screen_name']))
ni_le_total = len(leaveeu[leaveeu['location'].str.contains(nireland,case=False)])
ni_le_unique = len(set(leaveeu[leaveeu['location'].str.contains(nireland,case=False)]['screen_name']))
london_le_total = len(leaveeu[leaveeu['location'].str.contains(london,case=False)])
london_le_unique = len(set(leaveeu[leaveeu['location'].str.contains(london,case=False)]['screen_name']))

eng_l_total = len(leave[leave['location'].str.contains(england,case=False)])
eng_l_unique = len(set(leave[leave['location'].str.contains(england,case=False)]['screen_name']))
scot_l_total = len(leave[leave['location'].str.contains(scotland,case=False)])
scot_l_unique = len(set(leave[leave['location'].str.contains(scotland,case=False)]['screen_name']))
wales_l_total = len(leave[leave['location'].str.contains(wales,case=False)])
wales_l_unique = len(set(leave[leave['location'].str.contains(wales,case=False)]['screen_name']))
ni_l_total = len(leave[leave['location'].str.contains(nireland,case=False)])
ni_l_unique = len(set(leave[leave['location'].str.contains(nireland,case=False)]['screen_name']))
london_l_total = len(leave[leave['location'].str.contains(london,case=False)])
london_l_unique = len(set(leave[leave['location'].str.contains(london,case=False)]['screen_name']))

l_ht_uniq = ((eng_vl_unique + scot_vl_unique + wales_vl_unique + ni_vl_unique + london_vl_unique + eng_le_unique + scot_le_unique + wales_le_unique + ni_le_unique + london_le_unique + eng_l_unique + scot_l_unique + wales_l_unique + ni_l_unique + london_l_unique) / (eng_vl_total + scot_vl_total + wales_vl_total + ni_vl_total + london_vl_total + eng_le_total + scot_le_total + wales_le_total + ni_le_total + london_le_total + eng_l_total + scot_l_total + wales_l_total + ni_l_total + london_l_total) * 100)

r_ht_uniq = ((eng_r_unique + scot_r_unique + wales_r_unique + ni_r_unique + london_r_unique + eng_si_unique + scot_si_unique + wales_si_unique + ni_si_unique + london_si_unique) / (eng_r_total + scot_r_total + wales_r_total + ni_r_total + london_r_total + eng_si_total + scot_si_total + wales_si_total + ni_si_total + london_si_total) * 100)

locations = brexit['location'].str.lower()
all_locations = locations.str.findall('[\w\W\s]+', re.IGNORECASE) 
all_locations_NB = all_locations[all_locations.str.len() > 0]
all_locations_NB_list = [i for j in all_locations_NB.tolist() for i in j]
all_locations_NB_pd = pd.Series(all_locations_NB_list)
total_hashtags = len(ht_NB_pd)
unique_hashtags = len(set(ht_NB_pd))
total_locations = len(all_locations_NB_pd)
unique_locations = len(set(all_locations_NB_pd))

#determining top 10 hashtags among the top 10% of users by follower count
top_quant = brexit['followers_count'].quantile(.9)
brexit_quant = brexit[brexit['followers_count'] >= top_quant]['tweet_text'].str.lower()
ht_quant = brexit_quant.str.findall('\#[a-z0-9\_]+', re.IGNORECASE)
ht_quant_NB = ht_quant[ht_quant.str.len() > 0]
ht_quant_NB_list = [i for j in ht_quant_NB.tolist() for i in j]
ht_quant_NB_pd = pd.Series(ht_quant_NB_list)
ht_quant_NB_pd.value_counts()[:10].to_csv('top_10_ht_fc_count.csv',header=['Top 10 Hashtags Among the Top 10% of Users by Folower Count'])

print('The #brexit Twitter data set has been loaded.')
print('The top 10 hashtags were:\n',ht_NB_pd.value_counts()[:10])
print('The top 10 mentions were:\n',men_NB_pd.value_counts()[:10])
print('The top 10 hashtags among users in the top 10% of follower counts were:\n',ht_quant_NB_pd.value_counts()[:10])
print('The retweet percentage of the UK was',str(uk_rt_pct)+'%.')
print('The retweet percentage of the EU was',str(eu_rt_pct)+'%.')
print('The retweet percentage of Russia was',str(ru_rt_pct)+'%.')
print('The retweet percentage of North America was',str(na_rt_pct)+'%.')
print('The retweet percentage of vague locations was',str(world_rt_pct)+'%.')
print('The retweet percentage of Asia was',str(asia_rt_pct)+'%.')
print('The retweet percentage of Oceania was',str(oceania_rt_pct)+'%.')
print('The retweet percentage of Africa was',str(africa_rt_pct)+'%.')
print('The retweet percentage of South America was',str(sa_rt_pct)+'%.')

print('Spreadsheets detailing the day-by-day count of the top 10 hashtags and the top 5 mentions have been created and saved.')
propensity = input('Would you like to know how remain- and stay-related hashtags would have translated into vote percentages in the UK by region? (Y/N): ')
if propensity.lower() == 'y':
    print('Based on hashtag propensity, England would have been tipped to leave the EU with',str((eng_vl_total + eng_le_total + eng_l_total) / (eng_vl_total + eng_le_total + eng_l_total + eng_si_total + eng_r_total) * 100)+'% of the vote.')
    print('Based on hashtag propensity, Scotland would have been tipped to leave the EU with',str((scot_vl_total + scot_le_total + scot_l_total) / (scot_vl_total + scot_le_total + scot_l_total + scot_si_total + scot_r_total) * 100)+'% of the vote.')
    print('Based on hashtag propensity, Wales would have been tipped to leave the EU with',str((wales_vl_total + wales_le_total + wales_l_total) / (wales_vl_total + wales_le_total + wales_l_total + wales_si_total + wales_r_total) * 100)+'% of the vote.')
    print('Based on hashtag propensity, Northern Ireland would have been tipped to leave the EU with',str((ni_vl_total + ni_le_total + ni_l_total) / (ni_vl_total + ni_le_total + ni_l_total + ni_si_total + ni_r_total) * 100)+'% of the vote.')
    print('Based on hashtag propensity, London would have been tipped to leave the EU with',str((london_vl_total + london_le_total + london_l_total) / (london_vl_total + london_le_total + london_l_total + london_si_total + london_r_total) * 100)+'% of the vote.')
else:
    print('Ok.')
uniqueness = input('Would you like to know about the screen name uniqueness of those used to calculate the propensity/vote? (Y/N): ')
if uniqueness.lower() == 'y':
    print('The screen name uniqueness of #voteleave was:',str(eng_vl_unique / eng_vl_total * 100)+'% in England;',str(scot_vl_unique / scot_vl_total * 100)+'% in Scotland;',str(wales_vl_unique / wales_vl_total * 100)+'% in Wales;',str(ni_vl_unique / ni_vl_total * 100)+'% in Northern Ireland; and',str(london_vl_unique / london_vl_total * 100)+'% in London.')
    print('The screen name uniqueness of #remain was:',str(eng_r_unique / eng_r_total * 100)+'% in England;',str(scot_r_unique / scot_r_total * 100)+'% in Scotland;',str(wales_r_unique / wales_r_total * 100)+'% in Wales;',str(ni_r_unique / ni_r_total * 100)+'% in Northern Ireland; and',str(london_r_unique / london_r_total * 100)+'% in London.')
    print('The screen name uniqueness of #strongerin was:',str(eng_si_unique / eng_si_total * 100)+'% in England;',str(scot_si_unique / scot_si_total * 100)+'% in Scotland;',str(wales_si_unique / wales_si_total * 100)+'% in Wales;',str(ni_si_unique / ni_si_total * 100)+'% in Northern Ireland; and',str(london_si_unique / london_si_total * 100)+'% in London.')
    print('The screen name uniqueness of #leaveu was:',str(eng_le_unique / eng_le_total * 100)+'% in England;',str(scot_le_unique / scot_le_total * 100)+'% in Scotland;',str(wales_le_unique / wales_le_total * 100)+'% in Wales;',str(ni_le_unique / ni_le_total * 100)+'% in Northern Ireland; and',str(london_le_unique / london_le_total * 100)+'% in London.')
    print('The screen name uniqueness of #leave was:',str(eng_l_unique / eng_l_total * 100)+'% in England;',str(scot_l_unique / scot_l_total * 100)+'% in Scotland;',str(wales_l_unique / wales_l_total * 100)+'% in Wales;',str(ni_l_unique / ni_l_total * 100)+'% in Northern Ireland; and',str(london_l_unique / london_l_total * 100)+'% in London.')
    print('Collectively, the leave-related hashtags had a',str(l_ht_uniq)+'% screen name uniqueness rate compared to',str(r_ht_uniq)+'% among the remain-related hashtags.')
else:
    print('Ok.')
print('The #brexit Twitter dataset contains dates ranging between', brexit['date'].min(),'and',str(brexit['date'].max())+'.')
user_date = input('Please enter a date in YYYY-MM-DD format: ')
hashtags = brexit[brexit['date'] == user_date]['tweet_text'].str.lower()
user_ht = hashtags.str.findall('\#[a-z0-9\_]+', re.IGNORECASE)
user_ht_NB = user_ht[user_ht.str.len() > 0]
user_ht_NB_list = [i for j in user_ht_NB.tolist() for i in j]
user_ht_NB_pd = pd.Series(user_ht_NB_list)
mentions = brexit[brexit['date'] == user_date]['tweet_text'].str.lower()
user_men = mentions.str.findall('\@[a-z0-9\_]+', re.IGNORECASE)
user_men_NB = user_men[user_men.str.len() > 0]
user_men_NB_list = [i for j in user_men_NB.tolist() for i in j]
user_men_NB_pd = pd.Series(user_men_NB_list)
locations = brexit[brexit['date'] == user_date]['location'].str.lower()
user_loc = locations.str.findall('[\w\W\s]+', re.IGNORECASE)
user_loc_NB = user_loc[user_loc.str.len() >0]
user_loc_NB_list = [i for j in user_loc_NB.tolist() for i in j]
user_loc_NB_pd = pd.Series(user_loc_NB_list)

uktweets = brexit[brexit["location"].str.contains(uk,case=False)]['tweet_text'].str.lower()
eutweets = brexit[brexit["location"].str.contains(eu,case=False)]['tweet_text'].str.lower()
rutweets = brexit[brexit["location"].str.contains(ru,case=False)]['tweet_text'].str.lower()
natweets = brexit[brexit["location"].str.contains(na,case=False)]['tweet_text'].str.lower()
worldtweets = brexit[brexit["location"].str.contains(world,case=False)]['tweet_text'].str.lower()
asiatweets = brexit[brexit["location"].str.contains(asia,case=False)]['tweet_text'].str.lower()
oceaniatweets = brexit[brexit["location"].str.contains(oceania,case=False)]['tweet_text'].str.lower()
africatweets = brexit[brexit["location"].str.contains(africa,case=False)]['tweet_text'].str.lower()
satweets = brexit[brexit["location"].str.contains(sa,case=False)]['tweet_text'].str.lower()

uk_ht = uktweets.str.findall('\#[a-z0-9\_]+', re.IGNORECASE)
eu_ht = eutweets.str.findall('\#[a-z0-9\_]+', re.IGNORECASE)
ru_ht = rutweets.str.findall('\#[a-z0-9\_]+', re.IGNORECASE)
na_ht = natweets.str.findall('\#[a-z0-9\_]+', re.IGNORECASE)
world_ht = worldtweets.str.findall('\#[a-z0-9\_]+', re.IGNORECASE)
asia_ht = asiatweets.str.findall('\#[a-z0-9\_]+', re.IGNORECASE)
oceania_ht = oceaniatweets.str.findall('\#[a-z0-9\_]+', re.IGNORECASE)
africa_ht = africatweets.str.findall('\#[a-z0-9\_]+', re.IGNORECASE)
sa_ht = satweets.str.findall('\#[a-z0-9\_]+', re.IGNORECASE)

uk_ht_NB = uk_ht[uk_ht.str.len() > 0]
eu_ht_NB = eu_ht[eu_ht.str.len() > 0]
ru_ht_NB = ru_ht[ru_ht.str.len() > 0]
na_ht_NB = na_ht[na_ht.str.len() > 0]
world_ht_NB = world_ht[world_ht.str.len() > 0]
asia_ht_NB = asia_ht[asia_ht.str.len() > 0]
oceania_ht_NB = oceania_ht[oceania_ht.str.len() > 0]
africa_ht_NB = africa_ht[africa_ht.str.len() > 0]
sa_ht_NB = sa_ht[sa_ht.str.len() > 0]

uk_ht_NB_list = [i for j in uk_ht_NB.tolist() for i in j]
eu_ht_NB_list = [i for j in eu_ht_NB.tolist() for i in j]
ru_ht_NB_list = [i for j in ru_ht_NB.tolist() for i in j]
na_ht_NB_list = [i for j in na_ht_NB.tolist() for i in j]
world_ht_NB_list = [i for j in world_ht_NB.tolist() for i in j]
asia_ht_NB_list = [i for j in asia_ht_NB.tolist() for i in j]
oceania_ht_NB_list = [i for j in oceania_ht_NB.tolist() for i in j]
africa_ht_NB_list = [i for j in africa_ht_NB.tolist() for i in j]
sa_ht_NB_list = [i for j in sa_ht_NB.tolist() for i in j]

uk_ht_NB_pd = pd.Series(uk_ht_NB_list)
eu_ht_NB_pd = pd.Series(eu_ht_NB_list)
ru_ht_NB_pd = pd.Series(ru_ht_NB_list)
na_ht_NB_pd = pd.Series(na_ht_NB_list)
world_ht_NB_pd = pd.Series(world_ht_NB_list)
asia_ht_NB_pd = pd.Series(asia_ht_NB_list)
oceania_ht_NB_pd = pd.Series(oceania_ht_NB_list)
africa_ht_NB_pd = pd.Series(africa_ht_NB_list)
sa_ht_NB_pd = pd.Series(sa_ht_NB_list)

regional_ht_total = len(uk_ht_NB_pd) + len(eu_ht_NB_pd) + len(ru_ht_NB_pd) + len(na_ht_NB_pd) + len(world_ht_NB_pd) + len(asia_ht_NB_pd) + len(oceania_ht_NB_pd) + len(africa_ht_NB_pd) + len(sa_ht_NB_pd)

print('On', user_date, ',there were', len(set(user_ht_NB_pd)), 'unique hashtags and', len(set(user_men_NB_pd)), 'unique mentions tweeted by users from', len(set(user_loc_NB_pd)), 'unique locations.')
user_top = input('How many of the top results would you like to see? Enter a numerical character only, please: ')
user_top = int(user_top)
print('The top', user_top, 'mentions on', user_date, 'are\n', user_men_NB_pd.value_counts()[:user_top])
print('The top', user_top, 'hashtags on', user_date, 'are\n', user_ht_NB_pd.value_counts()[:user_top])
print('The top', user_top, 'locations on', user_date, 'are\n', user_loc_NB_pd.value_counts()[:user_top])

uk_answer = input("Would you like to view the UK's statistics? (Y/N): ")
if uk_answer.lower() == 'y':
    print('The top 10 hashtags for the UK were:\n', uk_ht_NB_pd.value_counts()[:10])
    print('The top hashtag in the UK was',str(uk_ht_NB_pd.value_counts().index[0])+'.')
    print('It was tweeted',uk_ht_NB_pd.value_counts().iloc[0], 'times.')
    print('It accounted for',str(uk_ht_NB_pd.value_counts().iloc[0] / len(uk_ht_NB_pd) * 100)+'% of all hashtags in the UK and',str(uk_ht_NB_pd.value_counts().iloc[0] / regional_ht_total * 100)+'% of all hashtags worldwide.')
    print('The second-most tweeted hashtag in the UK was',str(uk_ht_NB_pd.value_counts().index[1])+'.')
    print('It was tweeted',uk_ht_NB_pd.value_counts().iloc[1], 'times.')
    print('It accounted for',str(uk_ht_NB_pd.value_counts().iloc[1] / len(uk_ht_NB_pd) * 100)+'% of all hashtags in the UK and',str(uk_ht_NB_pd.value_counts().iloc[1] / regional_ht_total * 100)+'% of all hashtags worldwide.')
else:
    print('Ok.')
eu_answer = input("Would you like to view the EU's statistics? (Y/N): ")
if eu_answer.lower() == 'y':
    print('The top 10 hashtags for the EU were:\n', eu_ht_NB_pd.value_counts()[:10])
    print('The top hashtag in the EU was',str(eu_ht_NB_pd.value_counts().index[0])+'.')
    print('It was tweeted',eu_ht_NB_pd.value_counts().iloc[0], 'times.')
    print('It accounted for',str(eu_ht_NB_pd.value_counts().iloc[0] / len(eu_ht_NB_pd) * 100)+'% of all hashtags in the EU and',str(eu_ht_NB_pd.value_counts().iloc[0] / regional_ht_total * 100)+'% of all hashtags worldwide.')
    print('The second-most tweeted hashtag in the EU was',str(eu_ht_NB_pd.value_counts().index[1])+'.')
    print('It was tweeted',eu_ht_NB_pd.value_counts().iloc[1], 'times.')
    print('It accounted for',str(eu_ht_NB_pd.value_counts().iloc[1] / len(eu_ht_NB_pd) * 100)+'% of all hashtags in the EU and',str(eu_ht_NB_pd.value_counts().iloc[1] / regional_ht_total * 100)+'% of all hashtags worldwide.')
else:
    print('Ok.')
ru_answer = input("Would you like to view Russia's statistics? (Y/N): ")
if ru_answer.lower() == 'y':
    print('The top 10 hashtags for Russia were:\n', ru_ht_NB_pd.value_counts()[:10])
    print('The top hashtag in Russia was',str(ru_ht_NB_pd.value_counts().index[0])+'.')
    print('It was tweeted',ru_ht_NB_pd.value_counts().iloc[0], 'times.')
    print('It accounted for',str(ru_ht_NB_pd.value_counts().iloc[0] / len(ru_ht_NB_pd) * 100)+'% of all hashtags in Russia and',str(ru_ht_NB_pd.value_counts().iloc[0] / regional_ht_total * 100)+'% of all hashtags worldwide.')
    print('The second-most tweeted hashtag in Russia was',str(ru_ht_NB_pd.value_counts().index[1])+'.')
    print('It was tweeted',ru_ht_NB_pd.value_counts().iloc[1], 'times.')
    print('It accounted for',str(ru_ht_NB_pd.value_counts().iloc[1] / len(ru_ht_NB_pd) * 100)+'% of all hashtags in Russia and',str(ru_ht_NB_pd.value_counts().iloc[1] / regional_ht_total * 100)+'% of all hashtags worldwide.')
else:
    print('Ok.')
na_answer = input("Would you like to view North America's statistics? (Y/N): ")
if na_answer.lower() == 'y':
    print('The top 10 hashtags for North America were:\n', na_ht_NB_pd.value_counts()[:10])
    print('The top hashtag in North America was',str(na_ht_NB_pd.value_counts().index[0])+'.')
    print('It was tweeted',na_ht_NB_pd.value_counts().iloc[0], 'times.')
    print('It accounted for',str(na_ht_NB_pd.value_counts().iloc[0] / len(na_ht_NB_pd) * 100)+'% of all hashtags in North America and',str(na_ht_NB_pd.value_counts().iloc[0] / regional_ht_total * 100)+'% of all hashtags worldwide.')
    print('The second-most tweeted hashtag in North America was',str(na_ht_NB_pd.value_counts().index[1])+'.')
    print('It was tweeted',na_ht_NB_pd.value_counts().iloc[1], 'times.')
    print('It accounted for',str(na_ht_NB_pd.value_counts().iloc[1] / len(na_ht_NB_pd) * 100)+'% of all hashtags in North America and',str(na_ht_NB_pd.value_counts().iloc[1] / regional_ht_total * 100)+'% of all hashtags worldwide.')
else:
    print('Ok.')
vague_answer = input("Would you like to view the statistics of locations like 'international' and 'world'? (Y/N): ")
if vague_answer.lower() == 'y':
    print('The top 10 hashtags for vague locations were:\n', world_ht_NB_pd.value_counts()[:10])
    print('The top hashtag for vague locations was',str(world_ht_NB_pd.value_counts().index[0])+'.')
    print('It was tweeted',world_ht_NB_pd.value_counts().iloc[0], 'times.')
    print('It accounted for',str(world_ht_NB_pd.value_counts().iloc[0] / len(world_ht_NB_pd) * 100)+'% of all hashtags from vague locations and',str(world_ht_NB_pd.value_counts().iloc[0] / regional_ht_total * 100)+'% of all hashtags worldwide.')
    print('The second-most tweeted hashtag in vague locations was',str(world_ht_NB_pd.value_counts().index[1])+'.')
    print('It was tweeted',world_ht_NB_pd.value_counts().iloc[1], 'times.')
    print('It accounted for',str(world_ht_NB_pd.value_counts().iloc[1] / len(world_ht_NB_pd) * 100)+'% of all hashtags from vague locations and',str(world_ht_NB_pd.value_counts().iloc[1] / regional_ht_total * 100)+'% of all hashtags worldwide.')
else:
    print('Ok.')
asia_answer = input("Would you like to view Asia's statistics? (Y/N): ")
if asia_answer.lower() == 'y':
    print('The top 10 hashtags for Asia were:\n', asia_ht_NB_pd.value_counts()[:10])
    print('The top hashtag in Asia was',str(asia_ht_NB_pd.value_counts().index[0])+'.')
    print('It was tweeted',asia_ht_NB_pd.value_counts().iloc[0], 'times.')
    print('It accounted for',str(asia_ht_NB_pd.value_counts().iloc[0] / len(asia_ht_NB_pd) * 100)+'% of all hashtags in Asia and',str(asia_ht_NB_pd.value_counts().iloc[0] / regional_ht_total * 100)+'% of all hashtags worldwide.')
    print('The second-most tweeted hashtag in Asia was',str(asia_ht_NB_pd.value_counts().index[1])+'.')
    print('It was tweeted',asia_ht_NB_pd.value_counts().iloc[1], 'times.')
    print('It accounted for',str(asia_ht_NB_pd.value_counts().iloc[1] / len(asia_ht_NB_pd) * 100)+'% of all hashtags in Asia and',str(asia_ht_NB_pd.value_counts().iloc[1] / regional_ht_total * 100)+'% of all hashtags worldwide.')
else:
    print('Ok.')
oceania_answer = input("Would you like to view Oceania's statistics? (Y/N): ")
if oceania_answer.lower() == 'y':
    print('The top 10 hashtags for Oceania were:\n', oceania_ht_NB_pd.value_counts()[:10])
    print('The top hashtag in Oceania was',str(oceania_ht_NB_pd.value_counts().index[0])+'.')
    print('It was tweeted',oceania_ht_NB_pd.value_counts().iloc[0], 'times.')
    print('It accounted for',str(oceania_ht_NB_pd.value_counts().iloc[0] / len(oceania_ht_NB_pd) * 100)+'% of all hashtags in Oceania and',str(oceania_ht_NB_pd.value_counts().iloc[0] / regional_ht_total * 100)+'% of all hashtags worldwide.')
    print('The second-most tweeted hashtag in Oceania was',str(oceania_ht_NB_pd.value_counts().index[1])+'.')
    print('It was tweeted',oceania_ht_NB_pd.value_counts().iloc[1], 'times.')
    print('It accounted for',str(oceania_ht_NB_pd.value_counts().iloc[1] / len(oceania_ht_NB_pd) * 100)+'% of all hashtags in Oceania and',str(oceania_ht_NB_pd.value_counts().iloc[1] / regional_ht_total * 100)+'% of all hashtags worldwide.')
else:
    print('Ok.')
africa_answer = input("Would you like to view Africa's statistics? (Y/N): ")
if africa_answer.lower() == 'y':
    print('The top 10 hashtags for Africa were:\n', africa_ht_NB_pd.value_counts()[:10])
    print('The top hashtag in Africa was',str(africa_ht_NB_pd.value_counts().index[0])+'.')
    print('It was tweeted',africa_ht_NB_pd.value_counts().iloc[0], 'times.')
    print('It accounted for',str(africa_ht_NB_pd.value_counts().iloc[0] / len(africa_ht_NB_pd) * 100)+'% of all hashtags in Africa and',str(africa_ht_NB_pd.value_counts().iloc[0] / regional_ht_total * 100)+'% of all hashtags worldwide.')
    print('The second-most tweeted hashtag in Africa was',str(africa_ht_NB_pd.value_counts().index[1])+'.')
    print('It was tweeted',africa_ht_NB_pd.value_counts().iloc[1], 'times.')
    print('It accounted for',str(africa_ht_NB_pd.value_counts().iloc[1] / len(africa_ht_NB_pd) * 100)+'% of all hashtags in Africa and',str(africa_ht_NB_pd.value_counts().iloc[1] / regional_ht_total * 100)+'% of all hashtags worldwide.')
else:
    print('Ok.')
sa_answer = input("Would you like to view South America's statistics? (Y/N): ")
if sa_answer.lower() == 'y':
    print('The top 10 hashtags for South America were:\n', sa_ht_NB_pd.value_counts()[:10])
    print('The top hashtag in South America was',str(sa_ht_NB_pd.value_counts().index[0])+'.')
    print('It was tweeted',sa_ht_NB_pd.value_counts().iloc[0], 'times.')
    print('It accounted for',str(sa_ht_NB_pd.value_counts().iloc[0] / len(sa_ht_NB_pd) * 100)+'% of all hashtags in South America and',str(sa_ht_NB_pd.value_counts().iloc[0] / regional_ht_total * 100)+'% of all hashtags worldwide.')
    print('The second-most tweeted hashtag in South America was',str(sa_ht_NB_pd.value_counts().index[1])+'.')
    print('It was tweeted',sa_ht_NB_pd.value_counts().iloc[1], 'times.')
    print('It accounted for',str(sa_ht_NB_pd.value_counts().iloc[1] / len(sa_ht_NB_pd) * 100)+'% of all hashtags in South America and',str(sa_ht_NB_pd.value_counts().iloc[1] / regional_ht_total * 100)+'% of all hashtags worldwide.')
    print('Thank you!')
else:
    print('Thank you!')