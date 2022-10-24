


class Professional:
    def __init__(self,
                formation: list = None, 
                certifications: list = None, 
                professional_experiences: str = None, 
                languages: list[str] = None):
        self.formation = formation
        self.certifications = certifications
        self.professional_experiences = professional_experiences
        self.languages = languages
    
    