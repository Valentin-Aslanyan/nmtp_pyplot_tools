

Various simple tools for pyplot

Requires numpy and matplotlib


plot_curly_bracket

Create an arbitrarily sized curly bracket/brace, i.e. } as a line plot in matplotlib / pyplot

	Arguments:

	- direction: should be a string, "up", "down", "left", "right"
			direction in which the bracket "points", e.g. left == {, right == }

	- x_boundaries: must be a tuple or length 2+ list etc; plot coordinates for the two horizontal edges of the brace

	- y_boundaries: same as x_boundaries, but for vertical

	- aspect_ratio: for the round parts of the braces, vertical/horizontal ratio of circle size
			e.g. aspect_ratio=2 would make the round parts pieces of an ellipse 2x as wide horizontally (in plot coordinates)

	- linewidth: pyplot line plot line width

	- color: pyplot line plot line color


plot_chamfered_rectangle
	  ____
	 /    \
	/      \
	|      |
	|      |
	\      /
	 \____/

	Arguments:

	- center: must be a tuple or length 2+ list etc; plot coordinates for the center of the rectangle

	- widths: must be a tuple or length 2+ list etc; width of rectangle in plot coordinates

	- chamfer_size: width of chamfer

	- chamfer_aspect_ratio: (height of chamfer)/(width of chamfer)

	- linewidth: pyplot line plot line width

	- color: pyplot line plot line color
