
# AuthentiCo 
AN ATTRIBUTE BASED ACCESS CONTROL

AuthentiCo adopts a comprehensive and innovative solution approach to provide secure, efficient, and tailored access control and collaboration within cloud-based environments. The project leverages advanced technologies and methodologies to ensure robust security management while maintaining a user-friendly experience.


## DEMO

[screen-capture.webm](https://github.com/suryansh4424/AuthentiCo_Abac/assets/131521058/80c1bc53-135a-4be7-a3de-069e823ecc2f)
## RUN LOCALLY

1. Clone the project

```bash
  git clone https://github.com/suryansh4424/AuthentiCo_Abac.git
```

2. Set up Environment:

 On Windows:
```bash
  python -m venv env
```
 On macOS/Linux:
```bash
  source env/bin/activate
```

3. Install Requirements:
```bash
  pip install -r requirements.txt

```
4. Database Setup:
```bash
  python manage.py migrate
```
5. Create Superuser (Optional):
```bash
  python manage.py createsuperuser
```

6. Run Development Server:
```bash
  python manage.py runserver
```