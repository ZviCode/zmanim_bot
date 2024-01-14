from pyrogram import Client, filters
import requests
from pyrogram import enums

app = Client("my_account")


@app.on_message(~filters.location)
def start(client, message):
    message.reply_text("יש לשלוח מיקום")


@app.on_message(filters.location)
def location(client, message):
    app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    url = f"https://www.hebcal.com/zmanim?cfg=json&latitude={message.location.latitude}&longitude={message.location.longitude}"
    response = requests.get(url)
    data = response.json()
    text_to_replay = f"הזמנים נכונים לתאריך : {data['date']}\n\n" \
                        f"חצות הלילה : {data['times']['chatzotNight'].split('T')[1].split( '+')[0]}\n" \
                        f"עלות השחר : {data['times']['alotHaShachar'].split('T')[1].split( '+')[0]}\n" \
                        f"משיכיר : {data['times']['misheyakir'].split('T')[1].split( '+')[0]}\n" \
                        f"משיכיר מחמיר : {data['times']['misheyakirMachmir'].split('T')[1].split( '+')[0]}\n" \
                        f"זריחה : {data['times']['sunrise'].split('T')[1].split( '+')[0]}\n" \
                        f"סוף זמן שמע : {data['times']['sofZmanShma'].split('T')[1].split( '+')[0]}\n" \
                        f"סוף זמן שמע מגן אברהם : {data['times']['sofZmanShmaMGA'].split('T')[1].split( '+')[0]}\n" \
                        f"סוף זמן תפילה : {data['times']['sofZmanTfilla'].split('T')[1].split( '+')[0]}\n" \
                        f"סוף זמן תפילה מגן אברהם : {data['times']['sofZmanTfillaMGA'].split('T')[1].split( '+')[0]}\n" \
                        f"חצות : {data['times']['chatzot'].split('T')[1].split( '+')[0]}\n" \
                        f"מנחה גדולה : {data['times']['minchaGedola'].split('T')[1].split( '+')[0]}\n" \
                        f"מנחה קטנה : {data['times']['minchaKetana'].split('T')[1].split( '+')[0]}\n" \
                        f"פלג המנחה : {data['times']['plagHaMincha'].split('T')[1].split( '+')[0]}\n" \
                        f"שקיעה : {data['times']['sunset'].split('T')[1].split( '+')[0]}\n" \
                        f"בין הערביים : {data['times']['dusk'].split('T')[1].split( '+')[0]}\n" \
                        f"צאת הכוכבים 42 דקות : {data['times']['tzeit42min'].split('T')[1].split( '+')[0]}\n" \
                        f"צאת הכוכבים 50 דקות : {data['times']['tzeit50min'].split('T')[1].split( '+')[0]}\n" \
                        f"צאת הכוכבים 72 דקות : {data['times']['tzeit72min'].split('T')[1].split( '+')[0]}\n\n" \
                        f"הזמנים מתקבלים מ [hebcal ](https://www.hebcal.com) ואין לסמוך עליהם להלכה"
    message.reply_text(text_to_replay)


app.run()

