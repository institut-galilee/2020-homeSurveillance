# Simple home surveillace system 

Since security and privacy has became something crucial nowadays we decided to build a simple surveillance system designed mainly for houses 
but the general design can be used to larger propreties such as companies  parkinglots or any sort of proprety that can be assigned one or more individuals  

### Members
  * Abdel Mounaim BOUZERIRA 
  * Marwane GHARS

### Description 

A house autonomous surveillance system that notify the owner whenever it detects any sort of movements and trigger a sound alarm in the absence of the owner's feedback.

### fonctionement 

The system is a combination of two cameras , two motion  sensors  and finger print working in parallel .
The sytem is continuously proccessing its environment , and when a object  is close enough the system begin a live stream , if the system does recognize  the owner using the fingerprint device he will receive an email wich contains an image of the detected object as well as a link to the camera live stream , the owner than will have the choise to trigger an alarm or discard the the warning , in the absence of any feedback the alarm will be trigged any way .

### Market study 


There are already a tons of [houmeSurveillance-like](https://www.tike-securite.fr/243-alarme-maison-sans-fil-mn209f.html?gclid=Cj0KCQiA48j9BRC-ARIsAMQu3WReq7Y6WCVNlIxuxQOOR9IWSm7pvf__gAiLMfgyl7jEtpM_jIfzBuMaAiPlEALw_wcB) device with almost the same range of prices (200€ - 1000€)  in the market however none of them  provide the fingerprint feature which make security more robust and reliable .

#### Leading companies 
  * VERISURE  
       Verisure, formerly Securitas Direct, is a Swedish-based company specializing in alarms with remote monitoring for individuals and small businesses. It is present in 17          countries1 in Europe and South America and has 3.3 million customers 
 
    ** Description de leur produits

       Once the system is connected, the remote monitoring must respond to alarm signals at all times. In the event of an alarm, it is necessary to remove the doubt, this is          compulsory according to the internal security  before notifying the police, the fire brigade or the SAMU. The remote surveillance officers can communicate with the              customer or potential intruders via the intercom in the alarm center. The company can also send a guard on the proprety



### composants 

  ### composants 
     =>rasberry pi 
     =>500W Raspberry Pi Camera Module HD 160 ° Vidéo Grand Angle Webcam
     =>DC 2.7 À 12 V Infrarouge PIR Motion Capteur Humain Détecteur Automatique Module Mini Module PIR Mini Module D'induction Du Corps Humain
     =>Arduino capteur digital 
