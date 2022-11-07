from py2neo import *
from models import Person, SocialMedia


class Neo4jConnection:
    def __init__(self):
        self.graph = Graph("bolt://localhost:7687", auth=("neo4j", "123456"))

    def run_cypher(self, cypher:str):
        result = self.graph.run(cypher=cypher)
        return result

    def run_cypher_transaction(self, cypher_list:list[str]):
        tx = self.graph.begin()
        for cypher in cypher_list:
            tx.run(cypher)
        self.graph.commit(tx)

    # def get_node(self):


class MetaSocialMediaGraph:
    def __init__(self):
        self.neo4j = Neo4jConnection()

    def _exist_follow_relationship(self, user_id_1:int, user_id_2:str ,social_media_name:str)->bool:
        cypher = f"match (s {{UserId:{user_id_1},Name:\"{social_media_name}\"}})-[f]-(m {{UserId:{user_id_2},Name:\"{social_media_name}\"}}) return f"

        result = self.neo4j.run_cypher(cypher)
        result_dict = result.data()
        number_of_relations = len(result_dict)
        if number_of_relations == 0:
            return False
        else:
            return True

    def create_follow(self, user_id_1:int, user_id_2:int ,social_media_name:str):
        social_media = SocialMedia.get_social_media(social_media_name)
        cypher_list = []

        is_mutual = self._exist_follow_relationship(user_id_1,user_id_2,social_media_name)

        if is_mutual:
            social_media.mutual_follow()
            delete_old_relationship = f"match (s {{UserId:{user_id_1},Name:\"{social_media_name}\"}})-[f]-(m {{UserId:{user_id_2},Name:\"{social_media_name}\"}}) delete f"
            cypher_list.append(delete_old_relationship)
        else:
            social_media.follow()

        cypher = f"match (s {{UserId:{user_id_1},Name:\"{social_media_name}\"}}) match (m {{UserId:{user_id_2},Name:\"{social_media_name}\"}}) merge (s)-[:{social_media.type}]-(m)"
        cypher_list.append(cypher)
        self.neo4j.run_cypher_transaction(cypher_list)

    def create_people(self, people: list[Person]):
        cypher_list = []
        for person in people:
            query = f"create({person.name}:Person {{Id: {person.id}, Name:\"{person.name}\", LastName:\"{person.last_name}\"}})"
            cypher_list.append(query)
        self.neo4j.run_cypher_transaction(cypher_list)


    def create_social_medias(self, social_media_list:list[SocialMedia]):
        cypher_list = []
        for social_media in social_media_list:
            s =  social_media.name + social_media.user_id + social_media.username
            query = f" create({s}:SocialMedia {{UserId:{social_media.user_id}, Name:\"{social_media.name}\", Username:\"{social_media.username}\"}})"
            cypher_list.append(query)
        self.neo4j.run_cypher_transaction(cypher_list)

    def create_has_properties(self):
        query = (f"match (p:Person) match (s:SocialMedia {{UserId:p.Id}}) merge (p)-[:HAS]-(s)")
        self.neo4j.run_cypher(query)
        