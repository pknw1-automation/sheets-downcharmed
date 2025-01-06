from flask import Flask, request, render_template, redirect, current_app
from dotenv import load_dotenv
import pygsheets
import re
import os
import sys
from datetime import datetime
import glob
import requests

load_dotenv()

sheets = pygsheets.authorize(service_file='config/auth.json')
document = sheets.open_by_key(os.environ['SPREADSHEET'])
lookup = document.worksheet('title','Lookup')
enabled = lookup.range("B2:B20")

site_enabled = []
for item in enabled:
    if item[0].value != '':
        site_enabled.append(item[0].value)


for section in site_enabled:
    print("parsing : "+section+" section")
    parsed_section = {}
    raw_section_data = document.worksheet('title',section)

    parsed_section = {"page_name": raw_section_data.cell("B1").value,
            "page_title" : raw_section_data.cell("B4").value,
            "page_subtitle" : raw_section_data.cell("B5").value,
            "page_text" : raw_section_data.cell("B6").value,
            "page_button_1_text": raw_section_data.cell("B7").value,
            "page_button_1_link": raw_section_data.cell("B8").value,
            "page_button_2_text": raw_section_data.cell("D7").value,
            "page_button_2_link": raw_section_data.cell("D8").value}


    page_data_hdr_start = raw_section_data.cell("B9").value
    page_data_hdr_end = raw_section_data.cell("B10").value
    page_data_start = raw_section_data.cell("C9").value
    page_data_end = raw_section_data.cell("C10").value
    raw_page_data = raw_section_data.range(page_data_start+":"+page_data_end)
    raw_page_hdr_data = raw_section_data.range(page_data_hdr_start+":"+page_data_hdr_end)
    #print(raw_page_data)
    parsed_data = []

    for i in raw_page_hdr_data:
        print(i)
    print("-------")

    for i in raw_page_data:
        print(i)
        for count in range(1,len(i)):
            ncount=count-1
            print(ncount)
            print(str(raw_page_hdr_data[count])+" : "+i[count].value)

        #entry = {"id": i[0].value,
        #        "pid": i[1].value,
        #        "title": i[2].value,
        #        "link": i[3].value }
        #parsed_data.append(entry)

    #print(parsed_data)
    #if page_data_hdr_start != 'None':
    #    raw_data_value = raw_section_data.range(page_data_start+":"+page_data_end)
    #    raw_data_hdrs = raw_section_data.range(page_data_hdr_start+":"+page_data_hdr_end)
    #    for row in raw_data_hdrs:
    #        print("headers "+str(row[1].value))
        #for row in raw_data_value:
        #    print(len(row))
        #    print(row)
        #    row[0]
   #     print(raw_data_hdrs)
   #     print(raw_data_value)
        

    #custom_cols_hdr_start = section_data.cell("B9").value
    #if custom_cols_hdr_start != 'None':
    #    custom_cols_hdr_end = section_data.cell("B10").value
    #    custom_headers = []
    #    for cell in section_data.range(custom_cols_hdr_start+":"+custom_cols_hdr_end):
    #        print(section)
    #        print(cell)
    #custom_cols_data_start = section_data.cell("C9").value 
    #custom_cols_data_end = section_data.cell("C10").value


   # print(section+" "+custom_cols_hdr_start+" "+custom_cols_hdr_end)

