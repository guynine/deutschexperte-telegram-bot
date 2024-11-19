import aiogram
from aiogram import *
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from aiogram.utils.markdown import hide_link
import markups
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import *
storage = MemoryStorage()
bot = Bot('TOKEN', parse_mode='html')
dp = Dispatcher(bot, storage=storage)


admin_id = [ID, ID, ID]
group_id = -ID


name_enter = {}
phone_enter = {}
massive_names = {}
text_m = {}
msg = {}



class text_post_message(StatesGroup):
	text = State()
	button_name = State()
	button_link = State()

text_post_message_static = {}



class media_post_message(StatesGroup):
	text = State()
	photo_id = State()
	button_name = State()
	button_link = State()

media_post_message_static = {}


newssender_state = True
	
#========================= START COMMAND =========================
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
	text_start = f"{hide_link('https://telegra.ph/file/1d13c87f36b2654eae2dd.png')}Здравствуйте, <b>{message.from_user.first_name}</b> !\nВас приветствует бот курсов немецкого языка от <b>DeutschExperte</b>.\n\nКого мы ждем на нашем курсе?🗣\n\nМы ждем всех, для кого Германия и ее язык находятся в фокусе жизненных интересов - тех, кто нацелен на бизнес с немецкими компаниями, на знакомство со страной, на учёбу/работу в Германии – и широкий круг любознательных, желающих расширить свои горизонты в путешествиях и учебе, а также для студентов и учителей, которые хотят углубить свои знания по немецкому языку.\n\n<b>Наши контакты</b>\n📘 <a href='https://www.facebook.com/Deutschexpert'>Facebook</a>\n📞 <a href='https://api.whatsapp.com/send?phone=998935905905'>WhatsApp</a>\n📩gennadiy.gerasimov@dbaconsulting.co"
	if message.chat.id in admin_id:
		await message.answer(text_start, reply_markup=markups.start_admin_kb)
	else:
		await message.answer(text_start, reply_markup=markups.start_kb)
	file = open('id_base.txt', 'r+')
	text = file.read()
	if str(message.chat.id) not in text:
		for i in admin_id:
			await bot.send_message(i, f"<b>Система информирования:</b>\n{str(message.chat.id)}, впервые зашел в бота!")
		print(str(message.chat.id) + ', впервые зашел в бота!')
		file.write('\n' + str(message.chat.id))
		file.close()

#================================================================










#==== ПОЛЬЗОВАТЕЛИ ====
@dp.message_handler(commands=['clear'])
async def command_clear(message: types.Message):
	open('id_active.txt','w+').close()
	await message.answer('База активных пользователей очищина!')
#==== ==== ==== ==== ====













@dp.message_handler(content_types=['photo'])
async def rassilka(message: types.Message):
    global back_date, days, link2, check
    try:
        #---------------
        #Отправка рассылки без кнопки
        if message.from_user.id in admin_id and 'Кнопка' not in message.caption:
            await bot.send_message(message.chat.id, 'Принято! Рассылка начата.')
            file_info = await bot.get_file(message.photo[2].file_id)
            downloaded_file = await bot.download_file(file_info.file_path)
            with open('rassilka.jpg', 'wb') as new_file:
                new_file.write(downloaded_file.getvalue())
            baza = open('id_base.txt', 'r')
            text = baza.readlines()
            await bot.send_message(message.chat.id, 'Удалось разослать пользователям: ' + text[i])
            for i in range(len(text)):
                try:
                    src = open('rassilka.jpg', 'rb')
                    await bot.send_photo(text[i], photo=src, caption=message.caption)
                    print('Удалось разослать пользователю: ' + text[i])
                except:
                    pass
            baza.close()
        #---------------
        #Отправка рассылки с кнопкой
        elif message.from_user.id in admin_id and 'Кнопка' in message.caption:
            x = message.caption.split('Кнопка')
            name = x[1].split('Название')
            m = InlineKeyboardMarkup(row_width=1)
            button2 = KeyboardButton(text=name[1], url=name[0])
            m.add(button2)
            await bot.send_message(message.chat.id, 'Принято! Рассылка начата.')
            file_info = await bot.get_file(message.photo[2].file_id)
            downloaded_file = await bot.download_file(file_info.file_path)
            with open('rassilka.jpg', 'wb') as new_file:
                new_file.write(downloaded_file.getvalue())
            baza = open('id_base.txt', 'r')
            text = baza.readlines()
            for i in range(len(text)):
                try:
                    src = open('rassilka.jpg', 'rb')
                    await bot.send_photo(text[i], photo=src, caption=f"{x[0]}", reply_markup=m)
                    await bot.send_message(message.chat.id, 'Удалось разослать пользователю: ' + text[i])
                    print('Удалось разослать пользователю: ' + text[i])
                except:
                    pass
            baza.close()
    except:
        await message.answer('Ошибка рассылки! Возможно параметры не указаны или введены неверно!')        

        

		
		
		
		
		

@dp.message_handler(content_types=['text'])
async def text_message(message: types.Message):
	#---------------
	#Инциализация отправки сообщений в администрацию
	file = open('id_active.txt', 'r+')
	text = file.read()
	#---------------
	#Проверка активного пользователя
	if str(message.chat.id) not in text:
		for i in admin_id:
			await bot.send_message(i, f"<b>Система информирования:</b>\n{str(message.chat.id)}, стал активным пользователем!")
		print(str(message.chat.id) + ', стал активным пользователем!')
		file.write('\n' + str(message.chat.id))
		file.close()
	if message.text == '💻Напишите нам💻':
		text_m[message.from_user.id] = True
		await message.answer('<b>Напишите свой вопрос и администрация ответит вам в ближайшее время</b>📩')
		return
	#---------------
	#Запрет на отправку ссылок в администрацию
	#elif text_m[message.from_user.id] == True  and 'http' in message.text:
		#await message.answer('Нельзя отправлять ссылки в тех. поддержку!')
		#text_m[message.from_user.id] = False
		#return
	#---------------
	#Отправка сообщений в администрацию
	try:
		if text_m[message.from_user.id] == True:
			for i in admin_id:
				await bot.send_message(i, f"<code>{str(message.chat.id)}@</code> {message.text}\n\n<b>Чтобы ответить на это сообщение нажмите на ID пользователя для копирования, затем введите ваше сообщение.</b>")
			text_m[message.from_user.id] = False
			if message.from_user.id in admin_id:
				await message.answer('Наш специалист ответит вам в ближайшее время📧', reply_markup=markups.start_admin_kb)
			else:
				await message.answer('Наш специалист ответит вам в ближайшее время📧', reply_markup=markups.start_kb)
			
			return
	except:
		pass
	#---------------
	#Ответ администратора по айди
	if '@' in message.text and message.chat.id in admin_id:
		u_id = message.text.split('@')
		await bot.send_message(u_id[0], f'Администратор: {u_id[1]}\n\n<b>Чтобы ответить на это сообщение нажмите на кнопку "Напишите нам" и введите свой ответ.</b>')
		return
	#---------------
	
	
	
	
	#=================== ADMIN PANEL ===================
	if message.from_user.id in admin_id:
		if message.text == "🙎‍♂ADMIN🙎‍♂":
			f=open('id_base.txt', 'r')
			all_users = f.readlines()
			f.close()
			f=open('id_active.txt', 'r')
			active_users = f.readlines()
			f.close()
			await message.answer(f"<b>Админ панель пользователя <u>{message.from_user.full_name}({message.from_user.id})</u></b>\n\nВсего пользователей: {len(all_users)}👾\nАктивных пользователей: {len(active_users)}👾", reply_markup=markups.admin_panel)
	if message.text == "👨‍💻Наша команда👨‍💻":
		text_message = f"{hide_link('https://telegra.ph/file/49488f221e9b68970f1cb.jpg')}<b>Геннадий</b>\n\nРуководитель курса - высококвалифицированный специалист с ученой степенью Ph.D с многолетним академическим и профессиональным опытом (о научных работах и конференциях подробнее на сайте). 30 лет работы в немецких государственных структурах и корпорациях – наша гарантия успеха."
		await message.answer(text_message)
		text_message = f"{hide_link('https://telegra.ph/file/5a98ccad631f5cfc682c3.jpg')}<b>Фрау Йокер</b>\n\nСпикер курса – наш человек в Германии, дипломированный педагог с богатым опытом работы в государственных учреждениях ФРГ."
		await message.answer(text_message)
		return
	#=======================================================
	
	#======================= PRICE ========================
	elif message.text == "📑Прайс-лист📑":
		text_message = "<b>Цены💴</b>\nМы не бизнес-структура в общепринятом смысле этого слова, а ученое сообщество и клуб по интересам, хотя в наше время изучение языков – один способов инвестиций.\n\nНаши цены зависят от уровня сложности поставленной задачи, и мы совместно определим их в ходе бесплатного собеседования. Интересные собеседники получают доступ к языковому клубу и внеаудиторным занятиям бесплатно. Мы используем в своей деятельности гибкую систему бонусов для лучших студентов – все зависит от вас!\nНиже вы можете посмотреть цены за наши услуги."
		builder = types.InlineKeyboardMarkup()
		builder.add(types.InlineKeyboardButton(
			text="Индивидуальные занятия",
			callback_data="individual_lessons")
				   )
		builder.add(types.InlineKeyboardButton(
			text="Группа (три человека)",
			callback_data="group_lessons")
				   )
		builder.add(types.InlineKeyboardButton(
			text="Доступ в разговорный клуб",
			callback_data="club_lessons")
				   )
		await message.answer(text_message, reply_markup=builder)
		return
	#=============================================================
	
	
	#==================== REQUEST START ========================
	if message.text == "☎️Заказать звонок☎️":
		name_enter[message.chat.id] = True
		await message.answer("Введите своё Имя👤")
		return
	try:
		if name_enter[message.chat.id] == True:
			name_enter[message.chat.id] = False
			massive_names[message.chat.id] = message.text
			m = ReplyKeyboardMarkup(resize_keyboard=True)
			button1 = KeyboardButton(text="Отправить контакт✍", request_contact=True)
			m.add(button1)
			await message.answer("Отлично, теперь отправьте мне свой контакт✍", reply_markup=m)
			phone_enter[message.chat.id] = True
	except:
		pass
	#=============================================================
    

	
	
	
#=================== REQUEST SEND ==================
@dp.message_handler(content_types=['contact'])
async def contact(message):
	global select
	if message.contact is not None and phone_enter[message.chat.id] == True:
		phonenumber = str(message.contact.phone_number)
		m = InlineKeyboardMarkup()
		button1 = KeyboardButton(text="Принять✅", callback_data=f"ac_{phonenumber}")
		m.add(button1)
		await bot.send_message(chat_id=group_id, text=f"<b>Новая заявка на звонок</b>\n\nТелефон: +{phonenumber}\nИмя: {massive_names[message.chat.id]}\nID: <code>{message.chat.id}</code>", reply_markup=m)
		if message.from_user.id in admin_id:
			await message.answer("<b>Ваша заявка отправлена менеджерам, ожидайте звонка📞</b>", reply_markup=markups.start_admin_kb)
		else:
			await message.answer("<b>Ваша заявка отправлена менеджерам, ожидайте звонка📞</b>", reply_markup=markups.start_kb)
        
        
#=============================================================        
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
@dp.callback_query_handler()
async def callback_data(call: types.CallbackQuery):
	global list_, msg, newssender_state
	call_data = call.data
	
	#==================== USERS INFORMATION ====================
	if call_data == "clear_acu":
		try:
			await bot.delete_message(call.message.chat.id, msg[call.message.chat.id].message_id)
		except:
			pass
		if call.from_user.id in admin_id:
			open("id_active.txt", "w+").close()
			msg[call.message.chat.id] = await call.message.answer('Список активных пользователей очищен.')
			
	elif call_data == "list_active_users":
		try:
			await bot.delete_message(call.message.chat.id, msg[call.message.chat.id].message_id)
		except:
			pass
		if call.from_user.id in admin_id:
			with open('id_active.txt','r') as acu:
				acu_lines = acu.read().split('\n')
				list_ = ""
				for id in acu_lines:
					try:
						chat = await bot.get_chat(id)
						list_ += f"<code>{id}</code> <b>{str(chat.full_name)}</b> - @{str(chat.username)}\n"
					except:
						list_ += f"{id} не найден\n"
				msg[call.message.chat.id] = await bot.send_message(call.from_user.id, 'Список активных пользователей: \n' + str(list_))
				acu.close()
		return
	
	elif call_data == "list_all_users":
		try:
			await bot.delete_message(call.message.chat.id, msg[call.message.chat.id].message_id)
		except:
			pass
		if call.from_user.id in admin_id:
			with open('id_base.txt','r') as acu:
				all_users_lines = acu.read().split('\n')
				list_ = ""
				for id in all_users_lines:
					try:
						chat = await bot.get_chat(id)
						list_ += f"<code>{id}</code> <b>{str(chat.full_name)}</b> - @{str(chat.username)}\n"
					except:
						list_ += f"{id} не найден\n"
				msg[call.message.chat.id] = await bot.send_message(call.from_user.id, 'Список всех пользователей: \n' + str(list_))
				acu.close()
		return
	
	#=============================================================
	
	
	
	#======================== PRICE ==============================
	elif call_data == "individual_lessons":
		try:
			await bot.delete_message(call.message.chat.id, msg[call.message.chat.id].message_id)
		except:
			pass
		text_message = "Тип: <b>Индивидуальные занятия🙋‍♂</b>\n\n Во время индивидуальных занятий вы можете выбрать наиболее удобное для вас расписание, обсуждать с преподавателем сложные вопросы и углубляться в темы, которые наиболее важны для вашего обучения.\n\nЦена занятия за академический час: <b>10$</b> 💴\nОплата производится в валюте резидента."
		msg[call.message.chat.id] = await call.message.answer(text_message)
		return
	
	elif call_data == "group_lessons":
		try:
			await bot.delete_message(call.message.chat.id, msg[call.message.chat.id].message_id)
		except:
			pass
		text_message = "Тип: <b>Занятия в мини-группе из 3 человек👥</b>\n\n В этом формате занятий вы будете учиться вместе с двумя другими студентами, что позволит вам улучшить коммуникативные навыки, узнавать разные точки зрения и делиться знаниями с другими участниками.\n\nЦена занятия за академический час: <b>5$</b> 💴\nОплата производится в валюте резидента."
		msg[call.message.chat.id] = await call.message.answer(text_message)
		return
	elif call_data == "club_lessons":
		try:
			await bot.delete_message(call.message.chat.id, msg[call.message.chat.id].message_id)
		except:
			pass
		text_message = "Тип: <b>Доступ в разговорный клуб👩‍🏫</b>\n\n В рамках языкового клуба вы сможете общаться на немецком языке с другими участниками, практиковать устную речь, улучшать свою грамматику и словарный запас.\n\nЦена занятия за месяц <b>50$</b> 💴\nОплата производится в валюте пользвателя."
		msg = await call.message.answer(text_message)
		return
	
	#=============================================================
	
	
	#=========================== CONSTRUCTOR =========================
	elif call_data == "constructor_posts":
		msg[call.message.chat.id] = await call.message.answer('*Это конструктор постов для рассылки📧\n Тут вы можете создать/удалить/разослать посты всем пользователям телеграмм бота🧖‍♂\nФормат создания постов Фото/Текст/Кнопка📥*', reply_markup=markups.constructor_posts, parse_mode="MarkdownV2")
	#=================================================================
	
	
	
	#=========================== TEXT POST =========================
	elif call_data == "create_text_post":
		try:
			await bot.delete_message(call.message.chat.id, msg[call.message.chat.id].message_id)
		except:
			pass
		msg[str(call.message.chat.id)+" edit"] = await call.message.answer("Пока что ваш текстовый пост пустой.", reply_markup = markups.text_post)
		
	elif call_data == "add_text_tpost":
		msg[call.message.chat.id] = await call.message.answer("*Введите текст рекламного сообщения*\n\nПоддерживаемый язык форматирования текста HTML пример💬: \n\<b\>*Жирный*\</b\> \n\<i\>_Курсивный_\</i\> \n\<u\>__Подчеркнутый__\</u\>", parse_mode="MarkdownV2")
		await text_post_message.text.set()

	elif call_data == "add_button_tpost":
		try:
			await bot.delete_message(call.message.chat.id, msg[call.message.chat.id].message_id)
		except:
			pass
		msg[call.message.chat.id] = await call.message.answer("Введите название кнопки под постом:")
		await text_post_message.button_name.set()
		
	elif call_data == "start_tpost":
		newssender_state = True
		try:
			m = InlineKeyboardMarkup(row_width=1)
			button2 = KeyboardButton(text=text_post_message_static['button_name'], url=text_post_message_static['button_link'])
			m.add(button2)
		except Exception as e:
			print(str(e))
			if str(e) == "'button_name'":
				await call.message.answer('Вы не создали кнопку.')
		baza = open('id_base.txt', 'r')
		text = baza.readlines()
		msg[str(call.message.chat.id) + ' edit_rassilka'] = await bot.send_message(call.message.chat.id, f'<b>Рассылка запущена</b>\nУдалось разослать пользователю: 0/{len(text)}👾', reply_markup=markups.stop_newssender)
		for i in range(len(text)):
			try:
				if newssender_state == False:
					await call.message.answer('Рассылка остановлена !')
					await bot.delete_message(call.message.chat.id, msg[str(call.message.chat.id) + ' edit_rassilka'].message_id)
					return
				await bot.send_message(text[i], text_post_message_static['text'], reply_markup=m)
				await msg[str(call.message.chat.id) + ' edit_rassilka'].edit_text(f'<b>Рассылка запущена</b>\nУдалось разослать пользователю: {i}/{len(text)}👾', reply_markup=markups.stop_newssender)
				print('Удалось разослать пользователю: ' + text[i])
			except Exception as e:
				print(e)
				if str(e) == "Can't parse inline keyboard button: text buttons are unallowed in the inline keyboard":
					await bot.send_message(text[i], text_post_message_static['text'])
					await msg[str(call.message.chat.id) + ' edit_rassilka'].edit_text(f'<b>Рассылка запущена</b>\nУдалось разослать пользователю: {i}/{len(text)}👾', reply_markup=markups.stop_newssender)
					print('Удалось разослать пользователю: ' + text[i])
				elif "wrong http url" in str(e):
					await call.message.answer('Ссылка кнопки не действительна❌')
					await bot.delete_message(call.message.chat.id, msg[str(call.message.chat.id) + ' edit_rassilka'].message_id)
					return
				elif "Message text is empty" in str(e):
					await call.message.answer('Текст рассылки не может быть пустым❌')
					await bot.delete_message(call.message.chat.id, msg[str(call.message.chat.id) + ' edit_rassilka'].message_id)
					return
				continue
		baza.close()
		text_post_message_static['button_link'] = ""
		text_post_message_static['button_name'] = ""
		text_post_message_static['text'] = ""
	#=============================================================	
		
		
	#=========================== MEDIA POST =========================
	elif call_data == "create_media_post":
		try:
			await bot.delete_message(call.message.chat.id, msg[call.message.chat.id].message_id)
		except:
			pass
		msg[str(call.message.chat.id)+" edit_m"] = await bot.send_photo(call.message.chat.id, photo=InputFile("post.png"), caption="Пока что ваш медиа пост пустой.", reply_markup = markups.media_post)

	elif call_data == "add_text_mpost":
		msg[call.message.chat.id] = await call.message.answer("*Введите текст рекламного сообщения*\n\nПоддерживаемый язык форматирования текста HTML пример💬: \n\<b\>*Жирный*\</b\> \n\<i\>_Курсивный_\</i\> \n\<u\>__Подчеркнутый__\</u\>", parse_mode="MarkdownV2")
		await media_post_message.text.set()
	elif call_data == "add_photo":
		msg[call.message.chat.id] = await call.message.answer("Отправьте фото для вашего медиа поста")
		await media_post_message.photo_id.set()
	elif call_data == "add_button_mpost":
		try:
			await bot.delete_message(call.message.chat.id, msg[call.message.chat.id].message_id)
		except:
			pass
		msg[call.message.chat.id] = await call.message.answer("Введите название кнопки под постом:")
		await media_post_message.button_name.set()
		
	elif call_data == "start_mpost":
		newssender_state = True
		try:
			await bot.delete_message(call.message.chat.id, msg[str(call.message.chat.id)+" edit_m"].message_id)
		except:
			pass
		try:
			m = InlineKeyboardMarkup(row_width=1)
			button2 = KeyboardButton(text=media_post_message_static['button_name_m'], url=media_post_message_static['button_link_m'])
			m.add(button2)
		except Exception as e:
			print(str(e))
			if str(e) == "'button_name'":
				await call.message.answer('Вы не создали кнопку !')
		baza = open('id_base.txt', 'r')
		text = baza.readlines()
		msg[str(call.message.chat.id) + ' edit_rassilka_m'] = await bot.send_message(call.message.chat.id, f'<b>Рассылка запущена</b>\nУдалось разослать пользователю: 0/{len(text)}👾', reply_markup=markups.stop_newssender)
		for i in range(len(text)):
			try:
				if newssender_state == False:
					await call.message.answer('Рассылка остановлена !')
					await bot.delete_message(call.message.chat.id, msg[str(call.message.chat.id) + ' edit_rassilka_m'].message_id)
					media_post_message_static['button_link_m'] = ""
					media_post_message_static['button_name_m'] = ""
					media_post_message_static['photo_id'] = ""
					media_post_message_static['text_m'] = ""
					return
				await bot.send_photo(text[i], photo=open("post.png", "rb"), caption=media_post_message_static['text_m'], reply_markup=m)
				await msg[str(call.message.chat.id) + ' edit_rassilka_m'].edit_text(f'<b>Рассылка запущена</b>\nУдалось разослать пользователю: {i}/{len(text)}👾', reply_markup=markups.stop_newssender)
				print('Удалось разослать пользователю: ' + text[i])
			except Exception as e:
				print(e)
				if str(e) == "Can't parse inline keyboard button: text buttons are unallowed in the inline keyboard":
					await bot.send_message(text[i], media_post_message_static['text_m'])
					await msg[str(call.message.chat.id) + ' edit_rassilka_m'].edit_text(f'<b>Рассылка запущена</b>\nУдалось разослать пользователю: {i}/{len(text)}👾', reply_markup=markups.stop_newssender)
					print('Удалось разослать пользователю: ' + text[i])
				elif "wrong http url" in str(e):
					await call.message.answer('Ссылка кнопки не действительна❌')
					await bot.delete_message(call.message.chat.id, msg[str(call.message.chat.id) + ' edit_rassilka_m'].message_id)
					return
				elif "Message text is empty" in str(e):
					await call.message.answer('Текст рассылки не может быть пустым❌')
					await bot.delete_message(call.message.chat.id, msg[str(call.message.chat.id) + ' edit_rassilka_m'].message_id)
					return
				continue
		baza.close()
		media_post_message_static['button_link_m'] = ""
		media_post_message_static['button_name_m'] = ""
		media_post_message_static['photo_id'] = ""
		media_post_message_static['text_m'] = ""
	#=============================================================	
	
	
	
	
	
	
	#=========================== STOP NEWSSENDER =================
	
	elif call_data == "stop_newssender":
		newssender_state = False
		
	#=============================================================	
	
	
	
	
	
	#============================= REQUESTS =======================
	else:
		await bot.edit_message_text(
			chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text=f"{call.message.text}\nВзял в обработку: {call.from_user.first_name}")

		
	#=============================================================	
	
		

		
#=============== TEXT POST FORM =================
@dp.message_handler(state=text_post_message.text)
async def text_tpost_field(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['text'] = message.text
		text_post_message_static['text'] = data['text']
		try:
			await msg[str(message.chat.id)+" edit"].edit_text(text=data['text']
															  + f"\n\nНАЗВАНИЕ КНОПКИ: {text_post_message_static['button_name']}"
															  + f"\nССЫЛКА КНОПКИ: {text_post_message_static['button_link']}",
															  reply_markup=markups.text_post)
		except:
			await msg[str(message.chat.id)+" edit"].edit_text(text=data['text'], reply_markup=markups.text_post)
	
	try:
		await bot.delete_message(message.chat.id, msg[message.chat.id].message_id)
		await bot.delete_message(message.chat.id, message.message_id)
	except:
		pass
	await state.finish()
	
	
	
@dp.message_handler(state=text_post_message.button_name)
async def button_name_tpost_field(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['button_name'] = message.text
		text_post_message_static['button_name'] = data['button_name']
		try:
			await msg[str(message.chat.id)+" edit"].edit_text(text=text_post_message_static['text']
															  + f"\n\nНАЗВАНИЕ КНОПКИ: {data['button_name']}", 
															  reply_markup=markups.text_post)
			msg[str(message.chat.id)+" edit"].text = msg[str(message.chat.id)+" edit"].text + f"\n\nНАЗВАНИЕ КНОПКИ: {message.text}"
		except:
			await msg[str(message.chat.id)+" edit"].edit_text(text=msg[str(message.chat.id)+" edit"].text
												  + f"\n\nНАЗВАНИЕ КНОПКИ: {data['button_name']}", 
												  reply_markup=markups.text_post)
			msg[str(message.chat.id)+" edit"].text = msg[str(message.chat.id)+" edit"].text + f"\n\nНАЗВАНИЕ КНОПКИ: {message.text}"
	try:
		await bot.delete_message(message.chat.id, msg[message.chat.id].message_id)
		await bot.delete_message(message.chat.id, message.message_id)
	except:
		pass
	msg[message.chat.id] = await message.answer("Отправьте ссылку для кнопки: ")
	await text_post_message.button_link.set()
	
	
	
@dp.message_handler(state=text_post_message.button_link)
async def button_link_tpost_field(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['button_link'] = message.text
		text_post_message_static['button_link'] = data['button_link']
		try:
			await msg[str(message.chat.id)+" edit"].edit_text(text=text_post_message_static['text'] 
															  + f"\n\nНАЗВАНИЕ КНОПКИ: {text_post_message_static['button_name']}"
															  + f"\nССЫЛКА КНОПКИ: {data['button_link']}", 
															  reply_markup=markups.text_post)
		except Exception as e:
			print(e)
			await msg[str(message.chat.id)+" edit"].edit_text(text=msg[str(message.chat.id) + " edit"].text
												  + f"\nССЫЛКА КНОПКИ: {data['button_link']}", 
												  reply_markup=markups.text_post)
	try:
		await bot.delete_message(message.chat.id, msg[message.chat.id].message_id)
		await bot.delete_message(message.chat.id, message.message_id)
	except:
		pass
	await state.finish()

#=============================================================		
		
		
		


#=============== MEDIA POST FORM =================
@dp.message_handler(state=media_post_message.text)
async def text_mpost_field(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['text_m'] = message.text
		media_post_message_static['text_m'] = data['text_m']


		try:
			file_except1 = InputMedia(media=InputFile("post.png"), caption=media_post_message_static['text_m']
																		   + f"\n\nНАЗВАНИЕ КНОПКИ: {media_post_message_static['button_name_m']}"
																		   + f"\nССЫЛКА КНОПКИ: {media_post_message_static['button_link_m']}")
			await msg[str(message.chat.id)+" edit_m"].edit_media(media=file_except1,
															  reply_markup=markups.media_post)
			msg[str(message.chat.id) + " edit_m"].caption = msg[
															 str(message.chat.id) + " edit_m"].caption
		except Exception as e:
			print(e)
			file_except2 = InputMedia(media=InputFile("post.png"), caption=data['text_m'])
			await msg[str(message.chat.id)+" edit_m"].edit_media(media=file_except2,
															  reply_markup=markups.media_post)
			msg[str(message.chat.id) + " edit_m"].caption = msg[
															str(message.chat.id) + " edit_m"].caption
	try:
		await bot.delete_message(message.chat.id, msg[message.chat.id].message_id)
		await bot.delete_message(message.chat.id, message.message_id)
	except:
		pass
	await state.finish()
	
	
	
@dp.message_handler(state=media_post_message.button_name)
async def button_name_mpost_field(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['button_name_m'] = message.text
		media_post_message_static['button_name_m'] = data['button_name_m']

		try:
			file_except1 = InputMedia(media=InputFile("post.png"), caption=data['text_m']
																		   + f"\n\nНАЗВАНИЕ КНОПКИ: {media_post_message_static['button_name_m']}")
			await msg[str(message.chat.id)+" edit_m"].edit_media(media=file_except1,
															  reply_markup=markups.media_post)
			msg[str(message.chat.id)+" edit_m"].caption = msg[str(message.chat.id)+" edit_m"].caption + f"\n\nНАЗВАНИЕ КНОПКИ: {message.text}"
		except:
			file_except2 = InputMedia(media=InputFile("post.png"), caption=msg[str(message.chat.id) + " edit_m"].caption
																		   + f"\n\nНАЗВАНИЕ КНОПКИ: {data['button_name_m']}")
			await msg[str(message.chat.id)+" edit_m"].edit_media(media=file_except2,
															  reply_markup=markups.media_post)
			msg[str(message.chat.id)+" edit_m"].caption = msg[str(message.chat.id)+" edit_m"].caption + f"\n\nНАЗВАНИЕ КНОПКИ: {message.text}"
	try:
		await bot.delete_message(message.chat.id, msg[message.chat.id].message_id)
		await bot.delete_message(message.chat.id, message.message_id)
	except:
		pass
	msg[message.chat.id] = await message.answer("Отправьте ссылку для кнопки: ")
	await media_post_message.button_link.set()
	
	
	
@dp.message_handler(state=media_post_message.button_link)
async def button_link_mpost_field(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['button_link_m'] = message.text
		media_post_message_static['button_link_m'] = data['button_link_m']

		try:

			file_except1 = InputMedia(media=InputFile("post.png"), caption=media_post_message_static['text_m']
																		   + f"\n\nНАЗВАНИЕ КНОПКИ: {media_post_message_static['button_name_m']}"
																		   + f"\nССЫЛКА КНОПКИ: {data['button_link']}")
			await msg[str(message.chat.id)+" edit_m"].edit_media(media=file_except1,
															  reply_markup=markups.media_post)
		except Exception as e:
			file_except2 = InputMedia(media=InputFile("post.png"), caption=msg[str(message.chat.id) + " edit_m"].caption
																		   + f"\nССЫЛКА КНОПКИ: {data['button_link_m']}")
			print(e)
			await msg[str(message.chat.id)+" edit_m"].edit_media(media=file_except2,
															  reply_markup=markups.media_post)

	try:
		await bot.delete_message(message.chat.id, msg[message.chat.id].message_id)
		await bot.delete_message(message.chat.id, message.message_id)
	except:
		pass
	await state.finish()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=media_post_message.photo_id)
async def process_photo(message: types.Message, state: FSMContext):
	photo_id = message.photo[-1].file_id
	async with state.proxy() as data:
		data['photo_id'] = photo_id
		photo = await bot.get_file(data['photo_id'])
		await photo.download(f"post.png")
		try:

			file_except1 = InputMedia(media=InputFile("post.png"), caption=media_post_message_static['text_m']
																		   + f"\n\nНАЗВАНИЕ КНОПКИ: {media_post_message_static['button_name_m']}"
																		   + f"\nССЫЛКА КНОПКИ: {data['button_link']}")
			await msg[str(message.chat.id)+" edit_m"].edit_media(media=file_except1,
															  reply_markup=markups.media_post)
		except Exception as e:
			print(e)
			try:
				file_except2 = InputMedia(media=InputFile("post.png"), caption=msg[str(message.chat.id) + " edit_m"].caption
																			   + f"\nССЫЛКА КНОПКИ: {data['button_link_m']}")

				await msg[str(message.chat.id)+" edit_m"].edit_media(media=file_except2,
																  reply_markup=markups.media_post)
			except Exception as e:
				print(e)
				file_except3 = InputMedia(media=InputFile("post.png"), caption=media_post_message_static['text_m'])
				await msg[str(message.chat.id)+" edit_m"].edit_media(media=file_except3,
																  reply_markup=markups.media_post)
	try:
		await bot.delete_message(message.chat.id, msg[message.chat.id].message_id)
		await bot.delete_message(message.chat.id, message.message_id)
	except:
		pass
	msg[message.chat.id] = await message.answer("Фото поста успешно загружено!")
	await state.finish()



#=============================================================		
		
		

		
		
		
async def main(_):
	#---------------
	#Сообщение о запуске бота!
	for i in admin_id:
		await bot.send_message(i, text='<b>Система информирования:</b>\nБот запущен!')
	print("bot started")

if __name__ == '__main__':
	#---------------
	#Инициализация запуска
	print('Успешно cоеденено')
	executor.start_polling(dp, skip_updates=True, on_startup=main)

