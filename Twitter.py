from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard

class Twitter:
    def __init__(self,username,password):
        self.driver = webdriver.Firefox()
        self.username = username
        self.password = password
    
    def signIn(self):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(2.5)
        mailBul = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        mailBul.click()
        mailBul.send_keys(self.username)
        time.sleep(.6)
        btnIleri = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        btnIleri.click()
        time.sleep(1.5)
        try:
            kAdiBul = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            kAdiBul.click()
            kAdi = self.username
            kAdiBul.send_keys(kAdi)
            time.sleep(.6)
            btnIleri2 = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
            btnIleri2.click()
            time.sleep(1.5)
        except:
            print('kAdi istenmedi')
        finally:
            sifreBul = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            sifreBul.click()
            sifreBul.send_keys(self.password)
            time.sleep(.5)
            giris = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
            giris.click()
            time.sleep(2)
            bird = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[1]/h1/a/div')
            bird.click()
            time.sleep(1.5)
    
    def tweetCek(self):
        twitter.Bird()
        ekle = []
        url = 'https://twitter.com/dhainternet','https://twitter.com/ihacomtr'
        for i in url:
            self.driver.get(i)
            self.driver.implicitly_wait(7)
            time.sleep(3.5)
            loopCounter = 0
            #last_height = self.driver.execute_script("return document.documentElement.scrollHeight")
            last_height = 0
            """tweets = self.driver.find_elements_by_xpath('//div[@data-testid="tweetText"]')
            time.sleep(1.5)
            for tweet in tweets:
                ekle.append(tweet.text)
            time.sleep(1)"""
            while True:
                if loopCounter > 4:
                    break
                self.driver.execute_script(f"window.scrollTo({last_height},{last_height+1500});")
                time.sleep(1)
                self.driver.implicitly_wait(5)
                new_height = last_height+1500
                if last_height == new_height:
                    break
                last_height = new_height
                loopCounter+=1
                tweets = self.driver.find_elements_by_xpath('//div[@data-testid="tweetText"]')
                time.sleep(1.5)
                for tweet in tweets:
                    deger = tweet.text
                    if deger not in tweets:
                        ekle.append(deger)
            time.sleep(1.5)
            self.driver.implicitly_wait(7)
        with open('tweet.txt','w',encoding="UTF-8") as yaz:
            for i in ekle:
                tw = str(i).split("\n")
                yaz.write(f"{tw[0]}\n")

    def tweetPaylas(self):
        twitter.Bird()
        tweets = []
        tweets.clear()
        url2 = f"https://twitter.com/{self.username}"
        self.driver.get(url2)
        self.driver.implicitly_wait(7)
        time.sleep(2)
        with open('tweet.txt','r',encoding="UTF-8") as oku:
            for satir in oku:
                tweets.append(satir.lstrip("http://dha.com.tr/"))
        uzunluk = len(tweets)
        i = 0
        while i<uzunluk:
            try:
                tweetAt = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
                tweetAt.click()
                time.sleep(10)
                twitter.Share(deger=tweets[i])
            except:
                twitter.Error()
                twitter.Bird()
            finally:
                i+=1

    def Bird(self):
        self.driver.refresh()
        self.driver.implicitly_wait(3)
        time.sleep(1.5)

    def Error(self):
        print("Tıklanamadı")
        exit = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div')
        exit.click()
        time.sleep(1)
        vazgec = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]')
        vazgec.click()
        time.sleep(1.5)

    def Share(self,deger):
        tweetYaz = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweetYaz.click()
        time.sleep(1.5)
        tweetYaz.send_keys(deger+"\n#konya\n@konyagundemm\nKonya")
        time.sleep(1.5)
        paylas = self.driver.find_element_by_xpath('//div[@data-testid="tweetButton"]')
        paylas.click()
        time.sleep(3)

cikis = True
twitter = Twitter("erkanyesilyayla","Erkan.1334qazüiç")
print("###################################################")
print("###########Tweeter Bot \n by Recep KARATAŞ###########")
print("###################################################")            
twitter.signIn()
while cikis:
    try:
        twitter.tweetCek()
        try:
            twitter.tweetPaylas()
        except:
            print("Tweet Paylaşılamadı")
    except:
        print("Tweet Çekilemedi")
    finally:
        time.sleep(1800)
        if keyboard.is_pressed("q"):
            cikis=False
