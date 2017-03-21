#!/usr/bin/env python
from pprint import pprint
import json
import requests
import jinja2
import html2text
import time
import string

def filter_non_printable(s):
    printable = set(string.printable)
    return filter(lambda x: x in printable, s)

def get_meetup_events():
    api_url = 'https://api.meetup.com/{}/events'.format('Tel-Aviv-Yafo-Linux-Kernel-Meetup')
    request = requests.get(api_url, params=dict(scroll='future_or_past', page=200))
    return json.loads(request.content)

def render_post(jinja_env, event):
    template = jinja_env.get_template('post.jinja')
    return filter_non_printable(template.render(**event))

def convert_event_time_to_date(event_time, utc_offset):
    # Given time is in ms
    event_time /= 1000
    utc_offset /= 1000

    formatted_time = time.gmtime(event_time)
    params = dict(
        year=formatted_time.tm_year,
        month=formatted_time.tm_mon,
        day=formatted_time.tm_mday,
        hour=formatted_time.tm_hour,
        min=formatted_time.tm_min,
        sec=formatted_time.tm_sec,
        utc_sign='+' if utc_offset > 0 else '-',
        utc_hour=abs(utc_offset) / 3600,
        utc_min=abs(utc_offset) % 3600 / 60,
    )
    result = "{year:04d}-{month:02d}-{day:02d} {hour:02d}-{min:02d}-{sec:02d} " \
             "{utc_sign}{utc_hour:02d}{utc_min:02d}"
    return result.format(**params)

def get_event_post_file_name(event):
    name = event['name'].lower().replace(' ','-')
    name = ''.join([i for i in name
                    if i.isalpha() or i == '-' or i.isdigit()])
    date = event['date'].split(' ')[0]
    return '_posts/{date}-{name}.markdown'.format(date=date, name=name)

def main():
    print "Querying meetup api..."
    events = get_meetup_events()
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('jinja'))

    for event in events:
        event['description'] = html2text.html2text(event['description'])
        event['date'] = convert_event_time_to_date(event['time'], event['utc_offset'])

        file_name = get_event_post_file_name(event)
        print "Creating event: " + event['name']
        print "file: " + file_name
        with open(file_name, 'w') as post_file:
            post_file.write(render_post(jinja_env, event))

if __name__ == "__main__":
    main()
