class Project:
    def __init__(self, title, description, technologies, image, github_link, demo_link=None, category=None):
        self.title = title
        self.description = description
        self.technologies = technologies
        self.image = image
        self.github_link = github_link
        self.demo_link = demo_link
        self.category = category

class Experience:
    def __init__(self, title, company, period, description, achievements):
        self.title = title
        self.company = company
        self.period = period
        self.description = description
        self.achievements = achievements

class Achievement:
    def __init__(self, description):
        self.description = description 