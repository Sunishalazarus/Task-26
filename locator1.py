"""
To save the locators
"""

class WebLocators1:
    def __init__(self):
        self.expandLocator = "//span[contains(text(), 'Expand all')]"
        self.nameLocator = "//input[@aria-label='Name']"
        self.birthdateLocator = "//input[@aria-label='Enter birth date from']"
        self.birthdayLocator = "//input[@aria-label='Enter birthday']"
        self.awardsLocator = "//button[@data-testid='test-chip-id-oscar_best_actress_nominees']"
        self.birthplaceLocator = "//option[@value='BIRTH_PLACE']"
        self.name_birthplaceLocator = "//input[@aria-label='e.g. Arrested']"
        self.see_resultLocator = "//button[@data-testid='adv-search-get-results']"



