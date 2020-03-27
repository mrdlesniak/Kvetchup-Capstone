03/09/20 - 
    Set up django app template and virtual environment
    Created index view
    Created base.html and static style.css
03/10/20 - 
    Began users app 
    Set basic css for a mobile-first app 
    Fixed css issues with zoom, spacing, and general style 
03/11/20 - 
    Set up admin panel and models 
    Set up Vue.js
    Fixed bug where request was being called too quickly. Relied on vue data that hadn't yet been populated
    Changed body font 
03/12/20 - 
    More fields populate when site is selected 
    Created hamburger button for menu
    Menu switched from off to on via Vue.js
    Styled menu and links
    Menu transition added
03/13/20 - 
    fixed bug with select submission sending blank requests to the backend
    created site icon that appears in browser
    integrated and formatted user system into django and vue 
    created log in and logout buttons 
    send email will not send but will prompt user to login if not already logged in 
    upon successfully logging out, a nicely-formatted modal appears
    began creation of email sending and verification system 
03/16/20 - 
    populating database
    created customer_support_site field in models for sites where email address is not listed
    edited email submission screen to not appear if no email listed
    made email and cs_site blank-able, in case none provided 
    <!-- Create Additional Info field for URL and info not shown. Can minimize display  -->
    <!-- Create a url shortener for URLs over a certain length, or a hyperlink system -->
03/17/20 - 
    <!-- display username at top somewhere when logged in -->
    populated database
03/18/20 - 
    set up email system 
    Used django user.is_authenticated to automate if the text and submit objects appear. If anonymous, please login appears, no longer populates with button press
    successfully set up beginnings of email system
        can send email from only one address to one address
    tomorrow, create modal (identical to 'successfully logged out') for 'email sent'
03/19/20 - 
    pivot from user email system. Emails will still be sent to verify users, but will not send from user email address for security reasons
    changed form to a link that reads "Send Email" which opens up client's email 
    fixed css issues and improved mobile styling
    Created more modern buttons, including a new button to display additional information
        Minimizes site. Only a few lines will be displayed by default
        Will begin work on gathering ratings from yelp and such 
03/20/20 -
    Begin work on a ratings page with overall rating will reviews underneath it
    Edited models. Each company will have a rating, which is itself a model
        Each rating has a corresponding view which has a user, a review (blank-able ), and a date
03/23/20 - 
    Sent reviews models through View to my Vue (sorry for the homonyms)
    Reformatted reviews to contain users instead of user_id and formatted datetime to be legible
03/24/20 - 
    Class lectures and css
03/25/20 - 
    Fixed overlapping footer issue (margin-bottom was the trick)
    Create custom user system 
        Involed deleted all previous migrations and clearing my database. Previous data entries were copy and pasted
03/26/20 - 
    users can now add reviews for companies
    reviews connected to site and user
    modal appears to notify user of successful submission
    reviews ordered by date, most recent first