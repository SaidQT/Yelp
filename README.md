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
│   ├── views.py
│   ├── templates/
│   │   ├── main.html
│   │   ├── aboutus.html
│   │   ├── business.html
│   │   ├── category.html
│   │   ├── services.html
│   │   ├── reviews.html
│   │   ├── contactus.html
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

## project Image
![Screenshot of jQuery Badge](https://media.discordapp.net/attachments/1243485223698829312/1245374964714962954/image.png?ex=66588551&is=665733d1&hm=99f8214f660cf3a27f0a837680f323dff3b802c0b71ec14bc74ff83b2fa1c4d8&=&format=webp&quality=lossless&width=1410&height=662)
![Screenshot of jQuery Badge](https://media.discordapp.net/attachments/1243485223698829312/1245377632451694645/image.png?ex=665887cd&is=6657364d&hm=3063d7eaec27b325014bb79d58151302b77469b87988adf126237c88fa5de442&=&format=webp&quality=lossless&width=1410&height=662)
![Screenshot of jQuery Badge](https://media.discordapp.net/attachments/1243485223698829312/1245378299614724147/image.png?ex=6658886c&is=665736ec&hm=95b77e1f1f9cc7f1ff4e499212822fe8deb6923e75e0d9a0cc94bf9aef53db7f&=&format=webp&quality=lossless&width=1410&height=661)
