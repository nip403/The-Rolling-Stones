# Atari-Asteroids
Yet another clone of the classic game Asteroids by Atari in Python 3.x using the Pygame module.

# Maths
I draw the spaceship and the asteroid polygons using these equations:
- x = cx + r * cos(theta)
- y = cy + r * sin(theta)

where (cx,cy) is the centre point of the circle, r is the radius, and theta is the angle in [radians](https://en.wikipedia.org/wiki/Radian).\
Note that radians=0 begins at the rightmost point on the circle.

Refer to this [wikipedia article](http://en.wikipedia.org/wiki/Circle#Equations) for more information on Parametric equations.

The collision function between the ship, the bullets and the asteroids calculates the distance between the two objects (excluding the radii) and checks whether it is positive:

![](https://latex.codecogs.com/gif.latex?\sqrt{(ship.x-rock.x)^{2}&plus;(ship.y-rock.y)^{2}}&space;-&space;r1&space;-&space;r2&space;<&space;0)

# Gameplay

#### Controls
Use the UP arrow or the 'w' key to move the ship forward.\
Use the LEFT and RIGHT arrow keys or the 'a' and 'd' to rotate the ship.\
Left click or press 'e' or '/' to shoot in the direction the ship is facing.

#### Visuals
Particles will appear and fade into black as the player moves and dies.\
Once an asteroid is hit, it splits into two, and a 'ghost' forms in place, which slowly fades from yellow to black.

The asteroids themselves are polygons which have an odd number of sides.\
The more sides they have, the larger they will be.

The asteroids rotate in a random direction as they move, hence the name of this repository.

#### Mechanics
Asteroids and the ship cannot leave the map.\
Every time they get hit, they will explode into several children asteroids, until the parent asteroid only has 3 sides, to which it will disappear.

When you first enter the game, there are 2 game modes to choose from:
- Campaign (Selection of levels increasing in difficulty)
- Endless (Levels get progressively harder with no breaks)

There are 50 levels, but as it gets to the end, they are pretty much impossible.\
There are 2 ways the asteroids can split:
- Binary split (they split into 2)
- Linear split

For the latter, the first split will be in half, then each of the children will split in three, then in four etc.\
When the parent is split, the vectors of the children will be evenly distributed in a circle.

# To-do
- A scoring system
- Expand from minimalist design
- Bonus levels
- Obstacles
- Powerups/Different projectiles
- More accurate ship/asteroid collision detection
- Highscore
- Level medals

# Requirements
I am using the [Python 3.7](https://www.python.org/downloads/release/python-370/) IDLE.\
Python 3.6 and Pygame 1.7.x or above is required.\
You can download pygame either [here](https://www.pygame.org/download.shtml), [here](https://bitbucket.org/pygame/pygame/downloads/) or [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame).
