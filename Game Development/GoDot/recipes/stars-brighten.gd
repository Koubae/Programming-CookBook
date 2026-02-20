extends Node2D

@export var min_alpha_far: float = 0.15
@export var max_alpha_far: float = 0.30
@export var min_alpha_mid: float = 0.18
@export var max_alpha_mid: float = 0.45
@export var min_alpha_near: float = 0.20
@export var max_alpha_near: float = 0.65

@export var speed_far: float = 0.35
@export var speed_mid: float = 2.55
@export var speed_near: float = 3.85

var _t: float = 0.0

var _sprites: Array[Sprite2D] = []
var _min_a: Array[float] = []
var _max_a: Array[float] = []
var _speed: Array[float] = []
var _phase: Array[float] = []

func _ready() -> void:
	randomize()
	_clear_layers()

	_add_layer("Far",    min_alpha_far,  max_alpha_far,  speed_far)
	_add_layer("Middle", min_alpha_mid,  max_alpha_mid,  speed_mid)
	_add_layer("Near",   min_alpha_near, max_alpha_near, speed_near)
	_add_layer("Near2",  min_alpha_near, max_alpha_near, speed_near * 1.1)

func _process(delta: float) -> void:
	_t += delta

	for i in range(_sprites.size()):
		var s := _sprites[i]
		if s == null:
			continue

		var v: float = sin(_t * _speed[i] + _phase[i]) * 0.5 + 0.5 # 0..1
		# smoothstep
		v = v * v * (3.0 - 2.0 * v)

		var a: float = lerp(_min_a[i], _max_a[i], v)

		var c := s.modulate
		c.a = a
		s.modulate = c

func _add_layer(node_name: String, min_a: float, max_a: float, spd: float) -> void:
	var container := get_node_or_null(node_name)
	if container == null:
		push_warning("Missing node: %s" % node_name)
		return

	var sprite: Sprite2D = null
	for child in container.get_children():
		if child is Sprite2D:
			sprite = child
			break

	if sprite == null:
		push_warning("No Sprite2D under: %s" % node_name)
		return

	_sprites.append(sprite)
	_min_a.append(min_a)
	_max_a.append(max_a)
	_speed.append(spd)
	_phase.append(randf() * TAU)

func _clear_layers() -> void:
	_sprites.clear()
	_min_a.clear()
	_max_a.clear()
	_speed.clear()
	_phase.clear()

