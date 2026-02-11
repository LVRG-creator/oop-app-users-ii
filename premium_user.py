# import the User class from the User2 module
from User2 import User

# make a new class called PremiumUser that is based on user. Don't forget CamelCase for the class name
class PremiumUser(User):
    #premium users can make unlimited posts, so we don't need to set a limit or override the create_post method. We just inherit everything from User and add any new features we want for premium users here. For now, there are no new features, so this class is pretty simple. But we can always add more stuff later if we want to make premium users more special.
    pass    