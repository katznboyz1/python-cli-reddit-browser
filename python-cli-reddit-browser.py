#make it so that you can load a previously made manifest file instead of using the default one, also make it so that the manifest autosaves every time <redditBrowser.main> is called.
#the screenback command doesnt work

import os, sys, urllib.request #import the needed packages

class redditBrowser: #the main class for the application
    manifest = { #the dict that will contain all the data for the app
        'redditURL':'https://reddit.com', #the base URL for the app
        'currentSubreddit':'all', #the subreddit that the window is focused on
        'OS':None, #this is used to tell what OS the app is running on
        'running':True, #this is used to make sure that the application is still running
        'screen':'home', #this is used to tell what screen the user is on
        'lastScreen':'home', #this is used to roll back the screen
        'lastCommand':'screenset home', #this is used to tell what the last command was
    }

    def main() -> None:
        os.system('cls' if redditBrowser.manifest['OS'] == 'windowsOS' else 'clear') #clears all stdout on the screen

        lastCommand = redditBrowser.manifest['lastCommand'].split(' ') #splits the command into pieces
        passCurrentInput = False
        if (lastCommand[0] == 'screenset'):
            try:
                redditBrowser.manifest['screen'] = str(lastCommand[1])
            except IndexError:
                print ('IndexError - Not enough or too many arguments for "{}".'.format(lastCommand[0]))
        elif (lastCommand[0] == 'help'):
            passCurrentInput = True
            redditBrowser.manifest['screen'] = 'help'
            redditBrowser.manifest['lastCommand'] = 'pass'
        elif (lastCommand[0] == 'screenback'):
            redditBrowser.manifest['screen'] = redditBrowser.manifest['lastScreen']
        elif (lastCommand[0] == 'exit'):
            redditBrowser.manifest['running'] = False
            exit()

        currentScreen = redditBrowser.manifest['screen']
        print ('Current screen: {} | Last screen: {}'.format(currentScreen, redditBrowser.manifest['lastScreen']))
        if (currentScreen.split(':')[0] == 'home'):
            print ('Command Line Reddit Browser Tool - Made by katznboyz/katznboyz1 (2019).')
            print ('Type "help" for a list of commands.')
        if (currentScreen.split(':')[0] == 'help'):
            print ('''
Reddit Browser Help Menu:
    List Of Commands:
        help - Changes the screen to the help menu.
        pass - Does nothing.
        screenset <screen> - Sets the current screen to that screen.
        screenback - Resets the screen to the last screen, can only be done once in a row.
        exit - Exits the application.
    List Of Screens:
        home - The main intro/credits screen.
        redditPostOverview - The screen where you can view a list of reddit posts.
        redditCommentsSection - The screen where you can view the post\'s content and the comments that are available.
''')

        if (passCurrentInput):
            redditBrowser.main()
        else:
            redditBrowser.manifest['lastScreen'] = currentScreen
            redditBrowser.manifest['lastCommand'] = str(input('python-cli-reddit-browser$ ')) #the input where you will type in the command

if (sys.platform in ['win32', 'win64']): #checks what platform the program is running on, which will be used to determine which commands will be used
    redditBrowser.manifest['OS'] = 'windowsOS'
else:
    redditBrowser.manifest['OS'] == 'unixLikeOS' #this may not always work but its worth a shot...

while (redditBrowser.manifest['running']):
    redditBrowser.main()