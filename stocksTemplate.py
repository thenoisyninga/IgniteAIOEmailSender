import smtplib
from email.message import EmailMessage

from get_sender_credentials import read_email_from_file, read_password_from_file


# Set up this function to send mails
def send_stocks_credentials_mail(delNum, email, password, name):
    # sendmail to 'email' with 'delNum' and 'password'
    not_send_list = []
    failure_count = 0
    success_count = 0
    sender = read_email_from_file()
    sender_password = read_password_from_file()
    recipient_email = email
    msg = EmailMessage()
    msg['Subject'] = "Stock Round Login Credentials"
    msg['From'] = sender
    msg['To'] = recipient_email

    # Enter HTML message here....
    msg.set_content(f'''<!doctype html>
<!--Quite a few clients strip your Doctype out, and some even apply their own. Many clients do honor your doctype and it can make things much easier if you can validate constantly against a Doctype.-->
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FPS Ignite</title>
<link rel="icon" type="image/png" href="favicon.ico">

<!-- Please use an inliner tool to convert all CSS to inline as inpage or external CSS is removed by email clients -->
<!-- important in CSS is used to prevent the styles of currently inline CSS from overriding the ones mentioned in media queries when corresponding screen sizes are encountered -->

<style type="text/css">
</style>
</head>
<body style="margin:0; padding:0;" bgcolor="#ffffff">
    <table style="min-width:320px;" width="100%" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
      <!-- fix for gmail -->
      <tr>
        <td style="line-height:0;"><div style="display:none; white-space:nowrap; font:15px/1px courier;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</div></td>
      </tr>
      <!-- pre-header -->
      <!-- <tr>
        <td bgcolor="#000000">
          <table class="flexible" width="700" align="center" style="margin:0 auto;" cellpadding="0" cellspacing="0">
            <tr>
              <td align="center"  style="padding:9px 10px 11px; font:14px/19px Arial, Helvetica, sans-serif; color:#df7d26;">Not coming through? Click&nbsp;here&nbsp;to&nbsp;<a href="#" target="_blank" style="text-decoration:none; color:#fff;">view&nbsp;in&nbsp;browser</a></td>
            </tr>
          </table>
        </td>
      </tr>
      <tr> -->
        <td bgcolor="#fafafa" class="wrapper" style="padding:0 10px;">
          <table class="flexible" width="700" align="center" style="margin:0 auto;" cellpadding="0" cellspacing="0">
            <!-- fix for gmail -->
            <tr>
              <td class="hide">
                <table width="700" cellpadding="0" cellspacing="0" style="width:700px !important;">
                  <tr>
                    <td style="min-width:700px; font-size:0; line-height:0;">&nbsp;</td>
                  </tr>
                </table>
              </td>
            </tr>
            <!-- header -->
            <tr>
              <td class="header" style="padding:15px 0 15px;">

              </td>
            </tr>
            <!-- banner -->
            <tr>
              <td class="img-flex"><a href="http://fpsignite.com/" target="_blank"><img src="https://i.ibb.co/c2Ggj13/email-header.png" height="318" width="700" border="0" style="vertical-align:top;" alt="FPS IGNITE" /></a></td>

            </tr>
            <!-- section - 01 -->
            <tr>
              <td style="padding:0 0 50px;">
                <table width="100%" cellpadding="0" cellspacing="0">
                  <tr>
                    <td class="frame" bgcolor="#ffffff" style="padding:28px 40px 40px; border-radius:0 0 3px 3px;">
                      <table width="100%" cellpadding="0" cellspacing="0">
                        <tr>
                          <td align="center" style="padding:0 0 15px; font:bold 24px/26px Arial, Helvetica, sans-serif; color:#000;">Ignite Stock Market Login Credentials</td>
                        </tr>
                        <tr>
                          <td calign="center"  style="padding:0 0 43px; font:14px/25px Arial, Helvetica, sans-serif; color:#000000;">

<br>
Dear {name}, <br><br>

The following are your login credentials for the Ignite Stock Market Round<br><br>

Username: {delNum}<br>
Password: {password}<br><br>

<b>Important*: These credentials are to be kept highly confidential. One laptop per delegation is allowed to log in at the time of the stock round</b><br>
<b> </b><br>

<!-- All the relevant information regarding the Auction is provided <a href="https://docs.google.com/document/d/17FUz7JAlPOM6yR35CmXGbjerwrmPY7b76Abrt3idCh8/edit?usp=sharing">here.</a><br><br> -->

Regards,<br>
FPS Ignite Registrations Department.

      <!-- footer -->
      <tr>
        <td bgcolor="#181a26">
          <table class="flexible" width="700" align="center" style="margin:0 auto;" cellpadding="0" cellspacing="0">
            <tr>
              <td class="footer" style="padding:50px 20px;">
                <table width="100%" cellpadding="0" cellspacing="0">

                  <tr>
                    <td align="center" style="padding:0 0 15px; font:bold 16px/18px Arial, Helvetica, sans-serif; color:#fff;">INVEST | INSTILL | ILLUMINATE</td>
                    </tr>
                    <td align="center" style="font:14px/25px Arial, Helvetica, sans-serif; color:#fff;">
                      If you have any queries, contact us on <b><a href ="mailto:fpsalevelignite@fps.edu.pk">fpsalevelignite@fps.edu.pk</a><b> <br />
                      Or Call us on <br />
                      <a href="tel:03314464839">0336 IGNITE9</a><br/>
                      <a href="tel:03362250417">0336 2250417</a><br/>
                      <a href="tel:03353019641">0335 3019641</a><br/>

                      Copyright &copy; 2022. All rights reserved.
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
''', subtype='html')

    # Sending Messages...
    print(f'[+] Sending Message to {recipient_email} from delegation {delNum}...')
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        try:
            success_count += 1
            smtp.starttls()
            smtp.login(sender, sender_password)
            print(f"\nSending Message to {recipient_email}(Del {delNum}) with pass {password} ")
            smtp.send_message(msg)

            if recipient_email == "sarim.ahmed19621@fpseagles.com":
                check = input("All set?")
        except():
            not_send_list.append(recipient_email)
            print(f"\n[-] Message was not sent to {recipient_email}.\n")
            failure_count += 1
            success_count -= 1
