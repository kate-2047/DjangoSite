OVERVIEW
------------
This project is a full-stack Django-based web application created for Towne Engineering, P.C..

FEATURES
------------
- Home page - Displays a slideshow of images from past projects. Button overlaid on slideshow navigates to a page to view testimonials.
- About page - Shares the company's history with information about the Founder and Vice President of the company.
- Projects page - Displays completed projects with pictures and brief descriptions.
- Contact page - Shows the company's address, phone number, social media links, and an embedded Google Map of the office location.
  - Contact form - Found by using the 'Get in Touch' button, data is saved to a text file and SQLite database and can be viewed via admin site.
  - Testimonial form - can be filled out with name and message, data is saved to SQLite database and can be viewed via admin site or homepage button.

PREREQUISITES
------------
  - Python 3.x or higher
  - Django 3.x or higher

INSTALLATION
------------
1. Clone this repo
   ```
   git clone https://github.com/kate-2047/DjangoSite.git
   ```

2. Navigate to project directory
   ```
   cd DjangoSite
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations
   ```
   python manage.py migrate
   ```

5. Run the server
   ```
   python manage.py runserver
   ```

6. Open your browser and visit http://127.0.0.1:8000/

USAGE
------------
Once the server is running, you can access the application via your local server URL, http://127.0.0.1:8000/. 
Use the links in the navigation bar at the top of the page to move around the site and learn about Towne Engineering, P.C.

DJANGO ADMIN
------------
To access the admin panel and view/edit form submissions:
1. Create a superuser
```
python manage.py createsuperuser
```

2. Login at http://127.0.0.1:8000/admin/

CREDITS
------------
This project was created for a graduate-level course project. All images and content used are for educational purposes only. 
