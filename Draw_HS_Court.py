import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc

def draw_HS_court(color="black", lw=1, zorder=0):
    fig=plt.figure(figsize=(8.4,5.0))
#     ax=fig.add_subplot(1,1,1)
    ax = plt.gca()
        
    # Creates the out of bounds lines around the court
    outer = Rectangle((-42,-25), width=84, height=50, color=color,
                      zorder=zorder, fill=False, lw=lw)
    
    # Creates the center circles and center line
    center_circle = Circle((0, 0), radius=6, lw=lw, fill=False,
                           color=color, zorder=zorder)

    # Center line
    plt.plot([0,0],[25,-25], color=color, zorder=zorder, lw=lw)
    
    # The four dash lines near the middle of the court (Idk what they are called)
    plt.plot([-14,-14],[-22,-25], color=color, zorder=zorder, lw=lw)
    plt.plot([14,14],[-22,-25], color=color, zorder=zorder, lw=lw)
    plt.plot([-14,-14],[22,25], color=color, zorder=zorder, lw=lw)
    plt.plot([14,14],[22,25], color=color, zorder=zorder, lw=lw)
    
     # Left and right paint areas
    l_box = Rectangle((-42, -6), 19, 12, lw=lw, fill=False,
                            color=color, zorder=zorder)
    r_box = Rectangle((23, -6), 19, 12, lw=lw, fill=False,
                            color=color, zorder=zorder)
    
    # Left and right free throw circles
    l_free_throw_fill = Arc((-23,0), 12, 12, theta1=270, theta2=90, lw=lw, fill=False,
                          color=color, zorder=zorder)
    r_free_throw_fill = Arc((23,0), 12, 12, theta1=90, theta2=270, lw=lw, fill=False,
                          color=color, zorder=zorder)
    l_free_throw_dash = Arc((-23,0), 12, 12, theta1=90, theta2=270, lw=lw, fill=False, color=color,
                            zorder=zorder, linestyle='dashed')
    r_free_throw_dash = Arc((23,0), 12, 12, theta1=270, theta2=90, lw=lw, fill=False, color=color,
                            zorder=zorder, linestyle='dashed')
    
    # Backboard
    plt.plot([-38,-38],[3,-3], color=color, zorder=zorder, lw=1)
    plt.plot([38,38],[-3,3], color=color, zorder=zorder, lw=1)
    
    # Hoop
    l_hoop = Circle((-36.75,0), radius=0.75, lw=1, fill=False, 
                    color=color, zorder=zorder)
    r_hoop = Circle((36.75,0), radius=0.75, lw=1, fill=False,
                    color=color, zorder=zorder)
    
    # Straight part of corner 3pt lines (4 total)
    plt.plot([-42,-36.75],[-19.75,-19.75], color=color, zorder=zorder, lw=lw)
    plt.plot([-42,-36.75],[19.80,19.80], color=color, zorder=zorder, lw=lw)
    plt.plot([42,36.75],[-19.75,-19.75], color=color, zorder=zorder, lw=lw)
    plt.plot([42,36.75],[19.80,19.80], color=color, zorder=zorder, lw=lw)
    
    # 3pt Arc
    l_arc = Arc((-36.75,0), 39.5, 39.5, theta1=270, theta2=90, lw=lw,
                color=color, zorder=zorder)
    r_arc = Arc((36.75,0), 39.5, 39.5, theta1=90,theta2=270, lw=lw,
                color=color, zorder=zorder)
    
    # Extra Lines
    top_left_rect = Rectangle((-35,6), 1, 0.7, lw=lw, fill=True, color=color, zorder=zorder)
    bottom_left_rect = Rectangle((-35,-6.7), 1, 0.7, lw=lw, fill=True, color=color, zorder=zorder)
    top_right_rect = Rectangle((34,6), 1, 0.7, lw=lw, fill=True, color=color, zorder=zorder)
    bottom_right_rect = Rectangle((34,-6.7), 1, 0.7, lw=lw, fill=True, color=color, zorder=zorder)
    plt.plot([-31,-31],[6,6.7], color=color, zorder=zorder, lw=lw)
    plt.plot([31,31],[6,6.7], color=color, zorder=zorder, lw=lw)
    plt.plot([-31,-31],[-6,-6.7], color=color, zorder=zorder, lw=lw)
    plt.plot([31,31],[-6,-6.7], color=color, zorder=zorder, lw=lw)
    plt.plot([-28,-28],[6,6.7], color=color, zorder=zorder, lw=lw)
    plt.plot([28,28],[6,6.7], color=color, zorder=zorder, lw=lw)
    plt.plot([-28,-28],[-6,-6.7], color=color, zorder=zorder, lw=lw)
    plt.plot([28,28],[-6,-6.7], color=color, zorder=zorder, lw=lw)
    plt.plot([-25,-25],[6,6.7], color=color, zorder=zorder, lw=lw)
    plt.plot([25,25],[6,6.7], color=color, zorder=zorder, lw=lw)
    plt.plot([-25,-25],[-6,-6.7], color=color, zorder=zorder, lw=lw)
    plt.plot([25,25],[-6,-6.7], color=color, zorder=zorder, lw=lw)
    
    court_elements = [outer, center_circle, l_box, r_box, l_free_throw_fill, r_free_throw_fill, l_free_throw_dash, r_free_throw_dash, l_hoop, r_hoop, l_arc, r_arc, top_left_rect, bottom_left_rect, top_right_rect, bottom_right_rect]

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    plt.axis('off')
    plt.xlim([-43,43])
    plt.ylim([-26,26])
    plt.tight_layout()
    return fig, ax

if __name__ == "__main__":
    draw_HS_court()
    plt.show()