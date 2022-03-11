import numpy as np

def Homography(set1, set2):
    x, y = set1.T
    xp, yp = set2.T
    A = []
    for i in range(4):
        A.append([-x[i], -y[i], -1, 0, 0, 0, x[i]*xp[i], y[i]*xp[i], xp[i]])
        A.append([0, 0, 0, -x[i], -y[i], -1, x[i]*yp[i], y[i]*yp[i], yp[i]])
    A = np.array(A)
    U, E, V = np.linalg.svd(A)
    H = V[-1, :] / V[-1, -1]
    return H.reshape((3, 3))


def warpPerspective(img, H, size):
    if len(img.shape) == 3: 
        h, w, _ = img.shape
        result = np.zeros([size[1], size[0], 3], np.uint8)
    else:
        h, w = img.shape
        result = np.zeros([size[1], size[0]], np.uint8)

    x, y = np.indices((w, h))
    
    img_coords = np.vstack((x.flatten(), 
                            y.flatten(), 
                            [1]*x.size))
    
    new_coords = H @ img_coords
    new_coords = new_coords/(new_coords[2] + 1e-6)
    new_x, new_y, _ = np.int0(np.round(new_coords))
    new_x[np.where(new_x < 0)] = 0
    new_y[np.where(new_y < 0)] = 0
    new_x[np.where(new_x > size[0] - 1)] = size[0] - 1
    new_y[np.where(new_y > size[1] - 1)] = size[1] - 1
    result[new_y, new_x] = img[y.flatten(), x.flatten()]
    return result


def projectionMatrix(H, K):  
    b_t = np.linalg.inv(K) @ H
    b1, b2, b3 = b_t.T
    #calculating lamda
    lamda = 2 / (np.linalg.norm(b1) + np.linalg.norm(b2))
    b_t = lamda * b_t

    det = np.linalg.det(b_t)

    if det < 0: b_t = -1 * b_t  
        
    r1, r2, t = b_t.T                     
    r3 = np.cross(r1, r2)
    
    Rt = np.column_stack((r1, r2, r3, t))

    return K @ Rt


