import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import art.utility as utils

def plot_function(function, bounds, dimension, points=None): 
    
    
    ## Set fonts
    matplotlib.rcParams.update({'font.size': 20, 'font.family':'DejaVu Sans'})

    ## Create the grid of input variables and find corresponding responses (as per function above)
    n_points = 50
    lb, ub   = bounds[0], bounds[1]
    p1, p2   = np.linspace(lb,ub,n_points), np.linspace(lb,ub,n_points)
    P1, P2   = np.meshgrid(p1, p2)
    R        = function(np.array([P1, P2]),dimension)    
    dP1, dP2 = np.diff(p1)[1],np.diff(p2)[1]

    ## Creating fig
    fig, ax1 = plt.subplots()
    # Create colormap
    cmap = plt.get_cmap('viridis') 
    # Create levels to be plotted
    # p1 and p2 are bounds, so R should be the value *inside* those bounds. Therefore, remove the last value from the R array.
    R = R[:-1, :-1]  
    levels = matplotlib.ticker.MaxNLocator(nbins=15).tick_values(R.min(), R.max())
    # Contours are *point* based plots, so convert our bound into point centers
    cf = ax1.contourf(P1[:-1, :-1] + dP1/2.,P2[:-1, :-1] + dP2/2., R, levels=levels,cmap=cmap)
    fig.colorbar(cf, ax=ax1)
    # Labels for axes and title
    plt.ylabel("$p_1$",fontsize=20)
    plt.xlabel("$p_2$",fontsize=20)
    ax1.set_title('Isoprenol production',fontsize=20)

    # Plot points
    if points:
        x = points[0]
        y = points[1]
        scatter = ax1.scatter(x, y,c='k')

    plt.show()
    
def simulate_recommendations_responses(art,simulation_function, dim, file_name):
    P_new = art.recommendations.values[:, :-1]
    r_new = simulation_function(P_new.T, dim).reshape(-1, 1)
    P = np.concatenate((art.X, P_new))
    r = np.concatenate((art.y, r_new))
    utils.save_edd_csv(P, r, art.input_vars, file_name, response_vars_names=art.response_vars[0])
    
    return r
