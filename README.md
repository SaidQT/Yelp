# Yelp Business Review System

## Description
The Yelp Business Review System is a Django-based web application developed by Randa T., Said Q., Ibraheem K., and Muath A. The project aims to build a review system where businesses are rated by their customers. We believe such a tool to hold merchants (service providers) accountable for reviews can have a significant impact on their business. This tool also has the potential to evolve to incorporate advertisements.

## Installation
To get started with the Yelp Business Review System, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/SaidQT/Yelp.git
   ```

2. Navigate to the project directory:
   ```
   cd Yelp
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure the database settings in `settings.py`.

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage
To use the Yelp Business Review System:

1. Create a superuser account:
   ```
   python manage.py createsuperuser
   ```

2. Access the admin panel at [http://localhost:8000/admin](http://localhost:8000/admin) to manage businesses, reviews, and users.

3. Users can sign up, log in, and search for businesses to leave reviews.

## File Structure
```
Yelp/
├── yelp/
│   ├── settings.py
│   ├── urls.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── ...
│   │   
│   └── static/
│       ├── css/
│       ├── js/
│       └── ...
│   
├── manage.py
│
└── ...
```

## Contributing
We welcome contributions from the community. If you'd like to contribute to the project, please follow these guidelines:
- Fork the repository
- Create a new branch (`git checkout -b feature/your-feature`)
- Commit your changes (`git commit -am 'Add new feature'`)
- Push to the branch (`git push origin feature/your-feature`)
- Create a new Pull Request
