@Client.on_chat_join_request(filters.group | filters.channel)
async def autoapprove(c, m):
    await c.db.add_user(m.from_user.id)
    try:
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
        button = [[
            InlineKeyboardButton('🔰 JOIN MAIN CHANNEL🔰 ', url='https://t.me/Nazzymovies1')
            ],[
            InlineKeyboardButton('♻️ REQUEST GROUP ♻️', url='https://t.me/nazzymovies')
        ]]
        markup = InlineKeyboardMarkup(button)
        caption = f'Hello {m.from_user.mention()}\nYou Request To Join {m.chat.title} Was Approved.'
        await c.send_photo(
            m.from_user.id, 
            photo='https://te.legra.ph/file/b04fa018b48222755d3fe.jpg', 
            caption=caption, 
            reply_markup=markup
        )
    except UserIsBlocked:
        print(f"{m.from_user.first_name} blocked the bot")
    except PeerIdInvalid:
        print(f"User {m.from_user.first_name} haven't started the bot yet")
    except Exception as e:
        print('Error:', e)
