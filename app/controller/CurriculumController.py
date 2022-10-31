import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from model.Professional import Professional
from model.Image import Image
from definitions import IMAGE_DIR

class CurriculumController:
    
    def create_curriculum(self, path_doc: str = None ):
        doc = DocxTemplate(path_doc) #TODO: When go to Container => str(settings.BASE_DIR) + path_doc
        
        # path_photo_resized = Image().image_resize(img_path_to_resize=f"{IMAGE_DIR}/photo_person.png", name_of_new_image="photo_person_v3")
        photo = InlineImage(doc, f"{IMAGE_DIR}/photo_person.png", width=Mm(40), height=Mm(60))
        
        # TODO: this data can be passed by JSON or by body request (when to be 'api rest')
        professional = Professional(
            name                     = "Willian T. Lima",
            age                      = "26",
            address                  = "Rua Antonio Bandeiras, 123",
            city_and_state           = "Araçatuba/SP",
            phone_number             = "+55 11 97456-7895",
            email                    = "will@hotmail.com",
            birth_date               = "20/11/1998",
            linkedin                 = "https://www.linkedin.com/in/willian-tomaz-de-lima-a1aa81b6/",
            formation                = [],
            certifications           = [],
            professional_experiences = "",
            languages                = [str],
            photo                    = photo
        )

        professional_data_cv = {
            'name':                     professional.name,
            'age':                      professional.age,
            'age':                      professional.age,
            'city_and_state':           professional.city_and_state,
            'phone':                    professional.phone_number,
            'email':                    professional.email,
            'address':                  professional.address,
            'birth_date':               professional.birth_date,
            'linkedin':                 professional.linkedin,
            'today_date':               datetime.today().strftime("%d %b, %Y"),
            'formation':                professional.formation,
            'certifications':           professional.certifications,
            'professional_experiences': professional.professional_experiences,
            'languages':                professional.languages,
            'photo':                    professional.photo
        }

        doc.render(professional_data_cv)
        doc.save(f"generated_doc_{datetime.today()}.docx")
        