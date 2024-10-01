Unreal Engine Docs
==================


* [Gpu crash/d3d device removed error?](https://forums.unrealengine.com/t/gpu-crash-d3d-device-removed-error/514360/7)


### Docs

* [Class Creation Basics (LightSwitch with Blueprint, Class or a mix)](https://dev.epicgames.com/documentation/en-us/unreal-engine/class-creation-basics-in-unreal-engine)
* [Construction Script](https://dev.epicgames.com/documentation/en-us/unreal-engine/construction-script-in-unreal-engine)


### Tutorial
https://www.youtube.com/watch?v=KQgOqyYoHAs
* [Beginners Intro to UE5 - Create a Game in 3 Hours in Unreal Engine 5](https://dev.epicgames.com/community/learning/tutorials/OR8/beginners-intro-to-ue5-create-a-game-in-3-hours-in-unreal-engine-5)
	* [(video) - Beginners Intro to UE5 - Create a Game in 3 Hours in Unreal Engine 5]()
* [Unreal Engine 5 Beginner Tutorial - UE5 Starter Course!](https://www.youtube.com/watch?v=gQmiqmxJMtA)

* [Converting Blueprint to C++](https://dev.epicgames.com/community/learning/courses/KJ/unreal-engine-converting-blueprint-to-c/kjB/unreal-engine-introduction-to-blueprint-vs-c)
* [Balancing Blueprint and C++ in Game Development](https://dev.epicgames.com/community/learning/courses/bY/balancing-blueprint-and-c-in-game-development/LdK/introduction-to-the-course)
* [Blueprints vs. C++: How They Fit Together and Why You Should Use Both](https://www.youtube.com/watch?v=VMZftEVDuCE)




#### Cool Websise (benui)

* [uproperty](https://benui.ca/unreal/uproperty/)


### Visual Studio

* [ReSharper C++](https://www.jetbrains.com/resharper-cpp/)
* [Develop games faster & easier in Visual Studio C++](https://www.wholetomato.com/visual-assist-ue4-unreal-engine)
* [Cannot open source file name.generated.hc](https://forums.unrealengine.com/t/cannot-open-source-file-name-generated-hc/413312/2?u=koubae)


```bash
You need to do a little more than just regenerating VS project files. Close both the Unreal Editor and Visual Studio. Open your project directory and delete all these folders - .vs, Binaries, Intermediate, Saved [optional], and also YourGame.sln files. Make sure that the Config folder is there and that you do NOT accidentally delete it!

Next, right click on the YourGame.urpoject and select Generate Visual Studio project files. Open the .uproject file once it finishes regenerating. The Editor will prompt you with a missing .dll module again and will ask you to rebuild the solution. Click Yes and it will start rebuilding. It should now successfully compile if there are no bugs in your code.

Hope this helps :slight_smile:
```

### Youtube

* [How to Use C++ in Unreal Engine 5 - Beginner Tutorial](https://www.youtube.com/watch?v=HNfpKFER2hI)
* [Roll a Ball | Unreal Engine 5 Tutorial | With & Without Physics](https://www.youtube.com/watch?v=J_i6GZbtmwU)
* [Roll a Ball | Unreal Engine 5 Tutorial | Sound Effects](https://www.youtube.com/watch?v=7GEKdBjLwrQ)
* [Move the Ball - 02 - Roll A Ball in Unreal](https://www.youtube.com/watch?v=FbVkWXyqj08)
* [Unreal Engine 5 UE5 Free Tutorial - How To Change Colors Of Materials In Real Time](https://www.youtube.com/watch?v=kJBZDX-sT3o)
* [Unreal Engine 4 Tutorial - Lightswitch Actor](https://www.youtube.com/watch?v=THMd4HaHnZM)
* Cool -> [UE4 Emissive lighting and materials tutorial - unreal engine for beginners](https://www.youtube.com/watch?v=eVPuvCAEz4Q&t=70s)
* [Unreal Engine 4 C++ Tutorial: Rotate Angle Axis Specify Vector](https://www.youtube.com/watch?v=eicFMa3kis4)
* [How To Use The New Enhanced Input Action Mappings In Unreal Engine 5.1 (Tutorial)](https://www.youtube.com/watch?v=nXJuXUxQfa8)

* [Create and modify shapes in Unreal engine 5](https://www.youtube.com/watch?v=6NV7rqdtTTY)

#### Character 

* [Unreal Engine C++ Tutorial Character Movement 2022 (Beginner Friendly)](https://www.youtube.com/watch?v=xZjZimU31wc)
* [[Unreal Engine] Do you need it? Intro to Series | Character Movement Component In-Depth ](https://www.youtube.com/watch?v=urkLwpnAjO0&list=PLXJlkahwiwPmeABEhjwIALvxRSZkzoQpk&index=1)
* [HOW TO SPRINT | Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=EG9iYYraDgw)
* [[UE4 C++ Basics] Character Sprinting (Ep. 1)](https://www.youtube.com/watch?v=yyelCzlIWsM)
* [Spawning Actors with C++ - Unreal C++ Course #7](https://www.youtube.com/watch?v=gVjxtZrvbl4)

### Forum / Questions

* [Trying to follow CPP and CPP/BP Examples](https://forums.unrealengine.com/t/trying-to-follow-cpp-and-cpp-bp-examples/1543420)
* [What does “class” in class UPointLightComponent* PointLight1; mean?](https://forums.unrealengine.com/t/what-does-class-in-class-upointlightcomponent-pointlight1-mean/323406)
* [Faster compile times?](https://forums.unrealengine.com/t/faster-compile-times/148765/3)
* [ WUT? Axis and Action mappings are now deprecated, please use Enhanced Input Acitons and Input Mappi](https://forums.unrealengine.com/t/wut-axis-and-action-mappings-are-now-deprecated-please-use-enhanced-input-acitons-and-input-mapping-contexts-instead/776849)


### Game Design

* [Warren Winters -- Youtube](https://www.youtube.com/@WarrenWintersUI)


```cs
PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
PrivatePCHHeaderFile = "MaulProtoPrecompiled.h";  // This is yout main game Header
MinFilesUsingPrecompiledHeaderOverride = 1;
bUseUnity = false;
```
* [How to rotate children on their own pivot point when I rotate parent?](https://forums.unrealengine.com/t/how-to-rotate-children-on-their-own-pivot-point-when-i-rotate-parent/713963/5)

Code 
----

```c++
// Debug message https://forums.unrealengine.com/t/print-to-screen-using-c/357351/11
#include "Engine/GameEngine.h"

	// #if UE_BUILD_DEBUG (shouldn't add this directive.. is already there!)
	if (GEngine)
		GEngine->AddOnScreenDebugMessage(-1, 15.0f, FColor::Yellow, FString::Printf(TEXT("World delta for current frame equals %f | DeltaTime=%f"), GetWorld()->TimeSeconds, DeltaTime));
	// #endif



```

### Keyboard Shortcuts

* Shift + Move Object: Camera locks on object and moves together
* CTRL while spawning object: Will create objects multiple
* CTRL + Left Click on object: Select multiple objects
* e + d: Snap Actor to floor
* CTRL + l: Control Sun direction (Directional Light)
* CTRL + i: Edit Asset 


### Editor Setup

1. Turn off Realtime
2. Settings -> Dynamic Global Illumination: Lumnen -> None
3. Settings -> Reflection Method: Lumnen -> None
4. Settings -> Shadow Map Method: Virtual Shadow Maps -> Shadow Maps
5. Editor Preferences -> Asset Editor Open Location -> Main Window
6. Editor Preferences -> SOurce Code Editor: [Choose Editor .. VIsual Studio | Rider]