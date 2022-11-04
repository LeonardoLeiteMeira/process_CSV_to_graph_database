from enum import Enum


class RelationshipType(Enum):
    PERSONAL = "Personal"
    INFLUENCE = "Influence"
    PROFESSIONAL_RELATIONSHIP = "Professional_Relationship"
    CONTENTS = "Contents"
    UNDEFINED = "Undefined"

 
class Person:
    def __init__(self,id:int,name:str,last_name:str):
        self.id = id
        self.name = name
        self.last_name = last_name


class SocialMedia:
    def __init__(self,user_id:int, name:str, username:str):
        self.user_id = user_id
        self.name = name
        self.username = username

    def follow(self):
        raise NotImplementedError("Use an implementation of SocialMedia")

    def mutual_follow(self):
        raise NotImplementedError("Use an implementation of SocialMedia")

    @staticmethod
    def get_social_media(social_media_name:str):
        if social_media_name == "Instagram":
            return Instagram()
        if social_media_name == "LinkedIn":
            return LinkedIn()
        if social_media_name == "Facebook":
            return Facebook()
        if social_media_name == "Twitter":
            return Twitter()
        if social_media_name == "TikTok":
            return TikTok()
        if social_media_name == "Pinterest":
            return Pinterest()
        if social_media_name == "Youtube":
            return Youtube()
        else:
            raise "Error to get Social Media"

class Instagram(SocialMedia):
    def __init__(self):
        self.name = "Instagram"
        self.type = RelationshipType.UNDEFINED

    def follow(self):
        self.type = RelationshipType.INFLUENCE
        print("just follow INSTAGRAM")
        return self

    def mutual_follow(self):
        self.type = RelationshipType.PERSONAL
        print("Mutal connection INSTAGRAM")
        return self

class LinkedIn(SocialMedia):
    def __init__(self):
        self.name = "Linkedin"
        self.type = RelationshipType.UNDEFINED

    def follow(self):
        self.type = RelationshipType.INFLUENCE
        print("just follow LINKEDIN")
        return self

    def mutual_follow(self):
        self.type = RelationshipType.PROFESSIONAL_RELATIONSHIP
        print("Mutal connection LINKEDIN")
        return self

class Facebook(SocialMedia):
    def __init__(self):
        self.name = "Facebook"
        self.type = RelationshipType.UNDEFINED

    def follow(self):
        self.type = RelationshipType.CONTENTS
        print("just follow FACEBOOK")
        return self

    def mutual_follow(self):
        self.type = RelationshipType.PERSONAL
        print("Mutal connection FACEBOOK")
        return self

class Twitter(SocialMedia):
    def __init__(self):
        self.name = "Twitter"
        self.type = RelationshipType.UNDEFINED

    def follow(self):
        self.type = RelationshipType.INFLUENCE
        print("just follow Twitter")
        return self

    def mutual_follow(self):
        self.type = RelationshipType.PERSONAL
        print("Mutal connection Twitter")
        return self

class TikTok(SocialMedia):
    def __init__(self):
        self.name = "TikTok"
        self.type = RelationshipType.UNDEFINED

    def follow(self):
        self.type = RelationshipType.CONTENTS
        print("just follow TikTok")
        return self

    def mutual_follow(self):
        self.type = RelationshipType.CONTENTS
        print("Mutal connection TikTok")
        return self

class Pinterest(SocialMedia):
    def __init__(self):
        self.name = "Pinterest"
        self.type = RelationshipType.UNDEFINED

    def follow(self):
        self.type = RelationshipType.CONTENTS
        print("just follow Pinterest")
        return self

    def mutual_follow(self):
        self.type = RelationshipType.CONTENTS
        print("Mutal connection Pinterest")
        return self

class Youtube(SocialMedia):
    def __init__(self):
        self.name = "Youtube"
        self.type = RelationshipType.UNDEFINED

    def follow(self):
        self.type = RelationshipType.CONTENTS
        print("just follow Youtube")
        return self

    def mutual_follow(self):
        self.type = RelationshipType.CONTENTS
        print("Mutal connection Youtube")
        return self