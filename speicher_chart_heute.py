import tkinter as tk
import matplotlib.pyplot as plt
import requests
import api_key
import datetime
import time
import numpy as np



# Set the API endpoint URL and request headers
url = "https://api.tibber.com/v1-beta/gql"
headers = {
        "Authorization": 'Bearer ' + api_key.API_KEY,
        "Content-Type": "application/json",
    }

# Set the GraphQL query
query = """
{
  viewer {
    homes {
      currentSubscription{
        priceInfo{
          current{
            total
            energy
            tax
            startsAt
          }
          today {
            total
            energy
            tax
            startsAt
          }
          tomorrow {
            total
            energy
            tax
            startsAt
          }
        }
      }
    }
  }
}
"""

# Set the request body
data = {"query": query}

# Erstelle eine Matplotlib-Figur und lege sie in das Fenster
figure = plt.figure()
plot = figure.add_subplot(111)
figure.suptitle("tibber Strompreise für Heute")

# Ruft die API-Daten ab und zeigt sie in der Matplotlib-Figur an
response = requests.post(url, json=data, headers=headers)
response_data = response.json()

# Speichere die Liste der Häuser in der Variablen "homes"
homes = response_data['data']['viewer']['homes']

# Iteriere über die Häuser und speichere das Objekt "currentSubscription" in der Variablen "subscriptions", wenn es vorhanden ist
subscriptions = []
for home in homes:
    subscription = home.get('currentSubscription')
    if subscription:
        subscriptions.append(subscription)

# Iteriere über die Abonnements und speichere das Objekt "priceInfo" in der Variablen "price_infos", wenn es vorhanden ist
price_infos = []
for subscription in subscriptions:
    price_info = subscription.get('priceInfo')
    if price_info:
        price_infos.append(price_info)

# Gib die Liste der Preise aus
print(price_infos)

# Drucke den aktuell gültigen Preis
print(price_infos[0]["current"]["total"])
gueltpreis = price_infos[0]["current"]["total"]

# Analysieren Sie die Datumszeichenfolge mit der Funktion datetime.datetime.fromisoformat()
date = datetime.datetime.fromisoformat("2023-01-04T23:00:00.000+01:00")

# Extrahieren Sie Tag und Stunde mit der Methode strftime()
shortened_date = date.strftime("%H")

# Die Variable shortened_date enthält jetzt die Zeichenfolge „04/23:00“
print(shortened_date)

# Speichere die heutigen Daten in der Variablen "today_data"
today_data = price_infos[0]["today"]

# Füge die Zeitstempel in der "startsAt"-Eigenschaft und die Preise in der "total"-Eigenschaft der Y- und X-Achsen hinzu
x = [interval["startsAt"] for interval in today_data ]
y = [interval["total"] for interval in today_data]


# Analysieren Sie die Datumszeichenfolgen mit der Funktion datetime.datetime.fromisoformat()
dates = [datetime.datetime.fromisoformat(date_string) for date_string in x]

# Extract the day and hour using the strftime() method
shortened_dates = [date.strftime("%H:%M") for date in dates]

# Setze die Beschriftungen für die X- und Y-Achsen
figure = plt.figure()
plot = figure.add_subplot(111)
# Stärke der Chart Linie
plot.plot(shortened_dates, y, linewidth=5, color='black')
# Stärke des Rahmens
for spine in plot.spines.values():
    spine.set_linewidth(5)

# Schrift in der Legende und Beschriftung der Achsen anpassen
figure.suptitle("tibber Strompreise für Heute", fontsize=20, fontweight='bold', color='black', position=(0.3, 0.95))
plot.set_ylabel("Preis (EUR)", fontsize=20, fontweight='bold', color='black', ha= 'center', va='top', rotation=90, labelpad=20)
plot.grid(True)

# Füge die Datenpunkte mit den gekürzten Datumsstrings hinzu
plot.plot(shortened_dates, y)

# Holen Sie sich die Textobjekte für die Teilstrichbeschriftungen auf der X-Achse
xlabels = plot.get_xaxis().get_ticklabels()

    # Set the rotation angle for the labels
for label in xlabels:
    label.set_rotation(45)
# Lege die Schriftgröße der Beschriftung der X-Achse fest
plt.xticks(fontsize=16, fontweight='bold', rotation=45)
# Lege die Schriftgröße der Beschriftung der y-Achse fest
plt.yticks(fontsize=16, fontweight='bold')
# Vergrößern Sie den Platz unter dem Diagramm um 10 % der Abbildungshöhe
plt.subplots_adjust(bottom=0.2)

# Finden Sie den Index des höchsten y-Werts
highest_index = y.index(max(y))

# Holen Sie sich die x- und y-Koordinaten des höchsten Punkts
highest_x = x[highest_index]
highest_y = y[highest_index]

# Beschränke die highest_y Anzeige auf zwei Dezimalstellen
highest_y = round(highest_y, 2)

# Fügen Sie eine Beschriftung am höchsten Punkt hinzu
plt.text(highest_x , highest_y, 'max: {}€'.format(highest_y), fontsize=20, fontweight='bold', color='black', ha='right', backgroundcolor='white')

# Finden Sie den Index des niedrigsten y-Werts
lowest_index = y.index(min(y))

# Holen Sie sich die x- und y-Koordinaten des niedrigsten Punktes
lowest_x = x[lowest_index]
lowest_y = y[lowest_index]

# Beschränke die lowes_y Anzeige auf zwei Dezimalstellen
lowest_y = round(lowest_y, 2)

# Add a label at the lowest point
plt.text(lowest_x, lowest_y, 'min: {}€'.format(lowest_y), fontsize=20, fontweight='bold', color='black', ha='right', backgroundcolor='white')

# Finde den höchsten und niedrigsten y-Wert
highest_y = max(y)
lowest_y = min(y)

# Berechne den Unterschied zwischen dem höchsten und niedrigsten Wert
difference = highest_y - lowest_y

# Berechne den Prozentunterschied
percent_difference = (difference / lowest_y) * 100

# Runde den Prozentunterschied auf 2 Dezimalstellen
percent_difference = round(percent_difference, 2)

# Berechnen Sie den Durchschnittspreis
average_price = np.mean(y)

# Fügen Sie dem Diagramm eine Textbeschriftung hinzu, die den Durchschnittspreis anzeigt
plt.text(highest_x, highest_y, 'Ø Preis: {:.2f}€\n{}% Unterschied \n'.format(average_price, percent_difference), fontsize=14, ha='right', fontweight='bold', color='black')
# Passen Sie die Schriftgröße der Legende an
plt.legend(fontsize=14)
# Erzeuge eine wagerechte Linie die den gueltpreis anzeigt
plt.axhline(y=gueltpreis, color='0', linestyle='-.', linewidth=5)
# Zeige den gueltpreis als Text an
plt.text(x[0], gueltpreis, 'akt: {:.2f}€'.format(gueltpreis), fontsize=20, ha='right', fontweight='bold', color='black', backgroundcolor='white')

# Lege die Größe der Bilddatei auf 800 x 480 Pixel fest
figure.set_size_inches(8, 4.8)

# Lege die Auflösung der Bilddatei auf 100 dpi fest
figure.set_dpi(100)

# Lege die Schriftgröße der Chart Beschriftung auf 14 fest
plt.rcParams.update({'font.size': 14})

# Speichere den Chart als Bilddatei
figure.savefig("e-paper/pic/chart_von_heute.jpg")
# figure.savefig("/home/joerg/Desktop/e-paper/pic/chart_von_heute.jpg")
