import os
from dotenv import load_dotenv
import openai
from datetime import datetime, timedelta
from itertools import islice
import json


def find_line_number(data, target):
    lines = data.split('\n')
    line_number = None

    for idx, line in enumerate(lines, 1):
        if target in line:
            line_number = idx
            break

    return line_number


def get_last_n_days(n):
    date_format = "%d/%m/%Y"
    today = datetime.now()
    seven_days_ago = today - timedelta(days=n)

    date_list = []
    current_date = seven_days_ago
    while current_date <= today:
        date_list.append(current_date.strftime(date_format))
        current_date += timedelta(days=1)

    return date_list


dates = get_last_n_days(17) 
#dates = ['12/07/2023', '13/07/2023', '14/07/2023', '15/07/2023', '16/07/2023', '17/07/2023', '18/07/2023', '19/07/2023', '20/07/2023', '21/07/2023', '22/07/2023', '23/07/2023', '24/07/2023', '25/07/2023', '26/07/2023', '27/07/2023', '28/07/2023', '29/07/2023', '30/07/2023']
dates = [ '21/08/2023', '22/08/2023', '23/08/2023', '24/08/2023', '25/08/2023', '26/08/2023', '27/08/2023', '28/08/2023', '29/08/2023', '30/08/2023', '31/08/2023', '01/09/2023', '02/09/2023', '03/09/2023', '04/09/2023', '05/09/2023']
# print(dates)
# exit()

with open('./chat.txt', encoding='utf8') as f:
    content = f.read()
    lines = content.split("\n")
    last_line_number = len(lines)

ln_list = []

# load the line numbers in a simple list:
for index, date in enumerate(dates):
    try:
        ln_list.append(find_line_number(content, date))
    except:
        ln_list.append(find_line_number(content, dates[index-1]))
        print("not found")
ln_list.append(last_line_number)

# the daily chats are between ln1 & ln2 of the above list. Let's go get it and store in a separate var

chat_list = []

for i, ln in enumerate(ln_list):
    print(type(ln))
    if (ln != last_line_number):
        with open('chat.txt', encoding='utf-8') as f:
            if (type(ln_list[i+1]) is int and type(ln) is int):
                lines = list(islice(f, ln - 1, ln_list[i+1]))
                chat_list.append(lines)

# New function that removes the initial timestamp (we don't need it and it adds to our tokens usage)
# We'll just look for the first instance of "-" and remove everything till that point.


def sanitize_text(chat_lines):
    sanitized_list = []
    for line in chat_lines:
        # first clean up
        find_char = line[0:40].find(" - ")
        # second_index_of_colon = line[first_index_of_colon + 1:].find(":")
        if (find_char > 0):
            ln = line[find_char + 3:]
            ln = ln[ln.find(":") + 1:]
        else:
            ln = line

        # second clean up
        if (ln.find("joined from the community") > 0):
            ln = ''

        if (ln.find("<Media omitted>") > 0):
            ln = ''

        if (ln.find("joined using this group's invite link") > 0):
            ln = ''

        ln.replace("<This message was edited>", " ")

        if (ln != ''):
            sanitized_list.append(ln)
    return sanitized_list


sanit_chat_list = []

for chats in chat_list:
    sanit_chat_list.append(sanitize_text(chats))

# print(sanit_chat_list)

# now that the list is decently sanitized:
# it's time to invoke ChatGPT to get things going

load_dotenv()

print("START OPEN AI CALL")
openai.api_key = os.environ.get("OPENAI_KEY")

final_obj = []

for index, date in enumerate(dates):
    if( index < len(sanit_chat_list)):
        print("Calling " + str(index) + "for the date: " + date)
        message = [{
            "role": "system",
            "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following chat and summarize it into a concise topics (min 3, max 10).Don't use vague terms like various topics. Each topic has to be unique and not related to the next one. When you're giving the detailed topic summary, please retain links and important conversation pieces. Your response should be in a JSON format: { main_topics: [{ topic : '<list of main themes covered>', 'search_terms': [<2-3 unique search terms that are present in the text>], detailed_topic_summary: <verbose discussion details. minimum 70 words.>, key_points: [ list of points made by individuals]}, hiring_requests: <list of roles hired for as an array>, links: <list of links shared as an array>}"

        },
            {
            "role": "user",
            "content": "Below is a chat from a whatsapp group. Please summarize it as per the instructions given: " + " ".join(sanit_chat_list[index])
        }
        ]
        try:
            chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k-0613", messages=message)
            try:
                d = json.loads(chat_completion.choices[0].message.content)
            except RuntimeError:
                print(chat_completion.choices[0].message.content)
            # replace the date to the accepted value
            print("Call to " + str(index) + " done.")
            d["date"] = date.replace('/', '')
            final_obj.append(d)
        except RuntimeError:
            print("ERRROR!")
            print(RuntimeError)

datax = []

with open('frontend/content/final_data.json', 'r') as f:
    try:
        datax = json.load(f)
        datax.extend(final_obj)
    except:
        datax = []
        datax.extend(final_obj)

with open('frontend/content/final_data.json', 'w') as f:
    json.dump(datax,f)
