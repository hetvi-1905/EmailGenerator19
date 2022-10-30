# Automatic Email Generator using GPT3
- This is an automatic email generator app built using GPT3 and NLP 
- Heroku Deployment Link of Working Project : https://emailgenerator19.herokuapp.com/

# 📧Automatic Email Generator
![EmailGenerator19](https://user-images.githubusercontent.com/84613393/198873168-4489c84d-60dc-475f-bb1d-693660cf9f50.png)

## 🖊 Brief Intro 
An automatic email generator that generates whole email based on the subject inserted by the user.

## 📌 Importance 
Such mail generator are useful in order to generate some preformated mails automatically just by inserting the subject by the user without any manual typing.

## 🎥 Demo Video 
https://user-images.githubusercontent.com/84613393/198873840-f479bdf9-44ca-4182-84a0-2a0909b7835a.mp4

## API used
OpenAI’s API provides access to GPT-3, which performs a wide variety of NLP tasks, and Codex, which translates natural language to code.

## 🔁 Pipeline 
<ul>
  <li> Use UI to give subject,salutation and limit of words to the backend. </li>
  <li> After clicking on "Generate Email" button, the input is given to the OpenAI API to fetch email related to the subject.</li>
  <li> OpenAI uses GPT3 internally to get the corresponding result of the input entered. </li>
  <li> You can send the email, by clicking on send email. </li>
</ul>

## 🎯 Deployment at Heroku
I have deployed the ML-Pipeline on a Web application using Flask.
https://emailgenerator19.herokuapp.com/

## 📷 Screenshots
Landing Page 

User Input

Output


 ## 🔨 Tech-Stack
 <ul>
  <li> Front-end:Streamlit </li>
  <li> Back-end:Flask </li>
  <li> Machine Learning Libraries:Numpy, Pandas,OpenAI API,GPT3</li>
 </ul>
