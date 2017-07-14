#HTML-GTK PLAYER Copyright (c) 2017 JJ Posti <techtimejourney.net> 
#This program comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")
#!/usr/bin/env python
import sys
from gi.repository import Gtk, Gdk, WebKit, GObject

class HTML_5(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super(HTML_5, self).__init__(*args, **kwargs)
    def __init__(self):    
    # Create THE WINDOW
        self.window1=Gtk.Window()
        self.window1.set_position(Gtk.WindowPosition.CENTER)
        self.window1.set_default_size(800, 600)
        self.window1.set_title("HTML-GTK PLAYER")
        self.window1.connect("destroy", Gtk.main_quit)
#####################
#Webview
#######################
        self.web = WebKit.WebView()
        self.show()        
#######################
#User agent settings
######################  
        self.agent=self.web.get_settings()
        self.agent.set_property('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64: rv:52.0) Gecko/20100101 Firefox/52.0')
        self.agent.set_property("enable-plugins", True)
        self.agent.set_property("enable-dom-paste", True)
        self.agent.set_property("enable-private-browsing", True)
        self.agent.set_property("enable-spatial-navigation", True)
        self.agent.set_property('enable-default-context-menu', True)
        self.agent.set_property('enable-fullscreen', True)
        self.agent.set_property('enable-media-stream', True)
        self.agent.set_property('enable-webaudio', True)
        self.web.set_settings(self.agent)  
######################################################
#Toolbar/Scrolled Window
###################################################
#Youtube
        self.tube_button=Gtk.Button()
        self.tube_button.connect("clicked", self.tube)
        self.tube_button.set_label("Youtube")

#Dailymotion
        self.daily_button=Gtk.Button()
        self.daily_button.connect("clicked", self.daily)
        self.daily_button.set_label("Dailymotion") 
        
#Vimeo
        self.vimeo_button=Gtk.Button()
        self.vimeo_button.connect("clicked", self.vimeo)
        self.vimeo_button.set_label("Vimeo")               
#About
        self.about_button=Gtk.Button()
        self.about_button.connect("clicked", self.about1)
        self.about_button.set_label("About HTML-GTK Player")        
#Scrolled Window
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.web)

#####################################
#Main Box
        self.hbox=Gtk.HBox()
        self.hbox.pack_start(self.tube_button, False, False, 2)
        self.hbox.pack_start(self.daily_button, False, False, 2)
        self.hbox.pack_start(self.vimeo_button, False, False, 2)
        self.hbox.pack_start(self.about_button, False, False, 2)
                
        self.vbox2=Gtk.VBox()
        self.vbox2.pack_start(self.hbox, False, False, 0)
        self.vbox2.pack_start(scrolled_window, True, True, 0)

#Show everything		
        self.window1.add(self.vbox2)
        self.window1.show_all()   
#Functions
################
    def tube(self,widget):
        self.web.load_uri("https://www.youtube.com")
        self.hbox.hide()
  
    def vimeo(self,widget):
        self.web.load_uri("https://www.vimeo.com")
        self.hbox.hide()

    def daily(self,widget):
        self.web.load_uri("http://www.dailymotion.com")
        self.hbox.hide()
               		  		                    	        
#About dialog function
    def about1 (self, widget):
        about1 = Gtk.AboutDialog()
        about1.set_program_name("HTML-GTK-PLAYER")
        about1.set_version("0.2")
        about1.set_copyright(" Copyright (c) 2017 JJ Posti <techtimejourney.net>")
        about1.set_comments("This program comes with ABSOLUTELY NO WARRANTY; for details see: http://www.gnu.org/copyleft/gpl.html. This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991.---------------------------------------------------------------------------")
        about1.set_website("www.techtimejourney.net")
        about1.run()
        about1.destroy()         
if __name__ == "__main__":
    Gtk.init(sys.argv)
    browser = HTML_5()
    Gtk.main()
