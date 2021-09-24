from neo4j import GraphDatabase

uri = "neo4j://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", 'password'))

def create_friend_of(tx, name, friend):
    tx.run("create (a:Person)-[:KNOWS]->(f:Person {name: $friend})"
           "where a.name = $name "
           "return f.name as friend", name=name, friend=friend)

with driver.session() as session:
    session.write_transaction(create_friend_of, "Alice", "Bob")

with driver.session() as session:
    session.write_transaction(create_friend_of, "Alice", "Carl")

driver.close()
