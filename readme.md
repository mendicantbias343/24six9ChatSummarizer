# Whatsapp Chat Summarizer
This tool helps you summarize group chats by day and display it on a website.  
To do run this locally, there are 4 things you need to do:

1. Download Chat from Whatsapp group
2. Get an OPEN AI API key
3. Have Node & Python environment setup
4. Running the code

Let's get started.

***Disclaimer to any developer reading this***: 
_I'm not a developer. I can code, sort of... so if you jarring mistakes, please forgive the product manager who thought he could._

## 1. Downloading your chats
You can follow [this](https://www.marca.com/en/lifestyle/how-to/2021/11/10/618bbe63ca4741b2138b4608.html) article to get the specifics, but the main things to consider are:
1. The chat should be exported in a txt format.
2. The chat should not contain links to media (increases the token count without any benefit)
3. The file should not be modified (it breaks the extraction process)

I personally use the option to export the chat from my phone and forward it to one my other numbers. I can then open Whatsapp for Web and download it from there.  
Store this file as chat.txt in the root folder.

## 2. Get OPEN AI API Key
Follow [this](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/) link.  
Once you get your key (sk-*******...), create a new file in your root folder: ```.env```

Open the file and save the key as:
```
OPENAI_KEY = <YOUR API KEY, starting with sk>
```
Save the file.

## 3. Install NodeJS & Python
Download NodeJS [here](https://nodejs.org/en/download) and install it. It's fairly straight forward. If you're on Mac, install [Homebrew](https://brew.sh/) to make things easier to manage. 

Install [Python](https://www.python.org/downloads/), whichever way you like (Homebrew/download).

Also, download VS Code. It'll make development super-easy.

### 3.1 Download this repository
You can download this or clone it, by clicking on the big green button that says \<CODE\> on this page. Remember to extract it to a place where you can come back.

### 3.2 Install the packages - Python
Once you've cd'd into the root of the code, type the following:
```
pip install -r requirements.txt
```
This will install the libraries used in the Python code. For some reason, ```pipreq``` thinks that there are only two packages involved. YMMV.

### 3.3 Install the modules - Node
To install the node modules, type the following commands:
```
> cd frontend
> npm install
```
This will take some time, since it is installing a lot of things. You shouldn't face any issues during this process. If you do, please ping me.

## 4. Running the code
Once you have done all the above steps, you can now modify the ```init.py``` file. You can uncomment the line:
```
# dates = ["29/07/2023","30/07/2023"]
```
by removing the # and proceed to setup the dates yourself. Or you can keep the line commented and use the function ```get_last_n_days```.

_Note: When you use this function, it is important that the dates are present in the chat (atleast the current date). The function returns a list of dates from today to N days ago - and if you don't have an instance of that date in your chat history, you'll have a bad time._

Before you run this code, navigate to the ``frontend/content`` folder and remove the ```final_data.json```

Run the code:

```
python init.py
```

It should tell you when the execution is over and the file is written. If all goes well, you shouldn't be hit with any errors and a new file should be created in the ``frontend/content`` folder.

Next, run the following commands:

```
cd frontend
npm run dev
```

You can click on the link in the terminal (most probably it'll be [localhost:3000](http://localhost:3000))

Enjoy!

----

<br>

# Understanding the code
This is a fairly straight forward code. There are only a few steps in the Python side, and nearly none (in terms of modification in the JS side).

## Code flow
The below is an abstraction of the code flow:

1. Extract the relevant chats for each date that we're concerned with... the dates are in a date array (and can be changed depending upon what you pass to the function ```get_last_n_days```).
2. Call OpenAI API and get them to do our bidding: respond with the summary in a JSON format.
3. Fetch the current data from the ```final_data.json``` file in the ```frontend/content``` directory and merge it with new JSON we've generated and write back to the file.
4. Profit!

The key idea here is that since I'm using Server Side Rendering, my entire data can be stored in a single JSON object, which I import at the beginning and there are no server calls for subsequent renders/page changes.

Additionally, there is advantage in this process - I'm writing to the frontend directory, which also happens to be the source for my vercel application. Every time I commit the repo, the Vercel app updates and I don't have to do a lot of testing.

# Costs
Using OPEN AI is cheaper than I thought it would be.
I've used around 150k tokens in testing & deployment and it has cost me only $1.

The chat limitation is 16k tokens for the model we're using (`gpt-3.5-turbo-16k-0613`). That translates to around 2000 lines. YMMV.

# Roadmap
I'm planning to add the following functionalities:

1. Verbose description of the topics
2. Search by topic
3. See all hiring requirements by date
4. Weekly view
5. Categorizing topics
6. Leaderboards for contributors (based on quantity)
7. [Technical] Using components insteading of vomitting html in the pages
8. Changelog page
9. Analytics
10. Bug fixes

# Contribution
You can always contribute to the code. I don't know how it's done, but here are some things I need help with:

1. The link are looking meh, at the moment. I want to show them as social sharing cards with information (image, title, short description) without any server side rendering. 
2. Better UI? Any help on that would be appreciated. 

Any help would be appreciated. 

