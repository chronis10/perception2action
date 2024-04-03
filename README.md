# Perception to Action

![HUA](./assets/hua.png)

## Abstract 
 Providing a user-friendly interface for the operators of 
            robotic devices is challenging but can save them precious time when
            reprogramming a device to perform different tasks under varying conditions. 
            This paper presents a novel pipeline that adds context awareness at every 
            step of the task execution and employs LLMs to develop a textual interface 
            that supports commands and directions in natural language. Contextual 
            awareness is achieved by analysing input from a camera that supervises 
            the task execution and leveraging 6D pose estimation and scene graph 
            generation models, to create an enriched representation of the task's 
            environment. The rich scene graph incorporates spatial information and 
            refined relationships between objects, and along with the user prompt in 
            natural language is given as input to an LLM-powered chatbot, thus 
            enabling a more intuitive interaction between the user and the robot that 
            requires the minimum information from the user. The first experiments in a 
            simulated environment demonstrate the effectiveness of the proposed approach 
            in facilitating task execution through natural language inputs, empowering 
            users without programming expertise to interact seamlessly with robotic systems and achieve 
            complicated tasks with minimum effort.

<center>
    <video width="640" height="280" controls loop autoplay muted>
        <source src="./assets/SGGLLM.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</center>

## Authors

- Christos Chronis Ph.D. Candidate 
- Iraklis Varlamis, Professor 
- Dimitrios Michail, Associate Professor 
- Konstantinos Tserpes, Associate Professor 
- Georgios Dimitrakopoulos, Associate Professor 

Harokopio University of Athens, Department of Informatics and Telematics

## Clear Prompts
## Scenario 1
**Prompt** 
> Pick the blue cube and place it on pad three 

**LLM Explanation** 
> To place the blue cube on pad three, the arm first grasps the blue cube, which is on top of the green cube. After grasping the blue cube, the arm returns to the home position. Then, the arm places the blue cube on pad three, following the rule that objects can be placed on pads. Finally, the arm returns to the home position to complete the task.

**LLM Commands** 

* grasp -> blue cube
* go home
* place -> pad three
* go home
* go home

**Preview** 

![Preview](./expirements/c/1/exp.gif)
## Scenario 2
**Prompt** 
> Pick the green cude and place it on pad three

**LLM Explanation** 
> First, the blue_cube, which is on top of the green_cube, is moved to the table_surface to clear the green_cube. Then, the green_cube is grasped and placed on pad_three as requested. After each 'grasp' and 'place', the arm returns to the home position to ensure safety and precision.

**LLM Commands** 

* grasp -> blue cube
* go home
* place -> table surface
* go home
* grasp -> green cube
* go home
* place -> pad three
* go home

**Preview** 

![Preview](./expirements/c/2/exp.gif)
## Scenario 3
**Prompt** 
> Place the blue cube on top of the red cube 

**LLM Explanation** 
> To place the blue cube on top of the red cube, the robotic arm first grasps the blue cube, which is initially on top of the green cube. After grasping the blue cube, the arm returns to its home position. Then, it places the blue cube directly on top of the red cube, following the user's prompt. Finally, the arm returns to the home position to complete the task.

**LLM Commands** 

* grasp -> blue cube
* go home
* place -> red cube
* go home

**Preview** 

![Preview](./expirements/c/3/exp.gif)
## Scenario 4
**Prompt** 
> Pick the yellow cube and place it on top of the red cube 

**LLM Explanation** 
> First, the blue_cube is moved from the green_cube to pad_three to clear the way. Next, the green_cube is moved from the yellow_cube to pad_three. Then, the yellow_cube is picked up and placed on top of the red_cube. Each grasp and place action is followed by a return to the home position to comply with the rules.

**LLM Commands** 

* grasp -> blue cube
* go home
* place -> pad three
* go home
* grasp -> green cube
* go home
* place -> pad three
* go home
* grasp -> yellow cube
* go home
* place -> red cube
* go home

**Preview** 

![Preview](./expirements/c/4/exp.gif)
## Scenario 5
**Prompt** 
> Place the red cube on top of the blue cube 

**LLM Explanation** 
> To place the red cube on top of the blue cube, the robotic arm first grasps the red cube from its initial position on pad_two. After grasping the red cube, the arm returns to the home position. Then, it places the red cube directly on top of the blue cube, which is already on top of the green cube. Finally, the arm returns to the home position to complete the task.

**LLM Commands** 

* grasp -> red cube
* go home
* place -> blue cube
* go home
* go home

**Preview** 

![Preview](./expirements/c/5/exp.gif)
## Scenario 6
**Prompt** 
> Place the yellow cube on pad three 

**LLM Explanation** 
> To place the yellow cube on pad three, the blue cube and green cube, which are on top of the yellow cube, must be moved first to avoid violating the rule of not moving objects under other objects. The blue cube is moved to pad two, followed by the green cube to the same location, ensuring that objects are not stacked on the table surface and that no two objects occupy the same space. After clearing the yellow cube, it is grasped and placed on pad three. Each grasp and place action is followed by returning the arm to the home position to ensure the arm is correctly positioned for the next action.

**LLM Commands** 

* grasp -> blue cube
* go home
* place -> pad two
* go home
* grasp -> green cube
* go home
* place -> pad two
* go home
* grasp -> yellow cube
* go home
* place -> pad three
* go home

**Preview** 

![Preview](./expirements/c/6/exp.gif)
## Scenario 7
**Prompt** 
> Stack the cubes on pad three with the following order, blue cube on pad, red cube above blue, green cube above blue and yellow cube above green

**LLM Explanation** 
> The task was to stack the cubes on pad three in a specific order. First, the blue cube was moved from its initial position on top of the green cube to pad three. Next, the green cube was placed on top of the blue cube. Then, the yellow cube was moved from its initial position on pad one to the top of the green cube. Finally, the red cube was moved from pad two to the top of the blue cube, completing the stack in the specified order. Each grasp and place action was followed by a return to the home position to ensure the arm was correctly positioned for the next move.

**LLM Commands** 

* grasp -> blue cube
* go home
* place -> pad three
* go home
* grasp -> green cube
* go home
* place -> blue cube
* go home
* grasp -> yellow cube
* go home
* place -> green cube
* go home
* grasp -> red cube
* go home
* place -> blue cube
* go home

**Preview** 

![Preview](./expirements/c/7/exp.gif)
## Scenario 8
**Prompt** 
> At start place the blue cube on the pad three, then place the red cube on top of the blue cube, then place the green cube on top of the red cube and finally place the yellow cube on top of the green cube.

**LLM Explanation** 
> The task begins by moving the blue cube from its initial position on the green cube to pad three. Following this, the red cube is moved from pad two and placed on top of the blue cube. Next, the green cube, which was initially under the blue cube, is moved and placed on top of the red cube. Finally, the yellow cube, initially on pad one, is moved and placed on top of the green cube. Each 'grasp' and 'place' action is followed by a 'go_home' command to reset the arm's position, ensuring the task is completed efficiently and according to the rules.

**LLM Commands** 

* grasp -> blue cube
* go home
* place -> pad three
* go home
* grasp -> red cube
* go home
* place -> blue cube
* go home
* grasp -> green cube
* go home
* place -> red cube
* go home
* grasp -> yellow cube
* go home
* place -> green cube
* go home

**Preview** 

![Preview](./expirements/c/8/exp.gif)
## Abstract Prompts
## Scenario 1
**Prompt** 
> Clean up the table  

**LLM Explanation** 
> The task was to clean up the table by moving all cubes off the table surface and onto the pads. The sequence started by moving the yellow_cube, which was directly on the table surface, followed by the green_cube, which was on pad_one. The yellow_cube was then placed on pad_one, where the green_cube originally was. Next, the blue_cube, which was on pad_two, was moved, followed by the red_cube, also on pad_two. The green_cube was placed on the table surface temporarily to make room. Finally, the blue_cube was placed on pad_one (on top of the yellow_cube), and the red_cube was placed on pad_two. This sequence ensured that all cubes were moved off the table surface and onto the pads, adhering to the rules and minimizing movements.

**LLM Commands** 

* grasp -> yellow cube
* go home
* grasp -> green cube
* go home
* place -> yellow cube
* go home
* grasp -> blue cube
* go home
* place -> green cube
* go home
* grasp -> red cube
* go home
* place -> blue cube
* go home
* place -> red cube
* go home

**Preview** 

![Preview](./expirements/a/1/exp.gif)
## Scenario 2
**Prompt** 
> Put at least one cube on each pad 

**LLM Explanation** 
> To put at least one cube on each pad, the task starts with the yellow_cube, which is initially on the table_surface and not on any pad. The yellow_cube is grasped and placed on pad_three, which initially has no cube on it. This action ensures that each pad (pad_one, pad_two, and pad_three) has at least one cube on it. The blue_cube is already on pad_two, and the green_cube is on pad_one. The task is completed with minimal movements, adhering to the rules and the prompt's requirements.

**LLM Commands** 

* grasp -> yellow cube
* go home
* place -> pad three
* go home
* go home

**Preview** 

![Preview](./expirements/a/2/exp.gif)
## Scenario 3
**Prompt** 
> Make two stacks of two cubes on pad three and pad two

**LLM Explanation** 
> To make two stacks of two cubes on pad three and pad two, the task starts by moving the yellow_cube to pad_three. Then, the green_cube is placed on top of the yellow_cube to form the first stack on pad_three. Next, the red_cube is moved to pad_two, and finally, the blue_cube is placed on top of the red_cube to form the second stack on pad_two. The robot arm returns to the home position after each grasp and place action, and also at the end of the task to ensure it follows the rules.

**LLM Commands** 

* grasp -> yellow cube
* go home
* place -> pad three
* go home
* grasp -> green cube
* go home
* place -> yellow cube
* go home
* grasp -> red cube
* go home
* place -> pad two
* go home
* grasp -> blue cube
* go home
* place -> red cube
* go home
* go home

**Preview** 

![Preview](./expirements/a/3/exp.gif)
## Scenario 4
**Prompt** 
> Place the cube which is to the right of the blue cube on pad three.

**LLM Explanation** 
> The cube to the right of the blue cube is the green cube. The task is to place the green cube on pad three. To achieve this, the robotic arm first grasps the green cube, then returns to the home position. Next, it places the green cube on pad three and finally returns to the home position to complete the task.

**LLM Commands** 

* grasp -> green cube
* go home
* place -> pad three
* go home

**Preview** 

![Preview](./expirements/a/4/exp.gif)
## Scenario 5
**Prompt** 
> Place the cube which is in front of the yellow cube on pad three

**LLM Explanation** 
> The task was to place the cube which is in front of the yellow cube on pad three. The blue cube is identified as the cube in front of the yellow cube. The sequence of actions began by grasping the blue cube, then returning to the home position. Following this, the blue cube was placed on pad three, and the arm returned to the home position to complete the task.

**LLM Commands** 

* grasp -> blue cube
* go home
* place -> pad three
* go home
* go home

**Preview** 

![Preview](./expirements/a/5/exp.gif)
## Scenario 6
**Prompt** 
> Stack all the cubes on a pad

**LLM Explanation** 
> The task is to stack all the cubes on a pad. The sequence starts by moving the yellow_cube to pad_three to clear the way. Next, the green_cube is placed on the yellow_cube, following the rule of stacking objects on top of each other. Then, the red_cube is moved and placed on the green_cube. Finally, the blue_cube, which was initially on pad_two, is placed on the red_cube, completing the task of stacking all cubes. Each 'grasp' and 'place' action is followed by a 'go_home' command to reset the arm's position, ensuring efficient and safe operation.

**LLM Commands** 

* grasp -> yellow cube
* go home
* place -> pad three
* go home
* grasp -> green cube
* go home
* place -> yellow cube
* go home
* grasp -> red cube
* go home
* place -> green cube
* go home
* grasp -> blue cube
* go home
* place -> red cube
* go home

**Preview** 

![Preview](./expirements/a/6/exp.gif)
## Fuzzy Prompts
## Scenario 1
**Prompt** 
> Pick the cube that symbolize the sky

**LLM Explanation** 
> The task was to pick the cube that symbolizes the sky, which is the blue_cube. The blue_cube was directly accessible on pad_two, so the robotic arm grasped the blue_cube and then returned to the home position. No further actions were required to complete the task as per the user's prompt.

**LLM Commands** 

* grasp -> blue cube
* go home
* go home

**Preview** 

![Preview](./expirements/f/1/exp.gif)
## Scenario 2
**Prompt** 
> If red is patty, green is lettuce, yellow is banana and blue is water and every pad is a plate, i need the ingredients of the burger on the plates

**LLM Explanation** 
> The task is to place the ingredients of a burger (red_cube as patty and green_cube as lettuce) on the plates (pads). First, the red_cube (patty) is grasped and placed on pad_three, representing one plate. Then, the green_cube (lettuce) is grasped and placed on pad_two, representing another plate. The task is completed by returning the arm to the home position, ensuring all movements contribute meaningfully to arranging the burger ingredients on the plates as requested.

**LLM Commands** 

* grasp -> red cube
* go home
* place -> pad three
* go home
* grasp -> green cube
* go home
* place -> pad two
* go home
* go home

**Preview** 

![Preview](./expirements/f/2/exp.gif)
## Scenario 3
**Prompt** 
> If red is patty, green is lettuce, yellow is bread and blue is water and pad two is a plate, make a burger and on a  plate

**LLM Explanation** 
> To make a burger on a plate as per the prompt, the sequence of actions starts by creating the base of the burger with the bottom bread (yellow_cube_2), followed by the patty (red_cube), lettuce (green_cube), and top bread (yellow_cube), and placing this stack on the plate (pad_two). Each object is grasped and placed in sequence to form the burger, ensuring the burger is assembled correctly before placing it on the plate. The task is completed by returning the arm to the home position.

**LLM Commands** 

* grasp -> yellow cube 2
* go home
* place -> pad two
* go home
* grasp -> red cube
* go home
* place -> yellow cube 2
* go home
* grasp -> green cube
* go home
* place -> red cube
* go home
* grasp -> yellow cube
* go home
* place -> green cube
* go home
* go home

**Preview** 

![Preview](./expirements/f/3/exp.gif)
## Scenario 4
**Prompt** 
> Make the tallest tower you can  

**LLM Explanation** 
> To make the tallest tower possible, the strategy is to stack the cubes on top of each other in descending order of their initial positions from right to left, as they are all on the table surface and no cube is initially on top of another. The sequence starts with grasping the yellow_cube, placing it on the green_cube, then grasping the blue_cube and placing it on the yellow_cube, followed by grasping the red_cube and placing it on the blue_cube, and finally grasping the yellow_cube_2 and placing it on the red_cube. This sequence ensures the tallest possible tower is built with the available cubes, adhering to the rules of not moving pads or the table, and ensuring no unnecessary movements are made.

**LLM Commands** 

* grasp -> yellow cube
* go home
* place -> green cube
* go home
* grasp -> blue cube
* go home
* place -> yellow cube
* go home
* grasp -> red cube
* go home
* place -> blue cube
* go home
* grasp -> yellow cube 2
* go home
* place -> red cube
* go home
* go home

**Preview** 

![Preview](./expirements/f/4/exp.gif)
