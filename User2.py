class User:
    #this is the constructor
    #we will be inputting 3 things of name, email and license
    all_users = []
    all_posts = []
    total_users = 0
    
    def __init__(self, name, email, license):
        User.total_users += 1
        self._id = User.total_users
        
        
        #data is storing the inputs into the OBJECT'S memory
        self._name = name
        self._email = email
        self._license = license
        
        # each person has their own posts
        self._posts = []
        
        # add this user to the global list of users
        User.all_users.append(self)
        
    def __repr__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}', license='{self._license}')"

    # ID where can just read it
    @property
    def id(self):
        return self._id
    
    # so then do name next
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value
        
    # email
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not User.validate_email(value):
            raise ValueError("invalid email bozo")
        self._email = value
        
    # license
    @property
    def license(self):
        return self._license
    
    @license.setter
    def license(self, value):
        if not isinstance(value, (str, int)):
            raise ValueError("License must be a string or integer")
        self._license = value
        
    # posts (read only)
    @property
    def posts(self):
        return self._posts
    
    # method to create a post
    def create_post(self, content):
        post = {
            "user_id": self._id,
            "content": content
        }
        
        # add to this user's posts
        self._posts.append(post)
        
        # add to global list of posts
        User.all_posts.append(post)
        return post
    
# class methods 
    @classmethod
    def get_all_users(cls):
        return cls.all_users
    
    @classmethod
    def get_all_posts(cls):
        return cls.all_posts
    
    @staticmethod
    def validate_email(email):
        if not isinstance(email, str):
            return False
        if "@" not in email:
            return False
        return True

#----now a few peeps---
#user_one = User("Brandon Livrago", "brandon@livrago.com", "ABC12345")
#user_two = User("John Doe", "john@doe.com", "GONE12354")

#verify
#print(user_one)
#print(user_one.name)
#print(f"License for {user_two.name} is {user_two.license}")

# more tests
#print("Posts:", user_one.posts)

#user_two.create_post("This is John's first post!")
#user_one.create_post("Hello world!")
#print("posts are making one:", user_one.posts)
#print("all posts:", User.all_posts)

# test bad emails b/c of staticmethod
#print("valid email:" , User.validate_email("brandon@livrago.com"))
#print("invalid email:" , User.validate_email("brandonlivrago.com"))
#print("integer" , User.validate_email(12345))