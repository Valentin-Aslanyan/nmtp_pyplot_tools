

#Use the following 3 lines to create a curly bracket
import matplotlib.pyplot as plt
from nmtp_pyplot_tools import plot_curly_bracket
plot_curly_bracket("left",(1.4,2.2),(2.0,8.0))

#Use the following 3 lines to create a chamfered rectangle
import matplotlib.pyplot as plt
from nmtp_pyplot_tools import plot_chamfered_rectangle
plot_chamfered_rectangle([5.4,5.6],[4.0,2.6],0.6)

#Other examples of curly brackets
plot_curly_bracket("right",(8.6,9.4),(2.0,8.0))
plot_curly_bracket("up",(2.4,8.4),(8.2,9.0))
plot_curly_bracket("down",(2.4,8.4),(1.8,1.0))

plot_curly_bracket("up",(13.0,19.0),(9.2,9.8),color="red")
plot_curly_bracket("up",(13.0,19.0),(8.2,9.0),color="orange",aspect_ratio=0.4)
plot_curly_bracket("up",(13.0,19.0),(7.2,7.9),color="black",aspect_ratio=2.0,linewidth=4)
plot_curly_bracket("up",(13.0,19.0),(7.2,7.9),color="yellow",aspect_ratio=2.0)
plot_curly_bracket("up",(15.0,17.0),(6.2,6.9),color="green",aspect_ratio=1.0)
plot_curly_bracket("up",(14.0,18.0),(5.2,5.5),color="cyan",aspect_ratio=1.0)
plot_curly_bracket("up",(14.0,18.0),(4.2,4.9),color="blue",aspect_ratio=1.0,linewidth=5)
plot_curly_bracket("down",(14.0,18.0),(3.2,3.9),color="violet",aspect_ratio=1.0,linewidth=5)

#Other examples of chamfered rectangles
plot_chamfered_rectangle([5.4,5.0],[5.2,6.0],0.8,color="red")
plot_chamfered_rectangle([5.4,3.2],[3.8,1.4],0.4,chamfer_aspect_ratio=0.6,linewidth=3,color="blue")

#Labels and supplementary calls
plt.text(0.2,4.9,"Left")
plt.text(9.6,4.9,"Right")
plt.text(4.9,9.2,"Up")
plt.text(4.6,0.6,"Down")
plt.text(12.9,2.1,"Curly brackets")
plt.text(11.7,1.5,"Various colors, thicknesses")
plt.text(13.1,0.9,"and aspect ratios")
plt.text(3.6,7.5,"Chamfered")
plt.text(3.7,7.1,"rectangles")
plt.xlim([0,20])
plt.ylim([0,10])
plt.show()
