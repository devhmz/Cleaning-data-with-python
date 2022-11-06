import re as re 
import csv as csv 
import pandas as pd 



tab = []
fp = open("CSV_FILE_NAME", "r", encoding="utf-8")
for ligne in csv.reader(fp, delimiter=";"):
    for i in ligne : 
         text =  re.sub(r'@[A-Za-z0-9]+',' ',i) #removes the @mentions
         text =  re.sub(r'#',' ',text) #removes the hashtags
         text =  re.sub(r'RT[\s]+',' ',text) #removes the retweets
         text =  re.sub(r'https?://\S+',' ',text) #removes the hyper links
         text = text.lower() # removes lower case
         text = text.replace('\n', ' ').replace('\r', '') #removes sapces
         text = ' '.join(text.split()) #split string
         text = re.sub(r"[A-Za-z\.]*[0-9]+[A-Za-z%°\.]*", "", text) #removes the @mentions
         text = re.sub(r"(\s\-\s|-$)", "", text) #removes the $mentions
         text = re.sub(r"[,\!\?\%\(\)\/\"]", "", text)  #removes the \\\\mentions
         text = re.sub(r"\&\S*\s", "", text) #removes the &*mentions
         text = re.sub(r"\&", "", text)#removes the &mentions
         text = re.sub(r"\+", "", text)#removes the +mentions
         text = re.sub(r"\#", "", text)#removes the #mentions
         text = re.sub(r"\$", "", text)#removes the $mentions
         text = re.sub(r"\£", "", text)#removes the £mentions
         text = re.sub(r"\%", "", text)#removes the %mentions
         text = re.sub(r"\:", "", text)#removes the :mentions
         text = re.sub(r"\@", "", text)#removes the @mentions
         text = re.sub(r"\-", "", text)#removes the -mentions
         tab.append([text])
        
df = pd.DataFrame(tab, columns=['Tweets'])
df.to_csv("avis_nettoyes1.csv", index=False, encoding='utf-8')
