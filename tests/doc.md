In the Ports and Adapters architecture (also known as Hexagonal Architecture), there are several essential components that should be unit tested. Let's break this down:

Domain Logic:

Business entities
Value objects
Domain services
Aggregates

Use Cases / Application Services:

These orchestrate the flow of data to and from the domain entities and implement business rules

Port Interfaces:

Both primary (driving) and secondary (driven) port interfaces

Adapters:

Primary adapters (e.g., REST controllers, CLI interfaces)
Secondary adapters (e.g., database repositories, external service clients)

The core idea is to test each component in isolation, ensuring that the business logic is correct and that the components interact properly through well-defined interfaces.
Here's a more detailed explanation of what to focus on for each component:

Domain Logic: Test the behavior and rules of your domain objects, ensuring they maintain invariants and perform calculations correctly.
Use Cases: Test that they correctly orchestrate the flow between ports and the domain, applying business rules as expected.
Port Interfaces: While you don't test interfaces directly, you should test the implementations of these interfaces in your adapters.
Adapters: Test that they correctly translate between the external world and your application's internal representation.

It's important to note that while testing adapters, you should mock the external dependencies (like databases or external services) to keep the tests fast and focused.
Would you like me to provide an example of how to structure unit tests for one of these components?