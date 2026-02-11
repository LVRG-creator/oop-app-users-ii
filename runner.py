# bring in the FreeUser and the PremiumUser classes
from free_user import FreeUser
from premium_user import PremiumUser

#make a main function to run the code
def main():
    # make a free user & premium user
    free = FreeUser(name="Free User", email="bum@bezdoma.com", license="BUM123")
    premium = PremiumUser(name="Richard Gere", email = "hunk@hunk.com", license="HUNK123")
    
    # show what happens when a free user tries to post 3 times
    print("Free user trying to post 3 times:")
    free.create_post("First post")
    free.create_post("Second post")
    
    #3rd post
    try:
        free.create_post("Third post")
    except PermissionError as e:
        # show the message from the error
        print("Error:", e)
        
    # show the premium users can post as much as they want
    print("Premium user posting 3 times:")
    premium.create_post("Premium post 1")
    premium.create_post("Premium post 2")
    premium.create_post("Premium post 3")
    
    #show all the posts at once
    print("Richard gere posting like a hunk", premium.posts)
    
# run the main function
if __name__ == "__main__":
    main()