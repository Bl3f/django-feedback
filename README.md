===
django-feedback
===

django-feedback is a Django app to include quickly a feedback app to gather all your users message.


Quick start
---

1. Add "django-feedback" to you INSTALLED_APPS::

    INSTALLED_APPS = (
        ...
        'django-feedback',
    )

2. Include django-feedback URL module::

    url(r'^feedback/', include('feedback.urls')),

3. Sync the database to create the model::

    python manage.py syncdb

4. Add to your <head> feedback default style::

    <link rel="stylesheet" href="{% static 'feedback/css/feedback-default.css'%}">

5. Add after the body closing tag javascript call with your spinner::

    <script type="text/javascript" src="{% static 'feedback/js/feedback.js'%}"></script>
    <script>
        feedback(YOUR_SPINNER);
    </script>

6. Last, include feedback HTML at the end of the body, where you want the module::

    {% include "feedback/feedback.html" %}

