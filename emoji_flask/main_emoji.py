import emojis

#  pip install emojis
print(emojis.encode('This is a message with emojis :smile: :snake:'))
print(emojis.decode('This is a message with emojis 😄 🐍 🐢'))
print(emojis.get('Prefix 😄 🐍 😄 🐍 Sufix'))
print(emojis.count('😄 🐍 😄 🐍'))
print(emojis.count('😄 🐍 😄 🐢', unique=True))
print(emojis.db.get_emoji_by_alias('snake'))
print(emojis.db.get_categories())
