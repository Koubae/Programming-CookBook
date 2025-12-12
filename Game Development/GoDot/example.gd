extends Node2D


@export var speed: int = 500
#@export var speed := 500

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	print("Ready!!!")
	position = Vector2(500, 300)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	#move_local_x(1)
	var direction = Input.get_vector("left", "right", "up", "down")
	#print(direction)
	#move_local_x(direction[0])
	#move_local_y(direction[1])
	
	position += direction * speed * delta
	