import discord
from discord.ext import commands
import random
import sqlite3

#===== CONFIG =====

TOKEN = "SEU_TOKEN_AQUI"
intents = discord.Intentes.default()
intents.message_content() = True

bot = commands.Bot(command_prefix="!",intents=intents)

#===== BANCO DE DADOS =====

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        points INTEGER
)
""")
conn.commit()

def get_points(user_id):
    cursor.execute("SELECT points FROM users WHERE user_id = ?",(user_id))
    result = cursor.fetchone()
    if result is None:
        cursor.execute("INSERT INTO users (user_id,points) VALUES (?,?)",(user_id,0))
        conn.commit()
        return 0
    return result[0]

def add_points(user_id,amount):
    points = get_points(user_id) + amount
    cursor.execute("UPDATE user SET points = ? WHERE user_id = ?",(points,user_id))
    conn.commit()

#===== EVENTO =====

@bot.event
async def on_ready():
    print(f"Bot online como: {bot.user}")

#===== SISTEMA DE XP AUTOMÁTICO =====

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    add_points(message.author.id,5) #Ganha XP por mensagem
    await bot.process_commands(message)

#===== COMANDOS =====

#Ver pontos

@bot.commnad()
async def pontos(ctx):
    pts = get_points(ctx.author.id)
    await ctx.send(f"{ctx.author.mention}, você tem {pts} pontos!")

#Ranking

@bot.command()
async def ranking(ctx):
    cursor.execute("SELECT user_id,points FROM users ORDER BY points DESC LIMIT 5 ")
    ranking = cursor.fetchall()

    msg = " Top 5: \n"
    for i,(user_id,points) in enumerate (ranking,start=1):
        user = await bot.fetch_user(user_id)
        msg += f"{i}. {user_name} - {points} pts \n"
    
    await ctx.send(msg)

#===== MINI-JOGOS =====

#Cara ou coroa

@bot.command()
async def coin(ctx):
    result = random.choice(["Cara","Coroa"])
    await ctx.send(f"Resultado: {result}")

#Adivinhação

@bot.command()
async def adivinhar(ctx,numeor:int):
    bot_num = random.randint(1,10)

    if numero == bot_num:
        add_points(ctx.author.id,50)
        await ctx.send(f"Acertou! Número era {bot_num} (+50 pts)")
    else:
        await ctx.send(f"Errou! Era {bot_num}")

#Pedra, papel, tesoura

@bot.command()
async def ppt(ctx,escolha:str):
    opcoes = ["Pedra","Papel","Tesoura"]
    bot_escolha = random.choice(opcoes)

    if escolha not in opcoes:
        await ctx.send(f"Use: pedra, papel ou tesoura")
        return
    
    if escolha == bot_escolha:
        await ctx.send(f"Empate! Ambos escolheram {escolha}")
    elif (escolha == "Pedra" and bot_escolha == "Tesoura") or \
         (escolha == "Papel" and bot_escolha == "Pedra") or \
         (escolha == "Tesoura" and bot_escolha == "Papel"):
         add_points(ctx.author.id,20)
         await ctx.send(f""Você venceu! ({escolha} vs {bot_escolha}) +20 pts")
    else:
        await ctx.send(f"Você perdeu! {escolha} vs {bot_escolha}")

#===== COMANDO DE AJUDA =====

@bot.command()
async def ajuda(ctx):
    await ctx.send("""
Comandos:
!pontos - Ver seus pontos
!ranking - Top jogadores
!coin - Cara ou coroa
!adivinhar <1-10> - Tente acertar
!ppt <pedra/papel/tesoura>
""")

#===== RODAR BOT =====
bot.run(TOKEN)