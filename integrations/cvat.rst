=======================
CVAT
=======================

## The Annotation Tool

### Requirements

```
click==8.0.4
Flask==2.2.2
itsdangerous==2.0.1
Jinja2==3.1.2
MarkupSafe==2.1.1
Werkzeug==2.2.3
```

- Create an "uploads", "frames" and "videos" folder in static folder (here all the uploaded images/videos/frames will be saved).
- If you have more then 1000 images, use upload folder option in application.
- To run type this command where you have your app.py file: `flask run`
- In the browser, open: http://127.0.0.1:5000/annotate
