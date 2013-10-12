import webbrowser

class myBrowserOpener():
    def __init__(self):
        self.fireFoxController = webbrowser.get('firefox')
    def openIESite(self, url):
        webbrowser.open(url)
    def openFireFox(self, url):
        self.fireFoxController.open(url)


##ffController = webbrowser.get('firefox')
##ffController.open('www.google.com')
#webbrowser.open('www.google.com')
