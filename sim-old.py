G = 6.6743 * (10**(-11))
r = 6000000
rho = 5000
S = 1
L = 1
R = rho * S * L
M = 5.972 * (10**24)
m = 50
n = 10000
tick = 1
max_v = 100000
min_v = 0
tolerance = 0.1

def sim(v) :
    ys = [0]
    F = 0
    a = 0
    time = 0
    for k in range(n) :
        #力計算
        if r - ys[-1] != 0 :
            if ys[-1] < r or ys[-1] == r :
                g = (G*m*M)/((r - ys[-1])**2)
            elif r < ys[-1] :
                g = -(G*m*M)/((r - ys[-1])**2)
            else :
                raise ValueError()
        elif r - ys[-1] == 0 :
            g = 0
        F = g - R
        #加速度計算
        a = F/m
        #速度計算
        v += a * tick
        #物理演算
        ys.append(ys[-1] + v)
        time += tick
        #裏側判定
        if 2 * r < ys[-1] or 2 * r == ys[-1] :
            break
        elif ys[-1] < 0 :
            time = -1
            break
        print(ys[-1],v)
    return time

print(sim(23253.7))
# max 660869
print((G*m*M)/((r - 6003100.910601397)**2))