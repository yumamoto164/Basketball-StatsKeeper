import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc

def draw_NBA_court(color="black", lw=1, zorder=0):
    fig=plt.figure(figsize=(9.4,6.0))
#     ax=fig.add_subplot(1,1,1)
    ax = plt.gca()
        
    # Creates the out of bounds lines around the court
    outer = Rectangle((-47,-25), width=94, height=50, color=color,
                      zorder=zorder, fill=False, lw=lw)
    
    # Creates the center circles and center line
    center_circle = Circle((0, 0), radius=6, lw=lw, fill=False,
                           color=color, zorder=zorder)

    # Center line
    plt.plot([0,0],[25,-25], color=color, zorder=zorder, lw=lw)
    
    # The four dash lines near the middle of the court (Idk what they are called)
    plt.plot([-19,-19],[-22,-25], color=color, zorder=zorder, lw=lw)
    plt.plot([19,19],[-22,-25], color=color, zorder=zorder, lw=lw)
    plt.plot([-19,-19],[22,25], color=color, zorder=zorder, lw=lw)
    plt.plot([19,19],[22,25], color=color, zorder=zorder, lw=lw)
    
     # Left and right paint areas
    l_outer_box = Rectangle((-47, -8), 19, 16, lw=lw, fill=False,
                            color=color, zorder=zorder)    
    l_inner_box = Rectangle((-47, -6), 19, 12, lw=lw, fill=False,
                            color=color, zorder=zorder)
    r_outer_box = Rectangle((28, -8), 19, 16, lw=lw, fill=False,
                            color=color, zorder=zorder)

    r_inner_box = Rectangle((28, -6), 19, 12, lw=lw, fill=False,
                            color=color, zorder=zorder)
    
    # Left and right free throw circles
    l_free_throw_fill = Arc((-28,0), 12, 12, theta1=270, theta2=90, lw=lw, fill=False,
                          color=color, zorder=zorder)
    r_free_throw_fill = Arc((28,0), 12, 12, theta1=90, theta2=270, lw=lw, fill=False,
                          color=color, zorder=zorder)
    l_free_throw_dash = Arc((-28,0), 12, 12, theta1=90, theta2=270, lw=lw, fill=False, color=color,
                            zorder=zorder, linestyle='dashed')
    r_free_throw_dash = Arc((28,0), 12, 12, theta1=270, theta2=90, lw=lw, fill=False, color=color,
                            zorder=zorder, linestyle='dashed')
    
    # Restricted Areas
    l_restricted_arc = Arc((-41.75,0), 8, 8, theta1=260, theta2=100, lw=lw, fill=False, color=color, zorder=zorder)
    r_restricted_arc = Arc((41.75,0), 8, 8, theta1=80, theta2=280, lw=lw, fill=False, color=color, zorder=zorder)
    
    # Backboard
    plt.plot([-43,-43],[3,-3], color=color, zorder=zorder, lw=1)
    plt.plot([43,43],[-3,3], color=color, zorder=zorder, lw=1)
    
    # Hoop
    l_hoop = Circle((-41.75,0), radius=0.75, lw=1, fill=False, 
                    color=color, zorder=zorder)
    r_hoop = Circle((41.75,0), radius=0.75, lw=1, fill=False,
                    color=color, zorder=zorder)
    
    # Straight part of corner 3pt lines (4 total)
    plt.plot([-47,-32.802],[-22,-22], color=color, zorder=zorder, lw=lw)
    plt.plot([-47,-32.802],[22,22], color=color, zorder=zorder, lw=lw)
    plt.plot([47,32.802],[-22,-22], color=color, zorder=zorder, lw=lw)
    plt.plot([47,32.802],[22,22], color=color, zorder=zorder, lw=lw)
    
    # 3pt Arc
    l_arc = Arc((-41.75,0), 47.5, 47.5, theta1=292, theta2=68, lw=lw,
                color=color, zorder=zorder)
    r_arc = Arc((41.75,0), 47.5, 47.5, theta1=112, theta2=248, lw=lw,
                color=color, zorder=zorder)
    
    # Extra Lines
    plt.plot([-47,-46],[11,11], color=color, zorder=zorder, lw=lw)
    plt.plot([-47,-46],[-11,-11], color=color, zorder=zorder, lw=lw)
    plt.plot([47,46],[11,11], color=color, zorder=zorder, lw=lw)
    plt.plot([47,46],[-11,-11], color=color, zorder=zorder, lw=lw)
    plt.plot([-40,-40],[8,9], color=color, zorder=zorder, lw=lw)
    plt.plot([-40,-40],[-8,-9], color=color, zorder=zorder, lw=lw)
    plt.plot([-39,-39],[8,9], color=color, zorder=zorder, lw=lw)
    plt.plot([-39,-39],[-8,-9], color=color, zorder=zorder, lw=lw)
    plt.plot([-36,-36],[8,9], color=color, zorder=zorder, lw=lw)
    plt.plot([-36,-36],[-8,-9], color=color, zorder=zorder, lw=lw)
    plt.plot([-33,-33],[8,9], color=color, zorder=zorder, lw=lw)
    plt.plot([-33,-33],[-8,-9], color=color, zorder=zorder, lw=lw)
    plt.plot([40,40],[8,9], color=color, zorder=zorder, lw=lw)
    plt.plot([40,40],[-8,-9], color=color, zorder=zorder, lw=lw)
    plt.plot([39,39],[8,9], color=color, zorder=zorder, lw=lw)
    plt.plot([39,39],[-8,-9], color=color, zorder=zorder, lw=lw)
    plt.plot([36,36],[8,9], color=color, zorder=zorder, lw=lw)
    plt.plot([36,36],[-8,-9], color=color, zorder=zorder, lw=lw)
    plt.plot([33,33],[8,9], color=color, zorder=zorder, lw=lw)
    plt.plot([33,33],[-8,-9], color=color, zorder=zorder, lw=lw)
    
    court_elements = [outer, center_circle, l_outer_box, r_outer_box, l_inner_box, 
                      r_inner_box, l_free_throw_fill, r_free_throw_fill, l_free_throw_dash, r_free_throw_dash,
                      l_hoop, r_hoop, l_arc, r_arc, l_restricted_arc, r_restricted_arc]

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    plt.axis('off')
    plt.xlim([-48,48])
    plt.ylim([-26,26])
    plt.tight_layout()
    return fig, ax

if __name__ == "__main__":
    draw_NBA_court()
    # plt.xlim(-48, 48)
    # plt.ylim(-26,26)
#     plt.savefig('2DBasketballCourt.jpg', bbox_inches = 'tight')
    plt.show()