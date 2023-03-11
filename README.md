# E-Paper-tibber-Preisanzeige
Diese Information richtet sich an alle Nutzer von Tibber oder an die, die es werden wollen, dem Stromanbieter. Natürlich könnt ihr das Display auch für andere Zwecke nutzen.
Die Funktion der Anzeige zeige ich euch in einem Video: https://youtu.be/tMlHQ7NlYro

Hey, hier ist dein individueller Einladungscode für Tibber, den Stromanbieter, der dir hilft, deinen Stromverbrauch zu verstehen und zu reduzieren: https://invite.tibber.com/Techpirat. Du erhältst 100 % Ökostrom und kannst jederzeit mit einer Frist von 2 Wochen kündigen. Probiere es aus, und wir erhalten beide 50 € Bonus für den Tibber-Store.

Die Idee ist, den aktuellen Strompreis vom Stromanbieter Tibber auf dem Waveshare 7.5 Inch E-Paper Display anzuzeigen. Hast du noch keinen Waveshare 7.5 Inch E-Paper Display? Dann kannst du ihn hier kaufen: https://amzn.to/3Jxacx3. Mein Code ist erstellt und getestet mit Python 3.9.2. Ihr braucht auch einen Raspberry Pi Zero WH, das kannst du hier kaufen: https://amzn.to/3JxkLA9.

Als erstes müsst ihr eine SD-Karte mit dem Betriebssystem beschreiben. Dazu nutzt ihr am besten https://www.raspberrypi.com/software/operating-systems/.
Im Video zeige ich, wie ihr es am besten einrichtet. Nicht vergessen, das Display mit dem Raspberry Pi Zero zu verbinden.

Ihr müsst auch die lokale IP-Adresse des Raspberry Pi herausfinden. Diese findet ihr über euren Router. In meinem Fall ist es 192.168.2.186. Über die IP könnt ihr euch mit dem Raspberry Pi per VNC oder SSH (mit einer Terminal-Software) verbinden.

Ist euer Raspberry Pi Zero installiert und mit dem WLAN erfolgreich verbunden, müsst ihr euch als erstes per SSH verbinden und "sudo raspi-config" über die Konsole aufrufen und folgende Schritte abarbeiten:
Interface Options > VNC > Enable > Save. Bevor ihr neu startet, nochmal zurück zum Hauptmenü:
Display Options > VNC Resolution > und hier eure gewünschte Auflösung festlegen.
Ich nutze 1280 x 1024.

Jetzt könnt ihr euch über VNC verbinden und die Dateien hochladen. Dateien, die ihr über VNC hochladet, werden auf dem Desktop gespeichert.
Mit einem Doppelklick auf eines der beiden Skripte öffnet sich der Editor. Damit könnt ihr die beiden Skripte testen. Sollten Fehlermeldungen kommen, diese systematisch abarbeiten.

Bitte folgende Module installieren und importieren:
PIL 
tkinter
matplotlib
requests
numpy

Python-Module werden mit "pip install PIL" installiert. In diesem Fall installieren wir "PIL". Das Modul "waveshare_epd" wird mitgeliefert und muss nicht installiert werden.

Um die Echtzeit-Preisanzeige zu bekommen, braucht ihr einen API-Key von Tibber. Euren Tibber API-Key bekommt ihr hier: https://developer.tibber.com/settings/access-token. Einfach dort mit euren normalen Zugangsdaten anmelden. Diesen müsst ihr an der entsprechenden Stelle in der Datei api_key.py eintragen.

Mit "crontab -e" könnt ihr einen Job anlegen. Hier ein Beispiel:
3**** python3 /home/joerg/Desktop/e-paper/speicher_chart_heute.py >/dev/null 2>&1
Damit wird ein Skript immer um 3 Minuten nach jeder vollen Stunde gestartet.

Nach dem Starten wird das Display alle 60 Minuten aktualisiert.

Besucht mich auf YouTube: https://www.youtube.com/techpirat


##############################  

English version:
Sorry for the confusion, I will provide an English version of the text.

Please correct the spelling in the following text:

This information is for all Tibber users or those who want to become one. Of course, you can also use the display for other purposes.
I will show you how the display works in a video: https://youtu.be/tMlHQ7NlYro

Hey, here's your personal invitation code for Tibber, the electricity supplier that helps you understand and reduce your electricity consumption: https://invite.tibber.com/Techpirat. You will receive 100% green electricity and can cancel at any time with a notice period of 2 weeks. Try it out and we both receive a €50 bonus for the Tibber store.

The idea is to display the current electricity price from Tibber on the Waveshare 7.5 Inch E-Paper Display. Don't have a Waveshare 7.5 Inch E-Paper Display yet? You can buy it here: https://amzn.to/3Jxacx3. My code was created and tested with Python 3.9.2. You also need a Raspberry Pi Zero WH, which you can buy here: https://amzn.to/3JxkLA9.

First, you need to write an SD card with the operating system. You can use https://www.raspberrypi.com/software/operating-systems/ for this. In the video, I'll show you how to set it up. Don't forget to connect the display to the Raspberry Pi Zero.

You also need to find the local IP address of the Raspberry Pi. You can find this on your router. In my case, it's 192.168.2.186. You can connect to the Raspberry Pi via VNC or SSH (with a terminal software) using the IP address.

Once your Raspberry Pi Zero is installed and successfully connected to the Wi-Fi, you need to connect via SSH and call "sudo raspi-config" via the console and work through the following steps:
Interface Options > VNC > Enable > Save. Before you restart, go back to the main menu:
Display Options > VNC Resolution > and set your desired resolution here.
I use 1280 x 1024.

Now you can connect via VNC and upload the files. Files uploaded via VNC are saved on the desktop.
Double-clicking one of the two scripts opens the editor, allowing you to test the two scripts. If error messages appear, work through them systematically.

Please install and import the following modules:
PIL 
tkinter
matplotlib
requests
numpy

Python modules are installed with "pip install PIL". In this case, we install "PIL". The "waveshare_epd" module is included and does not need to be installed.

To get the real-time price display, you need an API key from Tibber. You can get your Tibber API key here: https://developer.tibber.com/settings/access-token. Simply log in with your normal access data. You must enter this at the appropriate place in the "api_key.py" file.

You can create a job with "crontab -e". Here is an example:
3**** python3 /home/joerg/Desktop/e-paper/speicher_chart_heute.py >/dev/null 2>&1
This starts a script every 3 minutes after each full hour.

After starting, the display is updated every 60 minutes.

Visit me on YouTube: https://www.youtube.com/techpirat