from neo4j import GraphDatabase
import pandas as pd
from my_neo4j import MetaSocialMediaGraph
from models import Person, SocialMedia

def insert_people(graph:MetaSocialMediaGraph):
    df = pd.read_csv("csv/WS-Project-People.csv", delimiter=",")
    people:list[Person] = []
    for row in df.iterrows():
        id = str(row[1]["Id"])
        name = row[1]["Name"]
        last_name = row[1]["LastName"]
        person = Person(id,name,last_name)
        people.append(person)
    
    graph.create_people(people)

def insert_social_media(graph:MetaSocialMediaGraph):
    df = pd.read_csv("csv/WS-Project-SocialMedias.csv", delimiter=",")
    social_media_list:list[SocialMedia] = []
    for row in df.iterrows():
        userId = str(row[1]["UserId"])
        name = row[1]["Name"]
        username = row[1]["Username"]

        socialMedia = SocialMedia(userId, name, username)

        social_media_list.append(socialMedia)

    graph.create_social_medias(social_media_list)


def create_follow_properties(graph:MetaSocialMediaGraph):
    df = pd.read_csv("csv/WS-Project-Follows.csv", delimiter=",")
    for row in df.iterrows():
        person1 = row[1]["IdPerson"]
        person2 = row[1]["IdFollow"]
        social_media_name = row[1]["SocialMedia"]
        graph.create_follow(person1,person2,social_media_name)


if __name__ == "__main__":
    graph = MetaSocialMediaGraph()
    try:
        insert_people(graph)
        insert_social_media(graph)
        graph.create_has_properties()
        create_follow_properties(graph)

        print("SUCCESS")
    except Exception as e:
        print(e)
