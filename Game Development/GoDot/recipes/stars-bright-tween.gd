extends Sprite2D


func _ready():
	var tween = create_tween().set_loops() # Infinite loop
	# Brighten to 2.0 (Shine) over 1 second
	tween.tween_property(self, "modulate", Color(2, 2, 2, 1), 1.0)
	# Dim back to 1.0 (Normal) over 1 second
	tween.tween_property(self, "modulate", Color("ff2e0990"), 1.0)
	
	

