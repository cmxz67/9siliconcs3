Scenario
Recall the sari-sari store inventory problem discussed in the KHub “Study Guide 3: Introduction to OOP (Procedural vs Object-Oriented programming)“.
A sari-sari store needs to keep track of several products. Each product may have information such as:
product name
price
quantity or available stock
Using a purely procedural approach may require several separate variables and functions as the number of products increases.
Object-Oriented Programming provides another way of organizing this information by representing products and other parts of the system as objects with related properties and behaviors.
Your Task
Using the sari-sari store inventory problem, explain how each of the following pillars of Object-Oriented Programming may be applied:EncapsulationAbstractionInheritancePolymorphism
For each OOP pillar, write 2-5 sentences explaining:
how the concept can be used in the sari-sari store inventory system
what data, object, property or method may be involved
how applying the concept can improve the organization or design of the program.

1. Encapsulation:
Encapsulation means keeping the product's information together in one object. A Product class can contain the product name, price, and stock, along with methods like add_stock() and remove_stock(). This makes it easier to keep track of which data belongs to each product.

2. Abstraction: 
Abstraction can be used for tasks that the store needs to do often. For example, an Inventory class could have a sell_product() method that checks the stock and decreases it when a product is sold. The person using the program does not have to deal with each step manually.

3. Inheritance can be useful when the store has different kinds of products. A FoodProduct class and a HouseholdProduct class could both inherit the basic information from a Product class. This means the same product information does not have to be written again for every type.

4. Polymorphism allows different objects to respond to the same method in their own way. For example, FoodProduct and HouseholdProduct could both have a display_info() method, but each one could display additional information that is specific to that product type. This makes it easier to handle different products using one general method.

Reflection: 
I think encapsulation would be the most useful for the inventory system. A store has many products, so putting each product's name, price, and stock in its own object would keep the information organized. It would also make changing the stock easier because the program can use methods instead of changing the values everywhere. If the store gets more products later, the same structure can still be used.
