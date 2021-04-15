import discord
import os
import requests
import json

from keep_alive import keep_alive

client = discord.Client()

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

'''
Para aceder ao API usa-se o link que eles tem na documentação
a variavel city é dada pelo user 
o jprint e isso é "default",
weather = json_data[][] --> escrito desta forma porque para aceder a 
                              dicionario de dicionario é dessa forma

o weather = json_data[][][] --> tem mais um [] porque aquilo ja é um 
                                array dentro do dicionario do dicionario

'''
def get_weather_weather(city,Dic_cond,cond):
  response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=8049c1ff67bb52cf975bf3c6bfaafd43")
  print(response.status_code)
  jprint(response.json())
  json_data = json.loads(response.text)
  print(json_data)
  weather = json_data[Dic_cond][0][cond]

  return weather

def get_weather_main(city,Dic_cond,cond):
  response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=8049c1ff67bb52cf975bf3c6bfaafd43")
  print(response.status_code)
  jprint(response.json())
  json_data = json.loads(response.text)
  print(json_data)
  weather = json_data[Dic_cond][cond]

  return weather  

def get_celsius(temp):
  return temp - 273.15


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  msg = message.content.lower()
  print(message.content[:20])

  if message.author == client.user:
    return

  if message.content.startswith('$help'):
    await message.channel.send("Comandos:\n\
    $hello - para olá \n\
    $covid - para saber onde anda \n\
    $hotel - trivago \n\
    $inspire - para mensagem inspiradora \n\
    $weather cidade - para saber temperatura da cidade \n\
    $weather description cidade - para ter descrição do tempo da cidade\
    ")

  if msg.startswith('$hello'):
    await message.channel.send("Eai galera como vai isso ne bleza")

  if msg.startswith('$covid'):
    await message.channel.send("Siga Estoril")
  
  if msg.startswith('$hotel'):
    await message.channel.send("Trivago")

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  
  '''
  ver as palavras que sao escritas se primeira palavra for weather entra se
  no if e depois ve-se se tem mais alguma coisa a frente se tiver if...
  '''

  w = '$weather'
  if msg.startswith(w):
    wd = '$weather description'
    if msg[:20] == wd:
      city = message.content[len(wd)+1:] 
      print(city)
      description = get_weather_weather(city,'weather','description')
      await message.channel.send(description)  

    else:
      city = msg[len(w)+1:] 
      temp = get_weather_main(city,'main','temp')
      feelsLike = get_weather_main(city,'main','feels_like')
      weather = "Temperature is " + str(round(get_celsius(temp),2)) + "ºC but it feels like " + str(round(get_celsius(feelsLike),2)) + "ºC"
      await message.channel.send(weather)

  else: pass
  

keep_alive()
client.run(os.getenv('DISCORD_TOKEN'))
    
