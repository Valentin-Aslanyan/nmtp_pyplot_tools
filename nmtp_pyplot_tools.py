
def plot_curly_bracket(direction,x_boundaries,y_boundaries,aspect_ratio=1.0,linewidth=2,color="black"):
	"""
	Create an arbitrarily sized curly bracket/brace, i.e. } as a line plot in matplotlib / pyplot

	Written by Valentin Aslanyan

	Requires numpy and matplotlib

	Arguments:

	- direction: should be a string, "up", "down", "left", "right"
			direction in which the bracket "points", e.g. left == {, right == }

	- x_boundaries: must be a tuple or length 2+ list etc; plot coordinates for the two horizontal edges of the brace

	- y_boundaries: same as x_boundaries, but for vertical

	- aspect_ratio: for the round parts of the braces, vertical/horizontal ratio of circle size
			e.g. aspect_ratio=2 would make the round parts pieces of an ellipse 2x as wide horizontally (in plot coordinates)

	- linewidth: pyplot line plot line width

	- color: pyplot line plot line color
	"""
	from numpy import linspace, sin, cos, concatenate, pi
	import matplotlib.pyplot as plt
	if type(direction)!=str:
		print("Type argument must be string")
		return
	direction=direction.lower()
	if direction!="up" and direction!="down" and direction!="left" and direction!="right":
		print("Direction must be one of: up, down, left, right")
		return
	if x_boundaries[0]<x_boundaries[1]:
		left_bdry=x_boundaries[0]
		right_bdry=x_boundaries[1]
	else:
		left_bdry=x_boundaries[1]
		right_bdry=x_boundaries[0]
	if y_boundaries[0]<y_boundaries[1]:
		bottom_bdry=y_boundaries[0]
		top_bdry=y_boundaries[1]
	else:
		bottom_bdry=y_boundaries[1]
		top_bdry=y_boundaries[0]
	if direction=="up":
		radius_y=(top_bdry-bottom_bdry)*0.5
		radius_x=radius_y/aspect_ratio
		straight_length=(right_bdry-left_bdry-radius_x*4.0)*0.5
		theta=linspace(0.0*pi,0.5*pi,num=50)
		r_sin_th=radius_y*sin(theta)
		r_cos_th=radius_x*cos(theta)
		x_path=concatenate((-r_cos_th+radius_x+left_bdry, [left_bdry+radius_x,left_bdry+radius_x+straight_length], r_cos_th[::-1]+radius_x+straight_length+left_bdry, -r_cos_th+3.0*radius_x+straight_length+left_bdry, [right_bdry-radius_x-straight_length,right_bdry-radius_x], r_cos_th[::-1]-radius_x+right_bdry))
		y_path=concatenate((r_sin_th+bottom_bdry, [bottom_bdry+radius_y,bottom_bdry+radius_y], -r_sin_th[::-1]+top_bdry, -r_sin_th+top_bdry,[bottom_bdry+radius_y,bottom_bdry+radius_y], r_sin_th[::-1]+bottom_bdry))
		plt.plot(x_path,y_path,linewidth=linewidth,color=color)
	if direction=="down":
		radius_y=(top_bdry-bottom_bdry)*0.5
		radius_x=radius_y/aspect_ratio
		straight_length=(right_bdry-left_bdry-radius_x*4.0)*0.5
		theta=linspace(0.0*pi,0.5*pi,num=50)
		r_sin_th=radius_y*sin(theta)
		r_cos_th=radius_x*cos(theta)
		x_path=concatenate((-r_cos_th+radius_x+left_bdry, [left_bdry+radius_x,left_bdry+radius_x+straight_length], r_cos_th[::-1]+radius_x+straight_length+left_bdry, -r_cos_th+3.0*radius_x+straight_length+left_bdry, [right_bdry-radius_x-straight_length,right_bdry-radius_x], r_cos_th[::-1]-radius_x+right_bdry))
		y_path=concatenate((-r_sin_th+top_bdry, [bottom_bdry+radius_y,bottom_bdry+radius_y], r_sin_th[::-1]+bottom_bdry, r_sin_th+bottom_bdry, [bottom_bdry+radius_y,bottom_bdry+radius_y], -r_sin_th[::-1]+top_bdry))
		plt.plot(x_path,y_path,linewidth=linewidth,color=color)
	if direction=="left":
		radius_x=(right_bdry-left_bdry)*0.5
		radius_y=radius_x*aspect_ratio
		straight_length=(top_bdry-bottom_bdry-radius_y*4.0)*0.5
		theta=linspace(0.0*pi,0.5*pi,num=50)
		r_sin_th=radius_y*sin(theta)
		r_cos_th=radius_x*cos(theta)
		x_path=concatenate((-r_cos_th[::-1]+right_bdry, [left_bdry+radius_x,left_bdry+radius_x], r_cos_th+left_bdry, r_cos_th[::-1]+left_bdry, [left_bdry+radius_x,left_bdry+radius_x], -r_cos_th+right_bdry))
		y_path=concatenate((-r_sin_th[::-1]+radius_y+bottom_bdry, [bottom_bdry+radius_y,bottom_bdry+radius_y+straight_length], r_sin_th+radius_y+straight_length+bottom_bdry, -r_sin_th[::-1]+3.0*radius_y+straight_length+bottom_bdry, [top_bdry-radius_y-straight_length,top_bdry-radius_y], r_sin_th-radius_y+top_bdry))
		plt.plot(x_path,y_path,linewidth=linewidth,color=color)
	if direction=="right":
		radius_x=(right_bdry-left_bdry)*0.5
		radius_y=radius_x*aspect_ratio
		straight_length=(top_bdry-bottom_bdry-radius_y*4.0)*0.5
		theta=linspace(0.0*pi,0.5*pi,num=50)
		r_sin_th=radius_y*sin(theta)
		r_cos_th=radius_x*cos(theta)
		x_path=concatenate((r_cos_th[::-1]+left_bdry, [left_bdry+radius_x,left_bdry+radius_x], -r_cos_th+right_bdry, -r_cos_th[::-1]+right_bdry, [left_bdry+radius_x,left_bdry+radius_x], r_cos_th+left_bdry))
		y_path=concatenate((-r_sin_th[::-1]+radius_y+bottom_bdry, [bottom_bdry+radius_y,bottom_bdry+radius_y+straight_length], r_sin_th+radius_y+straight_length+bottom_bdry, -r_sin_th[::-1]+3.0*radius_y+straight_length+bottom_bdry, [top_bdry-radius_y-straight_length,top_bdry-radius_y], r_sin_th-radius_y+top_bdry))
		plt.plot(x_path,y_path,linewidth=linewidth,color=color)
	return


def plot_chamfered_rectangle(center,widths,chamfer_size,chamfer_aspect_ratio=1.0,linewidth=2,color="black"):
	"""
	Create a rectangle with chamfered (i.e. cut) corners in matplotlib / pyplot
	Looks like this:
	  ____
	 /    \
	/      \
	|      |
	|      |
	\      /
	 \____/

	Written by Valentin Aslanyan

	Requires numpy and matplotlib

	Arguments:

	- center: must be a tuple or length 2+ list etc; plot coordinates for the center of the rectangle

	- widths: must be a tuple or length 2+ list etc; width of rectangle in plot coordinates

	- chamfer_size: width of chamfer

	- chamfer_aspect_ratio: (height of chamfer)/(width of chamfer)

	- linewidth: pyplot line plot line width

	- color: pyplot line plot line color
	"""
	import matplotlib.pyplot as plt
	if chamfer_size>widths[0]*0.5:
		print("Chamfer too large for width")
		return
	if chamfer_size>widths[1]*0.5*chamfer_aspect_ratio:
		print("Chamfer too large for height")
		return
	x_path=[center[0]-widths[0]*0.5,
	center[0]-widths[0]*0.5,
	center[0]-widths[0]*0.5+chamfer_size,
	center[0]+widths[0]*0.5-chamfer_size,
	center[0]+widths[0]*0.5,
	center[0]+widths[0]*0.5,
	center[0]+widths[0]*0.5-chamfer_size,
	center[0]-widths[0]*0.5+chamfer_size,
	center[0]-widths[0]*0.5,
	center[0]-widths[0]*0.5,
	center[0]-widths[0]*0.5]
	y_path=[center[1],
	center[1]+widths[1]*0.5-chamfer_size*chamfer_aspect_ratio,
	center[1]+widths[1]*0.5,
	center[1]+widths[1]*0.5,
	center[1]+widths[1]*0.5-chamfer_size*chamfer_aspect_ratio,
	center[1]-widths[1]*0.5+chamfer_size*chamfer_aspect_ratio,
	center[1]-widths[1]*0.5,
	center[1]-widths[1]*0.5,
	center[1]-widths[1]*0.5+chamfer_size*chamfer_aspect_ratio,
	center[1]+widths[1]*0.5-chamfer_size*chamfer_aspect_ratio,
	center[1]]
	plt.plot(x_path,y_path,linewidth=linewidth,color=color)
	return

