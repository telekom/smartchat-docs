# Two-Factor Authentication

Source: https://docs.smartchat.ai.t-systems.net/user/concepts/two-factor-authentication/

> How two-factor authentication works when you log in to Smartchat with email and password, and how the authenticator app relates to the login.

Logins with email and password are handled by [Keycloak](https://www.keycloak.org/), the identity and access management system behind Smartchat. Keycloak can ask for a **second factor** after the password: a one-time code from an authenticator app on your phone. Whether this is required, and for whom, depends on how your installation is configured.

> **Single Sign-On**
>
> If you log in with your company’s **SSO**, your company’s identity provider handles authentication, including any second factor. This page applies to logins with email and password.

## [Authenticator apps](https://docs.smartchat.ai.t-systems.net/user/concepts/two-factor-authentication/#authenticator-apps)

Any app that generates time-based one-time passwords (TOTP, [RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238)) works, for example FreeOTP, Google Authenticator, Microsoft Authenticator, or a password manager with TOTP support.

## [Setting it up](https://docs.smartchat.ai.t-systems.net/user/concepts/two-factor-authentication/#setting-it-up)

When two-factor authentication is required for your account, Keycloak asks you to set it up at your next login:

1. Scan the QR code shown on the login page with your authenticator app.
2. Enter the 6-digit code the app now shows, and optionally give the device a name.

From then on, every login asks for the current code from the app after your password. If you lose access to your phone, contact your administrator, who can have you set up a new authenticator app.

## [How the app and Smartchat communicate](https://docs.smartchat.ai.t-systems.net/user/concepts/two-factor-authentication/#how-the-app-and-smartchat-communicate)

**They don’t.** The authenticator app never connects to Smartchat or Keycloak, and Keycloak never sends anything to the app. Both sides compute the same codes independently:

*\[Image: Diagram]*

- **Setup:** Keycloak generates a random secret for your account and shows it as a QR code on the login page, which is delivered over HTTPS. The app reads the QR code through the camera and stores the secret on the phone. This is the only time the secret leaves Keycloak.
- **Login:** every 30 seconds, the app and Keycloak each derive a new code from the shared secret and the current time. You type the app’s code into the login page, and it is sent to Keycloak over HTTPS like the rest of the login form.

The app therefore works offline and sends no data of its own. Its clock must be roughly correct. Keycloak accepts the codes of neighbouring time intervals to absorb small clock differences ([look-around window](https://www.keycloak.org/docs/latest/server_admin/index.html#totp-configuration-options)).

## [For administrators](https://docs.smartchat.ai.t-systems.net/user/concepts/two-factor-authentication/#for-administrators)

Two-factor authentication is part of the Keycloak login flow of your installation. Depending on the configuration it is:

- required for every login with email and password,
- required only for users with a specific role, or
- asked only from users who have already set up an authenticator app.

Keycloak documents the building blocks:

- [OTP policies](https://www.keycloak.org/docs/latest/server_admin/index.html#one-time-password-otp-policies): algorithm, number of digits and code period. The standard configuration uses Keycloak’s defaults, which every common authenticator app supports.
- [Conditions in conditional flows](https://www.keycloak.org/docs/latest/server_admin/index.html#conditions-in-conditional-flows) and [2FA conditional workflow examples](https://www.keycloak.org/docs/latest/server_admin/index.html#twofa-conditional-workflow-examples): how the second factor is required for all users, by role, or only once configured.
- [Required actions](https://www.keycloak.org/docs/latest/server_admin/index.html#proc-setting-required-actions_server_administration_guide): how a user is asked to set up an authenticator app at the next login.
- [Creating an OTP](https://www.keycloak.org/docs/latest/server_admin/index.html#proc_creating-otp_server_administration_guide): how to make a user set up a new authenticator app, for example after losing their phone.
