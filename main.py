from scraper import search_jobs
from email_sender import send_email

jobs = search_jobs()

send_email(jobs)