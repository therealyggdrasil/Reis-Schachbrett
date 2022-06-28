anzahl = 0
for feld in range(64):
    korn = 2**feld
    anzahl = anzahl + korn
    print('Im Feld {} liegen jetzt {:>27,} Reiskörner. Die Gesamtanzahl beträgt somit {:>28,} Reiskörner.'.format(feld+1,korn,anzahl))

gewicht1 = anzahl * 0.025
gewicht2 = gewicht1 / 1000
gewicht3 = gewicht2 / 1000

print()
print('Ein Reiskorn wiegt zwischen 0,02 und 0,03 Gramm.')
print('Zur Berechnung, des Gesamtgewichtes der Reiskörner, nahmen wir einen Mittelwert von 0,025 Gramm pro Reiskorn.')
print()
print('Das Gewicht aller Reiskörner auf dem Schachbrett wird nun in GRAMM, KILOGRAMM und TONNEN angezeigt:')
print('Die Nachkommastellen haben wir weggelassen.')
print()
print('Alle Reiskörner auf dem Schachbrett wiegen {:>25,.0f} Gramm.'.format(gewicht1))
print('Alle Reiskörner auf dem Schachbrett wiegen {:>25,.0f} Kilogramm.'.format(gewicht2))
print('Alle Reiskörner auf dem Schachbrett wiegen {:>25,.0f} Tonnen.'.format(gewicht3))
