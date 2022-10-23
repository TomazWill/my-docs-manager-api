import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate
import docx

from app.model.Person import Person
from app.model.Professional import Professional


doc = DocxTemplate("app/data/template/curriculum-vitae.docx")

# TODO: this data can be passed by JSON or by body request (when to be 'api rest')
person = Person(
    name = "José Martin Filho",
    age = "26",
    address = "Rua Antonio Bandeiras, 123",
    city_and_state = "Araçatuba/SP",
    phone_number = "+55 11 97456-7895",
    email = "jose@hotmail.com",
    birth_date = "20/11/1998",
    linkedin = "https://www.linkedin.com/in/willian-tomaz-de-lima-a1aa81b6/",
)

professional = Professional(
formation = [],
certifications = [],
professional_experiences = "",
languages = [str],
)

today_date  = datetime.today().strftime("%d %b, %Y")

my_personal_data = {
    'name':    person.name,
    'phone':   person.phone_number,
    'email':   person.email,
    'address': person.address,
    'today_date': today_date
}

my_professional_career = {
    'formation': professional.formation,
    'certifications': professional.certifications,
    'professional_experiences': professional.professional_experiences,
    'languages': professional.languages,
}

df = pd.read_csv('fake_data.csv')

for index, row in df.iterrows():
    context = {
        'hiring_manager_name': row['name'],
        'address':             row['address'],
        'phone_number':        row['phone_number'],
        'email':               row['email'],
        'job_position':        row['job'],
        'company_name':        row['company']
    }

    context.update(my_personal_data)

    doc.render(context)
    # doc.save(f"generated_doc_{index}.docx")