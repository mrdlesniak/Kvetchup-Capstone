from .secrets import email_address, email_password

#for gmail 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = email_address
EMAIL_HOST_PASSWORD = email_password
EMAIL_PORT = 587