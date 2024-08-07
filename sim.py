filename = "simlog.txt"
with open(filename, 'w') as f:
    print("", file=f)
def write(*contents) :
    with open(filename, 'a') as f:
        print(contents, file=f)

g = 9.80665
r = 6378137
rho = 5000
S = 1
L = 1
R = rho * S * L
M = 5.972 * (10**24)
m = 50
n = 1000000000
tick = 10 ** (-2)
max_v = 100000
min_v = 0
tolerance = 10 ** (-3)

def sim(v) :
    ys = [0]
    F = 0
    a = 0
    time = 0
    for k in range(n) :
        #力計算
        if r - ys[-1] != 0 :
            if ys[-1] < r or ys[-1] == r :
                G = m * g
            elif r < ys[-1] :
                G = -m * g
            else :
                raise ValueError()
        elif r - ys[-1] == 0 :
            G = 0
        F = G - R
        #加速度計算
        a = F/m
        #速度計算
        v += a * tick
        #物理演算
        ys.append(ys[-1] + v * tick)
        time += tick
        #裏側判定
        if 2 * r < ys[-1] or 2 * r == ys[-1] :
            break
        elif ys[-1] < 0 :
            time = -1
            break
        write(ys[-1],v)
    return time

write(sim(80000))