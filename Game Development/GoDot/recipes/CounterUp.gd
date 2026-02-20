extends CanvasLayer


@onready var timer: Timer = $Timer

@onready var label = %Label

func _process(_delta: float) -> void:
	var time_elapsed = get_time_elasped()
	
	label.text = _format_seconds_to_str(time_elapsed)
	
func _format_seconds_to_str(time: float) -> String:
	var minutes: int = int(time / 60)
	var seconds: int = int(time) % 60
	return "%02d:%02d" % [minutes, seconds]


func get_time_elasped() -> float:
	return timer.wait_time - timer.time_left

