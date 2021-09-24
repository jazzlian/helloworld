Driver driver = GraphDatabase.driver("neo4j://localhost:7687", AuthTokens.basic("jim", "1234"))

try( Session session = driver.session() )
{
    session.writeTransaction(new TransactionWork<String>()
    {
        @Override
        public String execute( Transaction transaction)
        {
            Result result = 
                transaction.run(
                    "CREATE (a:Person {name: $name}) " +
                    "-[:KNOWS]->(f:Person {name: $friend}) " +
                    "RETURN f.name as friend",
                    parameters("name", "Alice", "friend", "Bob")
                );

            return result.single().get(0).asString();
        }
    } );
}

driver.close();