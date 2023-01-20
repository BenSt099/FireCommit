"""
Author(s): 👥
Date: 🗓️, Time: 🕒
Topic: 📋: FIX: ✅, REFACTORING, TEST, IMPLEMENTATION, INITIAL, GUI, BUSINESS_LOGIC; INFRASTRUCTURE, ARCHITECTURE, MILESTONE: 🎆🎇, DOCUMENTATION: 📓,
LINK: 🔗, CONTINUOUS_DELIVERY: ♾️, WARNING: ⚠️, FAILED: ❌
Keyword(s): 🔑⌨️
Change(s): LOCAL: 📌, GLOBAL: 🌐, MODULE: 🗃️, SUBMODULE: 🗄️
No. of Changes: 🧮
"""

from datetime import date
from datetime import datetime


def DateAndTime():
    dateNow = date.today()
    timeNow = datetime.now()
    return "🗓️ DATE: " + dateNow.strftime("%B %d, %Y") + "; 🕒 TIME: " + timeNow.strftime("%H:%M:%S")

def Authors():
    listofAuthors = input("👥 Author(s): ")
    return "👥 AUTHORS: " + listofAuthors

def NoOfChanges():
    no = input("🧮 No. of Changes: ")
    return "🧮 NO. OF CHANGES: " + no

def Keywords():
    keywords = input("🔑⌨️ Keyword(s): ")
    return "🔑⌨️ KEYWORDS: " + keywords    

def Topic():  
    top = input("Topic: ")
    return "📋 TOPIC: " + top  

def startWithMsg():
    return "| " + Topic() + " |\n" +  "| " + Authors() + " | " + NoOfChanges() + " | " + Keywords() + " |\n" + "| " + DateAndTime() + " |\n"