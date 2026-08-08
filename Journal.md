# Pie-A-Thon
Hi! Welcome to the Journal.md of my first software project, Pie-A-Thon! Read all about it in the Readme, I don't feel like saying it all again here. But you can watch its development here!

# Devlog 1
1h 5min 1sec Logged

I started making Pie-A-Thon today, a game where you work in a pie store, baking pies! It's my first software project, and I'm coding it in Python. I started off by getting used to the rules of Python and the PyGame add-on, which was easy, seeing how I have coded in C++ for my many Arduino projects. I made a simple sprite (a red cube) that can move around with ASWD. I made a wall with collision, and I made two stations for future minigames. My idea is that you need to get ingredients and prepare them and such. It's not much right now, but I think my game has potential!

![An image of the game thus far, with the sprite (red cube), wall (red wall)，flour station (bottom left), and crust station (center)](Images/P1.png)

# Devlog 2

1h 2min 19sec Logged

I added a background to the game (a checkered floor to make it feel more like a restaurant), and I added a minigame state. I figured out how to make drawn items different colors, and how to add pre-drawn sprites (I drew the BG!). I moved some of the minigame locations around, and I'll work on them next. I need to figure out how to get mouse inputs. 

![An image of the game with a checkered background](Images/P2.png)

# Devlog 3
1h 4min 22sec Logged

I figured out how to detect the actions of the mouse (click, position, and such) and I drew a bunch of sprites for the flour minigame! That's what took up the most time, drawing really isn't my thing. Still, I want this game to be fully my own, so I'm gonna have to draw (:

![The flower bag sprite](Images/pixil-frame-0(15).png)

# Devlog 4

50 min 39sec Logged

I'm mostly finished with the flour minigame! I thought that moving the spoon with the mouse would be tricky, but it turned out it was really easy. I just plugged in mouse_x and mouse_y for the spoon's x and y coords, and it worked fine. With a little tuning, of course (x + yada yada and y - yada yada). This was a lot simpler than I thought! I guess Python is known for being simple, though. However, I am dealing with a glitch where the spoon seems to constantly be sensing that it is touching the flour bag. I will have to look into that. 

![A picture of the in-progress flour minigame](Images/P3.png)

# Devlog 5
58m 17sec Logged

I finished the flour minigame! Turns out the bug was that the hitboxes of the sprites were drawn on top of each other and technically touching, while the actual sprites looked like they weren't. I fixed it and the flour minigame works well! I'll work on the crust minigame next.

![The completed flour minigame](Images/P4.png) 

# Devlog 6
1h 9min 47sec Logged

I made a dough minigame! That's right, I realized that you would need to make dough before shaping the crust. I wrote a complicated math algorithm to detect circles made by the mouse to detect kneading, which I totally didn't find on YouTube. I also had to draw many sprites to make the kneading interactive. Otherwise, it's more of the same knead-update-knead.

![A picture of the Dough0 sprite!](Images/P5.png)
![A picture of the Dough4 sprite!](Images/P6.png)

# Devlog 7
1h 8min 32sec Logged

I made the crust minigame! You initially circle the mouse to spread oil onto the dish, then you quickly left click to shape the crust. Again, I drew all the sprites. I added instructions on the top left of each minigame for user reference. 

![An image of the first stage of the crust-making minigame](Images/p7.png)
![An image of the completed crust-making minigame](Images/P8.png)

# Devlog 8
41min 22sec Logged

I made some functional changes to my game! I made it so that you can't make dough before collecting flour, and that you couldn't make crust before making dough. I added neat warnings when you were missing ingredients and notifications when you picked them up. I'll add ingredient stations for fillings, a filling making station, and a pie assembly station before adding an oven. I'll also need to get to making the player sprite soon ToT. My ultimate goal is to add customers!

![An image of a missing ingredient screen](Images/P9.png)
![An image of a player (me lol) that has just picked up some dough, giving him a notification!](Images/P10.png)

# Devlog 9
1h 23min 39sec Logged

I added a strawberry station to the game. You wash the strawberries and mash them to make a jam. Instead of a boolean for the acquisition, the strawberries are an integer, for customers may want multiple servings in their pie. I plan to add more fruits to the game. If room becomes a problem, I may replace individual fruit stations with an ingredient shelf. I honestly find the washing mechanic pretty boring after adding it, so I may get rid of it and add a jam maker to the game where you pour all your ingredients into a machine and crank a handle. I might add more ingredients next, or make a pie assembly station and an oven.

![An image of the strawberry-washing process](Images/P11.png)

# Devlog 10
1h 46min 12sec Logged

I replaced the strawberry station with an ingredients station. I also got rid of strawberries entirely, and am instead using blueberries, cherries, pumpkins, and apples. I'll make a filler-making station next. I figured out how to update text real-time, so I can display how much of each ingredient the player has in the ingredient-gathering minigame. 

![An image of the ingredient select minigame with the quantities of ingredients you have at the bottom](Images/P12.png)

# Devlog 11
1h 11min 50sec Logged

I successfully made an ingredient-gathering minigame by drawing four different fruits, making four different variables, and adding to those variables every time you click on those fruits in the minigame. I'll need to make a more complicated filler-making minigame now, but I have a good idea already (:

![An image of the ingredient-gathering minigame](Images/P13.png)

# Devlog 12
2h 2min 20sec Logged

I drew and coded a jam-making machine by drawing the main body in the back and drawing a crank on top. The crank rotates with the mouse. I had to do a lot of fine tuning to make sure that the mouse had to follow a very certain path in order for the crank to follow. The mouse also cannot be too far away from the crank, and the crank can only be spun clockwise. When spun 360 degrees, the crank will convert the last fruit that you picked up into jam, discarding the fruit in the process. 

![A picture of the jam-making machine](Images/P14.png)

# Devlog 13
1h 39min 50sec Logged

I coded the collection confirmation function of the ingredient shelf. I made it so that every time you collect an item of a different type, the collection message will create a new line for that item. That allows for up to four lines displayed above your character at a time. I also coded a trash can. It has the same confirmation message logic as the ingredient shelf, except its text is red. 

![An image of the ingredient shelf confirmation message](Images/P15.png)
![An image of the trash confirmation message](Images/P16.png)

# Devlog 14
1h 8min 24sec Logged

I coded the jam acquisition message, same as the fruit and trash confirmation messages. I have noticed an oversight where the acquisition message states the total number of items you have instead of the number you newly acquired. I must find a way to fix that. Anyway, I also added a fruit display to the jam-making minigame. It shows the fruits you currently have in your inventory in the fruit slot above the jam-maker, and as you turn the crank, the fruits disappear. 

![An image of the jam-making minigame, now with the fruits you need to process displayed above the crank in the fruit slot](Images/P17.png)
![An image of the jam acquisition message](Images/P18.png)

# Devlog 15
1h 1min 22sec Logged

I fixed two oversights. The first was an oversight where acquisition messages would print, say, "Acquired 1 Apples!" or "Acquired 1 Apple Jams!". I updated the messages so that they now print "Acquired an Apple!" and such when you only pick up one of an item. The second oversight was the fact that you would not get any acquisition messages if you quit the jam-making minigame early by pressing "e". I created acquisition messages for that event, and it was fixed. 

![An image of some of the single-unit acquisition messages](Images/Screenshot2026-08-07175153.png)
