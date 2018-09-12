import datetime
import re

from jobsbg.job import Job


def parse_job_element(job_element):
    title_text = job_element.find_element_by_xpath('.//a').text
    desc = job_element.find_element_by_xpath('.//div/span').text
    date = job_element.find_element_by_xpath('.//span[@class="explainGray"]').text

    tokens = [desc, None, None]

    if ';' in desc:
        tokens = desc.split('; ')
        tokens.extend('BGN')

        matches = re.findall('(\d+)', tokens[1])

        if len(matches) > 1:
            tokens[1] = (float(matches[0]) + float(matches[1])) / 2
        else:
            tokens[1] = float(matches[0])

        tokens[2] = re.findall('([A-Z]{3})\s(\((Бруто|Нето)\))', desc)[0]
        tokens[2] = tokens[2][0] + ' ' + tokens[2][2]

    if date == 'днес':
        date = datetime.datetime.now().strftime('%d.%m.%y')

    job = Job(title_text, tokens[0], date, tokens[1], tokens[2])

    return job
