import tkinter as tk
from PIL import Image, ImageTk
import random as rnd
# from blackjack.functions import *

bg_color = "#004400"
suits = ["clubs", "diamonds", "hearts", "spades"]
ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
dealer_hand = []
player_hand = []
deck = []

def deal_cards():
	# cria um baralho novo (não embaralhado)
	for st in suits:
		for rnk in ranks:
			deck.append("{}_of_{}.png".format(rnk, st))
	# dá as cartas ao computador
	for c in range(3):
		card = rnd.choice(deck)
		dealer_hand.append(card)
		deck.remove(card)
	# dá as cartas ao jogador
	for c in range(2):
		card = rnd.choice(deck)
		player_hand.append(card)
		deck.remove(card)
	# testa as mãos:
	for c in dealer_hand:
		print(c)
	print()
	for c in deck:
		print(c)


deal_cards()

def ask_card():
	pass

def compare_hands():
	pass

app = tk.Tk()
app.title("Blackjack")
app.geometry("300x200")
app.configure(bg=bg_color)

#== ELEMENTOS GRÁFICOS ===

message = tk.Label(app, text="Faça sua jogada", bg=bg_color, width=30, height = 5)
message.grid(column=0, columnspan=2, row=0, padx=5, pady=5)

btn_ask_card = tk.Button(app, text="Pedir Carta", command=ask_card, bg="silver", width=10, height=3)
btn_ask_card.grid(column=0, row=1, padx=5, pady=5)

btn_compare_hands = tk.Button(app, text="Comparar", command=compare_hands, bg="silver", width=10, height=3)
btn_compare_hands.grid(column=1, row=1, padx=5, pady=5)

# Crie o canvas
canvas = tk.Canvas(app, width=400, height=400)
canvas.pack()

# Carregue as imagens usando a PIL e redimensione
original_image1 = Image.open("deck/back.png")
resized_image1 = original_image1.resize((30, 50))
card_image1 = ImageTk.PhotoImage(resized_image1)

original_image2 = Image.open("deck/back.png")
resized_image2 = original_image2.resize((30, 50))
card_image2 = ImageTk.PhotoImage(resized_image2)

# Adicione as imagens ao canvas
image_item1 = canvas.create_image(50, 50, image=card_image1, anchor='nw')
image_item2 = canvas.create_image(100, 100, image=card_image2, anchor='nw')



#=================
app.mainloop()