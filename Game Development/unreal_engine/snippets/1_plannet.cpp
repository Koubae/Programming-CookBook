// Fill out your copyright notice in the Description page of Project Settings.


#include "GalacticObject.h"

// Sets default values
AGalacticObject::AGalacticObject()
{
 	// Set this pawn to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

}

// Called when the game starts or when spawned
void AGalacticObject::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void AGalacticObject::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

	FVector Location = GetActorLocation();

	
	//AActor* parent = GetParentActor();

 	AActor* parent = GetOwner();

	//if (GEngine && gravityLock) {
	if (GEngine) {
		//AActor* gravitationalPool = GetOwner();
		//FVector LocationParent = gravityLock->GetActorLocation();
		//FVector LocationParent2 = gravityLock->GetTransform();
		//GEngine->AddOnScreenDebugMessage(-1, 1.0f, FColor::Green, FString::Printf(TEXT("Parent %s | Location %f, %f, %f"), *gravityLock->GetName(), 
		//	LocationParent.X, LocationParent.Y, LocationParent.Z));


		/*GEngine->AddOnScreenDebugMessage(-1, 1.0f, FColor::Green, FString::Printf(TEXT("%s : Parent %s"), 
			*GetName(), *parent->GetName()));*/

	}

	// -------------------------
	// Revolution movement around a center point 
	// -------------------------
	//FVector NewLocation = FVector(Location.X, Location.Y, Location.Z);

	FVector NewLocation = FVector(Location.X, Location.Y, Location.Z);

	FVector Radius = FVector(RadiusX, 0, 0);
	
	AngleAxis += RevolutionSpeed;
	if (AngleAxis > 360.f)
	{
		AngleAxis = 0.0;
	}

	FVector RotateValue = Radius.RotateAngleAxis(AngleAxis, FVector(0, 0, 1));

	NewLocation.X += RotateValue.X;
	NewLocation.Y += RotateValue.Y;
	NewLocation.Z += RotateValue.Z;

	SetActorLocation(NewLocation);

}

// Called to bind functionality to input
void AGalacticObject::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

}
