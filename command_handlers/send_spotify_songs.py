import os
import uuid

from command_handlers.helpers import spotdl
from telegram import Update
from telegram.ext import CallbackContext


def send_spotify_songs(update: Update, context: CallbackContext):
    song_link = context.args[0]
    download_path = os.getcwd() + "/" + str(uuid.uuid4())

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"I'm downloading this song, please wait a while"
    )

    spotdl.download_from_spotify(download_path, song_link)
    spotdl.send_songs_from_directory(download_path, update, context)

    context.bot.send_message(chat_id=update.effective_chat.id, text="finished! If u can't see this please retry again or contact support here @SpotifySupportbot")
