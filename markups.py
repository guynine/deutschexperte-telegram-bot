import aiogram
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = [
      [types.KeyboardButton(text="☎️Заказать звонок☎️")],
      [types.KeyboardButton(text="📑Прайс-лист📑")],
      #[types.KeyboardButton(text="Как устроен курс?")],
      #[types.KeyboardButton(text="Для кого предназначены наши курсы?")],
      #[types.KeyboardButton(text="Наши модули для изучения немецкого языка")],
      #[types.KeyboardButton(text="К какой цели мы стремимся?")],
      [types.KeyboardButton(text="👨‍💻Наша команда👨‍💻")],
      [types.KeyboardButton(text='💻Напишите нам💻')],]
start_kb = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Навигационная панель")



admin_kb = [
      [types.KeyboardButton(text='🙎‍♂ADMIN🙎‍♂')],
      [types.KeyboardButton(text="☎️Заказать звонок☎️")],
      [types.KeyboardButton(text="📑Прайс-лист📑")],
      #[types.KeyboardButton(text="Как устроен курс?")],
      #[types.KeyboardButton(text="Для кого предназначены наши курсы?")],
      #[types.KeyboardButton(text="Наши модули для изучения немецкого языка")],
      #[types.KeyboardButton(text="К какой цели мы стремимся?")],
      [types.KeyboardButton(text="👨‍💻Наша команда👨‍💻")],
		[types.KeyboardButton(text='💻Напишите нам💻')],]
start_admin_kb = types.ReplyKeyboardMarkup(keyboard=admin_kb, resize_keyboard=True, input_field_placeholder="Навигационная панель")



admin_panel = types.InlineKeyboardMarkup()
admin_panel.add(types.InlineKeyboardButton(
 text="Список всех пользователей",
 callback_data="list_all_users")
		)
admin_panel.add(types.InlineKeyboardButton(
 text="Список активных пользователей",
 callback_data="list_active_users")
		)
admin_panel.add(types.InlineKeyboardButton(
 text="Очистить список активных пользователей",
 callback_data="clear_acu")
		)
admin_panel.add(types.InlineKeyboardButton(
 text="Конструктор постов",
 callback_data="constructor_posts")
		)



constructor_posts = types.InlineKeyboardMarkup()
constructor_posts.add(types.InlineKeyboardButton(
 text="Создать текстовый пост",
 callback_data="create_text_post")
		)
constructor_posts.add(types.InlineKeyboardButton(
 text="Создать медиа пост",
 callback_data="create_media_post")
		)




text_post = types.InlineKeyboardMarkup()
text_post.add(types.InlineKeyboardButton(
 text="Добавить текст",
 callback_data="add_text_tpost")
		)
text_post.add(types.InlineKeyboardButton(
 text="Добавить кнопку",
 callback_data="add_button_tpost")
		)
text_post.add(types.InlineKeyboardButton(
 text="Начать рассылку",
 callback_data="start_tpost")
		)




media_post = types.InlineKeyboardMarkup()
media_post.add(types.InlineKeyboardButton(
 text="Добавить фото",
 callback_data="add_photo")
		)
media_post.add(types.InlineKeyboardButton(
 text="Добавить текст",
 callback_data="add_text_mpost")
		)
media_post.add(types.InlineKeyboardButton(
 text="Добавить кнопку",
 callback_data="add_button_mpost")
		)
media_post.add(types.InlineKeyboardButton(
 text="Начать рассылку",
 callback_data="start_mpost")
		)





stop_newssender = types.InlineKeyboardMarkup()
stop_newssender.add(types.InlineKeyboardButton(
 text="Остановить❌",
 callback_data="stop_newssender")
		)
