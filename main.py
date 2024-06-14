import streamlit as st
import datetime
import time
from googletrans import Translator
import io

st.set_page_config(
    page_title="Numerology",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
)
st.header("Numeric Analysis")

on = st.toggle("ENG|TR")

def translate(text, src_lang='en', dest_lang='tr'):
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated_text.text

def reduce_to_single_digit_or_master_number(number):
    while number > 9 and number not in [11, 22, 33]:
        number = sum(int(digit) for digit in str(number))
    return number

def calculate_life_path_number(birth_date):
    day, month, year = map(int, birth_date.split('-'))

    # Reduce day, month, and year to single digits
    reduced_day = reduce_to_single_digit_or_master_number(day)
    reduced_month = reduce_to_single_digit_or_master_number(month)
    reduced_year = reduce_to_single_digit_or_master_number(year)

    # Sum the reduced values and reduce again
    life_path_number = reduced_day + reduced_month + reduced_year
    life_path_number = reduce_to_single_digit_or_master_number(life_path_number)

    return life_path_number


def letter_to_number(letter):
    letter = letter.upper()
    letter_mapping = {
        'A': 1, 'J': 1, 'S': 1,
        'B': 2, 'K': 2, 'T': 2,
        'C': 3, 'L': 3, 'U': 3,
        'D': 4, 'M': 4, 'V': 4,
        'E': 5, 'N': 5, 'W': 5,
        'F': 6, 'O': 6, 'X': 6,
        'G': 7, 'P': 7, 'Y': 7,
        'H': 8, 'Q': 8, 'Z': 8,
        'I': 9, 'R': 9
    }
    return letter_mapping.get(letter, 0)

def reduce_to_single_digit_or_master_number(number):
    while number > 9 :
        number = sum(int(digit) for digit in str(number))
    return number
    
def calculate_destiny_number(full_name):
    total = 0
    for letter in full_name.replace(' ', ''):
        total += letter_to_number(letter)
    return reduce_to_single_digit_or_master_number(total)


one = """Just as Aries, the first sign of the zodiac, is about action and initiation, 1 is linked to forward 
motion in Numerology. 1 symbolizes a pioneering spirit, independent nature, and innate leadership capabilities. 
On a bad day, 1 can be a bit bossy or boastful, hiding any insecurities behind over-developed self-importance.
1 must remember that although it is first, it can very quickly become the loneliest number. Even the most 
autonomous 1s need the support of their friends, family, and lovers."""

two = """The number 2 is linked to sensitivity, balance, and harmony. Within numerology, the 2 vibration assumes
the role of the mediator, creating harmony by bringing together dissonant forces through compassion, empathy, 
and kindness. 2 is linked to psychic abilities and intuition, and if this number appears as a Life Path or Destiny
Number, the individual will be astute to subtle energy shifts and emotional nuances. Because 2 is so sensitive,
it is very conflict-averse, and can end up feeling under-appreciated or unacknowledged. 2 must avoid seeking
external validation and, instead, realize that perfect equilibrium needed already exists within."""

three = """Communication is paramount for 3. Symbolically, 3 represents the output of two joined forces: It is the
essence of creation. 3 is highly gifted at expression, seamlessly sharing innovative and pioneering concepts
through art, writing, and oration. Your work inspires, motivates, and uplifts others, and 3 finds great joy making
others smile. However, 3 is also known to be quite moody, and if 3 feels misunderstood, may withdraw entirely. The
escapist tendencies of 3 are easily mitigated by practicing peaceful mindfulness: With such an active imagination,
it’s important for 3 to find moments of quiet to reset, restore, and recharge."""

four = """In numerology, 4 has an earthy-energy and is centered around fortifying its roots. 4 adamantly believes in
the physical world and knows that investing in a solid infrastructure is necessary for building a lasting legacy. 
Practical, hardworking, and responsible, the vibration of the number 4 is focused on creating logical systems that
can support scalable growth. There is a solidity to 4, however, that can quickly devolve into rigidity; 4 must 
remember that rules are meant to enhance, not inhibit. It’s easy for 4 to become stubborn, so 4 benefits from 
learning to loosen up and think outside the box. 4 will feel liberated and inspired by finding the bravery to take a
few bold risks."""

five = """Free-thinking, adventurous, and progressive, 5 is defined by freedom. 5 needs to experience the world by 
engaging its five senses: For 5, life lessons are acquired through spontaneous acts of bravery. Akin to Sagittarius
energy within astrology, 5 is known for its playful, impulsive, and vivacious spirit. But on the other side of its
signature joie de vivre, 5 can become restless and impatient. Since 5 is always seeking discovery, it has a difficult
time accepting life’s day-to-day responsibilities — including professional and interpersonal commitments. 5 must 
remember that when it narrows its gaze, it will discover that the most rewarding exploration exists in its own backyard."""

six = """6 is truly remarkable for its nurturing, supportive, and empathic nature, embodying the essence of a true healer. 
This special number has the remarkable ability to address emotional and physical challenges with a gentle yet effective 
approach. It is deeply committed to caring for the well-being of friends, family, and loved ones, and carries a strong sense 
of responsibility. With its gentle and empathetic demeanor, 6 can easily connect with children and animals, showing a deep 
sense of tenderness and a natural caregiving spirit. Nevertheless, 6's protective nature can sometimes overshadow others, 
becoming overly controlling. To find balance, 6 must learn to cultivate trust and understanding, recognizing that everyone 
has their own unique path to walk."""

seven = """Imagine a world where the number 7 is not just a digit, but a mysterious detective with extraordinary 
investigative abilities and unmatched analytical skills. Astrologically, 7 is a powerful blend of Virgo and Scorpio 
energy, which makes it extremely detail-oriented and driven by inner wisdom rather than tangible realities. With its 
keen eye and astute observations, 7 fuels a quick-witted, inventive spirit. This number can quickly identify flaws in 
any system, making it a bit of a perfectionist. However, 7 must remember to balance its inherent skepticism with an 
open mind, because not everything will be foolproof — and that's what makes life fun!"""

eight = """Get ready to unlock the power of 8! In numerology, the number 8 is all about abundance, material wealth, and 
financial success. With its natural magnetism, 8 effortlessly takes on leadership roles and races to extraordinary 
heights. But remember, with great power comes great responsibility. On a bad day, 8 can be overly controlling and 
possessive. Nevertheless, by giving back to the community, 8 can mitigate these negative qualities and realize the true 
value of contributing to the greater good."""

nine = """It indicates that you are an old soul with a deep understanding of life's challenges 
and triumphs. You have a unique ability to connect the dots and see the bigger picture. Your mission is to reach the highest 
state of consciousness and help others do the same. You are fearless when it comes to transformation, and your adaptable 
spirit inspires others to explore their own potential. Just remember to stay grounded and find the balance between 
imagination and reality – that's where your true power lies!"""


eleven = """Master Number 11 revs up the energy of Number 2; its purpose is to heal the self and others through 
its elevated psychic abilities. Often, Master Number 11's intuitive gifts are a result of extreme life circumstances: 
Master Number 11 has no choice but to cultivate extrasensory talents. In numerology, Master Number 11 is connected 
to spiritual enlightenment, awareness, and philosophical balance."""

twentytwo = """Master Number 22, often referred to as the Master Builder, expands on the vibrations
of Number 4. Master Number 22 is inspired to create platforms in the physical realm that transcend immediate 
realities — by fusing the tangible and intangible, Master Number 22 cultivates a dynamic long-term legacy. Master Number 
22's skills are usually a byproduct of early childhood instability that fuels innovative thought. Industrious, creative, and
dependable, Master Number 22 is always on a mission to transform."""


dictionary = {1:one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine, 11:eleven, 22:twentytwo}

with st.form("Information", clear_on_submit=False):
    data = st.date_input(label="What is your birthday?", value=datetime.date.today(), max_value=datetime.date.today(), min_value=datetime.date(year=1906, month=12, day=31))
    full_name = st.text_input(label= "Enter your full name")
    run = st.form_submit_button("Send", type="primary")


if run:
    birth_date = str(data)
    life_path_number = calculate_life_path_number(birth_date)
    destiny_number = calculate_destiny_number(full_name)
    path = f"Your life path number is {life_path_number}! " + dictionary[life_path_number]
    destiny = f"In addition, your destiny number is {destiny_number}! " + dictionary[destiny_number]
    if on:
        path = translate(path)
        destiny = translate(destiny)
        st.write(path)
        st.write(destiny)

    st.write(path)
    st.write(destiny)



