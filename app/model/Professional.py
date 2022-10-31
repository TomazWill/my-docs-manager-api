from model.Person import Person

class Professional(Person):
    def __init__(self,
                name: str = None,
                age: str = None,
                address: str = None,
                city_and_state: str = None,
                phone_number: str = None,
                email: str = None,
                birth_date: str = None,
                photo: str = None,
                formation: list = None, 
                certifications: list = None, 
                professional_experiences: str = None, 
                languages: list[str] = None,
                linkedin: str = None):
        super().__init__(name, age, address, city_and_state, phone_number, email, birth_date, photo),
        self.formation = formation
        self.certifications = certifications
        self.professional_experiences = professional_experiences
        self.languages = languages
        self.linkedin = linkedin
        