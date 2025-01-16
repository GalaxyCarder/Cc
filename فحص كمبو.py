import requests
import telebot
from telebot import types
from joker import Tele 
token = "7383332333:AAF9_ZGTjpdtsQMRJLrVScBswjOSGqJpecE" #التوكن هنا 
bot=telebot.TeleBot(token,parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,"𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑻𝑯𝑬 𝑮𝑨𝑳𝑨𝑿𝒀 𝑪𝑨𝑹𝑫𝑬𝑹 𝑪𝑪 𝑪𝑯𝑬𝑪𝑲𝑬𝑹  \n 𝙎𝙀𝙉𝘿 𝙈𝙀 𝙔𝙊𝙐𝙍 𝘾𝙊𝙈𝘽𝙊 𝙄 𝙒𝙄𝙇𝙇 𝘾𝙃𝙀𝘾𝙆 𝙔𝙊𝙐𝙍 𝘾𝘾 🔥 \n ᵈᵉᵛˡᵒᵖᵉᵈ ᵇʸ @Galaxy_Carder")
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	live = 0
	ch = 0
	last = 0
	ko = (bot.reply_to(message, "𝑪𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝒀𝒐𝒖𝒓 𝑪𝒂𝒓𝒅𝒔...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
			
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				hh = types.InlineKeyboardButton(f"• {last} •", callback_data='u8')
				cm2 = types.InlineKeyboardButton(f"• 𝑪𝑯𝑨𝑹𝑮𝑬𝑫 💲: [ {ch} ] •", callback_data='x')
				cm3 = types.InlineKeyboardButton(f"• 𝑳𝑰𝑽𝑬 ✅ : [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝑫𝑬𝑨𝑫 ❌ : [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝑻𝑶𝑻𝑨𝑳 🔥 : [ {total} ] •", callback_data='x')
				mes.add(hh,cm1, cm2, cm3, cm4, cm5)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''𝑾𝒂𝒊𝒕 𝒇𝒐𝒓 𝒑𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈  
𝒃𝒚 ➜ @Galaxy_Carder ''', reply_markup=mes)
				
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "𝒀𝒐𝒖𝒓 𝒄𝒂𝒓𝒅 𝒘𝒂𝒔 𝒅𝒆𝒄𝒍𝒊𝒏𝒆𝒅."
				
				msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ #Approved
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ Braintree 14$  
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @Galaxy_Carder
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
				print(last)
				if "Card Issuer Declined CVV" in last:
					bot.reply_to(message, msg)
					live += 1
				elif "Insufficient Funds" in last:
					live += 1
					bot.reply_to(message, msg)
				elif "Success" in last:
					ch += 1
					msg1 = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc}
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑺𝑈𝑪𝑪𝐸𝑆𝑆
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ Braintree 14$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @Galaxy_Carder
◆ 𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
					bot.reply_to(message, msg1)
				else:
					dd += 1
	except:
		pass
print("The bot has been activated.")
bot.polling()