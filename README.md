# SemSum

## What is SemSum?
Every semester, students spend countless minutes navigating their assessment schedules and what's where when for what. Confusing, right? What if you could see at a glance what you're studying every week and when you're getting tested for it?

**Introducing SemSum.** The easiest assessment summary for your USYD Semester. Simply enter your units and see a complete summary of all content and assessments, broken down by weeks. You can then export this directly to your calendar app of choice, or print a semester summary. The name is a portmanteau of *semester* and *summary*!

## Inspiration

Every semester, assessments creep up on us before we've even started studying. Study information is spread across multiple pages, and is sometimes hard to find. With SemSum, you'll **automatically** get to see all the important bits at a glance and export it directly, saving you from manually entering data and summaries! 

## Usage
Using SemSum is as simple as putting in your units of study. We display your sorted assessment info in a weekly grid, letting you quickly know when and what is due. You can export your assessments in ICS format and import them into your preferred calendar app. You can also download and print them from a pdf, so you’ll always be on track! In another tab, you can also see the weekly breakdown of all the content you’ll be studying, so you’ll know exactly what to study that week.

## How it was built
First we got the data for our program from the Sydney UOS website. We used pandas and matched the website tables and html with regex, and ended up scraping 2000+ units of study. We stored this data in a SQLite database with a Django backend, along with Bootstrap and Ajax for the frontend. We generated markdown and used PyPandoc to convert the content to a pdf, and used the ics library to create importable calendars. While it was challenging to integrate several modules such as scraping to a database, our modular code significantly eased this burden. 

## Dependencies:
This project was built using several packages:
- Pandas, BeautifulSoup4, requests for web scraping 
- Python ICS Library 
- PyPandoc 
- Django 
- Bootstrap, Bootstrap Select
- Jquery, PopperJS

## Technical Accomplishments:
- Scraping 2000+ units of study successfully.
- Outputting an .ics file from the assessment data using the Python ics library. 
- Outputting to a .pdf, compiled through PyPandoc with custom generated Markdown. 
- Bootstrap + Ajax for frontend, Django + SQLite for backend.

## Technical Challenges Overcome
- LaTeX formatting from a markdown file (manually generating the markdown from Python).
- Download button for dynamically generating a .pdf for each user, allowing them to download the file without us storing copies.
- Scraping websites: investigating multiple libraries (BS4, Selenium, etc) before settling on Pandas (with great success!)
- Deploying to Heroku (and using Whitenoise).
- Currently .pdf output is incompatible with the Heroku host platform, however this functionality works locally and can be implemented with another host like AWS.

## Roles
- [Steve Kraynov](https://www.linkedin.com/in/steve-kraynov/): Project manager, back-end engineer, web-scraping and object design, pitch designer and creator. 
- [Nathan Dugdale](https://www.linkedin.com/in/nathan-dugdale-1700971b6/): Full-stack developer, using Django and bootstrap to create a reactive web app with a database.
- [Joshua Wilkinson](https://www.linkedin.com/in/joshua-wilkinson-aabb901b4/): Back-end engineer, utilising pandas to scrape the unit and assessment information. Creating the pdf export functionality, and using heroku to deploy the Django app to the web.
- [Nicholas Sargeant](https://www.linkedin.com/in/nicholas-sargeant/): Creating the pdf export functionality, deploying the app to the web via heroku, project timelining and planning.
- [Alexandra Maher](https://www.linkedin.com/in/alexandra-maher-779973182/): Concept ideation, UI, logo and branch design, back-end development for assessment sorting, and exporting to .ics format.

## What's next for SemSum
Although we’ve successfully met our MVP, SemSum has great potential for future expansion. Integration with more resources like textbooks and videos would facilitate further learning, automatically finding them with ML and keywords. This can lead to partnerships with universities and companies for monetisation (such as from publishers) in future! In addition, we hope to make users a customised study plan for their units, such as hours spent studying per specific subject which can interface with their existing timetables. This opens up potential collaboration between students studying the same unit, or between universities and countries.
