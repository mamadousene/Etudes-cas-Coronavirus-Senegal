"""
Mamadou Lamine SENE
ML___SENE__17
"""
from tkinter import messagebox
import sys
import tweepy
import re
import bs4
import requests
import os
from io import BytesIO
from PIL import Image
import shutil
"""Fonction pour la AUTHENTIFICATION
   vers l API TWITTER
"""
def twitter_auth():
    try:
        costumer_key = "RLin4hhLDwdVuLznsOEHopZxm"
        costumer_secret = "2YmUVJjyUEhke1dtJ2CtKVhZbrwOEwPcH3p6qcDEL3CeyAlESl"
        access_token = "719520290242502656-K35or0oToHRGNO3NZBHnewAQVczu3ga"
        access_secret = "drsjWpWtChQ59ZIa3kh5uSbqVsV6iES4evxLi7AJXWI2W"
    except KeyError:
        sys.stderr.write("Twitter environnement variable  not set !\n")
        sys.exit(1)
    auth = tweepy.OAuthHandler(costumer_key,costumer_secret)
    auth.set_access_token( access_token,access_secret)
    return auth
"""Fonction pour recuperer l objet apres l authentification
"""
def get_twitter_client():
    auth = twitter_auth()
    client = tweepy.API(auth,wait_on_rate_limit=True)
    return client
"""Fonction pour recuperer
tous les tweets concernant les communicant
"""
def get_total_link(progress,limite=0):
    user ="MinisteredelaS1"
    client = get_twitter_client()
    total_link = []
    i=0
    maxI=10
    if limite==0:
        tweetAll = tweepy.Cursor(client.user_timeline,screen_name=user,tweet_mode="extended",include_rts=False,lang="fr",exclude_replies=True).items()
    else:
        tweetAll = tweepy.Cursor(client.user_timeline,screen_name=user,tweet_mode="extended",include_rts=False,lang="fr",exclude_replies=True).items(1)
    for tweets in tweetAll:
        full_link={}
        if "Communiqué"  and "déclarés positifs" in tweets.full_text:
            try:
                if tweets.extended_entities :
                    #print(i,"tweets charges")
                    full_link["date_tweet"]=str(tweets.created_at.date().isoformat())
                    link = []
                    for t in tweets.extended_entities.get("media",[]):
                        link.append(t["media_url"])
                    full_link["link_image"]=link
                    total_link.append(full_link)
                    i=i+1
                    texte=str(i)+" Communique Chargees depuis twitter"
                    progress.label_welcome.config(text=texte)
            except Exception as e :
                pass
    tw= str(i)+" tweets ont été bien chargés"
    messagebox.showinfo("Tweets charges",tw)
    return total_link
"""Fonction pour telecharger
 1 image apres recuperation des lien
"""
def telechargerImage(LIEN_DE_IMAGE,j):#cette fonction nous permet de telecharger les images
    if LIEN_DE_IMAGE :
        try:
            link_Extension = os.path.basename(LIEN_DE_IMAGE).split(".")
            extension = link_Extension[1]
            res =requests.get(LIEN_DE_IMAGE)
            imgFile = Image.open(BytesIO(res.content))
            imgFile.save(str(j)+'.'+extension)
        except Exception as e:
            pass
"""Fonction pour stocker les images
 dans un dossier local
"""
def telechargerImageDuJour(progress,tweets):
    messagebox.showinfo("Info","Fin de Chargement des Tweets depuis twitter")
    progress.pb1.stop()
    progress.fil.title("Telechargement des Images")
    messagebox.showinfo("Info","Debut telechargement des IMAGES")
    progress.pb1["mode"]="determinate"
    progress.pb1["value"]=0
    progress.label_welcome.config(text="")
    progress.fil.update_idletasks()
    Anne_Mois=tweets[0]["date_tweet"][:7]
    jour=tweets[0]["date_tweet"][8:]
    if not os.path.exists(Anne_Mois):
        try:
            os.mkdir(Anne_Mois)
        except:
            messagebox.showerror("Erreur","Impossible de creer le dossier")
    os.chdir(Anne_Mois)
    if not os.path.exists(jour):
        try:
            os.mkdir(jour)
        except: 
            messagebox.showerror("Erreur","Impossible de creer le dossier")
    else:
        os.chdir("..")
        return False
    os.chdir(jour)
    timage=1
    for Linkimage in  tweets[0]["link_image"]:
        pourcentage = int(50*timage)
        progress.pb1["value"]=pourcentage
        pourc=str(pourcentage)+"%\n\n"
        texte=pourc+str(timage)+" images telecharges"
        progress.label_welcome.config(text=texte)
        progress.fil.update_idletasks()
        telechargerImage(Linkimage,timage)
        timage=timage+1
    os.chdir("..")
    os.chdir("..")
    return True
def telechargerAllImages(progress,tweets):
    messagebox.showinfo("Info","Fin de Chargement des Tweets depuis twitter")
    progress.pb1.stop()
    progress.fil.title("Telechargement des Images")
    messagebox.showinfo("Info","Debut telechargement des IMAGES")
    progress.pb1["mode"]="determinate"
    progress.pb1["value"]=0
    progress.label_welcome.config(text="")
    progress.fil.update_idletasks()
    pos=1
    taille=len(tweets)
    for itemTweet in tweets :
        pourcentage = int(pos*100/taille)
        progress.pb1["value"]=pourcentage
        pourc=str(pourcentage)+"%\n\n"
        texte=pourc+str(pos)+"/"+str(taille)+" Communiques telecharges"
        progress.label_welcome.config(text=texte)
        progress.fil.update_idletasks()
        Anne_Mois=itemTweet["date_tweet"][:7]
        jour=itemTweet["date_tweet"][8:]
        if not os.path.exists(Anne_Mois):
            try:
                os.mkdir(Anne_Mois)
            except:
                messagebox.showerror("Erreur","Impossible de creer le dossier")
                sys.exit(1)
        os.chdir(Anne_Mois)
        if not os.path.exists(jour):
            try:
                os.mkdir(jour)
            except: 
                messagebox.showerror("Erreur","Impossible de creer le dossier")
                sys.exit(1)
        os.chdir(jour)
        timage=1
        for Linkimage in  itemTweet["link_image"]:
            telechargerImage(Linkimage,timage)
            timage=timage+1
        os.chdir("..")
        os.chdir("..")
        pos=pos+1
def fonctionMain(progress,type="ALL"):
    Nom_Dossier= "TweetAllImage"
    if not os.path.exists(Nom_Dossier):
        try:
            os.mkdir(Nom_Dossier)
        except:
            sys.exit(1)
            messagebox.showerror("Erreur","Impossible de creer le dossier")
    try:
            if(type=="ALL"):
                try:
                    shutil.rmtree(Nom_Dossier)
                    os.mkdir(Nom_Dossier)
                except:
                    messagebox.showerror("Erreur","Impossible de creer le dossier")
                os.chdir(Nom_Dossier)
                telechargerAllImages(progress,get_total_link(progress))
            else:
                os.chdir(Nom_Dossier)
                """Si on veut telecharger
                le dernier tweet(le communique du jour)"""
                if telechargerImageDuJour(progress,get_total_link(progress,1)):
                    os.chdir("..")
                    return True
                else :
                    os.chdir("..")
                    return False
    except Exception as e:
            messagebox.showerror("Probleme d ouverture du dossier ")
    os.chdir("..")
    return True