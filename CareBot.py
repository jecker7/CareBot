from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import threading

class CareBot(threading.Thread):

    def __init__(self):
        pass

    def authenticate(self, url, user, pass):
       url = "https://www.care.com/visitor/captureLogin.do"
        return

    def get_jobs(self, zipcode, miles, service, job_type, hourly_rate, frequency, applied_to, has_photo,
                 transportation_required, new_jobs_only, ending_soon_job, keywords, subject_areas):

        # TODO: look into adding subject areas to scrape
        url = "https://www.care.com/visitor/captureJobSearch.do?searchPerformed=true&" + \
        "refineSearch=true&sitterService=" + service + "&milesFromZipCode=" + miles + \
        "&zipCode=" + zipcode + "&jobType=" + job_type + "Company&hourlyRate=" + hourly_rate + \
        "&jobFrequency=" + frequency + "&appliedToJob=" + applied_to + "&hasPhoto=true" + \
        "&noTransportationRequired=" + transportation_required + "&newJobsOnly=" + new_jobs_only + \
        "&endingSoonJob=" + ending_soon_job + "&keyword=" + self.make_keywords(keywords)

        board = requests.get(url)
        soup = bs(board)
        jobs = soup.findall()


    def make_keywords(self, keywords):
        return keywords.join

    def notify(self):


    def refresh(self):
        return

    def apply_to(self, job):
        return

    def run(self):



if __name__ == "__main__":
    bot = new CareBot()
    user = ""
    pass = ""
    bot.authenticate(user, pass)
    jobs = bot.get_jobs(args)
    for job in jobs:
        bot.apply_to(job, statement)



