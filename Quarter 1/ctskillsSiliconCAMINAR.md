Annex A
Computational Thinking Exercise: "Smart School Canteen Queue"

Section: Silicon Score:____________

C# / Name:Chance Mateo V. Caminar Date: 08/16/2026


Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem

Main Problem: The school canteen queue is too slow and crowded because ordering, payment, and checking food supplies are done manually. A system is needed to make ordering and payment faster while also keeping track of available food items.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Students take too long to decide what to order.
2. The cashier manually calculates the total and change.
3. The canteen does not easily know which food items are running low.
4. The long queue becomes crowded during lunch break.

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

Sub-Problem
1. Students take too long to decide.
2. Cashier calculates totals manually.
3. Food stocks are difficult to track.
4. Queue becomes crowded.

CT Skill
1. Decomposition
2. Algorithm
3. Pattern Recognition
4. Decomposition

Example Solution
1. Divide ordering into menu selection, quantity, and confirmation.
2. Create steps that add item prices, receive payment, and calculate change.
3. Track how often each food item is sold and identify items that run low.
4. Separate the process into ordering, payment, and releasing the food.

 Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem

START

Display menu and prices

Ask student to select food
Ask for quantity

Calculate:
total = price × quantity

Ask for amount paid

IF amount paid >= total THEN
    change = amount paid - total
    Display total
    Display change
ELSE
    Display "Insufficient payment"
END IF

END