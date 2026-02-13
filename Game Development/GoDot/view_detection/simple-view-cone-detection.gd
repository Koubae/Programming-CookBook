extends Node2D

@export var angle: float 
@export var length: float
@export var direction: Vector2 = Vector2.UP

@onready var box = $ColorRect
@onready var rayCast = $RayCast2D

var half_angle_rads 
var target: CharacterBody2D

# credit: https://www.youtube.com/watch?v=SS9nAEpjS4o
func _ready() -> void:
	# TODO: Improve this
	var parent: Node2D = get_parent()
	var sprite: Sprite2D = parent.get_node("Sprite2D")

	var spriteRotationDeg = sprite.get_rotation()
	rotate(spriteRotationDeg)
	# ---------------
	
	# TODO: use mask
	target = get_tree().get_first_node_in_group("player")
	# 
	
	half_angle_rads = deg_to_rad((angle / 2))

func _physics_process(_delta: float) -> void:
	
	if is_in_view() and has_line_of_sight():
		box.color = Color.RED
	else:
		box.color = Color.WHITE
	

func _draw() -> void:
	var left_dir = direction.rotated(-half_angle_rads) * length
	var right_dir = direction.rotated(half_angle_rads) * length
	
	draw_line(Vector2.ZERO, left_dir, Color.YELLOW, 2.0)
	draw_line(Vector2.ZERO, right_dir, Color.YELLOW, 2.0)


func is_in_view() -> bool:
	var target_local_position = to_local(target.global_position)
	var angle_to_target = direction.angle_to(target_local_position)
	
	var distance = target_local_position.length()
	if distance > length:
		return false
	
	return abs(angle_to_target) <= half_angle_rads
	
func has_line_of_sight() -> bool: 
	rayCast.target_position = to_local(target.global_position)
	var collider = rayCast.get_collider()
	if not collider: 
		return false 
	
	var a = collider.is_in_group("player")
	return a
	