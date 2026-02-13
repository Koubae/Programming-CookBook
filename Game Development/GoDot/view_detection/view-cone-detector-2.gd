extends Node2D

@export var angle: float 
@export var length: float
@export var direction: Vector2 = Vector2.UP

@onready var rayCast = $RayCast2D
@onready var collider: CollisionPolygon2D = $Area2D/CollisionPolygon2D

var half_angle_rads 
var target: CharacterBody2D

var inTarget: bool = false
var coneColor: Color = Color.YELLOW

func _ready() -> void:
	# TODO: Improve this
	var parent: Node2D = get_parent()
	var sprite: Sprite2D = parent.get_node("Sprite2D")

	var spriteRotationDeg = sprite.get_rotation()
	rotate(spriteRotationDeg)
	# ---------------
	
	# TODO: use mask
	target = get_tree().get_first_node_in_group("player")
	
	half_angle_rads = deg_to_rad((angle / 2))
	
	var left_dir = direction.rotated(-half_angle_rads) * length
	var right_dir = direction.rotated(half_angle_rads) * length
	
	# TODO: can we improve this?
	collider.polygon = [Vector2.ZERO, left_dir, right_dir]


func _physics_process(_delta: float) -> void:
	if inTarget:
		rayCast.target_position = to_local(target.global_position)
		coneColor = Color.RED
		
	else:
		coneColor = Color.GREEN
	

func _draw() -> void:
	var left_dir = direction.rotated(-half_angle_rads) * length
	var right_dir = direction.rotated(half_angle_rads) * length
	
	draw_line(Vector2.ZERO, left_dir, coneColor, 5.0)
	draw_line(Vector2.ZERO, right_dir, coneColor, 5.0)
	draw_line(left_dir, right_dir, coneColor, 5.0)

func _on_area_2d_body_entered(body: Node2D) -> void:
	inTarget = body == target
	
	queue_redraw()
	
func _on_area_2d_body_exited(body: Node2D) -> void:
	inTarget = false
	
	queue_redraw()
