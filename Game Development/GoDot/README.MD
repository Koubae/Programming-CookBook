Godot
=====



Tutorials & Videos
------------------

* [Godot 4 Crash Course #1 - The Basics (Net Ninja)](https://www.youtube.com/watch?v=q7wlSvt0JIc&list=PL4cUxeGkcC9iHCXBpxbdsOByZ55Ez4bgF&index=1)
* [The ultimate introduction to Godot 4 (Clear Code)](https://www.youtube.com/watch?v=nAh_Kx5Zh5Q&t=5180s)

* [How to program in Godot - GDScript Tutorial](https://www.youtube.com/watch?v=e1zJS31tr88)
* [Best practices](https://docs.godotengine.org/en/stable/tutorials/best_practices/index.html)
* [GDScript style guide](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html)

* [SceneTree](https://docs.godotengine.org/en/stable/classes/class_scenetree.html#class-scenetree-method-change-scene)
* [Change scenes manually](https://docs.godotengine.org/en/latest/tutorials/scripting/change_scenes_manually.html)

* [Remaking Super Mario World in Godot (Playlist)](https://www.youtube.com/playlist?list=PLKCF1pHYsbiHNKGBoHrIM2l19tlN5GdVK)
* [How To Make a Space Shooter in 20 Minutes (Godot Engine)](https://www.youtube.com/watch?v=qd0UTOQ_la8)
* [How to Create PROCEDURAL Generation in Godot 4](https://www.youtube.com/watch?v=oB1xsCcO9wI)
* [Godot 2D — Light in the Darkness (Tutorial)](https://www.youtube.com/watch?v=PpMqg-GMInU)
* [How to Create PROCEDURAL Generation in Godot 4](https://www.youtube.com/watch?v=oB1xsCcO9wI)
* [How to add parallax scrolling to your 2D game in Godot 4 | step by step](https://www.youtube.com/watch?v=25qtnUolLc4&t=222s)

Tips tricks & memos
--------------------


* Area2D: An area that can check if another body entered | moved by changing position -> check if player enters an area... etc
* StaticBody2D: Static body, other body can colide with  | Shouldn't move -> walls, beds, obstacles
* RigidBody2D: Moving bodies via Physics                 | Set an initial velocity -> A granade, bullet, etc...
* CharacterBody2D: Moving body controlled by code        | built ins methodss -> entities

### Collisions layers

* Debug --> Visible Collision Shapes

##### Type 1 | Generic

1.	WorldStatic	            Walls, ground, level geometry
2.	WorldDynamic	        Moving platforms, doors
3.	Player	                Player body
4.	Enemies	                Enemy bodies
5.	PlayerHitbox	        Player attacks
6.	EnemyHitbox	            Enemy attacks
7.	PlayerHurtbox	        Player damage receiver
8.	EnemyHurtbox	        Enemy damage receiver
9.	Projectiles	            Bullets, missiles
10.	Pickups	                Coins, items
11.	Triggers	            Areas, sensors
12.	UIBlocking	            Rare, but useful

##### Type 2 | FPS 2D

1. WorldStatic
2. WorldDynamic
3. Player
4. Enemy
5. Projectile
5. Pickup
6. Trigger

--

Or we can leave "padding" space between so that in case we need to add in between in the future:

1. World            | (1, 2, 3, 4)
5. Player           | (5, 6, 7, 8)
9. Enemy            | (9, 10, 11, 12)
13. Projectile      | (13, 14, 15, 16)
17. Pickup
18. Trigger


Shortcuts (Editor)
------------------

* CTRL+A: Add Node
* CTRL+Shift+O: Open Scene



Terms & Keywords
----------------

* Scene
* Node
* Area2D, StaticBody2D, RigidBody2D, CharacterBody2D
* Signal

* Layer
* Mask


Forum | QA | Further Reading
----------------------------

* [How does change_scene_to_file() method exactly work?](https://forum.godotengine.org/t/how-does-change-scene-to-file-method-exactly-work/74909)

