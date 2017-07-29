import rumps
import datetime

@rumps.clicked("About")
def about(sender):
    rumps.alert("Simple work week app")

@rumps.timer(3600)  # create a new thread that calls the decorated function every 4 seconds
def update_ww(sender):
    week = datetime.datetime.now().isocalendar()[1]
    app.title = 'WW{}'.format(week)

if __name__ == "__main__":
    week = datetime.datetime.now().isocalendar()[1]
    app = rumps.App("Work Week", title='WW{}'.format(week))
    app.menu = [
        rumps.MenuItem('About'),  # can specify an icon to be placed near text
    ]
    app.run()
