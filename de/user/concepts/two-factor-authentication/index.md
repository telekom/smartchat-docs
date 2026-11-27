# Zwei-Faktor-Authentifizierung

Source: https://docs.smartchat.ai.t-systems.net/de/user/concepts/two-factor-authentication/

> Wie die Zwei-Faktor-Authentifizierung bei der Anmeldung mit E-Mail und Passwort funktioniert und wie die Authenticator-App mit der Anmeldung zusammenhängt.

Anmeldungen mit E-Mail und Passwort übernimmt [Keycloak](https://www.keycloak.org/), das Identitäts- und Zugriffsmanagement hinter dem Smartchat. Keycloak kann nach dem Passwort einen **zweiten Faktor** abfragen: einen Einmalcode aus einer Authenticator-App auf Ihrem Smartphone. Ob und für wen das verpflichtend ist, hängt von der Konfiguration Ihrer Installation ab.

> **Single Sign-On**
>
> Wenn Sie sich mit dem **SSO** Ihres Unternehmens anmelden, übernimmt der Identity Provider Ihres Unternehmens die Authentifizierung, einschließlich eines etwaigen zweiten Faktors. Diese Seite gilt für Anmeldungen mit E-Mail und Passwort.

## [Authenticator-Apps](https://docs.smartchat.ai.t-systems.net/de/user/concepts/two-factor-authentication/#authenticator-apps)

Jede App, die zeitbasierte Einmalpasswörter (TOTP, [RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238)) erzeugt, ist geeignet, zum Beispiel FreeOTP, Google Authenticator, Microsoft Authenticator oder ein Passwortmanager mit TOTP-Unterstützung.

## [Einrichtung](https://docs.smartchat.ai.t-systems.net/de/user/concepts/two-factor-authentication/#einrichtung)

Ist die Zwei-Faktor-Authentifizierung für Ihr Konto verpflichtend, fordert Keycloak Sie bei der nächsten Anmeldung zur Einrichtung auf:

1. Scannen Sie den QR-Code auf der Anmeldeseite mit Ihrer Authenticator-App.
2. Geben Sie den 6-stelligen Code ein, den die App nun anzeigt, und vergeben Sie optional einen Namen für das Gerät.

Ab dann fragt jede Anmeldung nach dem Passwort den aktuellen Code aus der App ab. Haben Sie keinen Zugriff mehr auf Ihr Smartphone, wenden Sie sich an Ihren Administrator. Er kann veranlassen, dass Sie eine neue Authenticator-App einrichten.

## [Wie App und Smartchat kommunizieren](https://docs.smartchat.ai.t-systems.net/de/user/concepts/two-factor-authentication/#wie-app-und-smartchat-kommunizieren)

**Gar nicht.** Die Authenticator-App baut keine Verbindung zum Smartchat oder zu Keycloak auf, und Keycloak sendet nichts an die App. Beide Seiten berechnen dieselben Codes unabhängig voneinander:

*\[Image: Diagram]*

- **Einrichtung:** Keycloak erzeugt einen zufälligen Schlüssel für Ihr Konto und zeigt ihn als QR-Code auf der Anmeldeseite an, die über HTTPS ausgeliefert wird. Die App liest den QR-Code über die Kamera ein und speichert den Schlüssel auf dem Smartphone. Nur in diesem Moment verlässt der Schlüssel Keycloak.
- **Anmeldung:** Alle 30 Sekunden leiten App und Keycloak jeweils aus dem gemeinsamen Schlüssel und der aktuellen Uhrzeit einen neuen Code ab. Sie tippen den Code der App auf der Anmeldeseite ein, und er wird wie das übrige Anmeldeformular über HTTPS an Keycloak übertragen.

Die App funktioniert daher auch offline und sendet selbst keine Daten. Ihre Uhr muss ungefähr stimmen. Keycloak akzeptiert auch die Codes benachbarter Zeitintervalle, um kleine Abweichungen auszugleichen ([Look-around window](https://www.keycloak.org/docs/latest/server_admin/index.html#totp-configuration-options)).

## [Für Administratoren](https://docs.smartchat.ai.t-systems.net/de/user/concepts/two-factor-authentication/#f%C3%BCr-administratoren)

Die Zwei-Faktor-Authentifizierung ist Teil des Keycloak-Anmeldeablaufs Ihrer Installation. Je nach Konfiguration ist sie:

- für jede Anmeldung mit E-Mail und Passwort verpflichtend,
- nur für Nutzer mit einer bestimmten Rolle verpflichtend oder
- nur für Nutzer aktiv, die bereits eine Authenticator-App eingerichtet haben.

Die Keycloak-Dokumentation (auf Englisch) beschreibt die Bausteine:

- [OTP policies](https://www.keycloak.org/docs/latest/server_admin/index.html#one-time-password-otp-policies): Algorithmus, Anzahl der Stellen und Gültigkeitsdauer der Codes. Die Standardkonfiguration nutzt die Keycloak-Voreinstellungen, die jede gängige Authenticator-App unterstützt.
- [Conditions in conditional flows](https://www.keycloak.org/docs/latest/server_admin/index.html#conditions-in-conditional-flows) und [2FA conditional workflow examples](https://www.keycloak.org/docs/latest/server_admin/index.html#twofa-conditional-workflow-examples): wie der zweite Faktor für alle Nutzer, nach Rolle oder erst nach der Einrichtung verlangt wird.
- [Required actions](https://www.keycloak.org/docs/latest/server_admin/index.html#proc-setting-required-actions_server_administration_guide): wie ein Nutzer bei der nächsten Anmeldung zur Einrichtung einer Authenticator-App aufgefordert wird.
- [Creating an OTP](https://www.keycloak.org/docs/latest/server_admin/index.html#proc_creating-otp_server_administration_guide): wie ein Nutzer eine neue Authenticator-App einrichten muss, zum Beispiel nach dem Verlust des Smartphones.
