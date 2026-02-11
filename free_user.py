# bring in main user class from User2.py
from User2 import User

# make a new class called FreeUser that is based on user and do it in camelCase for the class name
class FreeUser(User):
    # set a limit for how many posts a free user can make
    MAX_POSTS = 2
    
    # make a new version of create_post that replaces the one in User b/c this is the thing that is going to be different
    def create_post(self, content):
        #check how many posts free user made
        if len(self.posts) >= FreeUser.MAX_POSTS:
            # stop them from making more posts and give them a message
            raise PermissionError(f"Free users are broke. Give us more money for more things. You are limited to {FreeUser.MAX_POSTS} posts.")
        
        # if the limit is not reached, call the create_post method from the parent class to make the post
        return super().create_post(content)
    
