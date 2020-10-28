 > As you complete each section you **must** remove the prompt text. Every *turnin* of this project includes points for formatting of this README so keep it clean and keep it up to date. 
 > Prompt text is any lines beginning with "\<"
 > Replace anything between \<...\> with your project specifics and remove angle brackets. For example, you need to name your project and replace the header right below this line with that title (no angle brackets). 
# \<Study Mates!\>
 > Your author list below should include links to all members GitHub and should begin with a "\<" (remove existing author).
 
 > Authors: \<[Tann Nguyen](https://github.com/tannnguyen13)\> \<[Cindy Do](https://github.com/condoes)\> \<[Gabriela Alvarez](https://github.com/galva041)\>
 
 > You will be forming a group of **THREE** students and work on an interesting project that you will propose yourself (in this `README.md` document). You can pick any project that you'd like, but it needs ot implement three design patterns. Each of the members in a group is expected to work on at least one design pattern and its test cases. You can, of course, help each other, but it needs to be clear who will be responsible for which pattern and for which general project features.
 
 > ## Expectations
 > * Behavioral Pattern: Strategy
 >   * The goal of the user is to improve their focusing abilities. The user can do this by being able to input information (current study time, end study time, etc) into the program for the program to output a plan for the user to get to their end goal. The end result is a unique schedule/plan that will differ to each user depending on their specifications. Abiding by this plan will work towards hatching/growing your monster and completing this plan could reward the user with points to redeem for cosmetic items for your monster. 
 > * Creation Pattern: Abstract Factory
 >   * All of the monsters / eggs in the app are pretty much the same, except for the fact that there in a sense is a ‘class’ system (Longer hatch times = rarer monster). We can use the same structure for all the various monsters, but change out some details. Examples of these details would be the rarity, what element the monster is, etc. With this design pattern, we are using the egg system as the main interface for the monsters, but we can split up the different interfaces into different categories such as rarity, element, etc. Fire types would be able to implement the FireType interface, and so on.
 > * Structural Pattern: Decorator
 >   * Each character stems from a “character” abstract class and we want to implement the ability to earn points to customize each character’s clothing. With the decorator design pattern, we will be able to create a decorator object (Customizer) under the Character class that will help us easily update the user’s character (monster) without affecting the appearance of the other characters. The Customizer object will be extended to different clothing types (hat, shirt, pants, etc). 
 > * All three design patterns need to be linked together (it can't be three distinct projects)
 > * Your project should be implemented in C/C++. If you wish to choose anoher programming language (e.g. Java, Python), please discuss with your lab TA to obtain permission.
 > * You can incorporate additional technologies/tools but they must be approved (in writing) by the instructor or the TA.
 > * Each member of the group **must** be committing code regularly and make sure their code is correctly attributed to them. We will be checking attributions to determine if there was equal contribution to the project.

## Project Description
 > Your project description should summarize the project you are proposing. Be sure to include
 > * Why is it important or interesting to you?
 > * What languages/tools/technologies do you plan to use? (This list may change over the course of the project)
 >   * [toolname](link) - Short description
 > * What will be the input/output of your project?
 >   * Behavioral Pattern: Strategy
 >     * The goal of the user is to improve their focusing abilities. The user can do this by being able to input information (current study time, end study time, etc) into the program for the program to output a plan for the user to get to their end goal. The end result is a unique schedule/plan that will differ to each user depending on their specifications. Abiding by this plan will work towards hatching/growing your monster and completing this plan could reward the user with points to redeem for cosmetic items for your monster. 
 >   * Creation Pattern: Abstract Factory
 >     * All of the monsters / eggs in the app are pretty much the same, except for the fact that there in a sense is a ‘class’ system (Longer hatch times = rarer monster). We can use the same structure for all the various monsters, but change out some details. Examples of these details would be the rarity, what element the monster is, etc. With this design pattern, we are using the egg system as the main interface for the monsters, but we can split up the different interfaces into different categories such as rarity, element, etc. Fire types would be able to implement the FireType interface, and so on.
 >   * Structural Pattern: Decorator
 >     * Each character stems from a “character” abstract class and we want to implement the ability to earn points to customize each character’s clothing. With the decorator design pattern, we will be able to create a decorator object (Customizer) under the Character class that will help us easily update the user’s character (monster) without affecting the appearance of the other characters. The Customizer object will be extended to different clothing types (hat, shirt, pants, etc). 
 > * This description should be in enough detail that the TA/instructor can determine the complexity of the project and if it is sufficient for the team members to complete in the time allotted. 

 > ## Phase II
 > In addition to completing the "Class Diagram" section below, you will need to 
 > * Set up your GitHub project board as a Kanban board for the project. It should have columns that map roughly to 
 >   * Backlog, TODO, In progress, In testing, Done
 >   * You can change these or add more if you'd like, but we should be able to identify at least these.
 > * There is no requirement for automation in the project board but feel free to explore those options.
 > * Create an "Epic" (note) for each feature and each design pattern and assign them to the appropriate team member. Place these in the `Backlog` column
 > * Complete your first *sprint planning* meeting to plan out the next 7 days of work.
 >   * Create smaller development tasks as issues and assign them to team members. Place these in the `Backlog` column.
 >   * These cards should represent roughly 7 days worth of development time for your team, taking you until your first meeting with the TA
## Class Diagram
 > Include a class diagram(s) for each design pattern and a description of the diagram(s). This should be in sufficient detail that another group could pick up the project this point and successfully complete it. Use proper OMT notation (as discussed in the course slides). You may combine multiple design patterns into one diagram if you'd like, but it needs to be clear which portion of the diagram represents which design pattern (either in the diagram or in the description). 
 
 > ## Phase III
 > You will need to schedule a check-in with the TA (during lab hours or office hours). Your entire team must be present. 
 > * Before the meeting you should perform a sprint plan like you did in Phase II
 > * In the meeting with your TA you will discuss: 
 >   - How effective your last sprint was (each member should talk about what they did)
 >   - Any tasks that did not get completed last sprint, and how you took them into consideration for this sprint
 >   - Any bugs you've identified and created issues for during the sprint. Do you plan on fixing them in the next sprint or are they lower priority?
 >   - What tasks you are planning for this next sprint.

 > ## Final deliverable
 > All group members will give a demo to the TA during lab time. The TA will check the demo and the project GitHub repository and ask a few questions to all the team members. 
 > Before the demo, you should do the following:
 > * Complete the sections below (i.e. Screenshots, Installation/Usage, Testing)
 > * Plan one more sprint (that you will not necessarily complete before the end of the quarter). Your In-progress and In-testing columns should be empty (you are not doing more work currently) but your TODO column should have a full sprint plan in it as you have done before. This should include any known bugs (there should be some) or new features you would like to add. These should appear as issues/cards on your Kanban board. 
 ## Screenshots
 > Screenshots of the input/output after running your application
 ## Installation/Usage
 > Instructions on installing and running your application
 ## Testing
 > How was your project tested/validated? If you used CI, you should have a "build passing" badge in this README.
 
