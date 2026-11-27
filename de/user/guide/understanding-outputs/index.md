# Ausgaben verstehen & nutzen

Source: https://docs.smartchat.ai.t-systems.net/de/user/guide/understanding-outputs/

> Quellen einsehen und Funktionen auf Antworten anwenden.

## [Quellen einsehen](https://docs.smartchat.ai.t-systems.net/de/user/guide/understanding-outputs/#quellen-einsehen)

Wenn das Wissen eines Raumes zur Erstellung einer Antwort verwendet wird, werden die verwendeten Quellen (Referenzen) im Chat angezeigt. Durch Klicken auf eine Quelle werden weitere Informationen angezeigt. Hat ein Dokument eine ursprüngliche Adresse, zum Beispiel eine Confluence-Seite, verlinkt die Quelle auf dieses Original; andernfalls auf die in Smartchat gespeicherte Kopie.

*\[Image: Antwort mit Quellenangabe]*

Die Prozentzahl neben jeder Quelle gibt an, wie stark das jeweilige Dokument mit der erzeugten Antwort korreliert (Relevanz-Score). Die Werte entstehen automatisch durch den Retrieval- und Ranking-Mechanismus des Smartchat: Die semantische Ähnlichkeit zwischen Dokumentinhalt und Antwort-Abschnitten wird gemessen und in einen prozentualen Relevanz-Score umgerechnet. Der Relevanz-Score hat immer nur eine relative Aussagekraft in Bezug auf die anderen Quellen, die in der selben Anfrage herangezogen wurden.

*\[Image: Quellen-Detailansicht mit Relevanz-Score]*

## [Funktionen auf Antworten anwenden](https://docs.smartchat.ai.t-systems.net/de/user/guide/understanding-outputs/#funktionen-auf-antworten-anwenden)

Mit den Antworten des Smartchat kann weiter interagiert werden: bearbeiten, kopieren, vorlesen, fortsetzen, stoppen oder neu generieren.

*\[Image: Funktions-Symbole unter einer Antwort]*

### [Antwort bearbeiten](https://docs.smartchat.ai.t-systems.net/de/user/guide/understanding-outputs/#antwort-bearbeiten)

*\[Image: Bearbeiten-Button]*

Durch Klicken auf das **Bleistift-Symbol** kann die Antwort bearbeitet werden. Mittels “Als Kopie speichern” kann die Ausgabe als separate Kopie gespeichert oder durch den Speichern-Button überschrieben werden.

*\[Image: Bearbeitungsansicht mit Speicher-Optionen]*

### [Antwort kopieren](https://docs.smartchat.ai.t-systems.net/de/user/guide/understanding-outputs/#antwort-kopieren)

*\[Image: Kopieren-Button]*

Durch Klicken auf das **Kopier-Symbol** wird die Antwort in die Zwischenablage kopiert.

### [Antwort laut vorlesen](https://docs.smartchat.ai.t-systems.net/de/user/guide/understanding-outputs/#antwort-laut-vorlesen)

Diese Funktion startet die Vorlese-Funktion des Browser lokal auf dem Rechner. Diese ist nicht Bestandteil des Smartchats.

*\[Image: Vorlesen-Button]*

Durch Klicken auf das **Lautsprechersymbol** wird die Antwort laut vorgelesen.

### [Antwort fortsetzen/stoppen](https://docs.smartchat.ai.t-systems.net/de/user/guide/understanding-outputs/#antwort-fortsetzenstoppen)

*\[Image: Fortsetzen-Button]*

Durch Klicken auf das **Abspielen-Symbol** kann ein zusätzlicher Text generiert werden, falls die Ausführlichkeit der erhaltenen Antwort nicht den Wünschen entspricht.

*\[Image: Stopp-Button während der Generierung]*

Eine Antwortgenerierung kann über das **“Stopp”-Symbol** neben der Texteingabe unterbrochen werden.

### [Antwort neu generieren](https://docs.smartchat.ai.t-systems.net/de/user/guide/understanding-outputs/#antwort-neu-generieren)

*\[Image: Neu generieren-Button]*

Das **Kreislauf-Symbol** fordert das LLM auf, die Antwort mit anderen neu zu generieren. Da LLMs Komplexe-Systeme mit Zufallscharakter sind, wird in der Regel jedes Mal eine mehr oder weniger unterschiedliche Antwort generiert werden.

*\[Image: Neu generierte Antwort]*
