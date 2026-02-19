Game Development
========


### [Javascript](./javascript)
### [Python](./python/)
### [Unity](./unity/)

* [github.com/Koubae/java-libGDX](https://github.com/Koubae/java-libGDX)


Assets
------

### Images | Pixel Art | Pictures

* [krita](https://krita.org/en/download/)
   * [How to make 2D game art! Simple assets, even if you are bad at drawing](https://www.youtube.com/watch?v=bKgi6WcXtCY)

* [kenney.nl](https://kenney.nl/)


### Music 

* [opengameart](https://opengameart.org/)

## ✅ Best Practices When Using OpenGameArt

1. **Check the license for each asset**  
   Always verify that the license allows **commercial use** and note any obligations  
   (e.g., attribution or share-alike).

2. **Record attribution details**  
   Save the following for every asset you use:  
   - Name of the asset  
   - Author/creator  
   - License type  
   - Link to the original source  
   This makes it easier to include proper credits in your game.

3. **Prefer safe licenses**  
   Use assets under **CC0**, **OGA-BY**, or **CC-BY** (with attribution)  
   for the simplest usage in both commercial and closed-source projects.

4. **Be cautious with GPL / CC-BY-SA**  
   - **ShareAlike (SA)**: requires derivatives to use the same license.  
   - **GPL**: often conflicts with closed-source or proprietary games.  
   Use only if you fully understand the implications.

5. **Bundle license info with your game**  
   Include a file or folder in your game distribution listing:  
   - All used assets  
   - Their licenses  
   - Full license texts (if required)  
   This keeps everything transparent and legally safe.


## ⚠️ Caveats & What to Watch Out For

- **License matters per asset**  
  Just because the site is “free assets” doesn’t mean every piece is CC0.  
  Each upload has its own license.

- **CC-BY / CC-BY-SA / OGA-BY require attribution**  
  - **CC-BY**: You must credit the original creator.  
  - **CC-BY-SA**: In addition to attribution, derivatives must carry the same license.  
  - **OGA-BY**: Similar to CC-BY but removes certain technical restrictions.

- **GPL-licensed assets are tricky**  
  GPL is designed for software, not art.  
  Using GPL assets in a non-GPL (closed-source) game can create licensing conflicts.

- **Technical restriction clauses**  
  Some licenses (like CC-BY) include clauses against DRM or technical limitations.  
  OGA-BY was created to avoid these issues.

- **Safe choices for commercial games**  
  Stick with **CC0**, **OGA-BY**, or **CC-BY** (with proper attribution)  
  to avoid complications.


Mathematics & Geometry
----------------------

### Difference between Eucledian distance and Displacement vector

#### Displacement Vector

A direction AND magnitude - tells you both how far AND which way.

Use it when you need to know:

* "Which direction should I face?"
* "Where should I move?"
* "What angle is the target at?"

```java
Vector2 position = Vector2(x=10, y=20);
Vector2 target = Vector2(x=25, y=30);
Vector2 displacement = Vector2(x=target.x - position.x, y=target.y - position.y);

Vector2 displacement = new Vector2(100, 50); # 100 units right, 50 units up
float angle = Math.atan2(displacement.y, displacement.x); #  Calculate direction
#  Now I know which way to rotate/aim

``` 



#### Eucledian Distance

A single number - the straight-line distance between two points.
Use it when you need to know:
* "How far away is something?"
* "Is the target within range?"
* "Am I close enough to stop moving?"

```java


float distance = 150.5f; // 150.5 units away
if (distance < 200f) {
    // Target is within shooting range
}

Vector2 position = Vector2(x=10, y=20);
Vector2 target = Vector2(x=25, y=30);
Vector2 displacement = Vector2(x=target.x - position.x, y=target.y - position.y);
float eucledianDistance = (float)Math.sqrt((displacement.x * displacement.x) + (displacement.y * displacement.y));
// Also
float distance = (float) Math.hypot(displacement.x, displacement.y);
``` 


**Practical Example - Chasing a target:**

```java
// Where is the target relative to me?
Vector2 displacement = new Vector2(
    target.x - self.x,  // +100 means target is 100 units to the right
    target.y - self.y   // -50 means target is 50 units down
);

// How far away is it?
float distance = displacement.len(); // e.g., 111.8 units eucledian

// Decision making:
if (distance > 200) {
    // Use DISPLACEMENT to know which direction to move
    float angle = Math.atan2(displacement.y, displacement.x);
    rotateTowards(angle);
    moveForward();
} else {
    // Use DISTANCE to know we're close enough
    stop();
}
``` 
