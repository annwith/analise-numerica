import numpy as np

def fatoracao_lu(m, lub=False):
    # Inicializar matriz LU e b
    if lub == False:
        # Construir matriz LU
        lu = np.zeros_like(m[:, :-1])

        i = 0
        lu[i, :] = m[i, :-1]
        lu[i+1:, i] = m[i+1:, i] / m[i][i]

        for i in range(1, m.shape[0]):
            # coluna l
            for j in range(0, i):
                lu[i][j] = (m[i][j] - np.sum(lu[i, :j]*lu[:j, j])) / lu[j][j]
            # linha u
            for j in range(i, m.shape[0]):
                lu[i][j] = m[i][j] - np.sum(lu[i, :i]*lu[:i, j])
    else:
        lu = m[:, :-1]
    
    b = m[:, -1]

    # Ly = b : substituição direta
    y = []
    l = lu
    for i in range(l.shape[0]):
        y.append((b[i] - np.sum(l[i, :i])) / 1)
        l[i+1:, i] *= y[-1]
        # print(l)

    x = []
    # Ux = y substituição reversa
    for i in range(m.shape[0]-1, -1, -1):
        x.append((y[i] - np.sum(l[i, i+1:])) / l[i][i])
        l[:i, i] *= x[-1]
        # print(l)

    return lu, np.flip(x)

def main():
    input_txt = open('input-lu.txt', 'r')
    output_txt = open('output-lu.txt', 'w')
    np.set_printoptions(precision=6)
    np.set_printoptions(suppress=True)

    m = []
    for line in input_txt:
        if line[-1] == '\n':
            line = line[:-1]
        if line == "False":
            lub = False
            break
        if line == "True":
            lub = True
            break
        m.append(line.split(" "))
        m[-1] = list(map(lambda x: float(x), m[-1]))

    m = np.asarray(m)
    # m[:, :-1] = np.linalg.inv(m[:, :-1])
    lu, x = fatoracao_lu(np.copy(m), lub=lub)
    output_txt.write(str(lu)+"\n")
    output_txt.write(str(x)+"\n")

    m[:, :-1] *= x
    n = np.sum(m[:, :-1], axis=1)
    n = np.abs(m[:,-1]-n)

    output_txt.write(str(n)+"\n")

    input_txt.close()
    output_txt.close()

main()