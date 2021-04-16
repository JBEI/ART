import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import art.utility as utils

n_modifications = 3


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


def plot_distribution_of_designs(df): 
    bar_height = 1
    labels = ['KO', 'NoMod', 'UP']
    colors = ['#019600', 'grey', '#219AD8']
        
    plt.style.use('seaborn-white')
    
    dataframe = df.copy()
    reactions = dataframe.columns
    
    n_rec = len(dataframe)
    dataframe.loc[n_rec] = [[list(dataframe[reaction]).count(int(i))/n_rec*100 
                             for i in range(n_modifications)]  for reaction in reactions]
    
    data = [ [dataframe.iloc[-1][r][num] for r in reactions] 
            for num in range(n_modifications)]
    
    y_pos = np.arange(len(reactions))

    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(111)

    # Remove frame
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    patch_handles = []
    # left alignment of data starts at zero
    left = np.zeros(len(reactions)) 
    for i, d in enumerate(data):
        patch_handles.append(ax.barh(y_pos, d, 
                                     color=colors[i%len(colors)], edgecolor='white',
                                     height=bar_height, align='center', 
                                     left=left, label=labels[i]))
        left += d

    # search all of the bar segments and annotate
    for j in range(n_modifications):
        for i, patch in enumerate(patch_handles[j].get_children()):
            bl = patch.get_xy()
            x = 0.5*patch.get_width() + bl[0]
            y = 0.5*patch.get_height() + bl[1]
            ax.text(x,y, "%d%%" % (data[j][i]), ha='center')

    ax.set_title('Distribution of modifications')
    plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=True, 
                    labelbottom=False)
    plt.yticks(y_pos, reactions)
    ax.invert_yaxis()
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()
