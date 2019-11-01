import math
import numpy as np
import matplotlib.pyplot as plt

class Kalman_filter(object):
    def __init__(self):
        pass








if __name__ == "__main__":
    N = 200
    R = [0.36]

    T_mearsured = 25 + math.sqrt(R[0]) * np.random.randn(N)

    Sensor_mearsured = []
    for i in range(0, N):
        Sensor_mearsured.append(np.matrix([T_mearsured[i]]).T)

    Q = 1e-3

    T = 22.5
    P = 2

    F = [1] #状态转移矩阵
    H = [1] #观测矩阵

    out = []

    F_matrix = np.matrix(F)
    H_matrix = np.matrix(H)
    R_matrix = np.matrix(R)

    X_posterior_estimate = np.matrix(T).T
    P_posterior_estimate = np.matrix(P).T

    real = []
    for i in range(1, N):
        real.append(25)

    for i in range(1, N):
        X_prior_estimate = F_matrix * X_posterior_estimate # 暂时不考虑控制变量
        P_prior_estimate = F_matrix * P_posterior_estimate * F_matrix.T + np.matrix(Q)
        K_t = P_prior_estimate * H_matrix.T * (H_matrix * P_prior_estimate * H_matrix.T + R_matrix).I
        X_posterior_estimate = X_prior_estimate + K_t * (Sensor_mearsured[i] - H_matrix * X_prior_estimate)
        P_posterior_estimate = (np.identity(H_matrix.shape[0]) - K_t * H_matrix) * P_prior_estimate
        out.append(X_posterior_estimate.tolist()[0][0])

    plt.figure()    # 定义一个图像窗口
    plt.plot(range(1, N), real, color="blue", linewidth=0.5, linestyle="--", label="实际曲线") # 绘制实际曲线
    plt.plot(range(1, N), out, color="red", linewidth=1.0, linestyle="-", label="预测曲线") # 绘制预测曲线
    plt.plot(range(0, N), T_mearsured, color="#800080", linewidth=0.5, linestyle="-", label="测量") # 绘制测量曲线
    plt.show()
