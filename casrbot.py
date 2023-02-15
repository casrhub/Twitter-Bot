from pip import main
import tweepy, keysbot, openai


#identificar tweepy APIs
auth = tweepy.OAuthHandler(keysbot.api_key,keysbot.api_secret)
auth.set_access_token(keysbot.access_token,keysbot.access_token_secret)
api = tweepy.API(auth)
#API key de openai
openai.api_key = "XXX-XXX-XXX"

#definición de modelo y parametros con open ai
response= openai.Completion.create(
  model="text-davinci-002",
  prompt="",
  max_tokens=64
)
#extraer el parametro que nos importa "text"
text = response.choices[0].text
print(text)

#mandarlo a la cuenta de twitter
api.update_status(text)
