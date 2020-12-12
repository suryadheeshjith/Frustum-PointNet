
#### TEST 1   (Clipping)

def test_clip():
    import numpy as np

    a = np.array([[10,20],[4,29],[50,0]])
    b = (a[:,0]>9) & (a[:,0]<30)
    c = a[b]

    print(a)
    print(b)
    print(c)


#### TEST 2   (Delaunay [Tesselation])

def test_delaunay():
    from scipy.spatial import Delaunay
    import numpy as np


    points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])
    tri = Delaunay(points)
    print(points[tri.simplices])
    p = np.array([(0.1, 0.2), (1.5, 0.5), (0.5, 1.05), (0.9,0.2)])
    print(tri.find_simplex(p))

    #The returned integers in the array are the indices of the simplex the
    #corresponding point is in. If -1 is returned, the point is in no simplex.


#### TEST 3   (Cool PointCloud)

def test_mayavi():
    import numpy as np
    import mayavi.mlab as mlab

    # Setup figure and Draw Points
    pc = np.loadtxt('pc_sample.txt')
    fig = mlab.figure(figure=None, bgcolor=(0,0,0), fgcolor=None, engine=None, size=(1600, 1000))
    mlab.points3d(pc[:,0], pc[:,1], pc[:,2], pc[:,2], color=None, mode='point', colormap = 'gnuplot', scale_factor=1, figure=fig)
    mlab.points3d(0, 0, 0, color=(1,1,1), mode='sphere', scale_factor=0.2)


    # Axes
    axes=np.array([
        [2.,0.,0.,0.],
        [0.,2.,0.,0.],
        [0.,0.,2.,0.],
    ],dtype=np.float64)
    mlab.plot3d([0, axes[0,0]], [0, axes[0,1]], [0, axes[0,2]], color=(1,0,0), tube_radius=None, figure=fig)
    mlab.plot3d([0, axes[1,0]], [0, axes[1,1]], [0, axes[1,2]], color=(0,1,0), tube_radius=None, figure=fig)
    mlab.plot3d([0, axes[2,0]], [0, axes[2,1]], [0, axes[2,2]], color=(0,0,1), tube_radius=None, figure=fig)

    # draw fov (todo: update to real sensor spec.)
    fov=np.array([  # 45 degree
        [20., 20., 0.,0.],
        [20.,-20., 0.,0.],
    ],dtype=np.float64)

    mlab.plot3d([0, fov[0,0]], [0, fov[0,1]], [0, fov[0,2]], color=(1,1,1), tube_radius=None, line_width=1, figure=fig)
    mlab.plot3d([0, fov[1,0]], [0, fov[1,1]], [0, fov[1,2]], color=(1,1,1), tube_radius=None, line_width=1, figure=fig)

    # draw square region
    TOP_Y_MIN=-20
    TOP_Y_MAX=20
    TOP_X_MIN=0
    TOP_X_MAX=40
    TOP_Z_MIN=-2.0
    TOP_Z_MAX=0.4

    x1 = TOP_X_MIN
    x2 = TOP_X_MAX
    y1 = TOP_Y_MIN
    y2 = TOP_Y_MAX
    mlab.plot3d([x1, x1], [y1, y2], [0,0], color=(0.5,0.5,0.5), tube_radius=0.1, line_width=1, figure=fig)
    mlab.plot3d([x2, x2], [y1, y2], [0,0], color=(0.5,0.5,0.5), tube_radius=0.1, line_width=1, figure=fig)
    mlab.plot3d([x1, x2], [y1, y1], [0,0], color=(0.5,0.5,0.5), tube_radius=0.1, line_width=1, figure=fig)
    mlab.plot3d([x1, x2], [y2, y2], [0,0], color=(0.5,0.5,0.5), tube_radius=0.1, line_width=1, figure=fig)

    # View
    mlab.view(azimuth=180, elevation=70, focalpoint=[ 12.0909996 , -1.04700089, -2.03249991], distance=62.0, figure=fig)
    mlab.show()





if __name__=="__main__":
    test_mayavi()
